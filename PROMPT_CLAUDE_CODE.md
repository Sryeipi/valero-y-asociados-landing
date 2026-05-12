# Prompt para Claude Code (en esta carpeta)

> **Como se usa:**
> 1. Abre PowerShell.
> 2. `cd "C:\Users\Administrator\Downloads\Valero y Asociados"`
> 3. `claude`
> 4. Pega el bloque de abajo como primer mensaje.
>
> **Importante:** Claude Code en esta maquina YA tiene acceso al vault YEIPI. El `CLAUDE.md` de esta carpeta + el `.claude\CLAUDE.md` global ya lo obligan a pasar por Obsidian-First. Este prompt solo le da el pedido concreto.

---

```
Hola. Sesion nueva sobre el proyecto Valero & Asociados (estudio juridico
Guayaquil, cliente real, mi tio).

Antes de tocar nada:
  1. Lee el CLAUDE.md de esta carpeta - te explica que pasa por Obsidian-First.
  2. Activa Session Gateway segun el protocolo del vault.
  3. Carga la memoria del cliente desde:
     C:\Users\Administrator\Documents\Obsidian Vault\03_CLIENTES\Valero y Asociados\
     (Brand Memory Loader read-only - no escribas ahi salvo handoff de cierre).
  4. Registra esta sesion en Log de Sesiones.

Una vez tengas el contexto cargado:

Paso 1 - Revisa el estado actual:
  - El HTML real esta en _Landing_Project\landing\index.html
  - El WhatsApp ya esta integrado: +593 959 080 607
  - El paquete completo armado por Cowork esta en _Landing_Project\
  - Pendientes registrados en 03_CLIENTES\Valero y Asociados\03_Landing\README.md

Paso 2 - Devuelveme:
  (a) Resumen 5 lineas: que entendiste y que estado tiene el proyecto hoy.
  (b) Tres cambios concretos que harias al HTML antes de mostrarselo al cliente
      (priorizalos P0/P1/P2 y justifica cada uno).
  (c) Si falta algo critico para que Funnel Architect arranque el blueprint,
      decimelo.
  (d) Tu propuesta de proximos pasos como checklist con dependencias.

Paso 3 - Cuando apruebe la propuesta, iteramos. Reglas:
  · Antes de cualquier cambio, decir QUE y POR QUE.
  · Cambios grandes en branch git (feature/...). Chicos en main.
  · Si encontras algo que viola accesibilidad / SEO / performance / etica
    deontologica, parame.
  · Cualquier aprendizaje reusable -> consolidar en el vault al cierre.

Tono: espanol directo, sin relleno, cero halagos. Si dudas, pregunta. Si
discrepas, deci.

Empeza ya.
```
