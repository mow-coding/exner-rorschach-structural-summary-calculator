# [2026-06-22] v2.1.0 Versión menor

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.1.0 permite abrir la aplicación web como una aplicación instalada en los navegadores compatibles, acredita el proyecto público RorScore y mejora la forma en que la IA busca primero los documentos de referencia adecuados para una pregunta de codificación.

## Resumen

- En navegadores compatibles como Chrome y Edge, la aplicación web se puede abrir como una aplicación instalada.
- La función de instalación no incluye almacenamiento sin conexión, notificaciones push ni sincronización en segundo plano, y no guarda por separado en el dispositivo datos de evaluación sensibles ni respuestas de IA.
- Ante una pregunta de codificación como `DQ+`, la IA consulta primero los documentos de entrada de puntuación relacionados.
- El proyecto público RorScore se acredita como material de referencia.

## Instalación y conservación de datos

La función de instalación no cambia la forma en que la aplicación conserva los datos ni el principio de protección de la clave API. La clave API se usa cifrada para la conexión de IA; la conexión dura como máximo 24 horas y, al finalizarla, la clave también se elimina.

La aplicación instalada también se usa con conexión a internet y no guarda sin conexión datos de evaluación sensibles ni respuestas de IA.

Este cambio no afecta a los resultados del cálculo. Cuando el asistente de codificación recibe una pregunta como "¿Cuándo debe codificarse DQ+ en lugar de DQo o DQv/+?", consulta los documentos de entrada de puntuación relacionados antes que los documentos de interpretación.

## Reconocimiento a RorScore

El proyecto público RorScore se acredita como material de referencia.
