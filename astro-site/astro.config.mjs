import { defineConfig } from 'astro/config';

// DEUCE Website Astro Configuration
//
// For LOCAL testing, comment out 'base' to serve from root
// For PRODUCTION (Caddy subpath), use base: '/deuce'

export default defineConfig({
  site: 'https://ideal.unina.it',
  // LOCAL: Comment out for local testing (serves from /)
  // PRODUCTION: Uncomment for Caddy subpath deployment
  base: '/deuce',
  output: 'static',
  build: {
    assets: 'assets'
  },
  trailingSlash: 'always'
});
