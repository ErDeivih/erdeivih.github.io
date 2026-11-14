// Formación académica y cursos. Enlaces comprobados con petición real antes de publicar.
// «Certificado» distingue lo que es gratis de lo que no, sin prometer nada que no exista.
export type ItemFormacion = {
  nombre: { es: string; en: string };
  entidad: string;
  url?: string;
  estado: "en-curso" | "prevista" | "terminado";
  certificado: { es: string; en: string };
  coste: { es: string; en: string };
};

export const academica: ItemFormacion[] = [
  {
    nombre: { es: "Máster en Ingeniería Informática", en: "MSc in Computer Engineering" },
    entidad: "Universidad de Salamanca (USAL)",
    estado: "en-curso",
    certificado: { es: "Titulación oficial al terminar", en: "Official degree on completion" },
    coste: { es: "Matrícula oficial", en: "Official enrolment" },
  },
  {
    nombre: { es: "Grado en Ingeniería Informática", en: "BSc in Computer Engineering" },
    entidad: "Universidad de Salamanca (USAL)",
    estado: "terminado",
    certificado: { es: "Titulación oficial (2025)", en: "Official degree (2025)" },
    coste: { es: "Matrícula oficial", en: "Official enrolment" },
  },
];

export const cursos: ItemFormacion[] = [
  {
    nombre: { es: "Introduction to Data Science", en: "Introduction to Data Science" },
    entidad: "Cisco Networking Academy (Skills for All)",
    url: "https://www.netacad.com/courses/introduction-to-data-science",
    estado: "prevista",
    certificado: { es: "Badge gratuito al completarlo", en: "Free badge on completion" },
    coste: { es: "Curso gratuito", en: "Free course" },
  },
  {
    nombre: { es: "Pandas", en: "Pandas" },
    entidad: "Kaggle Learn",
    url: "https://www.kaggle.com/learn/pandas",
    estado: "prevista",
    certificado: { es: "Certificado gratuito", en: "Free certificate" },
    coste: { es: "Curso gratuito", en: "Free course" },
  },
  {
    nombre: { es: "Intro to Machine Learning", en: "Intro to Machine Learning" },
    entidad: "Kaggle Learn",
    url: "https://www.kaggle.com/learn/intro-to-machine-learning",
    estado: "prevista",
    certificado: { es: "Certificado gratuito", en: "Free certificate" },
    coste: { es: "Curso gratuito", en: "Free course" },
  },
  {
    nombre: { es: "Intro to SQL", en: "Intro to SQL" },
    entidad: "Kaggle Learn",
    url: "https://www.kaggle.com/learn/intro-to-sql",
    estado: "prevista",
    certificado: { es: "Certificado gratuito", en: "Free certificate" },
    coste: { es: "Curso gratuito", en: "Free course" },
  },
  {
    nombre: { es: "Google Analytics 4", en: "Google Analytics 4" },
    entidad: "Google Skillshop",
    url: "https://skillshop.withgoogle.com/",
    estado: "prevista",
    certificado: { es: "Certificado gratuito (Skillshop)", en: "Free certificate (Skillshop)" },
    coste: { es: "Curso y certificación gratuitos", en: "Free course and certification" },
  },
  {
    nombre: { es: "DP-900 · Azure Data Fundamentals", en: "DP-900 · Azure Data Fundamentals" },
    entidad: "Microsoft Learn",
    url: "https://learn.microsoft.com/es-es/credentials/certifications/azure-data-fundamentals/",
    estado: "prevista",
    certificado: { es: "Badge de Microsoft Learn gratuito; el examen de certificación no", en: "Free Microsoft Learn badge; the certification exam is not" },
    coste: { es: "Curso y badge gratis · examen de pago", en: "Free course and badge · paid exam" },
  },
];
