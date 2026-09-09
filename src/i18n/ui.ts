export type Locale = "es" | "en";
export const locales: Locale[] = ["es", "en"];
export const defaultLocale: Locale = "es";

export const ui = {
  es: {
    metaTitle: "David Pérez Velasco — Ingeniería de software, datos y producto",
    metaDescription: "Portfolio de David Pérez Velasco: aplicaciones reales, sistemas distribuidos y proyectos de datos explicados desde el problema hasta las decisiones técnicas.",
    nav: { home: "Inicio", projects: "Proyectos", about: "Perfil", certifications: "Certificaciones", contact: "Contacto", language: "Idioma" },
    hero: {
      eyebrow: "David Pérez Velasco · Ingeniero informático",
      availability: "Portfolio / 2026",
      headline: "Software para problemas concretos",
      intro: "Me gusta partir de una necesidad real, entenderla bien y convertirla en una aplicación que se pueda usar y mantener. Aquí cuento qué hice, por qué lo hice así y qué queda por mejorar.",
      viewProjects: "Ver proyectos",
      facts: [
        { label: "Ahora", value: "Máster en Ingeniería Informática" },
        { label: "Áreas", value: "Web · móvil · datos" },
        { label: "En cada proyecto", value: "Código, decisiones y cómo probarlo" },
      ],
    },
    about: {
      kicker: "Perfil",
      title: "Un poco sobre mí",
      lead: "Estudié Ingeniería Informática en la Universidad de Salamanca y ahora curso el máster. Suelo aprender mejor cuando tengo un problema real delante y algo que quiero dejar funcionando.",
      text: "Por eso mis proyectos son bastante distintos: una app para las cuentas de un equipo de fútbol, una pizarra para entrenadores, mi TFG sobre documentos e IPFS, una plataforma de datos para aeropuertos y una futura web de fútbol federado. En cada uno he tenido que moverme entre la interfaz, la lógica y la parte que nadie ve.",
      principles: [
        { title: "Entender antes de programar", text: "MuniPay empezó con un Excel incómodo; CDMPLab, con una pizarra que tenía que ser fácil de manejar." },
        { title: "Dejar las decisiones por escrito", text: "Intento explicar por qué elegí cada pieza y qué límites tiene, no solo enumerar tecnologías." },
        { title: "No esconder lo pendiente", text: "Si una parte es un prototipo o todavía está en el roadmap, prefiero decirlo claramente." },
      ],
    },
    projectsHome: {
      kicker: "Trabajo reciente",
      title: "Proyectos",
      intro: "He elegido cinco proyectos que enseñan partes distintas de mi trabajo. Algunos ya se pueden probar y otros aparecen atenuados porque todavía están en preparación.",
      all: "Ver archivo completo",
    },
    projectsPage: {
      kicker: "Archivo / 05",
      title: "Proyectos",
      intro: "Una selección de proyectos personales y académicos. En cada ficha explico el problema, las decisiones técnicas y el estado real del trabajo.",
    },
    project: {
      back: "← Todos los proyectos",
      viewRepo: "Código en GitHub ↗",
      demo: "Abrir demo ↗",
      plannedNote: "Todavía no está montado",
      resumen: "Caso de estudio",
      sectionsLabel: "Secciones del proyecto",
      keyPoint: "La idea clave",
      notFound: "No encuentro ese proyecto.",
      backLink: "← Volver",
      card: { view: "Leer el caso", repo: "Repo ↗" },
      statuses: { active: "En desarrollo", maintained: "En mantenimiento", paused: "En pausa", planned: "En preparación", archived: "Archivado", complete: "Completado" },
    },
    certifications: {
      kicker: "En formación",
      title: "Certificaciones",
      intro: "Esta sección está preparada para ir reuniendo las certificaciones que vaya completando. Prefiero dejarla vacía por ahora antes que rellenarla con cursos o conocimientos que no sean una acreditación real.",
      groups: [{ label: "Desarrollo" }, { label: "Cloud y datos" }, { label: "Idiomas y otras" }],
      empty: "Próximamente",
    },
    footer: {
      kicker: "Contacto",
      title: "¿Quieres hablar?",
      text: "Si te interesa alguno de los proyectos, crees que puedo encajar en una oportunidad o simplemente quieres comentar una decisión técnica, puedes escribirme.",
      madeWith: "Diseñado y construido por David · Astro",
    },
  },
  en: {
    metaTitle: "David Pérez Velasco — Software engineering, data and product",
    metaDescription: "David Pérez Velasco's portfolio: real applications, distributed systems and data projects explained from problem to technical decisions.",
    nav: { home: "Home", projects: "Projects", about: "Profile", certifications: "Certifications", contact: "Contact", language: "Language" },
    hero: {
      eyebrow: "David Pérez Velasco · Software engineer",
      availability: "Portfolio / 2026",
      headline: "Software for concrete problems",
      intro: "I like to start with a real need, understand it properly and turn it into software that people can use and maintain. Here I explain what I built, why I made those choices and what still needs work.",
      viewProjects: "View projects",
      facts: [
        { label: "Currently", value: "MSc in Computer Engineering" },
        { label: "Areas", value: "Web · mobile · data" },
        { label: "In each project", value: "Code, decisions and how to try it" },
      ],
    },
    about: {
      kicker: "Profile",
      title: "A little about me",
      lead: "I studied Computer Engineering at the University of Salamanca and I am now completing my master's. I learn best when I have a real problem in front of me and something I want to leave working.",
      text: "That is why my projects are quite different: an app for a football team's accounts, a tactical board for coaches, my final project on documents and IPFS, an airport data platform, and a future site for federated football. Each one made me work across the interface, the logic and the parts users never see.",
      principles: [
        { title: "Understand before coding", text: "MuniPay began with an awkward spreadsheet; CDMPLab with a board that needed to be easy to handle." },
        { title: "Write decisions down", text: "I try to explain why I chose each part and where its limits are, not just list technologies." },
        { title: "Be clear about unfinished work", text: "If something is a prototype or still on the roadmap, I would rather say so plainly." },
      ],
    },
    projectsHome: {
      kicker: "Recent work",
      title: "Projects",
      intro: "I chose five projects that show different parts of my work. Some can already be tried; others are dimmed because they are still being prepared.",
      all: "View full archive",
    },
    projectsPage: {
      kicker: "Archive / 05",
      title: "Projects",
      intro: "A selection of personal and academic projects. Each case explains the problem, the technical decisions and the work's current state.",
    },
    project: {
      back: "← All projects",
      viewRepo: "Code on GitHub ↗",
      demo: "Open live demo ↗",
      plannedNote: "Not built yet",
      resumen: "Case study",
      sectionsLabel: "Project sections",
      keyPoint: "The key idea",
      notFound: "I couldn't find that project.",
      backLink: "← Back",
      card: { view: "Read the case", repo: "Repo ↗" },
      statuses: { active: "In development", maintained: "Maintained", paused: "Paused", planned: "In preparation", archived: "Archived", complete: "Complete" },
    },
    certifications: {
      kicker: "Ongoing learning",
      title: "Certifications",
      intro: "This section is ready to collect certifications as I complete them. For now, I would rather leave it empty than pad it with courses or skills that are not actual credentials.",
      groups: [{ label: "Development" }, { label: "Cloud and data" }, { label: "Languages and other" }],
      empty: "Coming soon",
    },
    footer: {
      kicker: "Contact",
      title: "Want to talk?",
      text: "If a project caught your attention, you think I could fit an opportunity, or you simply want to discuss a technical decision, feel free to write.",
      madeWith: "Designed and built by David · Astro",
    },
  },
};

export function useTranslations(locale: string): typeof ui.es { return locale === "en" ? ui.en : ui.es; }
export function isLocale(locale: string): locale is Locale { return locale === "es" || locale === "en"; }
