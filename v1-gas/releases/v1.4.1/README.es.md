# v1.4.1

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Metadata

| Field | Value |
| --- | --- |
| Version | `v1.4.1` |
| Release date | 2026-01-07 |
| Release type | Corrección de errores |
| GAS deployment | [Open GAS app](https://script.google.com/macros/s/AKfycbxMCx13pkrSzFs8f2qXfmxy2LRhkBpZTItFTIfEOoOi-zwurbysnKGfDIYtAeEdQP99/exec) |

## Patch Notes

# Principales correcciones

## *Resumen*

> **Se corrigieron errores de v1.4.0.**

Los botones que se muestran al acceder por primera vez a la aplicación web y al volver a acceder aparecen ahora correctamente.
>
- Antes existía un error por el que el botón "Empezar con datos de muestra" se mostraba incluso al volver a acceder.
    - Primer acceso: se muestra el botón "Empezar con datos de muestra"
    - Nuevo acceso (con datos guardados): se muestra el botón "Cargar contenido autoguardado"
- La ventana modal mostrada al volver a acceder se ve ahora más limpia.
    - Se eliminó el título "Continuar el trabajo" y solo se muestra el mensaje "Hay contenido de la última sesión."

        en letra grande y negrita (para no decir lo mismo dos veces)


> Otras mejoras
>
- Se añadió un efecto más llamativo al pasar el ratón sobre las tarjetas de la pestaña Más.
    - La sombra es más intensa
    - La imagen de fondo detrás de la tarjeta se ve más nítida
    - El texto de la tarjeta se difumina para que destaque la imagen de fondo
- Los estilos que debían estar en `styles.html` pero seguían parcialmente en `index.html` se trasladaron por completo,

    dejando el código más ordenado.


Estos cambios también se reflejan en el [chatbot Gems](https://gemini.google.com/gem/1QDCPHshPvq5J9iIKeV-1Nvy0EFzKPN6Y?usp=sharing).

---

## *Detalles*

### *Corrección de la lógica de los botones del modal de primer acceso*

> **Implementación**
>
- **Problema**
    - El botón "Empezar con datos de muestra" se mostraba tanto en el primer acceso como en los siguientes
    - Al volver a acceder, pulsar "Empezar con datos de muestra" cargaba en realidad el contenido autoguardado
- **Solución**
    - Con datos guardados: se muestra el botón "Cargar contenido autoguardado"
    - Sin datos guardados: se muestra el botón "Empezar con datos de muestra"
    - `updateAllTexts()` ya no sobrescribe el texto mientras el modal ya está visible
    - Funciona igual en todos los idiomas admitidos (coreano, inglés, japonés, español, portugués)

> **Detalles técnicos**
>
- Se añadió una guarda en `updateAllTexts()` para no actualizar el texto del modal si ya está visible
- `handleScoringTabFirstLoad()` comprueba si hay datos guardados y establece el texto del modal
- Con datos guardados, `modalLoadBtn.textContent` se establece en `t('modal_welcome_load_saved')`
- Sin datos guardados, `modalLoadBtn.textContent` se establece en `t('modal_welcome_load')`
- `updateAllTexts()` también comprueba si hay datos guardados y establece el texto del modal (por si se ejecuta antes de mostrar el modal)

**Archivos**: `index.html` (líneas 2387–2426: función updateAllTexts; líneas 3974–4060: función handleScoringTabFirstLoad)

### *Mejora de la interfaz del modal de primer acceso*

> **Implementación**
>
- **Título eliminado**
    - Con datos guardados se oculta el título "Continuar el trabajo" y solo se muestra el mensaje "Hay contenido de la última sesión."
    - Evita decir lo mismo dos veces
- **Cambio de estilo del mensaje**
    - Con datos guardados, el mensaje se muestra en letra grande, negrita y negra (18px)
    - Antes: letra pequeña y gris
    - Después: letra grande, negrita y negra (font-weight: bold, font-size: 18px, color: #212529)
- **Primer acceso**
    - Sin datos guardados se muestran el título y el mensaje como antes
    - El mensaje conserva el estilo predeterminado (pequeño, gris)

> **Detalles técnicos**
>
- `handleScoringTabFirstLoad()` establece `modalTitle.style.display = 'none'` cuando hay datos guardados
- Con datos guardados se aplican estilos en línea (fontWeight, fontSize, color) a `modalMessage`
- Sin datos guardados se establece `modalTitle.style.display = 'block'` y se restablece el estilo del mensaje
- La misma lógica se aplica en `updateAllTexts()`

**Archivos**: `index.html` (líneas 3987–3993, 4049–4054, 2403–2409, 2413–2424)

### *Refactorización de estilos estáticos*

> **Implementación**
>
- **Problema**
    - Quedaban estilos en línea en `index.html`, lo que dificultaba el mantenimiento
    - CSS y HTML no estaban separados, por lo que había que revisar varios archivos para modificar un estilo
- **Solución**
    - Todos los estilos estáticos (no controlados dinámicamente por JavaScript) se trasladaron a `styles.html`
    - Los estilos controlados dinámicamente por JavaScript (`display: none`, etc.) se mantienen en `index.html`
- **Estilos trasladados**
    - `text-align: center` de títulos/mensajes de modales → añadido a `#reset-modal-title`, `#reset-modal-message`, `#ai-modal-title`, `#ai-modal-message`
    - Estilo del texto de guía → añadido a `#Scoring_Summary > p`
    - Estilo flex del contenedor del info-icon → añadido a `.row-controls > div`
    - Estilo de hr → añadido a `#Notice hr`
    - Ancho de la tabla → añadido a `#list-table-body table`
    - Ancho de colgroup → añadido a `#list-table-body colgroup col:nth-child()`

> **Detalles técnicos**
>
- Se eliminaron los atributos de estilo en línea de `index.html`
- Se añadieron las reglas CSS de esos selectores en `styles.html`
- Los estilos de modales se añadieron a la sección 8.0
- Los estilos de la pestaña Más se añadieron a las secciones 4.4 y 4.5
- Los estilos de componentes comunes se añadieron a la sección 2.1

**Archivos**:

- `index.html` (líneas 212–213, 224–225, 263, 271–275, 287, 325: estilos en línea eliminados)
- `styles.html` (líneas 1306–1311: estilos de modales; 655–666: estilos de tabla; 667–669: estilos de hr; 244–250: estilos de componentes comunes)

### *Ordenación del índice y de los comentarios*

> **Índice**
>
- **Cambios**
    - Se eliminaron entradas duplicadas del índice (10.31 aparecía dos veces)
    - El orden del índice se ajustó al orden real del código
    - Se reflejaron los nuevos estilos en el índice de `styles.html`
        - `#Scoring_Summary > p` y `.row-controls > div` añadidos a 2.1
        - 4.4 y 4.5 añadidos (ancho/columnas de tabla, separador)
        - IDs de modales añadidos a 8.0
- **Verificación**
    - Todos los comentarios del índice coinciden con la posición real del código
    - La estructura del código se puede entender con precisión a partir del índice

> **Eliminación de comentarios en línea innecesarios**
>
- **Tipos de comentarios eliminados**
    - Comentarios explicativos evidentes con solo leer el código
        - p. ej. `// 모달이 이미 표시되어 있으면 모달 텍스트는 업데이트하지 않음`
        - p. ej. `// (handleScoringTabFirstLoad에서 이미 설정했을 수 있음)`
        - p. ej. `// 저장된 데이터 유무에 따라 환영 모달 텍스트 설정`
        - p. ej. `// '항목' 열에 내용이 있으면 새 카테고리`
        - p. ej. `// "Card (카드)" -> "Card"`
        - p. ej. `// Excel에서 한글이 깨지지 않도록 BOM(Byte Order Mark)을 추가합니다.`
- **Comentarios importantes conservados**
    - Comentarios de separación de secciones (p. ej. `// 10.1.5. 모든 텍스트 업데이트 함수`)
    - Comentarios que explican un motivo técnico

**Archivos**:

- `index.html` (líneas 119–172: índice; 2387–2426: comentarios eliminados)
- `styles.html` (líneas 47–107: índice)

### *Mejora del efecto hover de las tarjetas de la pestaña Más*

> **Implementación**
>
- **Sombra más intensa**
    - Antes: `box-shadow: 0 4px 8px rgba(0,0,0,0.1)`
    - Después: `box-shadow: 0 8px 24px rgba(0,0,0,0.25)` (sombra más oscura y grande)
- **Imagen de fondo más nítida**
    - Al pasar el ratón, la opacidad de la imagen de fondo sube de 0.12 a 0.35
    - Se aplica `filter: saturate(1.2) contrast(1.1)` para realzar el color
- **Difuminado del texto**
    - Al pasar el ratón se aplican `filter: blur(2px)` y `opacity: 0.6` al texto de la tarjeta
    - El texto se difumina para que destaque la imagen de fondo
- **Transición**
    - Se aplica `transition` a todos los efectos para una animación suave

> **Detalles técnicos**
>
- Se añadieron sombra, opacidad de la imagen de fondo y filtro a `.link-button:hover`
- Se añadió el filtro a `.link-button:hover::before` (imagen de fondo más nítida)
- Se añadieron filtro y opacidad a `.link-button:hover > *` (difuminado del texto)
- Se añadió la propiedad `transition` (0.25s ease) a todos los efectos

**Archivos**: `styles.html` (líneas 1357–1375: efecto hover)

### *Cambios por archivo*

> **index.html**
>
- **Cambios principales**
    - Corrección de la lógica de los botones del modal de primer acceso
    - Mejora de la interfaz del modal (título eliminado, estilo del mensaje)
    - Eliminación de estilos estáticos en línea
    - Ordenación del índice y de los comentarios
    - Información de versión sin cambios (se mantiene v1.4.0)
- **Estadísticas del código**
    - Líneas totales: unas 4.839
    - Funciones principales: 35
    - Secciones del índice: 35 (todas coinciden con el código)

> **styles.html**
>
- **Cambios principales**
    - Estilos estáticos añadidos (modales, tabla, hr, componentes comunes)
    - Mejora del efecto hover de las tarjetas de la pestaña Más
    - Índice actualizado
    - Información de versión sin cambios (se mantiene v1.4.1)
- **Estadísticas del código**
    - Líneas totales: unas 1.561
    - Variables CSS: 33 (colores de grupo)

> **Code.gs**
>
- **Cambios principales**
    - Sin cambios
- **Estadísticas del código**
    - Líneas totales: unas 1.174

### *Pruebas y verificación*

> **Pruebas funcionales**
>
- ✅ En el primer acceso se muestra el botón "Empezar con datos de muestra"
- ✅ Al volver a acceder (con datos guardados) se muestra el botón "Cargar contenido autoguardado"
- ✅ Cada botón realiza la acción correcta
- ✅ Con datos guardados se oculta el título y solo se muestra el mensaje
- ✅ Con datos guardados el mensaje se muestra en letra grande, negrita y negra
- ✅ Funciona igual en todos los idiomas admitidos
- ✅ Efecto hover de las tarjetas de la pestaña Más comprobado (sombra, imagen de fondo, texto)

> **Comprobación de UI/UX**
>
- ✅ El texto de los botones del modal cambia correctamente según el estado de guardado
- ✅ El estilo del mensaje del modal cambia correctamente según el estado de guardado
- ✅ El efecto hover de las tarjetas de la pestaña Más funciona con suavidad

> **Comprobación de calidad del código**
>
- ✅ Los comentarios del índice coinciden con el código
- ✅ Comentarios en línea innecesarios eliminados
- ✅ Estilos estáticos trasladados correctamente a `styles.html`
- ✅ Estilos en línea reducidos al mínimo
- ✅ Estructura del código mejorada

---

# Hoja de ruta

Se seguirá supervisando el programa para corregir los errores que se vayan detectando.

## Source files

- `source/Code.gs`
- `source/index.html`
- `source/styles.html`

## How to use

Para reproducir esta versión, cree en un proyecto de Google Apps Script archivos con los mismos nombres y pegue tal cual los archivos de `source/`.
Al desplegar el proyecto de GAS como aplicación web, podrá ejecutar directamente la calculadora de esa versión.
