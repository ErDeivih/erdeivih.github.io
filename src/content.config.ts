import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const projects = defineCollection({
  // Cada proyecto = una carpeta en src/content/projects/<slug>/.
  // index.mdx       -> type: "project"  (ficha principal del proyecto)
  // <cualquier>.mdx -> type: "tab"      (una pestaña más por proyecto)
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/projects" }),
  schema: z
    .object({
      type: z.enum(["project", "tab"]),
      lang: z.string().default("es"),

      // --- Campos de FICHA de proyecto (type === "project") ---
      slug: z.string().optional(),
      title: z.string().optional(),
      description: z.string().optional(),
      tagline: z.string().optional(),
      repo: z.string().url().optional(),
      demo: z.string().url().optional(),
      image: z.string().optional(),
      imageAlt: z.string().optional(),
      color: z.string().optional(),
      status: z
        .enum(["active", "maintained", "paused", "archived", "complete"])
        .default("active"),
      tags: z.array(z.string()).default([]),
      stack: z.array(z.string()).optional(),
      order: z.number().default(0),
      featured: z.boolean().default(false),

      // --- Campos de PESTAÑA (type === "tab") ---
      project: z.string().optional(),
      tab: z.string().optional(),
      label: z.string().optional(),
    })
    .superRefine((data, ctx) => {
      if (data.type === "project") {
        if (!data.title) ctx.addIssue({ code: "custom", message: "project requiere 'title'" });
      } else {
        if (!data.project) ctx.addIssue({ code: "custom", message: "tab requiere 'project'" });
        if (!data.tab) ctx.addIssue({ code: "custom", message: "tab requiere 'tab'" });
        if (!data.label) ctx.addIssue({ code: "custom", message: "tab requiere 'label'" });
      }
    }),
});

export const collections = { projects };
