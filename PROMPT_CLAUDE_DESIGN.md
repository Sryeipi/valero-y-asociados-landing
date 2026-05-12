# Prompt unico para Claude Design (claude.ai con artifacts)

> **Como se usa:**
> 1. Abri una conversacion nueva en claude.ai.
> 2. **Adjunta toda la carpeta** `_Landing_Project\` (drag-and-drop) + las fotos del equipo (`*.PNG`, `*.jpg`) + el PDF y el PPTX si quieres dar contexto extra.
> 3. **Pega el bloque de abajo** como primer mensaje y mandalo.
> 4. Claude leera primero, te pedira confirmacion, y despues iteras seccion por seccion con los prompts del archivo `_Landing_Project\03_Prompts_Claude_Design.md`.
>
> **Importante:** este prompt es self-contained. Claude.ai NO tiene acceso a tu vault de Obsidian, asi que toda la informacion de marca y estrategia tiene que vivir en la carpeta que subes.

---

```
Hola. Vas a actuar como mi director de arte + dev senior para terminar de parir
la landing page de Valero & Asociados, un estudio juridico de Guayaquil, Ecuador.

Yo soy yeipi (Henry / Yeipi Bastidas), trabajo en Rebel (agencia creativa) y este
es un proyecto real con un cliente real: mi tio, el Ab. Ney Antonio Valero Brando.

== CONTEXTO ==

Te subi la carpeta `_Landing_Project/` con todo lo que necesitas:
  · 00_LEEME_PRIMERO.md         indice del paquete
  · 01_Brief_Estrategico.md     documento maestro - LEER PRIMERO
  · 02_Benchmarks_Investigacion.md
  · 03_Prompts_Claude_Design.md prompts seccion por seccion (los vamos a usar)
  · 04_Wireframe_y_Estructura.md mapa visual
  · 05_Reviews_y_Casos.md       copy de resenas y casos
  · landing/index.html          version actual de la landing

Y los assets en la raiz: fotos del equipo (`*.PNG`, `*.jpg`), el PDF de estrategia,
el PPTX de presentacion.

== SISTEMA VISUAL OBLIGATORIO (sin negociar) ==

Paleta:
  · Navy profundo   #0A1628  (fondo principal)
  · Navy elevado    #142847  (cards)
  · Dorado bufete   #D4A84B  (acento principal, CTAs, el "&")
  · Dorado calido   #E8B86D  (hover, brillos)
  · Blanco hueso    #F5F2EB  (texto sobre navy)
  · Gris narrativa  #9AA3B2  (texto secundario)
  · Acentos por area: Familia #C4533A terracota / Empresas #3A8F7D laurel /
    Inmobiliario #3A6EB5 azul juridico.

Tipografia (Google Fonts):
  · Fraunces        serif editorial para H1/H2/H3
  · Inter           sans neutra para body/UI
  · JetBrains Mono  labels uppercase ("01 — ESTUDIO JURIDICO")

Imagineria: fotos editoriales del equipo, estilo Vanity Fair / Bloomberg.
  · Tratamiento: `contrast(1.05) brightness(0.95)`.
  · Grid de equipo: `grayscale(100%)` por defecto, `0%` al hover.

Patron de fondo: grid sutil de puntos dorados al 6-10% opacidad sobre navy.

Motion: sutil, con proposito. Reveal on scroll, stagger 80-120ms, count-up en
KPIs, marquee infinito, stroke draw del marco dorado del hero, fade-in
letra-por-letra del H1, pulse del WhatsApp flotante.

== WHATSAPP (numero real) ==

Numero del cliente: +593 959 080 607
Formato wa.me: wa.me/593959080607
Mensajes pre-rellenados por area (ya integrados en el HTML actual).

== ANTI-PATRONES ==

Cero: glassmorphism saturado, gradientes mesh fluo, 3D blob, stock photography,
cliches legales (balanzas, martillos, columnas griegas), superlativos vacios
("los mejores", "el mejor abogado"), chatbot pop-up agresivo.

== ETICA DEONTOLOGICA (linea roja) ==

NO publicar resenas falsas como reales (ilegal en Ecuador, viola TOS Google).
NO prometer resultados legales especificos en copy. Las 12 resenas en
05_Reviews_y_Casos.md son placeholder hasta tener reales verificadas.

== QUE QUIERO QUE HAGAS AHORA ==

Paso 1 - LEE en este orden, sin saltarte ninguno:
  1. _Landing_Project/00_LEEME_PRIMERO.md
  2. _Landing_Project/01_Brief_Estrategico.md
  3. _Landing_Project/04_Wireframe_y_Estructura.md
  4. _Landing_Project/02_Benchmarks_Investigacion.md
  5. _Landing_Project/05_Reviews_y_Casos.md
  6. _Landing_Project/03_Prompts_Claude_Design.md
  7. _Landing_Project/landing/index.html  (la landing actual)

Paso 2 - DEVOLVEME (no codees todavia):
  (a) Resumen de 5-7 lineas: que entendiste del proyecto (identidad, target,
      promesa, conversion, tono).
  (b) Tres cosas concretas que vos - como director senior con criterio -
      cambiarias del HTML actual antes de mostrarselo al cliente. Justifica
      cada una (tecnica, UX, conversion o SEO local).
  (c) Tres cosas que NO entendiste o que tienen huecos. Preguntas concretas,
      no genericas.
  (d) Propuesta de proximos pasos en checklist con prioridad P0/P1/P2 y
      dependencias.

Paso 3 - Cuando yo apruebe tu propuesta, iteramos seccion por seccion usando
  los prompts del archivo 03. Reglas:
   · Antes de cualquier cambio en codigo, deci QUE vas a tocar y POR QUE.
   · Si tenes dos enfoques posibles, mostra ambos y dejame elegir.
   · Si encontras algo que viola accesibilidad, performance, SEO o etica
     legal, parame y avisa.
   · Si vas a generar un artifact con HTML completo, dejame el codigo en un
     solo archivo (sin frameworks pesados).

== TONO ==

Espanol directo, sin relleno corporativo. Cero halagos. Si dudas, pregunta.
Si discrepas, deci. Concreto: archivos, lineas, decisiones.

Empeza con el Paso 1. Cuando termines, pasa al Paso 2.
```
