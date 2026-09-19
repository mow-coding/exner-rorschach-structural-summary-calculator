# [2026-06-11] v2.0.3 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.3 corrige la apertura lenta de la pantalla de documentos de referencia y errores de conexión de IA. La disposición de las pantallas, el uso y el alcance de las respuestas de IA no cambian; la pantalla de documentos de referencia se abre más rápido y los datos de conexión de IA no válidos se gestionan de forma segura.

## Resumen

- La pantalla de documentos de referencia se abre más rápido.
- Las direcciones existentes de los 1.015 documentos públicos en cinco idiomas se mantienen.
- Los datos de conexión de IA no válidos o caducados se gestionan de forma segura como estado desconectado en lugar de mostrar una pantalla de error.
- El resultado de la comprobación del estado de la conexión de IA no se guarda por separado.
- Se resolvieron los problemas de seguridad de la aplicación web conocidos en ese momento.

## Pantalla de documentos de referencia

Hasta v2.0.2, la primera pantalla de los documentos de referencia podía tardar en aparecer según la velocidad de la conexión.

La calculadora, los resultados del Resumen Estructural y la pantalla de conversación con la IA no se veían afectados, y el contenido y los enlaces de los documentos de referencia no cambiaron. Sin embargo, la primera pantalla de los documentos de referencia podía tardar en aparecer según la velocidad de la conexión.

## Qué ha cambiado

La pantalla de documentos de referencia se abre más rápido y las direcciones de los documentos públicos existentes se mantienen.

Los datos de conexión de IA no válidos o caducados se gestionan como estado desconectado sin mostrar una pantalla de error. El resultado de la comprobación del estado de la conexión de IA no se guarda por separado.

Se resolvieron los problemas de seguridad de la aplicación web conocidos en ese momento.
