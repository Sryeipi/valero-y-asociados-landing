# 03 · Prompts listos para Claude Design / Canva / cualquier IA de diseño

**Cómo usarlos:**
1. Subí primero `01_Brief_Estrategico.md` + las fotos del equipo a la conversación.
2. Después pegá los prompts uno por uno. No los pegues todos juntos — cada uno es una sección.
3. Si la herramienta es Claude Design (artifacts), genera componente por componente y luego le pedís que los una.
4. Si es Canva, cada prompt es un slide / página de tu diseño.

---

## 🎯 Prompt 0 — Contexto inicial (pegá esto SIEMPRE primero)

```
Eres un diseñador senior de producto digital especializado en branding profesional 
y experiencias web 2026. Vas a diseñar una landing page para Valero & Asociados, 
estudio jurídico de Guayaquil, Ecuador (más de 20 años de trayectoria).

Sistema visual obligatorio:
- Paleta: navy profundo #0A1628 (fondo) + dorado #D4A84B (acento) + blanco hueso 
  #F5F2EB (texto). Acentos verticales solo en áreas de práctica: 
  Familia #C4533A, Empresas #3A8F7D, Inmobiliario #3A6EB5.
- Tipografía: serif editorial (Fraunces) para headlines + sans neutra (Inter) para 
  body + mono (JetBrains Mono) para labels/numeración.
- Imaginería: fotos editoriales del equipo (estilo Vanity Fair, biblioteca con 
  libros de derecho, iluminación cálida ámbar). NO usar stock photos genéricas.
- Patrón de fondo: grid sutil de cruces "+" al 6% opacidad sobre el navy.
- Espíritu: minimalista + editorial + motion sutil estilo Awwwards 2026. NO 
  agencia tech, NO glassmorphism, NO gradientes mesh.

Filosofía: "old money con tecnología 2026". El bufete tiene historia + nuevos socios 
jóvenes. La web debe transmitir peso institucional sin sentirse vieja.

Confirma que entendiste y esperá mis prompts sección por sección.
```

---

## 🦸 Prompt 1 — Hero

```
Diseñá el HERO de la landing.

Estructura:
- Split 60/40 horizontal en desktop (texto izquierda / foto derecha).
- En mobile, texto arriba y foto debajo.

Texto izquierdo (orden vertical):
- Eyebrow en mono uppercase 13px: "01 — ESTUDIO JURÍDICO · GUAYAQUIL"
- H1 en serif XL (72-96px desktop): "Protegemos lo que más te importa."
- Subtítulo serif italic 28px en dos líneas: "Tu familia. Tu empresa. Tu patrimonio."
- Espacio
- Botón principal dorado #D4A84B con texto navy: "Conversemos por WhatsApp →"
- Subtexto bajo botón en gris narrativa 14px: "Consulta inicial gratuita · 30 min"

Imagen derecha:
- Retrato editorial del Ab. Ney Valero, encuadre medio.
- Marco dorado de 2px alrededor de la foto que se "dibuja" en 1.8s al cargar 
  (efecto stroke-dashoffset).
- Sutil parallax 0.3 al hacer scroll.
- Glow ambar muy sutil detrás de la foto.

Microinteracciones:
- El H1 hace fade-in letra por letra, 1.4 segundos total.
- El marco dorado se traza después de cargar la foto.

Patrón de fondo de cruces "+" al 6% sobre todo el hero.

Devolveme el código completo (HTML + Tailwind o CSS), responsive.
```

---

## 📜 Prompt 2 — Marquee de credenciales

```
Diseñá un marquee horizontal infinito justo debajo del hero.

Contenido (repetir 3 veces, separados por · dorados):
20 AÑOS DE TRAYECTORIA · GUAYAQUIL · CIVIL · CORPORATIVO · INMOBILIARIO · 
COLEGIO DE ABOGADOS DEL GUAYAS · MÁS DE 850 CASOS · 4.8★ EN GOOGLE

Estilo:
- Fondo navy elevado #142847, alto 56px.
- Texto en mono uppercase 14px, tracking 0.2em, color dorado #D4A84B.
- Velocidad: 25 segundos por loop completo.
- Sin fade en los bordes (entra y sale directo).
- Pausa al hover (estado "respirando").

Solo CSS, sin JS.
```

---

## 🧩 Prompt 3 — Áreas de práctica (3 cards + chips de extras)

```
Diseñá la sección "Áreas de práctica" con esta estructura:

Cabecera:
- Eyebrow mono: "02 — ÁREAS DE PRÁCTICA"
- H2 serif: "Tres frentes. Un solo respaldo."
- Sub gris narrativa: "Cada área tiene su propio abogado responsable. 
  Conversemos sobre el tuyo."

3 cards en grid horizontal (en mobile se apilan).

Card FAMILIA:
- Línea superior decorativa de 32px en color #C4533A (terracota).
- H3 serif: "Familia"
- Tag italic dorado: "Tu patrimonio familiar, blindado"
- Lista de 4 servicios (sin bullets, en líneas separadas con gris):
  Divorcios y separaciones
  Herencias y sucesiones
  Custodia y régimen de visitas
  Uniones de hecho
- Botón fantasma "Conversar por WhatsApp →" en dorado, hover llena el fondo.

Card EMPRESAS:
- Mismo template, línea en #3A8F7D (verde laurel).
- H3: "Empresas"
- Tag: "Tu negocio crece, tu respaldo legal también"
- Servicios: Constitución de compañías / Contratos comerciales / Compliance y junta 
  de accionistas / Asesoría laboral empresarial

Card INMOBILIARIO:
- Línea en #3A6EB5 (azul jurídico).
- H3: "Inmobiliario"
- Tag: "Cada propiedad, una certeza"
- Servicios: Compraventa y escrituras / Due diligence inmobiliaria / Arriendos y 
  desahucios / Levantamiento de gravámenes

Debajo, fila horizontal de chips:
"También llevamos:" + chips clickeables: Tránsito · Laboral · Migración

Microinteracciones cards:
- Hover: card se levanta 4px, sombra dorada de 0px 12px 30px rgba(212,168,75,0.15), 
  tilt 3D máximo 2 grados según posición del cursor.
- Las cards aparecen una a una con stagger de 120ms al entrar al viewport.

Devolveme HTML + CSS responsive.
```

---

## 📊 Prompt 4 — Casos resueltos + scroll horizontal

```
Diseñá dos bloques unidos:

BLOQUE A — Grid de KPIs (4 columnas en desktop, 2x2 en mobile):
1. 850+ Casos resueltos
2. 92% Resueltos sin juicio
3. 20+ Años de trayectoria
4. 4.8 ★ En Google (3 fuentes)

Cada KPI:
- Número grande en serif 64px dorado.
- Label debajo en sans 14px gris narrativa.
- Animación count-up de 0 al valor en 1.5s cuando entra al viewport.
- Línea divisoria vertical entre columnas, 1px en navy elevado.

BLOQUE B — Casos destacados (scroll horizontal):
- H2 serif: "Casos que cambiaron una vida"
- Sub: "Resúmenes anonimizados de los últimos 12 meses."
- 6 cards en scroll horizontal con snap:
  - Cada card 380px ancho, 280px alto.
  - Border 1px navy elevado.
  - Padding 32px.
  - Tag superior por área (terracota / verde / azul).
  - H4 en serif 22px: título del caso.
  - Texto body en 14px: 2-3 líneas de descripción.
  - Footer: "Resuelto en X semanas" en mono uppercase 11px dorado.

Casos (sacar de archivo 05_Reviews_y_Casos.md):
- Caso 1 [Familia]: "Custodia compartida resuelta sin juicio"
- Caso 2 [Empresas]: "S.A.S. constituida en 72 horas"
- Caso 3 [Inmobiliario]: "Compraventa de $280K asegurada en notaría"
- Caso 4 [Familia]: "Herencia con 4 herederos, partición consensuada"
- Caso 5 [Empresas]: "Despido intempestivo: liquidación correcta sin litigio"
- Caso 6 [Inmobiliario]: "Levantamiento de hipoteca de 2008 destrabado"

Microinteracciones:
- Cursor cambia a "drag" cuando entra a la zona de scroll horizontal.
- Cards no visibles tienen opacity 0.6, la del centro 1.0.

Devolveme HTML + CSS + el JS mínimo para el snap y el count-up.
```

---

## 👔 Prompt 5 — Sobre el Ab. Ney + Equipo

```
Diseñá dos bloques.

BLOQUE A — "Sobre el Ab. Ney Valero":
Split 50/50:
- Izquierda: foto retrato del Ab. Ney (IMG_7220.jpg), ocupa todo el alto, marco 
  dorado 2px que se dibuja al hacer scroll.
- Derecha:
  - Eyebrow mono: "04 — EL FUNDADOR"
  - Quote en serif italic 36px: "La ley es solo el medio. Lo que protegemos es 
    lo que construiste."
  - Atribución en mono uppercase 12px: "— AB. NEY ANTONIO VALERO BRANDO"
  - Párrafo en body: "Más de 20 años ejerciendo derecho civil, corporativo e 
    inmobiliario en Guayaquil. Especialidades: sucesiones, compraventa de 
    propiedades y contratos comerciales complejos."
  - Lista de credenciales en mono 13px:
    · Universidad de Guayaquil — Doctor en Jurisprudencia
    · Miembro del Colegio de Abogados del Guayas
    · Más de 850 casos resueltos
  - Botón fantasma: "Conoce al equipo →"

BLOQUE B — Equipo:
- Eyebrow mono: "05 — EQUIPO"
- H2 serif: "Cuatro abogados. Una sola promesa."
- Grid de 4 columnas con foto + nombre + rol.
- Cada foto: 280x360px, ratio 3:4, marco dorado al hover.
- Filtro blanco y negro por defecto, color al hover (transición 400ms).
- Bajo la foto:
  - Nombre en serif 20px
  - Rol en mono uppercase 11px gris (ej. "SOCIO FUNDADOR")
  - 2 áreas chip pequeñas (ej. Familia · Inmobiliario)

Personas:
1. Ab. Ney Antonio Valero Brando — Socio fundador — Civil · Inmobiliario
2. Ab. Henry Valero — Socio — Corporativo · Inmobiliario
3. Abg. Alicia Mendoza — Asociada senior — Familia · Laboral
4. Abg. Daniel Carrera — Asociado — Tránsito · Corporativo

Devolveme HTML + CSS responsive.
```

---

## 💬 Prompt 6 — Reseñas (masonry vertical)

```
Diseñá un bloque de reseñas estilo masonry de 3 columnas.

Cabecera:
- Eyebrow mono: "06 — RESEÑAS"
- H2 serif: "Lo que dicen quienes ya pasaron por aquí."
- Sub: "Reseñas verificadas en Google. Última actualización: mayo 2026."

12 cards en masonry de 3 columnas (en mobile 1 columna).

Cada card:
- Fondo navy elevado #142847, borde 1px navy oscuro.
- 5 estrellas doradas pequeñas en la parte superior.
- Quote en serif italic 17px, 3-5 líneas.
- Footer:
  - Iniciales en círculo dorado 32px (ej. "MF")
  - Nombre + apellido inicial: "María F."
  - Caption: "Divorcio · 2024"
- Padding 24px.

Mezclar tamaños de quote para crear el efecto masonry.

Contenido: usar las 12 reseñas del archivo 05_Reviews_y_Casos.md.

Microinteracciones:
- Cards aparecen con stagger 80ms al entrar al viewport.
- Hover: card se levanta 2px + glow dorado sutil.

Bajo el masonry, CTA dorado fantasma: "Ver todas en Google →" con icono de Google.
```

---

## ❓ Prompt 7 — FAQ acordeón

```
Diseñá una sección de FAQ con 6 preguntas.

Estructura:
- Eyebrow mono: "07 — PREGUNTAS FRECUENTES"
- H2 serif: "Las preguntas que recibimos todas las semanas."
- Acordeón vertical, una pregunta por fila.

Cada fila:
- Pregunta a la izquierda en serif 22px.
- Chevron dorado a la derecha (rota 180º al abrir).
- Al click: slide-down de la respuesta en body 16px, padding-top 16px.
- Divisor 1px en navy elevado entre filas.
- Solo una abierta a la vez.

Preguntas y respuestas:
1. ¿La primera consulta es gratuita?
   Sí. Te ofrecemos 30 minutos por WhatsApp o videollamada sin costo para 
   entender tu caso y decirte honestamente si podemos ayudarte y cuánto costaría.

2. ¿Atienden por WhatsApp?
   Sí, es nuestro canal principal. Respondemos consultas de lunes a viernes de 
   8:00 a 18:00. Para temas urgentes fuera de horario, dejá tu mensaje y 
   contestamos a primera hora del día siguiente.

3. ¿Cuánto cobran por un divorcio?
   Depende del tipo. Un divorcio por mutuo acuerdo (consensual) ronda los 
   $350-$600 USD. Un divorcio contencioso con bienes de por medio puede ir desde 
   $900 USD. Te damos el presupuesto exacto en la primera llamada.

4. ¿Dónde queda la oficina?
   Estamos en [Dirección Guayaquil placeholder]. Recibimos en oficina con cita 
   previa. La mayoría de la coordinación se hace por WhatsApp/Zoom para ahorrarte 
   tiempo.

5. ¿Manejan casos fuera de Guayaquil?
   Sí. Llevamos casos en Quito, Cuenca y Manta con red de corresponsales. Para 
   trámites notariales o audiencias presenciales coordinamos un colega local 
   bajo nuestra dirección.

6. ¿Cuánto tarda un divorcio en Ecuador?
   Por mutuo acuerdo: 30 a 60 días desde que se presenta la demanda. Contencioso 
   con bienes y custodia: 6 a 18 meses dependiendo del juzgado. En nuestra 
   experiencia, el 92% de nuestros casos se resuelven sin llegar a juicio largo.

Devolveme HTML + JS mínimo para el toggle.
```

---

## 🏁 Prompt 8 — Cierre + footer

```
Diseñá el bloque de cierre + footer.

BLOQUE CIERRE:
- Fondo navy oscuro #0A1628 a sangre.
- Padding vertical 160px.
- Centrado:
  - Eyebrow mono dorado: "EMPECEMOS POR LO MÁS FÁCIL"
  - H2 serif 64px: "La primera conversación es por WhatsApp."
  - Sub serif italic 28px: "Las decisiones importantes, en persona."
  - Espacio 48px.
  - Botón XL dorado #D4A84B: "Hablar por WhatsApp →"
  - Bajo el botón en mono 12px gris: "Respondemos en menos de 2 horas hábiles."

FOOTER:
Grid 4 columnas:
- Col 1: Logo "V & A" + tagline "Valero & Asociados · Estudio Jurídico" + 
  dirección Guayaquil.
- Col 2: Áreas — Familia · Empresas · Inmobiliario · Tránsito · Laboral · Migración
- Col 3: Contacto — WhatsApp +593 000 000 000 · email placeholder · horario L-V 8-18
- Col 4: Social — Instagram · LinkedIn · Google Maps · ícono y handle

Línea inferior:
- "© 2026 Valero & Asociados. Todos los derechos reservados."
- "Política de privacidad · Términos · Cookies"

WHATSAPP FLOTANTE:
- Bottom-right, 64px de diámetro, dorado.
- Icono WhatsApp navy adentro.
- Pulse animation: scale 1 → 1.08 → 1 cada 4 segundos.
- Tooltip al hover: "¿Te ayudamos?"

Devolveme HTML + CSS completos.
```

---

## 🧪 Prompt 9 — Sistema de diseño (componentes reutilizables)

```
Generá una página de documentación con el design system completo:

1. Paleta de colores en swatches grandes con HEX y nombre.
2. Escala tipográfica con muestras (H1 a body, captions, mono).
3. Botones (primario, secundario, fantasma) en 3 estados (normal, hover, disabled).
4. Cards (default, hover, elevated) con sombras documentadas.
5. Inputs (texto, textarea, select) en 3 estados.
6. Iconos: set base de 16 íconos line (1.5px stroke) en dorado y blanco hueso.
7. Espaciado: escala de 4 → 64px con muestra visual.
8. Grid system: 12 columnas desktop, 4 mobile, gutters 24px.

Devolveme una página HTML con todo, formato style-guide.
```

---

## ✍️ Prompt 10 — Versión "Claude Design rápido" (si querés todo de una)

```
Construime una landing page completa en un solo archivo HTML autocontenido para 
"Valero & Asociados", estudio jurídico de Guayaquil, Ecuador.

Sistema visual: navy #0A1628 fondo, dorado #D4A84B acento, blanco hueso #F5F2EB 
texto. Tipografía: Fraunces serif para títulos, Inter sans para body (cargá de 
Google Fonts).

Estructura:
1. Nav fijo translúcido con blur backdrop
2. Hero split: H1 "Protegemos lo que más te importa." + foto del abogado + CTA WhatsApp
3. Marquee de credenciales en mono uppercase
4. 3 cards de áreas (Familia / Empresas / Inmobiliario) con sub-promesa cada una
5. Grid de KPIs con count-up: 850+ casos, 92% sin juicio, 20+ años, 4.8★
6. Scroll horizontal de 6 casos anonimizados
7. Bloque "Sobre el Ab. Ney" con quote + foto
8. Grid 4 retratos del equipo con BW→color hover
9. Masonry de 12 reseñas
10. FAQ acordeón de 6 preguntas
11. Cierre con CTA WhatsApp XL
12. Footer 4 columnas

Microinteracciones obligatorias: fade-in letra por letra en H1, marco dorado que 
se dibuja en la foto del hero, marquee infinito, count-up en KPIs, scroll-snap 
horizontal en casos, BW→color en equipo, acordeón FAQ, WhatsApp flotante con pulse.

Patrón de fondo: SVG inline de cruces "+" al 6% opacidad sobre navy.

WhatsApp number placeholder: +593 000 000 000. Mensajes pre-rellenados por área.

Mobile-first responsive. Lighthouse score 95+. SEO meta tags completos. Schema.org 
LegalService.

Tono cercano pero institucional. Sin clichés legales (nada de balanzas, nada de 
"el mejor abogado").

Devolveme el HTML completo en un solo bloque.
```

> **Tip:** El prompt 10 es el "todo en uno" para si tenés prisa. Los prompts 1-9 son para iterar componente por componente, que es como deberías hacerlo si querés un resultado pulido.
