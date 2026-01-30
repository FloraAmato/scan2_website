# DEUCE Website (Astro)

A fast, modern static website for the DEUCE project, built with Astro.

DEUCE focuses on improving the enforcement of judicial decisions in cross-border pecuniary claims through European Enforcement Orders (EEO) and European Orders for Payment (EOP).

## Quick Start

### Development (npm)

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

## Local Testing with Docker

For local testing without Caddy/edge network:

1. **Comment out the base path** in `astro.config.mjs`:
   ```js
   // base: '/deuce',
   ```

2. **Update docker-compose.yml** for local mode:
   ```yaml
   services:
     deuce_website:
       build: .
       restart: unless-stopped
       ports:
         - "8080:80"
       # networks:
       #   - edge

   # networks:
   #   edge:
   #     external: true
   ```

3. **Build and run**:
   ```bash
   docker-compose up -d --build
   ```

4. **Access at**: http://localhost:8080

## Production Deployment (Caddy)

For production with Caddy reverse proxy at `/deuce` subpath:

1. **Ensure base path is set** in `astro.config.mjs`:
   ```js
   base: '/deuce',
   ```

2. **Use edge network** in `docker-compose.yml` (default configuration)

3. **Add Caddy configuration**:
   ```
   handle_path /deuce/* {
       reverse_proxy deuce_website:80
   }
   ```

4. **Deploy**:
   ```bash
   docker-compose up -d --build
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

## Configuration Files

| File | Purpose |
|------|---------|
| `astro.config.mjs` | Site URL, base path, build options |
| `docker-compose.yml` | Docker service, networking, ports |

## Performance

- Zero JavaScript by default
- Pre-rendered static HTML
- Optimized CSS
- Fast nginx serving
- Gzip compression enabled

## License

DEUCE Project - EU Justice Programme (2021-2027)
