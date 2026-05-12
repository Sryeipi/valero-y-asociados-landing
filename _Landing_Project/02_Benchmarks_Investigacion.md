# 02 · Benchmarks e Investigación — Webs de abogados 2026

Investigación cruzada en Awwwards, agencias especializadas (Pravaah, Clio, Magnify Lab, Parallel HQ) y bufetes ecuatorianos. Lo organizo de **referente → qué tomar → qué evitar**.

---

## A · Referentes globales premium

### 1. Kirkland & Ellis
- **Qué tomar:** Esquema blanco-negro con jerarquía tipográfica que transmite autoridad sin ornamento. Headlines en serif XL.
- **Qué evitar:** Demasiado corporativo / frío — Valero necesita más calidez humana.

### 2. AttorneyX (Awwwards nominee)
- **Qué tomar:** Rebrand que rompe con la estructura clásica "team + bios". Hero como manifiesto.
- **Qué evitar:** El brutalismo extremo — no encaja con público ecuatoriano 35-60 años.

### 3. Lajos Law Firm (Awwwards nominee)
- **Qué tomar:** Motion graphics 2D sutiles que ANUNCIAN servicios al hacer scroll. Geometría limpia, sin distraer.
- **Qué evitar:** Su paleta es muy fría (gris/azul eléctrico). Valero va por dorado cálido.

### 4. Russell-Cooke (Reino Unido)
- **Qué tomar:** Dark palette navy + verde profundo con acentos sobrios. Tipografía editorial.
- **Qué evitar:** Densidad excesiva de información en la home — no scrollea fácil en mobile.

### 5. Infense (Awwwards honorable mention)
- **Qué tomar:** Transiciones de página tipo "cortinas" cinematográficas. Cada sección es un acto.
- **Qué evitar:** Requiere JS pesado / no es SEO-friendly. Adaptar a CSS puro.

### 6. Michael Gonzalez Attorney At Law (Awwwards)
- **Qué tomar:** Hispano-friendly. Hero con retrato grande del abogado + name + claim. Es la fórmula que mejor funciona para abogados-marca.
- **Qué evitar:** Falta de áreas claras de práctica — todo se siente "general".

---

## B · Referentes regionales (Latam / Ecuador)

### 7. Coronel y Pérez — Guayaquil ([coronelyperez.com](https://coronelyperez.com))
- **Qué tomar:** Es el referente local. Branding institucional sobrio, dark mode con dorado. Navegación clarísima por área de práctica.
- **Qué evitar:** Es 100% corporativo internacional — no agendan por WhatsApp, no muestran precios, no hay calor humano. Valero juega exactamente al revés de eso. **Diferenciación = humanidad + WhatsApp + cercanía.**

### 8. Bufetes en directorios de Awwwards (Brill Law Group, McKeen Law, Gabriela Bar - Law & AI, Eskesen Law)
- **Qué tomar:** Estructura: hero con foto editorial → manifiesto → 3 áreas → caso destacado → "sobre el abogado" → CTA. Es el "framework" ganador 2025-2026.

---

## C · Síntesis: qué define a una landing de abogados de 2026

### Visual
1. **Dark backgrounds con un acento cálido único** (dorado, ámbar, terracota) — nunca paleta multi-color.
2. **Serif editorial en headlines + sans en body** — ratio 70/30. Da peso histórico sin perder modernidad.
3. **Una sola foto humana hero** (no carrusel) — el abogado mirando a cámara, retrato medio.
4. **Patrones sutiles de fondo** (grid, ruido, líneas) al 5-10% de opacidad. Genera profundidad sin ruido.
5. **Microinteracciones premiadas:** scroll progress, hover en cards con tilt sutil, marquees de prensa/reseñas.

### Motion (la parte de "hypermotion 2026")
- **Scroll-linked animations** — los textos aparecen a medida que el usuario scrollea, no de golpe. Usar `IntersectionObserver` + `transform: translateY`.
- **Letter-by-letter fade-in en headline hero** (3-4 segundos total).
- **Marquee horizontal de "frases del bufete"** o de logos de prensa/aliados.
- **Cursor custom sutil** — solo desktop, círculo de 12px que se agranda en links.
- **Page transitions cinemáticas:** cortina que sube del navy oscuro entre páginas (1.2s).
- **Parallax leve** (factor 0.3-0.5) en hero photo. Nunca en texto.
- **Hero frames** — la foto del Ab. Ney aparece "enmarcada" por una línea dorada que se dibuja en 1.5s al cargar.

### Estructura (orden ganador)
```
1. Hero — manifiesto + foto + 1 CTA WhatsApp
2. Áreas de práctica (3 + las extras)
3. Caso destacado / Reseñas con scroll horizontal
4. "Sobre el Ab. Ney" — años, valores, foto
5. Equipo (los 4 retratos editoriales)
6. FAQs (acordeón)
7. Cierre — CTA final fuerte + WhatsApp flotante
```

### Lo que la diferencia del 95% de webs de abogados
- **NO** "Bienvenido a [Nombre del bufete]" en hero. Esa frase mata la conversión.
- **NO** carrusel de servicios con icono genérico de balanza.
- **NO** formulario de contacto largo. Solo WhatsApp + un email único.
- **SÍ** mostrar el número de casos resueltos (anonimizados pero específicos: *"180+ divorcios resueltos. 92% por mutuo acuerdo"*).
- **SÍ** mostrar precios o rangos. Aunque sea *"desde $X"*. Rompe la fricción #1.

---

## D · Fuentes de inspiración consultadas

Para que abras y mires tú mismo:

- [Awwwards — Law firm websites](https://www.awwwards.com/websites/law/)
- [Infense - Awwwards](https://www.awwwards.com/sites/infense-lawyers)
- [Lajos Law Firm - Awwwards](https://www.awwwards.com/sites/lajos-law-firm)
- [AttorneyX - Awwwards](https://www.awwwards.com/sites/attorneyx)
- [Coronel y Pérez (Guayaquil, EC)](https://coronelyperez.com/en/)
- [Best Law Firm Websites 2026 — Clio](https://www.clio.com/blog/best-law-firm-websites/)
- [30 Amazing Law Firm Website Designs — Magnify Lab](https://www.magnifylab.com/blog/best-law-firm-website-designs/)
- [15+ Best Law Firm Website Designs 2026 — Pravaah](https://www.pravaahconsulting.com/post/best-attorney-firm-website-designs)
- [20 páginas web abogados con diseños modernos — Mitziweb](https://www.mitziweb.com/blog/20-paginas-web-abogados-disenos-modernos/)
