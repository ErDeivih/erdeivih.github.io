// Diccionario i18n (es/en) — textos de la interfaz.
// El contenido de los proyectos (MDX) se traduce en sus propios ficheros (campo `lang`).

export type Locale = "es" | "en";
export const locales: Locale[] = ["es", "en"];
export const defaultLocale: Locale = "es";

export const ui = {
  es: {
    metaTitle: "David Pérez Velasco — Developer Portfolio",
    metaDescription:
      "Portfolio de David Pérez Velasco, ingeniero informático. Proyectos explicados con su teoría, sus técnicas y cómo ejecutarlos y probarlos.",
    langLabel: "ES",
    nav: { home: "Inicio", projects: "Proyectos", about: "Sobre mí" },
    hero: {
      whoami: "whoami",
      hello: "Hola, soy",
      roles: ["Desarrollador", "Full-Stack", "Creador de apps", "Resolver problemas"],
      intro:
        "Construyo aplicaciones web y herramientas, y las documento aquí. Este es mi portfolio: proyectos explicados con su teoría, sus técnicas y su código en GitHub.",
      viewProjects: "Ver proyectos",
      github: "GitHub",
      celebrate: "✨ ¡Celebrar!",
      stats: [
        { n: "3+", l: "proyectos" },
        { n: "100%", l: "código propio" },
        { n: "0€", l: "en hosting" },
      ],
    },
    about: {
      cmd: "cat about.md",
      title: "Sobre mí",
      text: "Soy David Pérez Velasco, ingeniero informático por la Universidad de Salamanca y ahora cursando el máster en Ingeniería Informática. Empecé con Java y acabé aterrizando en el desarrollo web: TypeScript, React y Node.js, con Spring Framework en la parte de backend. Mi TFG, DocumentChain, junta blockchain (Ethereum), IPFS y cifrado para gestionar documentos con trazabilidad y control de acceso. Me gustan los proyectos donde hay sistema y producto a la vez: base de datos de verdad, autenticación y una interfaz que no estorbe. Aquí cada proyecto explica qué es, cómo está hecho y cómo se ejecuta y se prueba.",
      stackTitle: "stack con el que trabajo",
      stack: [
        "Java / Spring Framework",
        "TypeScript / React / Node.js",
        "Solidity / Blockchain / IPFS",
        "Flutter · Docker · Git",
      ],
    },
    projectsHome: { cmd: "ls ./proyectos", title: "Proyectos", all: "ver todos" },
    projectsPage: {
      cmd: "ls ./proyectos",
      title: "Proyectos",
      intro:
        "Cada proyecto tiene su propia página con pestañas (resumen, teoría, técnicas y documentación) y su enlace al repositorio en GitHub.",
    },
    project: {
      back: "← volver a proyectos",
      viewRepo: "Ver repo ↗",
      demo: "Demo en vivo ↗",
      resumen: "Resumen",
      notFound: "Proyecto no encontrado.",
      backLink: "← volver",
      card: { view: "Ver proyecto →", repo: "Repo ↗" },
      statuses: {
        active: "ACTIVO",
        maintained: "EN MANTENIMIENTO",
        paused: "EN PAUSA",
        archived: "ARCHIVADO",
        complete: "COMPLETADO",
      },
    },
    footer: { madeWith: "$ Hecho con Astro · diseño propio retro-terminal · {year}" },
  },

  en: {
    metaTitle: "David Pérez Velasco — Developer Portfolio",
    metaDescription:
      "Portfolio of David Pérez Velasco, software engineer. Projects explained with their theory, their techniques and how to run and test them.",
    langLabel: "EN",
    nav: { home: "Home", projects: "Projects", about: "About me" },
    hero: {
      whoami: "whoami",
      hello: "Hi, I'm",
      roles: ["Developer", "Full-Stack", "App builder", "Problem solver"],
      intro:
        "I build web apps and tools and document them here. This is my portfolio: projects explained with their theory, techniques and code on GitHub.",
      viewProjects: "View projects",
      github: "GitHub",
      celebrate: "✨ Celebrate!",
      stats: [
        { n: "3+", l: "projects" },
        { n: "100%", l: "own code" },
        { n: "€0", l: "hosting" },
      ],
    },
    about: {
      cmd: "cat about.md",
      title: "About me",
      text: "I'm David Pérez Velasco, software engineer from the University of Salamanca, now doing an MSc in Computer Engineering. I started with Java and ended up in web development: TypeScript, React and Node.js, with Spring Framework on the backend. My final project, DocumentChain, combines blockchain (Ethereum), IPFS and encryption to manage documents with traceability and access control. I like projects that mix system and product: a real database, authentication and an interface that doesn't get in the way. Here each project explains what it is, how it's built and how to run and test it.",
      stackTitle: "stack I work with",
      stack: [
        "Java / Spring Framework",
        "TypeScript / React / Node.js",
        "Solidity / Blockchain / IPFS",
        "Flutter · Docker · Git",
      ],
    },
    projectsHome: { cmd: "ls ./projects", title: "Projects", all: "view all" },
    projectsPage: {
      cmd: "ls ./projects",
      title: "Projects",
      intro:
        "Each project has its own page with tabs (overview, theory, techniques and how-to-run) and a link to its GitHub repository.",
    },
    project: {
      back: "← back to projects",
      viewRepo: "View repo ↗",
      demo: "Live demo ↗",
      resumen: "Overview",
      notFound: "Project not found.",
      backLink: "← back",
      card: { view: "View project →", repo: "Repo ↗" },
      statuses: {
        active: "ACTIVE",
        maintained: "MAINTAINED",
        paused: "PAUSED",
        archived: "ARCHIVED",
        complete: "COMPLETED",
      },
    },
    footer: { madeWith: "$ Made with Astro · custom retro-terminal design · {year}" },
  },
};

export function useTranslations(locale: string): typeof ui.es {
  return locale === "en" ? ui.en : ui.es;
}

export function isLocale(locale: string): locale is Locale {
  return locale === "es" || locale === "en";
}
