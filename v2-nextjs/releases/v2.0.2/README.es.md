# [2026-05-21] v2.0.2 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.2 corrige problemas del CSV del Resumen Estructural detectados después de v2.0.1. No cambia la dirección general del producto ni la forma de usar las funciones de IA; los datos que se copian o descargan desde la pantalla de resultados reflejan ahora con más precisión el Resumen Estructural que se muestra en pantalla.

**Los valores del Resumen Estructural no han cambiado, por lo que no es necesario recalcular.** Sin embargo, si realizó una interpretación con IA a partir de un CSV del Resumen Estructural copiado en v2.0.1, es posible que faltaran algunos elementos o que un mismo nombre apareciera repetido; compruebe esa interpretación con valores copiados de nuevo en v2.0.2 o posterior. Por la misma razón, es más seguro volver a generar los CSV descargados que conserve.

## Resumen

- En la ventana de descarga de datos, el nombre del elemento en coreano `입력값 원자료 CSV` se corrigió a `점수계열 원자료 CSV`.
- Se corrigió un problema por el que la cadena CSV generada con el botón `Copiar valores del Resumen Estructural` podía contener cabeceras duplicadas y elementos faltantes.
- Copiar y descargar ofrecen ahora los mismos elementos del Resumen Estructural.
- Se corrigió que la ventana de inicio de sesión apareciera repetidamente tras un error de la clave del proveedor de IA en una sesión iniciada con clave API.
- El modelo de conversación predeterminado de OpenAI se actualizó de GPT-5.4 a GPT-5.5.
- La confirmación de pegado de los valores del Resumen Estructural en el asistente de interpretación se muestra ahora como `Introducido ✅`.

## Qué comprobar en el asistente de interpretación

En v2.0.1, el asistente de interpretación se usa copiando los valores desde la pantalla de resultados con el botón `Copiar valores del Resumen Estructural`, pegándolos en el campo de valores del Resumen Estructural de la pantalla de IA de interpretación e iniciando la conversación.

En v2.0.1, nombres usados en varias secciones, como `D`, `Zf`, `Zd`, `GHR` y `PHR`, podían aparecer duplicados en los datos copiados. También podían faltar algunos elementos visibles en pantalla, como `Single`, `Contents`, `Form Quality`, `Special Scores`, `Approach` y `Blends`.

No se trataba de un problema de la conexión con la clave API ni de la conversación con la IA, pero los datos del Resumen Estructural que llegaban al asistente de interpretación podían ser incompletos o ambiguos.

## Qué ha cambiado

Copiar y descargar ofrecen ahora el mismo conjunto completo de elementos, y los elementos con el mismo nombre se muestran de forma que puedan distinguirse.

El CSV de datos brutos de la serie de puntuaciones incluye solo las filas de puntuación realmente usadas en el cálculo. Se excluyen las filas provisionales con la lámina vacía y las filas incompletas.

El asistente de interpretación acepta los datos del Resumen Estructural copiados desde la pantalla de resultados y no trata frases ordinarias sin relación como datos del Resumen Estructural.
