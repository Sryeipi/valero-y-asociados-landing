# 04 · Wireframe y Estructura de la Landing

Wireframe en texto (ASCII) + descripción funcional de cada sección. Sirve como mapa antes de meterse a diseñar pixel-perfect.

---

## Vista global (desktop, 1440px)

```
┌──────────────────────────────────────────────────────────────┐
│  V & A  ·  Familia · Empresas · Inmobiliario · Más     [WA] │ ← nav fijo, blur
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   01 — ESTUDIO JURÍDICO · GUAYAQUIL                          │ ← eyebrow mono
│                                                              │
│   Protegemos lo que            [   FOTO AB. NEY VALERO   ]   │ ← H1 serif XL +
│   más te importa.              [   marco dorado animado  ]   │   foto editorial
│                                [   gradient cálido       ]   │
│   Tu familia. Tu empresa.                                    │
│   Tu patrimonio.                                             │
│                                                              │
│   [Conversemos por WhatsApp →]   ·   Consulta inicial gratis │ ← CTA dorado
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ ━━━━━━━ MARQUEE: "20 años · Guayaquil · Ecuador · Civil ━━━ │ ← marquee dorado
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   02 — ÁREAS DE PRÁCTICA                                     │
│                                                              │
│   Tres frentes. Un solo respaldo.                            │
│                                                              │
│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐         │
│   │ FAMILIA      │ │ EMPRESAS     │ │ INMOBILIARIO │         │ ← 3 cards
│   │              │ │              │ │              │         │   hover tilt
│   │ Divorcios    │ │ Constitución │ │ Compraventa  │         │
│   │ Herencias    │ │ Contratos    │ │ Escrituras   │         │
│   │ Custodia     │ │ Compliance   │ │ Arriendos    │         │
│   │              │ │              │ │              │         │
│   │ Tu patrimonio│ │ Tu negocio   │ │ Cada propiedad│        │
│   │ familiar,    │ │ crece, tu    │ │ una certeza  │         │
│   │ blindado     │ │ respaldo     │ │              │         │
│   │              │ │              │ │              │         │
│   │ [WhatsApp →] │ │ [WhatsApp →] │ │ [WhatsApp →] │         │
│   └──────────────┘ └──────────────┘ └──────────────┘         │
│                                                              │
│   ──── Otras áreas: Tránsito · Laboral · Migración ────      │ ← row chips
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   03 — CASOS RESUELTOS                                       │
│                                                              │
│   Más de 800 casos. Cada uno, una decisión bien tomada.      │
│                                                              │
│   ┌──────────┬──────────┬──────────┬──────────┐              │
│   │ 850+     │ 92%      │ 20+      │ 4.8 ★    │              │ ← KPIs grid
│   │ casos    │ resueltos│ años     │ Google   │              │
│   └──────────┴──────────┴──────────┴──────────┘              │
│                                                              │
│   ▶ Scroll horizontal de 6 mini casos anonimizados           │ ← horizontal
│   ┌────────────────────┐ ┌────────────────────┐              │   scroll cards
│   │ "Custodia compartida│ │ "Constitución de    │  → → →      │
│   │  resuelta en 4 sem"│ │  S.A.S. en 72h"     │              │
│   └────────────────────┘ └────────────────────┘              │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   04 — SOBRE EL AB. NEY VALERO                               │
│                                                              │
│   [FOTO RETRATO]   |   "La ley es solo el medio.            │
│                    |    Lo que protegemos es lo que          │
│   ┌───────────┐    |    construiste."                        │ ← split 50/50
│   │           │    |                                         │
│   │  Foto     │    |   Más de 20 años ejerciendo derecho    │
│   │  editorial│    |   civil, corporativo e inmobiliario     │
│   │           │    |   en Guayaquil.                          │
│   │           │    |                                         │
│   └───────────┘    |   Miembro del Colegio de Abogados...    │
│                    |                                         │
│                    |   [Conoce al equipo →]                  │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   05 — EQUIPO                                                │
│                                                              │
│   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                │
│   │  NEY   │ │ HENRY  │ │ ALICIA │ │ DANIEL │                │ ← 4 retratos
│   │ socio  │ │ socio  │ │ asocia │ │ asocia │                │   bw → color
│   │ fundad.│ │        │ │        │ │        │                │   on hover
│   └────────┘ └────────┘ └────────┘ └────────┘                │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   06 — LO QUE DICEN NUESTROS CLIENTES                        │
│                                                              │
│   ★★★★★ "..."                                                │
│   ★★★★★ "..."           [scroll vertical de 12 reseñas]      │ ← masonry o
│   ★★★★★ "..."                                                │   vertical scroll
│                                                              │
│   [Ver todas en Google →]                                    │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   07 — PREGUNTAS FRECUENTES                                  │
│                                                              │
│   ▾ ¿La primera consulta es gratuita?                        │
│   ▾ ¿Atienden por WhatsApp?                                  │ ← acordeón
│   ▾ ¿Cuánto cobran un divorcio?                              │   con dorado
│   ▾ ¿Dónde queda la oficina?                                 │
│   ▾ ¿Manejan casos fuera de Guayaquil?                       │
│   ▾ ¿Cuánto tarda un divorcio en Ecuador?                    │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   08 — CIERRE / CTA FINAL                                    │
│                                                              │
│         La primera conversación es por WhatsApp.             │ ← bloque XL
│         Las decisiones importantes, en persona.              │
│                                                              │
│         [Hablar por WhatsApp →]                              │ ← CTA grande
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  FOOTER · Dirección GYE · Tel · Email · IG · LinkedIn        │
│  © 2026 Valero & Asociados · Política de privacidad          │
└──────────────────────────────────────────────────────────────┘

      [WhatsApp flotante ●]  ← bottom-right siempre visible
```

---

## Vista mobile (375px)

```
┌────────────────────┐
│  V&A         ☰     │ ← burger menu
├────────────────────┤
│ 01 — ESTUDIO JUR.. │
│                    │
│ Protegemos lo que  │ ← H1 más compacto
│ más te importa.    │
│                    │
│ [ FOTO Ab. Ney ]   │ ← foto debajo, no
│                    │   side by side
│ [WhatsApp →]       │
├────────────────────┤
│ ━━━ MARQUEE ━━━    │
├────────────────────┤
│ 02 — ÁREAS         │
│ ┌────────────────┐ │
│ │ FAMILIA        │ │ ← cards apiladas
│ │ ...            │ │
│ └────────────────┘ │
│ ┌────────────────┐ │
│ │ EMPRESAS       │ │
│ └────────────────┘ │
│ ...                │
└────────────────────┘
       [WA ●]
```

---

## Inventario de microinteracciones

| Elemento | Animación | Duración | Trigger |
|---|---|---|---|
| Headline hero | Letter-by-letter fade-in | 1.4s | On load |
| Marco dorado foto Ney | Línea dibujada (stroke-dashoffset) | 1.8s | On load |
| Marquee 20 años | Loop horizontal continuo | infinito | siempre |
| Cards de áreas | Tilt 3D suave + glow dorado | 300ms | hover |
| KPIs (850+, 92%) | Count-up de 0 al valor | 1.5s | viewport-in |
| Casos scroll horizontal | Snap entre cards + cursor "drag" | — | scroll |
| Equipo (retratos) | B/N → color | 400ms | hover |
| Acordeón FAQ | Slide-down + chevron rotate 180º | 250ms | click |
| Botón WhatsApp flotante | Pulse sutil cada 4s | 1.2s | siempre |
| Page scroll | Progress bar dorada arriba | — | scroll |

---

## Jerarquía tipográfica

```
H1 Hero       Serif Bold      72-96px  (mobile: 40-48px)
H2 Sección    Serif Semibold  48-56px  (mobile: 32-36px)
H3 Card       Sans Semibold   24px
Eyebrow       Mono Uppercase  13px tracking 0.2em
Body L        Sans Regular    18-20px  line-height 1.6
Body          Sans Regular    16px     line-height 1.6
Caption       Sans Regular    13px     color gris narrativa
```

---

## CTAs primarios y secundarios

| Posición | Texto | Acción |
|---|---|---|
| Hero (primario) | **Conversemos por WhatsApp** → | WhatsApp con mensaje genérico |
| Áreas Familia | WhatsApp Familia → | WhatsApp con mensaje "Familia" pre-rellenado |
| Áreas Empresas | WhatsApp Empresas → | WhatsApp con mensaje "Empresas" pre-rellenado |
| Áreas Inmobiliario | WhatsApp Inmobiliario → | WhatsApp con mensaje "Inmobiliario" pre-rellenado |
| Sobre Ney | Conoce al equipo → | Scroll a sección equipo |
| Cierre | **Hablar por WhatsApp** → | WhatsApp genérico, mensaje "general" |
| Flotante (fijo) | ● icono | WhatsApp genérico, siempre visible |
