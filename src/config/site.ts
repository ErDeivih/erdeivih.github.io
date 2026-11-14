// Metadatos y enlaces del sitio — edítalos para tu marca.
export const site = {
  // Nombre real de la persona. "ErDeivih" se usa solo para lo que es de GitHub.
  name: "David Pérez Velasco",
  brand: "David",
  title: "David Pérez Velasco — Ingeniero Informático",
  description:
    "Porfolio de David Pérez Velasco: Ingeniero Informático por la Universidad de Salamanca (2025) y estudiante del Máster en Ingeniería Informática. Proyectos de software, sistemas y datos.",
  author: "David Pérez Velasco",
  lang: "es",
  locale: "es-ES",
  url: "https://erdeivih.github.io",
} as const;

// Perfiles / redes. El footer y el hero los usan para los enlaces.
// "ErDeivih" es el usuario de GitHub — personal y GitHub son cosas distintas.
export type Social = {
  github: string;
  githubHandle: string;
  linkedin?: string;
  email?: string;
};
export const social: Social = {
  github: "https://github.com/ErDeivih",
  githubHandle: "@ErDeivih",
  linkedin: "https://www.linkedin.com/in/david-p%C3%A9rez-velasco",
  email: "mailto:davidpeve01@gmail.com",
};
