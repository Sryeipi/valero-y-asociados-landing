# Valero & Asociados — Landing

Landing oficial del estudio jurídico **Valero & Asociados** (Guayaquil, Ecuador). Más de 20 años de trayectoria en derecho civil, corporativo e inmobiliario.

**Producción:** `_Landing_Project/landing/index.html` (HTML + CSS + JS vanilla, sin frameworks pesados).

## Conversión

WhatsApp como único CTA primario. Mensajes pre-rellenados por área (Familia / Empresas / Inmobiliario / Tránsito / Laboral / Migración).

## Stack

- HTML5 + CSS custom properties + JS vanilla
- Imágenes WebP responsive (3 variantes: full / -md / -sm)
- IntersectionObserver para reveals + scroll-driven animations
- prefers-reduced-motion respetado en todo el motion
- SEO local enriquecido con Schema.org LegalService (geo, priceRange, openingHours, contactPoint, knowsAbout, employee, areaServed)

## Deploy

- **Vercel:** apunta a `_Landing_Project/landing/` (configurado vía `vercel.json`)
- **Repo:** branch `fix/landing-coherencia-visual` → merge a `main` cuando se aprueba

## Estructura

```
_Landing_Project/
├── landing/                  # ← lo que se publica
│   ├── index.html
│   ├── favicon.svg
│   ├── og-preview.png
│   └── img/                  # 18 archivos WebP (6 personas × 3 variantes)
├── _tools/                   # scripts Python (rebuild_webp.py)
├── 01_Brief_Estrategico.md
├── 02_Benchmarks_Investigacion.md
├── 03_Prompts_Claude_Design.md
├── 04_Wireframe_y_Estructura.md
├── 05_Reviews_y_Casos.md
├── 06_Obsidian_Claude_Code_Guia.md
├── verification-*            # auditorías Playwright multi-breakpoint
└── img.backup-*              # backups defensivos de iteraciones previas
```

## Reglas duras

- **No reseñas falsas como reales** (ilegal en EC + viola TOS Google).
- **No prometer resultados legales específicos** en copy (riesgo deontológico).
- **WhatsApp temporal:** `+593 959 080 607` (número del operador). Reemplazar cuando el cliente entregue comercial.

## Versión

v6 motion premium — Mayo 2026.
