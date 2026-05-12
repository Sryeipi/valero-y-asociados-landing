# CLAUDE.md - Valero & Asociados (boot Obsidian-First)

> **Este archivo es leido automaticamente por Claude Code cuando abre una sesion en `C:\Users\Administrator\Downloads\Valero y Asociados\`. Su unico trabajo es decirle a Claude Code que pase por el vault YEIPI antes de tocar nada aqui.**

---

## 1. Regla no negociable

**El vault gana sobre chat memory.** Cualquier sesion de Claude Code en esta carpeta arranca por Obsidian-First:

1. Leer `C:\Users\Administrator\Documents\Obsidian Vault\01_CEREBRO\01_Protocolos\Protocolo Obsidian Codex Claude Code.md`.
2. Activar `02_AGENTES\00_Orquestacion\Session Gateway - Agente.md`.
3. Rutear por `01_CEREBRO\02_Comunicacion\Router de Agentes.md`.
4. Registrar la sesion en `08_OPERACIONES\03_Logs\Log de Sesiones.md`.
5. Leer la nota raiz del cliente: `03_CLIENTES\Valero y Asociados\00_Valero y Asociados.md`.
6. Si el pedido toca diseno/web/landing, revisar `01_CEREBRO\01_Protocolos\Gates de Produccion de Diseno.md` y activar **Funnel Architect Agent** primero (intent = lead gen / conversion).

Si saltas estos pasos, la sesion queda fuera de contrato y se contradice con `.claude\CLAUDE.md` global.

---

## 2. Que vive donde

| Tipo de info | Ubicacion | Razon |
|---|---|---|
| Memoria estrategica del cliente | `Obsidian Vault\03_CLIENTES\Valero y Asociados\` | Persistencia + busqueda + handoffs |
| Brandkit operativo | `Obsidian Vault\03_CLIENTES\Valero y Asociados\02_Brandkit.md` | Reutilizable entre proyectos del cliente |
| Decisiones y pendientes | `Obsidian Vault\03_CLIENTES\Valero y Asociados\03_Landing\README.md` | Vault como fuente de verdad |
| HTML, fotos, PDF, PPTX | Esta carpeta (`Downloads\Valero y Asociados\`) | Binarios pesados fuera del vault |
| `_Landing_Project\` | Esta carpeta | Paquete original armado por Cowork |
| Prompts para Claude Design | `PROMPT_CLAUDE_DESIGN.md` (esta carpeta) | Self-contained, para subir a claude.ai |
| Prompt corto Claude Code | `PROMPT_CLAUDE_CODE.md` (esta carpeta) | Para arrancar sesiones nuevas |

---

## 3. Quien es yeipi y que estamos haciendo

- **Yo soy yeipi** (Henry / Yeipi Bastidas). Trabajo en Rebel.
- **Cliente:** Ab. Ney Antonio Valero Brando (mi tio), estudio juridico en Guayaquil, Ecuador.
- **Objetivo:** landing page reposicionando el estudio. Conversion = WhatsApp.
- **Areas core:** Familia, Empresas, Inmobiliario. Extras: Transito, Laboral, Migracion.

---

## 4. WhatsApp operativo

- **Numero actual:** `+593 959 080 607` (mi numero personal, temporal hasta que el cliente entregue el comercial).
- Formato wa.me: `wa.me/593959080607`.
- Mensajes pre-rellenados por area (ya integrados en `_Landing_Project\landing\index.html`).

---

## 5. Sistema visual (obligatorio - hereda de `02_Brandkit.md` del vault)

- **Paleta:** navy `#0A1628` / dorado `#D4A84B` / hueso `#F5F2EB`. Acentos: terracota `#C4533A` Familia, laurel `#3A8F7D` Empresas, azul juridico `#3A6EB5` Inmobiliario.
- **Tipografia:** Fraunces serif (titulos) + Inter sans (body) + JetBrains Mono (labels).
- **Estilo:** minimalista 2026, motion sutil. **NO** glassmorphism, **NO** gradientes mesh, **NO** cliches legales (cero balanzas, cero columnas griegas, cero "el mejor abogado").
- Anti-patrones detallados en `Obsidian Vault\03_CLIENTES\Valero y Asociados\02_Brandkit.md`.

---

## 6. Cadena de agentes esperada (segun Router v2.3 del vault)

```
Pedido del usuario
  -> Session Gateway (registra)
  -> Brand Memory Loader (lee 03_CLIENTES\Valero...)
  -> Funnel Architect Agent (intent = landing/lead gen/conversion)
  -> Creative Research si necesita ideas
  -> Design Production Agent (itera el HTML)
  -> Quality Gate Agent (antes de mostrar al cliente)
  -> Vault Architect (consolida aprendizajes)
```

**Saltarse Funnel Architect en este proyecto = error.** El intent es conversion, no diseno suelto.

---

## 7. Reglas duras del proyecto

1. **Antes de cambiar codigo,** decir QUE vas a tocar y POR QUE.
2. **Branches git para cambios grandes** (`feature/hero-v2`, `feature/casos-v2`, etc.). Cambios chicos directo en main.
3. **Si hay dos enfoques posibles,** mostrar ambos al usuario antes de elegir.
4. **No publicar resenas falsas como reales** (ilegal en Ecuador, viola TOS de Google).
5. **No prometer resultados legales especificos** en copy (riesgo deontologico).
6. **No agregar dependencias innecesarias** al HTML (mantenerlo en un solo archivo).
7. **No tocar las fotos originales** del cliente sin permiso.
8. **Cualquier aprendizaje reusable** se consolida en el vault (no se pierde en esta carpeta).

---

## 8. Tono operativo

- **Espanol, directo, sin relleno corporativo.**
- Cero halagos. Si duda, preguntar. Si discrepa, decirlo.
- Concreto: archivos, lineas, decisiones. Nada vago.
- Decisiones reversibles: tomarlas y ejecutar. Solo preguntar si es destructivo, irreversible o cambia el resultado final con el cliente.

---

## 9. Stack target

- Landing: HTML + CSS + JS vanilla en un solo archivo. Sin frameworks pesados.
- Deploy futuro: Cloudflare Pages o Vercel.
- Tipografias: Google Fonts.
- Tracking: GA4 + Meta Pixel cuando el cliente lo decida.

---

## 10. Cierre de sesion

Antes de terminar cualquier sesion no trivial:

1. Cerrar entrada en `Obsidian Vault\08_OPERACIONES\03_Logs\Log de Sesiones.md` con: archivos tocados, decisiones, verificaciones, aprendizajes, deuda.
2. Actualizar `Obsidian Vault\03_CLIENTES\Valero y Asociados\03_Landing\README.md` si cambiaron los pendientes.
3. Si aprendiste algo reusable, pedir a Vault Architect que lo convierta en skill/SOP/checklist.
