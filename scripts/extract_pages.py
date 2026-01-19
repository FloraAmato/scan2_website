#!/usr/bin/env python3
"""Extract WordPress pages from database dump for Astro migration."""
import re
import json
import html
import os

def extract_pages(dump_file):
    """Extract pages from WordPress SQL dump using a simpler approach."""
    with open(dump_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # First, get all page slugs and IDs
    slug_pattern = r"'([a-z0-9-]+)', '', '', '[^']+', '[^']+', '', \d+, 'http://localhost:8080/\?page_id=(\d+)', \d+, 'page'"
    slug_matches = re.findall(slug_pattern, content)

    pages = []
    for slug, page_id in slug_matches:
        # Now find the content for this page by ID
        # Pattern: (ID, 1, 'date', 'date', 'CONTENT', 'TITLE', ...
        # The content is between the dates and title

        # Build a pattern to find this specific page's row
        # Looking for: (page_id, 1, 'date', 'date', 'content', 'title',
        page_pattern = rf"\({page_id}, 1, '[\d-]+ [\d:]+', '[\d-]+ [\d:]+', '(.*?)', '([^']*)', '', 'publish'"

        match = re.search(page_pattern, content, re.DOTALL)
        if match:
            page_content = match.group(1)
            title = match.group(2)

            # Unescape
            page_content = page_content.replace("\\'", "'")
            page_content = page_content.replace("\\r\\n", "\n")
            page_content = page_content.replace("\\n", "\n")
            title = title.replace("\\'", "'")
            title = html.unescape(title)
        else:
            page_content = ""
            title = slug.replace('-', ' ').title()

        pages.append({
            'id': page_id,
            'slug': slug,
            'title': title if title else slug.replace('-', ' ').title(),
            'content': page_content
        })

    return pages

def clean_content(content):
    """Convert WordPress/Elementor content to clean HTML."""
    if not content:
        return ""

    # Remove Elementor data attributes and JSON
    content = re.sub(r'data-elementor[^=]*="[^"]*"', '', content)
    content = re.sub(r'data-widget_type="[^"]*"', '', content)
    content = re.sub(r'data-id="[^"]*"', '', content)
    content = re.sub(r'data-element_type="[^"]*"', '', content)
    content = re.sub(r'data-settings="[^"]*"', '', content)

    # Remove WordPress block comments
    content = re.sub(r'<!-- wp:[^>]+-->', '', content)
    content = re.sub(r'<!-- /wp:[^>]+-->', '', content)

    # Remove empty class attributes
    content = re.sub(r'\s+class=""', '', content)

    # Remove Elementor wrapper divs but keep content (simplified)
    # Keep the actual content structure

    # Clean excessive whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = content.strip()

    return content

def extract_text_content(html_content):
    """Extract meaningful text from HTML for preview."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html_content)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()[:200]

if __name__ == '__main__':
    pages = extract_pages('db/dump.sql')

    print(f"Found {len(pages)} published pages:\n")

    # Group pages
    country_pages = []
    main_pages = []

    eu_countries = ['austria', 'belgium', 'bulgaria', 'croatia', 'cyprus', 'czechia',
                    'denmark', 'estonia', 'finland', 'france', 'germany', 'greece',
                    'hungary', 'ireland', 'italy', 'latvia', 'lithuania', 'luxembourg',
                    'malta', 'netherlands', 'poland', 'portugal', 'romania', 'slovakia',
                    'slovenia', 'spain', 'sweden']

    for page in sorted(pages, key=lambda x: x['slug']):
        if page['slug'] in eu_countries:
            country_pages.append(page)
        else:
            main_pages.append(page)

    print("=== MAIN PAGES ===")
    for page in main_pages:
        preview = extract_text_content(page['content'])[:80]
        print(f"  {page['slug']}: {page['title']}")
        if preview:
            print(f"    Preview: {preview}...")
        print()

    print(f"\n=== COUNTRY PAGES ({len(country_pages)}) ===")
    for page in country_pages:
        print(f"  {page['slug']}: {page['title']}")

    # Save to JSON
    output = {
        'main_pages': main_pages,
        'country_pages': country_pages
    }

    with open('scripts/pages_data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(pages)} pages to scripts/pages_data.json")
