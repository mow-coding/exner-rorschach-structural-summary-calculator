# [2026-06-27] v2.1.1 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.1.1 corrige problemas de la pantalla de entrada de puntuación y del proceso de conexión de IA. Se eliminó la conexión con Gemini/Google AI y el proceso se simplificó a OpenAI con la clave API propia.

## Resumen

- Se corrigió un problema por el que arrastrar texto con el ratón dentro de la ventana de notas de la respuesta se interpretaba como un clic en el fondo y cerraba la ventana.
- Seleccionar otra fila durante una conversación con el asistente de codificación ya no elimina la conversación existente ni la respuesta en curso.
- Las funciones de IA solo aceptan una clave API de OpenAI; la conexión con Google Gemini ya no se ofrece.
- En la ventana de la clave API, el nombre del modelo y las indicaciones sobre la clave se muestran en una sola línea fácil de leer.

## Conexión de IA y pantalla de puntuación

Las funciones de IA ahora solo aceptan una clave API de OpenAI. Si se introduce una antigua clave de Google/Gemini, se muestra un aviso de que se necesita una clave de OpenAI. La clave API se usa cifrada para la conexión de IA; la conexión dura como máximo 24 horas y, al finalizarla, la clave también se elimina.

El asistente de codificación toma como referencia la fila seleccionada, pero al pasar a otra fila los mensajes existentes no desaparecen. Puede mantener la conversación y seguir preguntando con otra fila como referencia.

La corrección de la ventana de notas de la respuesta no afecta a los resultados del cálculo; solo se ajustó con más precisión la condición para cerrar la ventana durante la entrada.
