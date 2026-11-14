// Proyectos en marcha y próximos. Sin fechas ni promesas: solo estado real.
export type EnMarcha = {
  nombre: { es: string; en: string };
  linea: { es: string; en: string };
  estado: { es: string; en: string };
  href: string;
};

export const enMarcha: EnMarcha[] = [
  { nombre: { es: "Lyfta (Garmin)", en: "Lyfta (Garmin)" }, linea: { es: "App de fuerza que envía el plan al reloj Garmin. Por ahora es privada.", en: "Strength app that sends the plan to the Garmin watch. Private for now." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/garmin/" },
  { nombre: { es: "Fondo Popular (FACYLF)", en: "Fondo Popular (FACYLF)" }, linea: { es: "Base de datos y web del fútbol federado de Castilla y León.", en: "Database and web front end for federated football in Castile and León." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/facylf/" },
  { nombre: { es: "Cesta", en: "Cesta" }, linea: { es: "Comparador de la compra semanal entre supermercados.", en: "Weekly grocery comparison across supermarkets." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/compra-alimentacion/" },
  { nombre: { es: "CUE Digital", en: "CUE Digital" }, linea: { es: "Cuaderno de campo agrícola con validaciones y trazabilidad.", en: "Agricultural field notebook with validations and traceability." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/cue-digital/" },
  { nombre: { es: "EntrenoLab", en: "EntrenoLab" }, linea: { es: "Gestión de un club de fútbol base, con datos privados del club.", en: "Youth football club management, with private club data." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/entrenolab/" },
  { nombre: { es: "OpoFuente", en: "OpoFuente" }, linea: { es: "Temario y práctica de oposición con cobertura calculada.", en: "Exam syllabus and practice with measured coverage." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/opofuente/" },
  { nombre: { es: "Data School", en: "Data School" }, linea: { es: "Portal de datos e IA con datasets y material verificado.", en: "Data and AI portal with datasets and verified material." }, estado: { es: "En desarrollo", en: "In development" }, href: "/proyectos/data-school/" },
  { nombre: { es: "Datos · finanzas", en: "Data · finance" }, linea: { es: "Análisis de finanzas personales con un dataset de Data School.", en: "Personal finance analysis with a Data School dataset." }, estado: { es: "En preparación", en: "In preparation" }, href: "/datos/data-school-01/" },
  { nombre: { es: "Datos · Fórmula 1", en: "Data · Formula 1" }, linea: { es: "Análisis de telemetría y tiempos de vuelta con un dataset de Data School.", en: "Telemetry and lap-time analysis with a Data School dataset." }, estado: { es: "En preparación", en: "In preparation" }, href: "/datos/data-school-02/" },
  { nombre: { es: "Datos · fútbol", en: "Data · football" }, linea: { es: "Análisis de partidos, goles y xG con un dataset de Data School.", en: "Matches, goals and xG analysis with a Data School dataset." }, estado: { es: "En preparación", en: "In preparation" }, href: "/datos/data-school-03/" },
];
