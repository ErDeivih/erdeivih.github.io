// @ts-check
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://erdeivih.github.io",
  // Salida 100% estática -> apta para GitHub Pages (gratis).
  output: "static",
  trailingSlash: "always",
  i18n: {
    defaultLocale: "es",
    locales: ["es", "en"],
    // Ambas versiones usan prefijo explícito. La raíz decide el idioma y redirige.
    routing: { prefixDefaultLocale: true },
  },
  integrations: [mdx(), sitemap()],
  vite: {
    plugins: [tailwindcss()],
    build: { assetsInlineLimit: 0 },
  },
});
