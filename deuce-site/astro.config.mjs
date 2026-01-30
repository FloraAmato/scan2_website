import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://ideal.unina.it',
  base: '/deuce',
  output: 'static',
  build: {
    assets: 'assets'
  },
  trailingSlash: 'always'
});
