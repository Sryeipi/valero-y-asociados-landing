---
type: brandkit
domain: clientes
client: Valero y Asociados
tags: [brandkit, valero, paleta, tipografia, sistema-visual]
status: v1-borrador
created: 2026-05-11
updated: 2026-05-11
owner: Brand Intelligence Agent (mode: kit)
source: derivado de _Landing_Project/01_Brief_Estrategico.md
---

# Brandkit operativo - Valero & Asociados v1

## 1. Paleta

| Rol | Token | Hex | Uso |
|---|---|---|---|
| Navy profundo | `--navy` | `#0A1628` | Fondo principal |
| Navy elevado | `--navy-2` | `#142847` | Cards, secciones secundarias |
| Navy alto | `--navy-3` | `#1B3358` | Bordes, highlights navy |
| Dorado bufete | `--gold` | `#D4A84B` | Acento principal, CTAs, ampersand "&" |
| Dorado calido | `--gold-warm` | `#E8B86D` | Hover, brillos |
| Blanco hueso | `--bone` | `#F5F2EB` | Texto principal sobre navy |
| Gris narrativa | `--gray` | `#9AA3B2` | Texto secundario, captions |
| Terracota Familia | `--terracotta` | `#C4533A` | Acento area Familia |
| Verde laurel Empresas | `--laurel` | `#3A8F7D` | Acento area Empresas |
| Azul juridico Inmobiliario | `--jurid` | `#3A6EB5` | Acento area Inmobiliario |

## 2. Tipografia

| Rol | Familia | Pesos | Uso |
|---|---|---|---|
| Display / Headlines | **Fraunces** (Google Fonts) | 400-800 + italic | H1, H2, H3, frases editoriales |
| Body / UI | **Inter** (Google Fonts) | 300-700 | parrafos, navegacion, botones |
| Mono / Labels | **JetBrains Mono** (Google Fonts) | 400-500 | numeracion `01 —`, eyebrows, captions tecnicos |

**Reglas:**
- H1 con tracking apretado (`letter-spacing: -0.02em`).
- Mono siempre uppercase + tracking 0.18em+.
- Italic serif para sub-promesas y quotes.

## 3. Iconografia

- **Line icons 1.5px stroke**, color dorado o hueso.
- Usar **Lucide** o **Phosphor**. Adelgazar si vienen mas gruesos.
- Prohibido: icon packs comerciales, balanzas, martillos de juez, columnas griegas.

## 4. Imaginería

- **Fotos reales del equipo** (las del cliente). Estilo Vanity Fair / Bloomberg Editorial.
- Tratamiento: desaturar ligeramente, mantener temperatura calida ambar.
- Filtro recomendado: `contrast(1.05) brightness(0.95)`.
- Para retratos de equipo en grid: `filter: grayscale(100%)` por defecto, `0%` en hover (transicion 400-500ms).

## 5. Patron de fondo

Grid sutil de puntos/cruces dorados al 6-10% opacidad sobre navy:

```css
background-image: radial-gradient(circle at 1px 1px, rgba(212,168,75,0.06) 1px, transparent 0);
background-size: 32px 32px;
```

## 6. Motion

- **Reveal on scroll** (IntersectionObserver, threshold 0.12).
- **Stagger** 80-120ms entre elementos hermanos.
- **Count-up** para KPIs.
- **Marquee infinito** para credenciales (25-30s loop, pausa al hover).
- **Stroke draw** para marcos dorados (1.8s ease-out).
- **Letter-by-letter fade-in** para H1 hero (25ms delay por letra).
- **Pulse** sutil para WhatsApp flotante (4s, scale 1.0 a 1.08).

**Regla:** todo motion es sutil y tiene proposito. NO gratuito.

## 7. Tono de voz

| Cuando | Como suena |
|---|---|
| Hero | Sobrio, declarativo, con peso |
| Areas | Cercano, claro, sin tecnicismos |
| FAQs | Directo, util, primera persona |
| CTAs | Verbo + beneficio inmediato |

**Reglas duras:**
- Usar **usted** formal en Ecuador (contexto legal).
- Cero superlativos vacios ("los mejores", "lider").
- Cero jerga juridica innecesaria. Si hay termino tecnico (ej. "sucesion intestada"), explicarlo.

## 8. Anti-patrones (NO hacer)

- Glassmorphism saturado.
- Gradientes mesh fluo.
- 3D blob de moda.
- Stock photography generica.
- Iconografia comercial barata.
- Chatbot pop-up agresivo (WhatsApp flotante es suficiente).
- "GANAMOS TU CASO" / "EL MEJOR ABOGADO".
- Logos con balanza, martillo, columna griega.

## 9. Stack tecnico recomendado

- Landing en **un solo HTML** con CSS + JS vanilla. Sin frameworks pesados.
- Google Fonts: `Fraunces` + `Inter` + `JetBrains Mono`.
- Deploy: **Cloudflare Pages** o **Vercel**.
- Schema.org `LegalService` para SEO local.
- Tracking: GA4 + Meta Pixel (cuando el cliente apruebe).

## 10. Estado

- v1 borrador derivado del brief. Sin contraste WCAG validado aun.
- Pendiente: validacion contra fotos reales del equipo (color cast real, no inferido).
- Pendiente: paso por Quality Gate antes de mostrar al cliente.
