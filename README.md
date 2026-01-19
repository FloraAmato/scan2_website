# SCAN II Website

This repository contains two versions of the SCAN II website:

1. **`astro-site/`** - Modern static site (recommended)
2. **`site/`** - Original WordPress installation

---

## Option 1: Astro Static Site (Recommended)

A fast, lightweight static website with no database required.

### Prerequisites

- Node.js 18+ (for development)
- Docker (for production deployment)

### Development

```bash
cd astro-site

# Install dependencies
npm install

# Start development server
npm run dev
```

Open http://localhost:4321 in your browser.

### Production Deployment with Docker

```bash
cd astro-site

# Build and start the container
docker-compose up -d
```

Open http://localhost:8080 in your browser.

### Production Deployment without Docker

```bash
cd astro-site

# Build static files
npm run build

# The 'dist' folder contains your static site
# Upload it to any web server or static hosting service
```

### Hosting Options (Free)

- **Netlify**: Drag and drop the `dist` folder
- **Vercel**: Connect your Git repository
- **Cloudflare Pages**: Connect your Git repository
- **GitHub Pages**: Push to a `gh-pages` branch

---

## Option 2: WordPress (Legacy)

The original WordPress installation with database.

### Prerequisites

- Docker and Docker Compose

### Running WordPress

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env

# Start WordPress and database
docker-compose up -d
```

Open http://localhost:8080 in your browser.

### Changing WordPress User Password

After starting the containers:

```bash
./scripts/change-wp-password.sh bondo2488_zeoxh4x1 "YourNewPassword"
```

---

## Project Structure

```
scan2_website/
├── astro-site/          # Static site (recommended)
│   ├── src/
│   │   ├── pages/       # Website pages
│   │   ├── components/  # Reusable components
│   │   ├── layouts/     # Page layouts
│   │   └── styles/      # CSS styles
│   ├── public/          # Static assets
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── site/                # WordPress files (legacy)
├── db/                  # WordPress database dump
├── scripts/             # Utility scripts
├── docker-compose.yml   # WordPress Docker config
├── .env.example         # Environment template
└── .env                 # Your credentials (not in git)
```

---

## Customizing for Similar Projects

The Astro site is designed to be easily duplicated:

1. **Copy the project**
   ```bash
   cp -r astro-site my-new-project
   cd my-new-project
   ```

2. **Update site configuration**
   Edit `astro.config.mjs`:
   ```js
   export default defineConfig({
     site: 'https://your-new-domain.com',
   });
   ```

3. **Modify content**
   - Edit pages in `src/pages/`
   - Update navigation in `src/components/Header.astro`
   - Change footer in `src/components/Footer.astro`
   - Modify styles in `src/styles/global.css`

4. **Update country data** (if applicable)
   Edit the countries object in `src/pages/countries/[country].astro`

---

## Comparison

| Feature | Astro | WordPress |
|---------|-------|-----------|
| Load time | ~300ms | ~2-4s |
| Database | None | MariaDB |
| Hosting cost | Free | $5-20/month |
| Security patches | None | Regular |
| Customization | Edit code | Admin UI |
| Deployment | Static files | Docker + DB |

---

## License

SCAN II Project - Co-funded by the European Union's Justice Programme
