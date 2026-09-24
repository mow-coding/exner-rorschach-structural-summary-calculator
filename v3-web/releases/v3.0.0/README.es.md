# [2026-09-24] v3.0.0 versión mayor — Aplicación web de pago con asistentes de IA

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Exner v3.0.0 permite conversar libremente con asistentes de IA al revisar la codificación y la interpretación del Sumario Estructural del Sistema Comprehensivo de Rorschach. La nueva aplicación está disponible en [exner.app](https://exner.app). Las respuestas de IA son información de apoyo; la codificación e interpretación finales, basadas en la respuesta original y el registro de la fase de encuesta, corresponden al profesional clínico.

## ¿Qué cambió?

- Puede registrarse con una cuenta de Google y dar un consentimiento separado para enviar información a la IA antes de utilizar los asistentes de codificación e interpretación. Ambos emplean GPT-6 Luna con razonamiento `medium` y el nivel de servicio estándar. Evaluamos Jev, pero no forma parte de la generación de respuestas de v3.0.0.
- La aplicación busca material de referencia pertinente a la pregunta y resume lo anterior para preguntas posteriores en conversaciones largas. Ni el resumen ni una respuesta de IA modifican el protocolo original o un resultado verificado por la calculadora. El asistente puede pedir información que falte.
- La interfaz y el material de referencia están disponibles en coreano, inglés, japonés, español y portugués brasileño. Seguiremos mejorando las respuestas en cada idioma; no afirmamos que todos los juicios clínicos estén igual de completos en los cinco.
- La suscripción cuesta **US$3.99 al mes** o **US$42.99 al año**. El importe en otra moneda y los impuestos dependen de la pantalla de pago y de las condiciones de la tarjeta. El uso se administra mediante un presupuesto de costo de procesamiento de IA, no un número fijo de preguntas. La aplicación muestra el uso restante y el estado de la suscripción.

## ¿Debo recalcular un protocolo anterior?

Esta versión no modifica las fórmulas del Sumario Estructural de v2 ni los cálculos ya completados. No es necesario recalcular un protocolo de v2 debido a este lanzamiento. Los códigos y las explicaciones sugeridos por la IA no son una puntuación definitiva: para uso clínico, contrástelos con la respuesta original, la fase de encuesta y el conjunto de los datos clínicos.

## Evidencia y límites

Antes del lanzamiento comparamos GPT-5.6 Terra, GPT-6 Sol, GPT-6 Luna y Jev con **casos sintéticos**. Examinamos por separado la codificación, la interpretación, los resúmenes, la búsqueda real de referencias, los tiempos y el uso en cada idioma. También realizamos una revisión de IA separada con Claude Fable 5.1. No tratamos las pruebas automáticas de redacción como precisión clínica ni presentamos una revisión por IA como revisión clínica independiente. Los modelos exactos, cifras, cálculos de costos, fallos y respuestas incompletas figuran en la [comparación inicial](../../benchmarks/2026-09-23/) y el [informe posterior de la configuración de lanzamiento](../../benchmarks/2026-09-24/).

![Costo de generación y resultados de pruebas automáticas de redacción para tres modelos GPT con las mismas entradas sintéticas](../../benchmarks/2026-09-23/model-comparison.svg)

Las pruebas automáticas anteriores **no miden precisión clínica**. La siguiente comparación incluye búsqueda real de referencias, pero utilizó GPT-6 Luna **Fast**; no describe la velocidad ni el costo de la clase estándar publicada.

![Costo calculado de búsqueda y generación y tiempo hasta el primer texto de GPT-5.6 Terra estándar y GPT-6 Luna Fast](../../benchmarks/2026-09-24/retrieval-trial.svg)

En el sitio de producción comprobamos con cuentas sintéticas las respuestas de ambos asistentes y la creación de una pantalla de pago Live. **Al publicarlo, aún no habíamos completado una transacción real que incluyera nuevo registro, pago, concesión del acceso, cancelación y reembolso.** Contrastaremos los registros de transacciones y acceso y corregiremos cualquier problema observado. También quedan pendientes la revisión clínica independiente de las respuestas y algunas respuestas multilingües incompletas.

Las Condiciones de uso y la Política de privacidad entran en vigor el **2026-09-24**. El consentimiento para enviar información a la IA es independiente de la suscripción y puede retirarse. Publicaremos el código y los prompts de v3 por partes revisadas tras comprobar secretos, registros clínicos y derechos de terceros. Estas notas y los informes de referencia no significan que ya se haya publicado todo el código de producción.
