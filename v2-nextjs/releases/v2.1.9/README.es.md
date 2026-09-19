# [2026-07-12] v2.1.9 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Antes de continuar

v2.1.9 mejora el método de búsqueda para que el asistente de codificación y el asistente de interpretación encuentren de forma más fiable los documentos de referencia adecuados a una pregunta antes de responder.

Las pantallas de la aplicación no cambian. Los documentos de referencia relacionados con una pregunta se encuentran con más precisión en los cinco idiomas, y el asistente de codificación toma como referencia solo las filas seleccionadas por el usuario.

## Resumen

- Se reduce la confusión de palabras de una sola letra con códigos Rorschach, conservando los códigos explícitos por el contexto, como `Card I`, `Content A` y el determinante en minúscula `m`.
- Se reconocen con más precisión las preguntas con partículas y terminaciones del coreano o con japonés, y los índices compuestos como `3r+(2)/R`.
- Los documentos relacionados con la pregunta se encuentran con más precisión.
- Se excluyen los resultados con muy poco significado y un mismo documento de referencia ya no aparece varias veces.
- El asistente de codificación toma como referencia solo la fila seleccionada y las filas que el usuario haya seleccionado junto con ella.

Esta versión mejora la búsqueda de documentos de referencia, pero la IA no determina automáticamente el código final ni emite diagnósticos. El juicio final corresponde al clínico.

## Límites que persisten

- La mejora de la búsqueda no demuestra exactitud clínica.
- Las respuestas de GPT-5.5 son probabilísticas, por lo que no se garantizan todas las respuestas futuras.
- La utilidad clínica real, la calidad de las frases multilingües y la seguridad deben ser evaluadas por profesionales cualificados.
