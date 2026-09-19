# [2026-06-28] v2.1.2 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.1.2 ajusta la forma de responder del asistente de codificación y del asistente de interpretación: responden lo necesario, no se cortan a mitad de respuesta y no exceden el ámbito de juicio del clínico. Salvo un pequeño ajuste de alineación en la ventana de la clave API, las pantallas no cambian.

## Resumen

- Los asistentes de codificación e interpretación se comportan de forma más coherente en la longitud y la presentación de las respuestas.
- El asistente de codificación indica con más claridad los códigos candidatos y el límite de lo que el clínico debe revisar. Se bloquean las respuestas que podrían confundirse con una entrada o aplicación automática en la fila y, si faltan pruebas, pide más información de observación.
- Se refuerzan los límites del asistente de interpretación para que no determine diagnósticos, tratamientos ni cuestiones legales a partir de un solo índice. Ante preguntas amplias con pocos valores del Resumen Estructural, no inventa índices inexistentes y propone un orden de comprobación.
- En la ventana de la clave API, el nombre del modelo de OpenAI y el campo de la clave se muestran en una sola línea fácil de leer.
