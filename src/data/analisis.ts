// Análisis de datos del porfolio. Cada entrada tiene su versión en español e inglés.
// Los gráficos se generan con scripts/analisis-datos.py (NumPy + matplotlib) desde datos reales.

export type AnalisisTexto = {
  titulo: string;
  pregunta: string;
  fuente: string;
  metodo: string;
  conclusion: string;
};

export type Analisis = {
  slug: string;
  imagen: string;
  alt: string;
  es: AnalisisTexto;
  en: AnalisisTexto;
  stack: string[];
};

export type ProyectoDatos = {
  slug: string;
  es: { titulo: string; linea: string };
  en: { titulo: string; linea: string };
};

export const proyectosDatos: ProyectoDatos[] = [
  {
    slug: "facylf",
    es: { titulo: "Fondo Popular", linea: "Base de datos y web del fútbol federado de Castilla y León: recolección, modelo canónico y cobertura medida." },
    en: { titulo: "Fondo Popular", linea: "Database and web front end for federated football in Castile and León: collection, canonical model and measured coverage." },
  },
  {
    slug: "compra-alimentacion",
    es: { titulo: "Cesta", linea: "Comparador de la compra semanal entre supermercados con precio por unidad y calidad del dato medida." },
    en: { titulo: "Cesta", linea: "Weekly grocery comparison across supermarkets with unit price and measured data quality." },
  },
  {
    slug: "data-school",
    es: { titulo: "Data School", linea: "Portal de datos e IA con datasets con licencia, figuras con procedencia y pruebas detrás de cada cifra." },
    en: { titulo: "Data School", linea: "Data and AI portal with licensed datasets, sourced figures and a test behind every number." },
  },
];

export const analisis: Analisis[] = [
  {
    slug: "cobertura-fondo-popular",
    imagen: "/analisis/cobertura-fondo-popular.png",
    alt: "Gráfico de barras con el porcentaje de competiciones completas por temporada en Fondo Popular",
    stack: ["Python", "NumPy", "matplotlib"],
    es: {
      titulo: "Cuánto del catálogo de Fondo Popular está completo",
      pregunta: "De las 867 competiciones del catálogo, ¿cuántas tienen todos sus grupos completos y cómo cambia por temporada?",
      fuente: "Tabla canónica publicada por el proyecto Fondo Popular el 10/11/2026: 15 temporadas, 867 competiciones y 206 completas.",
      metodo: "Cargué la tabla por temporada en NumPy, calculé la cobertura de cada temporada y la media ponderada por número de competiciones, no la media de porcentajes.",
      conclusion: "La cobertura global es del 23,8 %. No es uniforme: la 2020-21 es la más completa (16 de 31, un 51,6 %) y la 2019-20 la que menos (1 de 56, un 1,8 %), porque esa temporada quedó sin cerrar. Las temporadas recientes bajan porque siguen en recolección.",
    },
    en: {
      titulo: "How much of the Fondo Popular catalogue is complete",
      pregunta: "Of the 867 competitions in the catalogue, how many have all their groups complete and how does that change by season?",
      fuente: "Canonical table published by the Fondo Popular project on 10/11/2026: 15 seasons, 867 competitions and 206 complete ones.",
      metodo: "I loaded the per-season table into NumPy, computed the coverage of each season and the weighted average by number of competitions, not the average of percentages.",
      conclusion: "Overall coverage is 23.8 %. It is not uniform: 2020-21 is the most complete (16 of 31, 51.6 %) and 2019-20 the least (1 of 56, 1.8 %), because that season never closed. Recent seasons are lower because they are still being collected.",
    },
  },
  {
    slug: "futbol-goles-xg",
    imagen: "/analisis/futbol-goles-xg.png",
    alt: "Distribución de goles por partido y dispersión de xG frente a goles reales en 380 partidos",
    stack: ["Python", "NumPy", "pandas", "matplotlib"],
    es: {
      titulo: "Goles, xG y ventaja de local",
      pregunta: "¿Se parece lo que generan los equipos (xG) a lo que acaban marcando, y cuánto pesa jugar en casa?",
      fuente: "Dataset CC0 de Data School: 380 partidos con goles, tiros, xG y resultado.",
      metodo: "Con NumPy calculé la media de goles, el reparto entre victoria local, empate y victoria visitante, y la correlación entre el xG del partido y los goles reales.",
      conclusion: "Los partidos acaban con 1,89 goles de media; gana el local en el 45,8 %, hay empate en el 30,0 % y gana el visitante en el 24,2 %. El xG explica parte de lo que pasa (r = 0,44), pero no lo suficiente para predecir un partido suelto: es una señal, no una promesa.",
    },
    en: {
      titulo: "Goals, xG and home advantage",
      pregunta: "Does what teams create (xG) look like what they end up scoring, and how much does playing at home matter?",
      fuente: "CC0 dataset from Data School: 380 matches with goals, shots, xG and result.",
      metodo: "With NumPy I computed the average number of goals, the split between home win, draw and away win, and the correlation between match xG and actual goals.",
      conclusion: "Matches average 1.89 goals; the home side wins 45.8 %, 30.0 % are draws and the away side wins 24.2 %. xG explains part of what happens (r = 0.44), but not enough to predict a single match: it is a signal, not a promise.",
    },
  },
  {
    slug: "ventas-tienda-dia-semana",
    imagen: "/analisis/ventas-tienda-dia-semana.png",
    alt: "Ingresos por tienda y gasto medio por día de la semana en una tienda de barrio",
    stack: ["Python", "NumPy", "pandas", "matplotlib"],
    es: {
      titulo: "Ventas de tres tiendas de barrio",
      pregunta: "¿Qué días vende más una tienda de barrio y cuánto pesa cada tienda en el total?",
      fuente: "Dataset CC0 de Data School: 180 días de ventas de tres tiendas entre enero y junio de 2026.",
      metodo: "Con NumPy sumé los ingresos por tienda y calculé la media por día de la semana agrupando las fechas.",
      conclusion: "Las tres tiendas venden parecido (entre 62 y 65 k€ en seis meses), pero el día pesa: sábado y domingo son los mejores (1.331 € y 1.180 € de media) y el martes el peor (809 €). El fin de semana concentra la caja.",
    },
    en: {
      titulo: "Sales of three neighbourhood stores",
      pregunta: "Which days does a neighbourhood shop sell more, and how much does each store weigh in the total?",
      fuente: "CC0 dataset from Data School: 180 days of sales for three stores between January and June 2026.",
      metodo: "With NumPy I summed revenue per store and computed the average per weekday by grouping the dates.",
      conclusion: "The three stores sell similarly (between €62k and €65k in six months), but the day matters: Saturday and Sunday are the best (€1,331 and €1,180 on average) and Tuesday the worst (€809). The weekend concentrates the takings.",
    },
  },
  {
    slug: "cartera-rentabilidad-volatilidad",
    imagen: "/analisis/cartera-rentabilidad-volatilidad.png",
    alt: "Crecimiento de 1 euro invertido en seis activos durante 60 meses, con rentabilidad y volatilidad anualizadas",
    stack: ["Python", "NumPy", "pandas", "matplotlib"],
    es: {
      titulo: "Rentabilidad y volatilidad de una cartera",
      pregunta: "Si hubiera invertido 1 € en cada activo hace 60 meses, ¿cuánto tendría y con qué volatilidad?",
      fuente: "Dataset CC0 de Data School: 120 meses de retornos mensuales para seis activos.",
      metodo: "Con NumPy calculé el producto acumulado de (1 + retorno) y la volatilidad anualizada como la desviación típica mensual multiplicada por raíz de 12.",
      conclusion: "El índice acabó plano (−1,3 % anual, volatilidad 6,7 %) y el mejor activo rindió un 9,3 % anual con una volatilidad del 21,3 %. Más rentabilidad vino con más vaivenes, y dos acciones perdieron cerca del 40 % en el periodo.",
    },
    en: {
      titulo: "Return and volatility of a portfolio",
      pregunta: "If I had invested €1 in each asset 60 months ago, how much would I have and with what volatility?",
      fuente: "CC0 dataset from Data School: 120 months of monthly returns for six assets.",
      metodo: "With NumPy I computed the cumulative product of (1 + return) and annualised volatility as the monthly standard deviation times the square root of 12.",
      conclusion: "The index ended flat (−1.3 % a year, 6.7 % volatility) and the best asset returned 9.3 % a year with 21.3 % volatility. More return came with more swings, and two stocks lost close to 40 % over the period.",
    },
  },
];
