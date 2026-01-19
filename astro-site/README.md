# SCAN II Website (Astro)

A fast, modern static website for the SCAN II project, built with Astro.

## Quick Start

### Development

```bash
# Install dependencies
npm install

# Start dev server (http://localhost:4321)
npm run dev
```

### Production Build

```bash
# Build static files
npm run build

# Preview production build
npm run preview
```

### Docker Deployment

```bash
# Build and run with Docker
docker-compose up -d

# Or build manually
docker build -t scan2-website .
docker run -p 8080:80 scan2-website
```

## Project Structure

```
astro-site/
├── src/
│   ├── pages/           # Page routes (automatic routing)
│   │   ├── index.astro  # Homepage
│   │   ├── about.astro  # About page
│   │   └── countries/   # Country pages (dynamic)
│   ├── layouts/         # Page layouts
│   ├── components/      # Reusable components
│   └── styles/          # Global CSS
├── public/              # Static assets (images, favicon)
├── astro.config.mjs     # Astro configuration
├── Dockerfile           # Docker build
└── docker-compose.yml   # Docker Compose config
```

## Customizing for New Projects

1. **Update site info**: Edit `astro.config.mjs` to change the site URL
2. **Modify content**: Edit pages in `src/pages/`
3. **Change styling**: Update `src/styles/global.css`
4. **Update navigation**: Edit `src/components/Header.astro`
5. **Add countries**: Edit the countries object in `src/pages/countries/[country].astro`

## Adding New Pages

Create a new `.astro` file in `src/pages/`:

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="My New Page">
  <div class="page-header">
    <div class="container">
      <h1>My New Page</h1>
    </div>
  </div>
  <section class="content">
    <div class="container">
      <p>Your content here...</p>
    </div>
  </section>
</Layout>
```

## Performance

- Zero JavaScript by default
- Pre-rendered static HTML
- Optimized CSS
- Fast nginx serving
- Gzip compression enabled

## License

SCAN II Project - EU Justice Programme
