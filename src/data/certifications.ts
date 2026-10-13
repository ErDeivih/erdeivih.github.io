export interface Certification {
  title: string;
  issuer: string;
  date: string;
  verification: string;
}

// Añadir únicamente acreditaciones obtenidas y enlaces públicos de verificación.
export const certifications: Certification[] = [];
