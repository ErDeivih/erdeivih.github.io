export type Locale = "es" | "en";
export const locales: Locale[] = ["es", "en"];
export const defaultLocale: Locale = "es";

export const ui = {
  es: {
    metaTitle: "David Pérez Velasco — Proyectos y desarrollo",
    metaDescription: "Proyectos de David Pérez Velasco: fútbol, datos, compra y alimentación, gestión agrícola y herramientas de estudio. Avances, código y versiones públicas.",
    nav: { home: "Inicio", projects: "Proyectos", about: "Perfil", certifications: "Certificaciones", contact: "Contacto", language: "Idioma" },
    hero: {
      eyebrow: "David Pérez Velasco · Ingeniero informático",
      availability: "Portfolio / 2026",
      headline: "Hola, soy David",
      intro: "Hago aplicaciones para cosas que tengo cerca: preparar un entrenamiento, organizar una compra o estudiar una oposición. Aquí voy reuniendo los proyectos, cómo avanzan y lo que ya se puede probar.",
      viewProjects: "Ver proyectos",
      facts: [
        { label: "Formación", value: "Ingeniería Informática · USAL" },
        { label: "Áreas", value: "Web · móvil · datos" },
        { label: "En cada proyecto", value: "Avances y próximos pasos" },
      ],
    },
    about: {
      kicker: "Perfil",
      title: "Un poco sobre mí",
      lead: "Estudié Ingeniería Informática en la Universidad de Salamanca. Me interesa hacer herramientas que encajen en el día a día, y muchas de las ideas salen del fútbol, del estudio o de tareas que repito en casa.",
      text: "Ahora estoy dedicando tiempo a CDMPLab, a los datos del fútbol federado y a varias aplicaciones de compra, gestión agrícola y estudio. Algunas tienen una versión pública; otras aún las uso en local. Las fichas recogen ese punto de partida y se irán actualizando.",
      principles: [
        { title: "Entender antes de programar", text: "MuniPay empezó con un Excel incómodo; CDMPLab, con una pizarra que tenía que ser fácil de manejar." },
        { title: "Dejar las decisiones por escrito", text: "Intento explicar por qué elegí cada pieza y qué límites tiene, no solo enumerar tecnologías." },
        { title: "No esconder lo pendiente", text: "Si una parte es un prototipo o todavía está en el roadmap, prefiero decirlo claramente." },
      ],
    },
    projectsHome: {
      kicker: "Trabajo reciente",
      title: "Proyectos",
      intro: "Aplicaciones personales y trabajos de la universidad. Cada ficha cuenta para qué sirve el proyecto, en qué punto está y qué estoy preparando después.",
      all: "Ver archivo completo",
    },
    projectsPage: {
      kicker: "Archivo",
      title: "Proyectos",
      intro: "Una selección de proyectos personales y académicos. En cada ficha explico el problema, las decisiones técnicas y el estado real del trabajo.",
    },
    project: {
      back: "← Todos los proyectos",
      viewRepo: "Código en GitHub ↗",
      demo: "Abrir aplicación ↗",
      plannedNote: "Todavía no está montado",
      resumen: "El proyecto",
      sectionsLabel: "Secciones del proyecto",
      keyPoint: "La idea clave",
      notFound: "No encuentro ese proyecto.",
      backLink: "← Volver",
      card: { view: "Ver proyecto", repo: "Repo ↗" },
      statuses: { active: "En desarrollo", maintained: "En mantenimiento", paused: "En pausa", planned: "En preparación", archived: "Archivado", complete: "Completado" },
    },
    certifications: {
      kicker: "En formación",
      title: "Certificaciones",
      intro: "Aquí iré añadiendo las certificaciones que complete, con la entidad que las emite, la fecha y un enlace para verificarlas.",
      groups: [{ label: "Desarrollo" }, { label: "Cloud y datos" }, { label: "Idiomas y otras" }],
      empty: "Todavía sin publicaciones",
    },
    footer: {
      kicker: "Contacto",
      title: "¿Quieres hablar?",
      text: "Si te interesa alguno de los proyectos, crees que puedo encajar en una oportunidad o simplemente quieres comentar una decisión técnica, puedes escribirme.",
      madeWith: "David Pérez Velasco",
    },
  },
  en: {
    metaTitle: "David Pérez Velasco — Projects and development",
    metaDescription: "David Pérez Velasco's projects: football, data, groceries and food planning, farm management and study tools. Progress, code and public versions.",
    nav: { home: "Home", projects: "Projects", about: "Profile", certifications: "Certifications", contact: "Contact", language: "Language" },
    hero: {
      eyebrow: "David Pérez Velasco · Software engineer",
      availability: "Portfolio / 2026",
      headline: "Hi, I'm David",
      intro: "I build applications for things close to me: planning a training session, organising groceries or studying for an exam. This is where I collect the projects, their progress and what you can try.",
      viewProjects: "View projects",
      facts: [
        { label: "Education", value: "Computer Engineering · USAL" },
        { label: "Areas", value: "Web · mobile · data" },
        { label: "In each project", value: "Progress and next steps" },
      ],
    },
    about: {
      kicker: "Profile",
      title: "A little about me",
      lead: "I studied Computer Engineering at the University of Salamanca. I enjoy making tools that fit everyday life; many ideas come from football, studying or things I do at home.",
      text: "I am currently working on CDMPLab, federated football data and applications for groceries, farm management and studying. Some have public versions; others still run locally. The project pages describe that starting point and will be updated as they progress.",
      principles: [
        { title: "Understand before coding", text: "MuniPay began with an awkward spreadsheet; CDMPLab with a board that needed to be easy to handle." },
        { title: "Write decisions down", text: "I try to explain why I chose each part and where its limits are, not just list technologies." },
        { title: "Be clear about unfinished work", text: "If something is a prototype or still on the roadmap, I would rather say so plainly." },
      ],
    },
    projectsHome: {
      kicker: "Recent work",
      title: "Projects",
      intro: "Personal applications and university work. Each page explains what the project is for, where it stands and what I am working on next.",
      all: "View full archive",
    },
    projectsPage: {
      kicker: "Archive",
      title: "Projects",
      intro: "A selection of personal and academic projects. Each case explains the problem, the technical decisions and the work's current state.",
    },
    project: {
      back: "← All projects",
      viewRepo: "Code on GitHub ↗",
      demo: "Open application ↗",
      plannedNote: "Not built yet",
      resumen: "Overview",
      sectionsLabel: "Project sections",
      keyPoint: "The key idea",
      notFound: "I couldn't find that project.",
      backLink: "← Back",
      card: { view: "View project", repo: "Repo ↗" },
      statuses: { active: "In development", maintained: "Maintained", paused: "Paused", planned: "In preparation", archived: "Archived", complete: "Complete" },
    },
    certifications: {
      kicker: "Ongoing learning",
      title: "Certifications",
      intro: "I will add completed certifications here, with the issuing organisation, the date and a verification link.",
      groups: [{ label: "Development" }, { label: "Cloud and data" }, { label: "Languages and other" }],
      empty: "No entries yet",
    },
    footer: {
      kicker: "Contact",
      title: "Want to talk?",
      text: "If a project caught your attention, you think I could fit an opportunity, or you simply want to discuss a technical decision, feel free to write.",
      madeWith: "David Pérez Velasco",
    },
  },
};

export function useTranslations(locale: string): typeof ui.es { return locale === "en" ? ui.en : ui.es; }
export function isLocale(locale: string): locale is Locale { return locale === "es" || locale === "en"; }
