export type Locale = "es" | "en";
export const locales: Locale[] = ["es", "en"];
export const defaultLocale: Locale = "es";

export const ui = {
  es: {
    metaTitle: "David Pérez Velasco — Ingeniero Informático",
    metaDescription: "Porfolio de David Pérez Velasco: Ingeniero Informático por la Universidad de Salamanca (2025) y estudiante del Máster en Ingeniería Informática. Proyectos de software, sistemas y datos.",
    nav: { home: "Inicio", projects: "Proyectos", analysis: "Datos", about: "Sobre mí", contact: "Contacto", cv: "CV", language: "Idioma" },
    hero: {
      availability: "Salamanca · Máster en Ingeniería Informática (USAL)",
      headline: "Ingeniero Informático",
      intro: "Ingeniero Informático por la Universidad de Salamanca (2025) y estudiante del Máster en Ingeniería Informática. He construido los proyectos que ves aquí: software, sistemas y algún análisis de datos. En 2023 hice prácticas curriculares en NTT Data (Spring Framework, Git). En cada ficha cuento qué hace, cómo está hecho y qué falta.",
      viewProjects: "Ver proyectos",
      facts: [
        { label: "Formación", value: "Grado en Ingeniería Informática · USAL (2025)" },
        { label: "Ahora", value: "Máster en Ingeniería Informática · USAL" },
        { label: "En cada ficha", value: "Qué hace y cómo está hecho" },
      ],
    },
    about: {
      kicker: "Sobre mí",
      title: "Sobre mí",
      lead: "Soy ingeniero informático y estoy cursando el Máster en Ingeniería Informática en la Universidad de Salamanca. Me interesa construir software que funcione de verdad: aplicaciones, servicios y las piezas de sistema que hay detrás.",
      text: "Programo sobre todo en Java, TypeScript, C# y Python, y he trabajado con Node.js, React, Spring, PostgreSQL, Docker y Git. En los proyectos de este porfolio he montado la recolección de datos, el modelo, el backend, el frontend y el despliegue; algunos están publicados y otros solo funcionan en local, y lo digo en cada ficha. Los análisis de datos los hago como aprendizaje, no como especialidad.",
      principles: [
        { title: "Primero que funcione", text: "Prefiero una aplicación pequeña que se pueda usar a una maqueta grande. Si algo no está terminado, la ficha lo dice." },
        { title: "Entender lo que hay debajo", text: "Me interesa el recorrido completo: de dónde vienen los datos, cómo se guardan, qué hace el servidor y qué ve el usuario." },
        { title: "Dejar por escrito las decisiones", text: "Cada ficha explica cómo está construido el proyecto y qué límites tiene. No solo enumera tecnologías." },
      ],
    },
    projectsHome: {
      kicker: "Proyectos",
      title: "Proyectos",
      intro: "Aplicaciones y sistemas que he construido. En cada ficha cuento qué resuelve, cómo está hecho, las capturas reales y en qué punto está.",
      all: "Ver todos los proyectos",
    },
    projectsPage: {
      kicker: "Proyectos",
      title: "Proyectos",
      intro: "Aplicaciones y sistemas que he construido, de la base de datos a la interfaz. Puedes filtrar por estado y abrir cada ficha.",
    },
    project: {
      back: "← Todos los proyectos",
      viewRepo: "Código en GitHub ↗",
      demo: "Abrir aplicación ↗",
      plannedNote: "Todavía no está montado",
      resumen: "El proyecto",
      sectionsLabel: "Secciones del proyecto",
      capturesLabel: "Capturas del proyecto",
      keyPoint: "Dato",
      notFound: "No encuentro ese proyecto.",
      backLink: "← Volver",
      card: { view: "Ver proyecto", repo: "Repo ↗" },
      statuses: { active: "En desarrollo", maintained: "En mantenimiento", paused: "En pausa", planned: "En preparación", archived: "Archivado", complete: "Completado" },
    },
    analysis: {
      title: "Datos y análisis",
      intro: "Análisis cortos que hago para aprender: una pregunta concreta, datos reales y el cálculo hecho con NumPy. No es mi especialidad; es la parte de datos que uso cuando un proyecto la necesita.",
      question: "La pregunta",
      source: "De dónde salen los datos",
      method: "Qué hice",
      conclusion: "Qué saco",
      back: "← Volver al inicio",
      link: "Ver los análisis",
    },
    certifications: {
      kicker: "Formación",
      title: "Certificaciones",
      intro: "",
      groups: [{ label: "Desarrollo" }],
      empty: "Todavía sin publicaciones",
    },
    footer: {
      kicker: "Contacto",
      title: "Escríbeme",
      text: "Si quieres comentar algún proyecto o pedirme el CV, puedes escribirme.",
      madeWith: "David Pérez Velasco",
    },
  },
  en: {
    metaTitle: "David Pérez Velasco — Computer Engineer",
    metaDescription: "Portfolio of David Pérez Velasco: Computer Engineer from the University of Salamanca (2025) and a student of the Master's in Computer Engineering. Software, systems and data projects.",
    nav: { home: "Home", projects: "Projects", analysis: "Data", about: "About", contact: "Contact", cv: "CV", language: "Language" },
    hero: {
      availability: "Salamanca · Master's in Computer Engineering (USAL)",
      headline: "Computer Engineer",
      intro: "Computer Engineer from the University of Salamanca (2025) and a student of the Master's in Computer Engineering. I have built the projects you see here: software, systems and some data analysis. In 2023 I did a curricular internship at NTT Data (Spring Framework, Git). Each page explains what it does, how it is built and what is missing.",
      viewProjects: "View projects",
      facts: [
        { label: "Education", value: "BSc in Computer Engineering · USAL (2025)" },
        { label: "Now", value: "MSc in Computer Engineering · USAL" },
        { label: "In each page", value: "What it does and how it is built" },
      ],
    },
    about: {
      kicker: "About",
      title: "About me",
      lead: "I am a computer engineer studying the Master's in Computer Engineering at the University of Salamanca. I like building software that actually works: applications, services and the system pieces behind them.",
      text: "I code mainly in Java, TypeScript, C# and Python, and I have worked with Node.js, React, Spring, PostgreSQL, Docker and Git. In the projects in this portfolio I have built the data collection, the model, the backend, the frontend and the deployment; some are published and others only run locally, and each page says which. I do data analysis as a way of learning, not as a speciality.",
      principles: [
        { title: "Working first", text: "I prefer a small application people can use to a big mock-up. If something is not finished, the page says so." },
        { title: "Understand what is underneath", text: "I care about the whole path: where the data comes from, how it is stored, what the server does and what the user sees." },
        { title: "Write decisions down", text: "Each page explains how the project is built and what its limits are. It does not just list technologies." },
      ],
    },
    projectsHome: {
      kicker: "Projects",
      title: "Projects",
      intro: "Applications and systems I have built. Each page explains what it solves, how it is built, real screenshots and where it stands.",
      all: "View all projects",
    },
    projectsPage: {
      kicker: "Projects",
      title: "Projects",
      intro: "Applications and systems I have built, from the database to the interface. You can filter by status and open each page.",
    },
    project: {
      back: "← All projects",
      viewRepo: "Code on GitHub ↗",
      demo: "Open application ↗",
      plannedNote: "Not built yet",
      resumen: "Overview",
      sectionsLabel: "Project sections",
      capturesLabel: "Project screenshots",
      keyPoint: "Fact",
      notFound: "I couldn't find that project.",
      backLink: "← Back",
      card: { view: "View project", repo: "Repo ↗" },
      statuses: { active: "In development", maintained: "Maintained", paused: "Paused", planned: "In preparation", archived: "Archived", complete: "Complete" },
    },
    analysis: {
      title: "Data and analysis",
      intro: "Short analyses I do to learn: one concrete question, real data and the work done with NumPy. It is not my speciality; it is the data side I use when a project needs it.",
      question: "The question",
      source: "Where the data comes from",
      method: "What I did",
      conclusion: "What I take away",
      back: "← Back to home",
      link: "See the analyses",
    },
    certifications: {
      kicker: "Learning",
      title: "Certifications",
      intro: "",
      groups: [{ label: "Development" }],
      empty: "No entries yet",
    },
    footer: {
      kicker: "Contact",
      title: "Get in touch",
      text: "If you want to discuss a project or ask for my CV, feel free to write.",
      madeWith: "David Pérez Velasco",
    },
  },
};

export function useTranslations(locale: string): typeof ui.es { return locale === "en" ? ui.en : ui.es; }
/** Ruta localizada: el idioma por defecto va en la raíz, el resto con prefijo. */
export function localePath(locale: string, path: string): string {
  const prefix = locale === defaultLocale ? "" : `/${locale}`;
  return `${prefix}${path}`;
}
export function isLocale(locale: string): locale is Locale { return locale === "es" || locale === "en"; }
