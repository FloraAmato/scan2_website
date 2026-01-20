import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://ideal.unina.it',
  base: '/scan2',
  output: 'static',
  build: {
    assets: 'assets'
  },
  trailingSlash: 'always'
});
