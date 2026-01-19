import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://scan2.example.com',
  output: 'static',
  build: {
    assets: 'assets'
  }
});
