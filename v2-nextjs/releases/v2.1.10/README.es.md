# [2026-07-13] v2.1.10 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Antes de continuar

v2.1.10 corrige problemas de la búsqueda de documentos de referencia que persistían tras v2.1.9.

Las pantallas de la aplicación y las fórmulas no cambian. Se conservan los códigos Rorschach unidos a frases en japonés, y las preguntas de interpretación amplias usan solo documentos de interpretación. La IA no determina el código final ni sustituye el juicio del clínico.

## Resumen

- Un código Rorschach seguido de japonés, como en `FQ+の...`, `v/+の...` o `3r+(2)/Rの...`, se reconoce como el código completo.
- Las preguntas de interpretación amplias formuladas de forma natural también reciben los documentos de interpretación relacionados, y las preguntas amplias reciben solo documentos de interpretación.
- Un mismo documento de referencia ya no aparece repetido en los resultados de búsqueda.

La IA no determina automáticamente los códigos ni emite diagnósticos; el juicio final corresponde al clínico.

## Límites que persisten

- Según la formulación de la pregunta, puede pasarse por alto un documento de interpretación relacionado.
- La mejora de la búsqueda y de la forma de responder no demuestra exactitud clínica.
- La utilidad clínica real, la calidad de las frases multilingües y la seguridad deben ser evaluadas por profesionales cualificados.
