---
type: proyecto
domain: clientes
client: Valero y Asociados
tags: [proyecto, landing, web, lead-gen, whatsapp]
status: v9-feedback-cliente-azul-nombres
created: 2026-05-11
updated: 2026-08-03
git_branch: main
git_state: ver ultimo commit en origin/main; Vercel production READY (deploy automatico por Git integration)
owner: Funnel Architect Agent + Design Production Agent
---

# Landing v1 - Valero & Asociados

## Donde vive el proyecto

Todo el proyecto vive **dentro del vault** (migrado de Downloads el 2026-05-12):

```
Obsidian Vault\03_CLIENTES\Valero y Asociados\_Landing_Project\landing\index.html
```

Repo: `https://github.com/Sryeipi/valero-y-asociados-landing` (raiz = carpeta del cliente; `vercel.json` apunta a `_Landing_Project/landing`). Push a `main` = deploy automatico en Vercel.
**URL produccion:** https://valero-y-asociados-landing.vercel.app/

## Conversion

- **CTA primario:** WhatsApp (`wa.me/593959080607`).
- **Mensajes pre-rellenados** por area: Familia / Empresas / Inmobiliario / Transito / Laboral / Migracion.
- **Numero actual:** `+593 959 080 607` (personal de YEIPI, temporal hasta que el cliente entregue el comercial).

## Secciones implementadas en `_Landing_Project/landing/index.html`

1. Nav fijo + WhatsApp CTA
2. Hero split con foto Ab. Ney + marco dorado animado
3. Marquee de credenciales
4. 3 cards de areas + chips extras
5. KPIs (850 casos, 92% sin juicio, 20+ anos, 4.8 ★)
6. Scroll horizontal de 6 casos anonimizados
7. Bloque fundador (quote + foto + credenciales)
8. Grid 4 retratos del equipo (BW -> color hover)
9. 9 resenas en masonry
10. FAQ acordeon (6 preguntas)
11. Cierre con CTA WhatsApp
12. Footer 4 columnas + WhatsApp flotante

## Pendientes (P0 / P1 / P2)

### P0 - bloqueantes para mostrar al cliente
- [x] Quality Gate tecnico inicial del HTML actual (accesibilidad basica, consola, imagenes, overflow, SEO local estructural).
- [x] Validacion deontologica del copy (cero promesas legales, cero superlativos, sin resultados garantizados).
- [x] Confirmar resenas placeholder vs reales: se retiraron como testimonios y se reemplazaron por bloque de confianza/metodo.
- [ ] Direccion de oficina real en FAQ y footer.

### P1 - para v1 lanzable
- [ ] Funnel Architect blueprint con fit validation.
- [x] OG image custom.
- [x] Favicon.
- [ ] Pagina politica de privacidad (legal LSSI Ecuador).
- [ ] Numero WhatsApp comercial real (cuando el cliente lo entregue).

### P2 - mejora continua
- [x] Carga lazy para fotos + conversion WebP + carpeta deploy liviana.
- [ ] Tracking GA4 + Meta Pixel.
- [ ] A/B test de hero (split: foto Ab. Ney vs equipo grupal).
- [ ] Version EN para clientes migratorios USA.

## Handoffs registrados

- **2026-05-11 - Codex / Design Production + Quality Gate tecnico:** version nueva del ZIP sincronizada como base, HTML iterado, imagenes convertidas a WebP, originales movidos fuera de `landing`, bloque de testimonios reemplazado por confianza, FAQ accesible, motion optimizado y verificado en desktop/mobile/reduced-motion.
- **2026-05-12 - Claude Code / Funnel Architect + Design Production (cadena):** iteracion v2 premium sobre la version Codex. Mejoras quirurgicas sin rehacer:
  - **Sticky CTA bar inferior** con selector de area (Familia/Empresas/Inmobiliario), aparece despues del hero, se oculta en el cierre, dismissable via sessionStorage. Mobile collapsa a CTA grande sin pills.
  - **Hyperframe drawn-on-scroll** en founder y tarjeta del Ney en equipo — consistencia con el marco del hero. Auto-cap por perimetro real con IntersectionObserver.
  - **Hero ticker progress fill** dentro del dot activo (linea dorada sincronizada con el ciclo Ken Burns de 6.2s).
  - **Counter easing premium** (easeOutExpo) en KPIs, duracion adaptativa.
  - **JSON-LD enriquecido SEO local:** priceRange, geo, openingHoursSpecification, contactPoint, knowsAbout, areaServed (GYE/UIO/Cuenca/Manta), employee, alumniOf, slogan.
  - **Fade-edge en cases scroll** + hint "Deslizar" con flecha animada que se oculta al llegar al final.
  - **Parallax sutil en tiles** del mosaico atmosphere (data-speed por tile, rAF-throttled, respeta reduced-motion).
  - **Nav active section indicator** con underline animado via IntersectionObserver (rootMargin -40%/-55%).
- **2026-05-12 - Codex / Design Production + Quality Gate:** correccion puntual del modal de perfiles:
  - Carrusel real por abogado usando solo imagenes existentes en Obsidian.
  - Ney: 4 fotos; Adrian: 3 fotos; Patricia: 2 fotos; Daniel: 2 fotos.
  - Eliminada la repeticion falsa de una sola foto con tres puntos.
  - Verificado local y en Vercel: conteos correctos, imagenes unicas y 0 errores de consola.
  - Deploy production READY: commit `a392d79`, deployment `dpl_DHGUqPvM4viF4copaGm9QRxW1VdW`.

## Decisiones acumuladas

- **2026-05-11:** WhatsApp temporal = `+593 959 080 607` (numero personal YEIPI). Reemplazar cuando el cliente entregue el numero comercial.
- **2026-05-11:** El paquete `_Landing_Project/` armado originalmente por Cowork queda como base. No se rehace, se itera.
- **2026-05-11:** Los prompts de Cowork se **adaptan** para respetar Obsidian-First; no se ejecutan tal cual.
- **2026-05-11:** Para mejoras de motion se usara un prompt de iteracion quirurgica: no rehacer pagina, preservar estructura/copy/WhatsApp/SEO, elevar microinteracciones y scroll effects con criterio MotionSites/Motion, y validar performance/accesibilidad antes de entregar.
- **2026-05-11:** La landing publicable vive en `C:\Users\Administrator\Downloads\Valero y Asociados\_Landing_Project\landing\` y el ZIP liviano listo para compartir/deploy es `C:\Users\Administrator\Downloads\Valero-y-Asociados-landing-mejorada-20260511-205845.zip`.
- **2026-05-12:** Iteracion v2 premium aplicada sobre el HTML vivo. No se rehizo el ZIP — se itera in-place. Para regenerar paquete liviano, repetir el flujo de Codex (conversion WebP ya estable + minify opcional). La sticky CTA bar es la mejora de conversion mas impactante; respeta dismissal por sesion para no molestar usuarios recurrentes.
- **2026-05-12 v3:** **Bug critico detectado y arreglado.** Las WebP generadas el 2026-05-11 estaban en dimensiones miniatura (ej: ney.webp = 55x164 cuando deberia ser 1200x1800). HTML declaraba dimensiones full -> browser reservaba espacios enormes para thumbnails. Solucion: script Python `_tools/rebuild_webp.py` con Pillow regenera 51 archivos (full + -md + -sm) desde los PNGs originales en root. Backup de las rotas en `img.backup-webp-broken-20260512-001931/`. Todos los `<img>` ahora con `srcset` + `sizes` apropiados. **Aprendizaje:** auditar binarios de imagen (parsing VP8 headers) antes de asumir bug de layout.
- **2026-05-12 v3 modernizacion:** Agregado section badge editorial flotante, hero H1 gold sweep en scroll, sticky storytelling en proceso, mosaic reveal-on-scroll, KPI shine sweep, founder clip-path mask, section H2 underline, gradient border en cases, breakpoint intermedio tablet (721-1080px) ausente antes. Mobile fixes: hero stats horizontal scroll, touch targets 44px, mosaic 2-cols, captions siempre visibles, marquee 60s.
- **2026-05-12 v4 fix + Mr Brook pattern:** YEIPI reporta hero mal encuadrado, foto fundador invisible, efectos no notorios. Fixes: (a) bug critico founder clip-path reemplazado por overlay sliding con safety fallback 4s; (b) imagenes regeneradas con focal_y 0.18-0.22 para retratos + calidad 88 + UnsharpMask + color boost; (c) nueva seccion sticky scroll storytelling "El metodo Valero" 280vh con 3 momentos narrativos (escuchar/decir/defender), foto cambiante, grid pattern drift, 3 floats parallax, progress dots; (d) efectos reforzados: hero deep-blur a 0.3vh, H1 sweep dramatico 4 stops, idle float 4px en areas, body bg parallax con mouse, section H2 reveal, sticky proceso en tablet tambien. Adaptado del pattern Mr Brook al contexto legal (sin pirata, sin humor; serio editorial). Total imagenes 5.6MB (de 3.5).
- **2026-05-12 v5 fix arquitectural + cirugia coherencia:** YEIPI dice "esta mal revisa todo". Diagnostico con Playwright revela bug TDZ critico (`'cases' before initialization` linea 2684) que rompia TODO el JS post-v2 — explica porque "nada funcionaba" antes. Tras fix TDZ, cowork pasa prompt detallado (PROMPT_FIX_LANDING.md) con 5 problemas raiz arquitecturales. Solucion en 5 commits en branch `fix/landing-coherencia-visual`:
    - **Eliminadas 4 secciones** (de 12 a 7): hero-cinema slideshow, method-scroll sticky, atmosphere mosaico, founder (Ney duplicado), closing-bg
    - **Hero v5 clasico** con foto vertical de Ney aspect 3/4 object-position 18%, quote del fundador absorbida como blockquote, trust row 3 items, hyperframe drawn
    - **Proceso v5 editorial** con 3 step-cards (icono line 32px + eyebrow "PASO 01 · CONVERSACIÓN" + h3 serif + body + meta flecha), sin sticky scroll, hover lift
    - **Team v5** 3 miembros (sin Ney duplicado), aspect 4/3 horizontal (fiel a fotos originales 1448x1086), object-position por persona (30%/35%/25%)
    - **Backups** scenes (24 archivos) y editorials (9 archivos) preservados en disco
  Resultado: pagina 31% mas concisa (15163px → 10432px desktop, 15333px → 10887px mobile), 0 errores consola, sin overflow mobile, repo git inicializado retroactivamente.
  **NO mergeado a main** — branch lista para review YEIPI antes de merge.

## Cierre v6 Codex - 2026-05-12

- **Ruta:** Session Gateway -> Orquestador -> Funnel Architect + Design Production -> Skill Web Premium UI UX Motion -> Quality Gate.
- **Cambios:** correccion del H1 visible, motion polish con entrance blur/scale, parallax sutil de hero photo, glow scroll-driven en cierre, sticky CTA oculto en equipo para no tapar retratos, `og-preview.png`, `favicon.svg`, `theme-color`, `twitter:card` y `og:image`.
- **Verificacion:** Playwright en `verification-20260512-codex-motion-final`: desktop 1440, mobile 390, mobile reduced motion, 0 errores consola, scrollWidth = viewport, 15 links WhatsApp correctos.
- **Deploy:** bloqueado por credenciales Vercel. `npx vercel@latest --yes --prod` devuelve `The specified token is not valid`; el conector Vercel de Codex solo indico usar CLI. Pendiente renovar login/token Vercel o conectar repo remoto.

## Cierre v7 Codex - 2026-05-13

- **Ruta:** Session Gateway -> Router -> Design Production + Skill Web Premium UI UX Motion -> Quality Gate -> Git/Vercel.
- **Problema raiz:** el navegador/CDN podia seguir sirviendo imagenes viejas o variantes pequenas (`sm/srcset`) aunque los WebP del vault ya estuvieran regenerados en alta calidad.
- **Cambios:** preload del retrato principal, cache-buster `?v=20260512-hq` en WebP, eliminacion de `srcset/sizes` en fotos principales para forzar archivo grande del vault, loader reducido de 2.2s a 720ms, delays hero recortados, fallback `motionSafetyShow` para evitar bloques invisibles si JS falla, retirada del halftone del hero y fotos de equipo en color real.
- **Verificacion local:** Playwright desktop 1440 y mobile 390 sin errores consola, sin overflow horizontal, hero `ney.webp?v=20260512-hq` cargando 1290x1935, 0 bloques invisibles en viewport.
- **Deploy:** CLI Vercel sigue con token invalido, pero Git integration funciono. Commit `903d08b` (`fix: improve landing motion and image quality`) pushed a `origin/main`; Vercel production `dpl_CF8igdtJinLyAMoiGGBmweyrPkTv` quedo `READY`.
- **URL:** https://valero-y-asociados-landing.vercel.app/

## Cierre v9 Claude Code - 2026-08-03 (feedback del cliente por WhatsApp)

Cambios pedidos por David Bastidas Guillen (WhatsApp 2026-08-02):

1. **Paleta azul/plomo**: el estudio tiene papeleria azul/gris. HTML re-tokenizado a la paleta navy del brandkit (`#0A1628/#142847/#1B3358` + dorado `#D4A84B` + plomo `#9AA3B2/#C3CAD6` + acentos `#C4533A/#3A8F7D/#3A6EB5`). Todos los rgba/hex hardcodeados migrados (gold, navy, gray viejos).
2. **Nombres reales con segundos apellidos**: Ney Valero Brando · David Bastidas Guillen (antes "Adrian Bastidas") · Patricia Bastidas de Valero (antes "Patricia Valero") · Fernando Carrillo Arteaga (antes "Daniel Carrera"). Cards, modal, JSON-LD, alts y mensajes WhatsApp actualizados. Archivos de foto conservan nombres viejos (adrian/daniel) — no renombrar.
3. **Areas ampliadas, sin responsables**: se quitaron los "Resp. X" de las cards; listas ampliadas con el detalle del PPTX del cliente (divorcios express/judicial/contencioso, pensiones, testamentos, posesion efectiva, SAS/Ltda/SA, marca SENADI, cobro judicial, retainer PyME, promesas, prescripcion adquisitiva, propiedad horizontal). Chips nuevos: declaraciones juramentadas, poderes, actas de finiquito.
4. **Copy**: "firmamos honorarios escritos" → "firmamos un acuerdo de honorarios por escrito, con alcance y plazos definidos". Caso S.A.S.: "clausulas clave" → "clausulas claves", "pudiera" → "pueda" (tambien en caso registral).

Verificado con Playwright (desktop 1440 + mobile 375, sin overflow). Pendiente que sigue vivo: direccion de oficina real, WhatsApp comercial, politica de privacidad.
