# PROMPT_FIX_LANDING.md
**Para pegar en Claude Code, sesión activa, branch nueva.**

Fecha: 2026-05-12 · Después de auditar la versión actual del HTML y los screenshots de verificación, identificamos 5 problemas raíz. Este prompt los ataca quirúrgicamente. **No es un rediseño completo** — son cirugías puntuales con commits chicos.

---

## Pegale a Claude Code esto, tal cual

```
Claude. Auditamos el index.html actual y los screenshots de 
verification-20260511-205845/ y encontramos 5 problemas concretos. Necesito que 
los arregles uno por uno, en este orden exacto, cada uno en su propio commit.

ANTES DE EMPEZAR — Briefing del problema

1. Las proporciones de las fotos no encajan en los slots. Cuatro de cinco 
   retratos del equipo son HORIZONTALES (adrian, patricia, daniel ~4:3, MAIN 
   ~3:2). Solo ney.jpg es VERTICAL (2:3). Pero la página fuerza aspect-ratio 
   3/4 vertical en hero y team-grid, lo que recorta caras y deja torsos.

2. Hay imágenes generadas (scene-01 a scene-08, editorial-01/02/03) que no 
   estaban en el brief original. Mezclan aspect ratios distintos en la galería 
   .atmosphere → ese es el "collage horrible" que el cliente identificó.

3. La página creció a 12-14 secciones cuando el wireframe original tenía 8. 
   Aparecieron .hero-cinema, .process con fotos, .atmosphere — todo agregado 
   en iteraciones sin pasar por el wireframe.

4. La misma persona aparece varias veces (Ney en hero + founder + team-grid). 
   Genera redundancia y sensación de relleno.

5. El object-position está hardcodeado global ("center 20%"). No funciona para 
   fotos donde la cara está en otra parte del frame.

REGLAS IRRENUNCIABLES — aplicalas en todos los pasos

R1 · Una sección, una proporción. Si las fotos de un grid son horizontales, 
     el grid es horizontal (cards 4:3 o 16:9). No mezclar.
R2 · Cada persona aparece UNA sola vez en toda la página.
R3 · Eliminar la sección .atmosphere completa. Mover las imágenes scene-* y 
     editorial-* a una carpeta de backup, NO borrarlas del disco.
R4 · La sección .process se mantiene pero SIN fotos. Solo tipografía + 
     números grandes + 3 iconos line. La hacemos editorial, no ilustrada.
R5 · La sección .hero-cinema (Ken Burns slideshow con scene-04/scene-07) se 
     elimina. El hero queda solo con texto + foto vertical de Ney.
R6 · object-position por imagen, no global. Cada <img> con su propio 
     style="object-position: X% Y%" calibrado.
R7 · Volver a 8 secciones máximo. Si dudás si una sección debe quedarse, 
     parámente y pregúntame.

QUÉ NO TOCAR

· Los tokens CSS (variables :root con paleta, tipografías).
· La nav, el marquee, los KPIs, las reseñas, el FAQ, el cierre, el footer, 
  el WhatsApp flotante. Esos están bien.
· El JSON-LD schema (LegalService).
· El número de WhatsApp (+593 959 080 607).

PLAN DE EJECUCIÓN — un commit por paso

Paso 1 — Crear branch
  git checkout -b fix/landing-coherencia-visual

Paso 2 — Backup defensivo
  · Mover img/scene-*.webp y img/scene-*-md.webp y img/scene-*-sm.webp a 
    img.backup-scenes-20260512/
  · Mover img/editorial-*.webp (todas las variantes) a 
    img.backup-editorials-20260512/
  · Commit: "chore: backup scenes y editorials antes de fix visual"

Paso 3 — Eliminar .hero-cinema
  · Borrar el bloque <div class="hero-cinema">...</div> y todo su CSS y JS 
    asociado (data-label, ken-slide, etc).
  · El hero principal pasa a ser la primera sección visible debajo de la nav.
  · Commit: "feat(hero): elimina hero-cinema, deja solo hero principal"

Paso 4 — Fix del hero
  · El hero usa img/ney.webp (la versión vertical de ney.jpg) — confirmá que 
    es la vertical, no la grupal.
  · Cambiá object-position de "center 20%" a "center 15%" para que se vea 
    la cara completa, no el torso.
  · Eliminá la sección "founder" (la que repite a Ney con quote grande). La 
    quote del fundador se mueve AL hero como sub-eyebrow:
      <div class="hero-quote">"La ley es solo el medio. Lo que protegemos 
      es lo que construiste." — Ab. Ney Valero</div>
    Estilo: serif italic 18px, color gray-2, max-width 480px, margin-top 16px 
    después del subtítulo, antes del CTA.
  · Commit: "fix(hero): encuadre correcto + absorbe quote del fundador"

Paso 5 — Eliminar .atmosphere completa
  · Borrar la sección <div class="atmosphere">...</div> entera, su CSS y el 
    item correspondiente del array de breadcrumbs/section-index ({sel:'.atmosphere'...}).
  · Renumerar los eyebrows de las secciones siguientes si los hay.
  · Commit: "feat: elimina seccion atmosphere"

Paso 6 — Refactor .process SIN fotos
  · Mantener la estructura .process-grid pero quitar TODAS las <img>.
  · Cada step queda con:
      - Número grande arriba en serif, font-size 80px, color gold, opacity 0.4
      - Eyebrow mono (ej: "PASO 01")
      - H3 serif (título del paso)
      - Body sans (descripción)
      - Icono line SVG dorado 32px, stroke 1.5 (uno por paso)
  · Los 3 pasos sugeridos:
      01 · Conversación inicial — "Hablamos por WhatsApp 30 minutos. Sin compromiso. 
            Te decimos si tu caso es para nosotros o te referimos."
      02 · Diagnóstico y plan — "Revisamos documentos, evaluamos riesgos y te 
            entregamos un plan de acción con presupuesto cerrado por escrito."
      03 · Ejecución y cierre — "Ejecutamos. Te avisamos cada hito por WhatsApp. 
            Al cerrar el caso, tenés documentación firmada y registro completo."
  · Animación: stagger reveal de los 3 pasos al entrar al viewport (delay 120ms 
    entre cada uno). NO sticky steps, NO scroll-linked complicado. Simple y limpio.
  · Commit: "refactor(process): elimina imagenes, pasa a sistema tipografico + iconos"

Paso 7 — Fix del team grid
  · Cambiar el aspect-ratio del .member-photo de 3/4 a 4/5 (vertical pero menos 
    extremo). Las fotos horizontales (adrian, patricia, daniel) van a recortar 
    pero menos agresivamente.
  · MEJOR ALTERNATIVA: usar aspect-ratio 4/3 (horizontal) y aceptar que sea un 
    grid de retratos editoriales horizontales. Es más fiel a las fotos originales.
  · Aplicar object-position por persona:
      - Ney (si está en team grid): "center 20%"
      - Adrián: "center 30%"
      - Patricia: "center 35%"
      - Daniel: "center 25%"
    (Calibrá cada uno mirando los screenshots — ajustá ±5% hasta que la cara 
    quede en tercio superior).
  · IMPORTANTE: como ya tenemos a Ney protagonizando el hero y la quote, en el 
    team grid podemos QUITAR a Ney y dejar solo Adrián, Patricia, Daniel. 3 
    columnas, no 4. Eso resuelve la repetición.
  · Commit: "fix(team): aspect ratio horizontal + object-position por persona + remueve duplicado de Ney"

Paso 8 — Verificación visual
  · Tomar screenshots actualizados con tu script de verification a 1440x900 
    y 390x844 (iPhone 14 Pro).
  · Guardalos en verification-20260512-fix/
  · Hacé un diff visual mental contra los anteriores. Devolveme:
      a) Confirmación de qué se arregló
      b) Cualquier cosa que veas que sigue mal
      c) Tu opinión honesta de si la página ya está lista para mostrar al 
         cliente o necesita otra pasada
  · NO HACER MERGE TODAVÍA. Quiero revisar yo antes.

REGLAS DE COMUNICACIÓN MIENTRAS TRABAJÁS

· Después de cada commit, paráte y avisame qué hiciste y si encontraste algo 
  inesperado.
· Si en algún paso descubrís que la realidad del código no coincide con mi 
  briefing (por ejemplo, "no existe el selector .hero-cinema en el HTML"), 
  pará y preguntá antes de improvisar.
· Si dudás entre dos enfoques, mostrame ambos.
· No agregues secciones nuevas. Si pensás que falta algo, decímelo después, 
  no lo metas vos.

Empezá por el Paso 1. Cuando termines el commit del Paso 2, avisame.
```

---

## Después de aplicar el prompt

Cuando Claude Code termine los 8 pasos y vos revises la branch `fix/landing-coherencia-visual`:

1. Abrí el index.html nuevo en tu navegador.
2. Si te gusta → merge a main: `git checkout main && git merge fix/landing-coherencia-visual`.
3. Si algo todavía no convence → reabrí esta conversación conmigo o pedile a Claude Code más ajustes en la misma branch antes de mergear.

## Qué NO vas a obtener con este prompt (y es a propósito)

- No vas a obtener transiciones cinematográficas tipo Awwwards top 10. Ese es un trabajo de polish que viene **después** de tener la base coherente. Hoy la base no lo está. Primero estabilizamos, después decoramos.
- No vas a obtener hover states ultra-pulidos en todas las cards. Ese es otro paso.
- No vas a obtener todas las microinteracciones que te prometí en el wireframe. Algunas ya están (marquee, count-up, fade hero), otras requieren JS que recién agregamos en una segunda iteración cuando la página tenga orden.

**Cuando esto esté limpio, hacemos una segunda vuelta para meter motion premium.** Es la forma profesional: primero arquitectura, después polish.
