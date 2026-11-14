export type Locale = "es" | "en";
export const locales: Locale[] = ["es", "en"];
export const defaultLocale: Locale = "es";

export const ui = {
  es: {
    metaTitle: "David Pérez Velasco — Business Analyst · Datos y BI",
    metaDescription: "Portfolio de David Pérez Velasco, ingeniero informático: proyectos de datos y BI con fuentes, modelos de datos, procesos de carga, KPIs e informes. En busca de prácticas de Business Analyst.",
    nav: { home: "Inicio", projects: "Proyectos", about: "Perfil", certifications: "Certificaciones", contact: "Contacto", cv: "CV", language: "Idioma" },
    hero: {
      eyebrow: "David Pérez Velasco · Business Analyst / datos y BI",
      availability: "Abierto a prácticas · 2026",
      headline: "Datos y BI",
      intro: "Soy David Pérez Velasco, ingeniero informático. Busco mis primeras prácticas como Business Analyst para trabajar en modelos de datos, procesos de carga, KPIs e informes. Aquí reúno los proyectos con los que practico, su estado real y lo que queda pendiente.",
      viewProjects: "Ver proyectos",
      facts: [
        { label: "Objetivo", value: "Prácticas de Business Analyst" },
        { label: "Formación", value: "Ingeniería Informática · USAL" },
        { label: "En cada ficha", value: "Problema, datos y estado real" },
      ],
    },
    about: {
      kicker: "Perfil",
      title: "Un poco sobre mí",
      lead: "Soy ingeniero informático por la Universidad de Salamanca y estoy orientando mi perfil a los datos y la BI: entender un proceso, ordenar sus datos y convertirlos en información que se pueda consultar y usar para decidir.",
      text: "Busco mis primeras prácticas como Business Analyst. Para prepararme trabajo en proyectos propios en los que aparecen las piezas del oficio: fuentes de datos, modelos de datos, procesos de carga, KPIs e informes. Algunos ya se pueden probar; otros siguen en local. Las fichas recogen el estado real de cada uno y lo que falta.",
      principles: [
        { title: "Entender el proceso antes de modelar", text: "Antes de elegir tablas o métricas, intento describir qué decide una persona y qué dato necesita para decidirlo. MuniPay empezó con un Excel incómodo; Fondo Popular, con datos repartidos entre federaciones." },
        { title: "Dejar las decisiones por escrito", text: "Cada ficha explica de dónde salen los datos, cómo se relacionan y qué límites tiene el resultado. No solo enumera tecnologías." },
        { title: "No esconder lo pendiente", text: "Si una parte es un prototipo o todavía no está desplegada, prefiero decirlo: el estado real dice más que aparentar más de lo que hay." },
      ],
    },
    projectsHome: {
      kicker: "Trabajo reciente",
      title: "Proyectos",
      intro: "Proyectos de datos y software con los que practico el trabajo de Business Analyst: fuentes, modelos de datos, procesos de carga, KPIs e informes. Cada ficha cuenta el problema, en qué punto está y qué queda pendiente.",
      all: "Ver archivo completo",
    },
    projectsPage: {
      kicker: "Archivo",
      title: "Proyectos",
      intro: "Una selección de proyectos personales y académicos. Los de datos y BI van primero: en cada ficha explico el problema, las fuentes, el modelo de datos, las métricas que se pueden obtener y el estado real del trabajo.",
    },
    project: {
      back: "← Todos los proyectos",
      viewRepo: "Código en GitHub ↗",
      demo: "Abrir aplicación ↗",
      plannedNote: "Todavía no está montado",
      resumen: "El proyecto",
      sectionsLabel: "Secciones del proyecto",
      capturesLabel: "Capturas reales del proyecto",
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
      text: "Si buscas a alguien para unas prácticas de Business Analyst, o quieres comentar cómo he planteado los datos de algún proyecto, puedes escribirme.",
      madeWith: "David Pérez Velasco",
    },
  },
  en: {
    metaTitle: "David Pérez Velasco — Business Analyst · Data & BI",
    metaDescription: "Portfolio of David Pérez Velasco, computer engineer: data and BI projects covering sources, data models, loading processes, KPIs and reports. Looking for a Business Analyst internship.",
    nav: { home: "Home", projects: "Projects", about: "Profile", certifications: "Certifications", contact: "Contact", cv: "CV", language: "Language" },
    hero: {
      eyebrow: "David Pérez Velasco · Business Analyst / data & BI",
      availability: "Open to internships · 2026",
      headline: "Data and BI",
      intro: "I'm David Pérez Velasco, a computer engineer. I'm looking for my first Business Analyst internship to work on data models, loading processes, KPIs and reports. This is where I collect the projects I practise with, their real status and what still needs work.",
      viewProjects: "View projects",
      facts: [
        { label: "Goal", value: "Business Analyst internship" },
        { label: "Education", value: "Computer Engineering · USAL" },
        { label: "In each project", value: "Problem, data and real status" },
      ],
    },
    about: {
      kicker: "Profile",
      title: "A little about me",
      lead: "I studied Computer Engineering at the University of Salamanca and I am focusing my profile on data and BI: understanding a process, organising its data and turning it into information that can be consulted and used to decide.",
      text: "I am looking for my first Business Analyst internship. To prepare, I work on personal projects that include the core pieces of the job: data sources, data models, loading processes, KPIs and reports. Some can already be tried; others still run locally. The project pages describe each one's real status and what is missing.",
      principles: [
        { title: "Understand the process before modelling", text: "Before choosing tables or metrics, I try to describe what a person decides and which data they need for it. MuniPay started from an awkward spreadsheet; Fondo Popular from data scattered across federations." },
        { title: "Write decisions down", text: "Each page explains where the data comes from, how it relates and what the result's limits are. It does not just list technologies." },
        { title: "Be clear about unfinished work", text: "If something is a prototype or not deployed yet, I say so: the real status says more than claiming more than exists." },
      ],
    },
    projectsHome: {
      kicker: "Recent work",
      title: "Projects",
      intro: "Data and software projects I use to practise Business Analyst work: sources, data models, loading processes, KPIs and reports. Each page explains the problem, where it stands and what is still pending.",
      all: "View full archive",
    },
    projectsPage: {
      kicker: "Archive",
      title: "Projects",
      intro: "A selection of personal and academic projects. Data and BI projects come first: each page explains the problem, the sources, the data model, which metrics can be obtained and the work's real state.",
    },
    project: {
      back: "← All projects",
      viewRepo: "Code on GitHub ↗",
      demo: "Open application ↗",
      plannedNote: "Not built yet",
      resumen: "Overview",
      sectionsLabel: "Project sections",
      capturesLabel: "Real project screenshots",
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
      text: "If you are looking for a Business Analyst intern, or want to discuss how I approached a project's data, feel free to write.",
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
