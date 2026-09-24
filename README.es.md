# Calculadora del Sumario Estructural del Sistema Comprehensivo de Rorschach de Exner

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Exner es una aplicación web que ayuda a revisar la codificación y el Sumario Estructural del Sistema Comprehensivo de Rorschach. La versión actual, **v3.0.0**, combina la calculadora con asistentes de IA a los que se puede hacer preguntas de seguimiento. Los códigos y las explicaciones sugeridos son información de apoyo; el juicio final corresponde al profesional, a partir de la respuesta original y el registro de la fase de encuesta.

## Acceder a la aplicación

- [Aplicación web v3 de pago](https://exner.app): disponible en coreano, inglés, japonés, español y portugués brasileño. La suscripción cuesta **US$3.99 al mes** o **US$42.99 al año**.
- [Aplicación web v2 gratuita](https://exner.yesucan.co.kr): la calculadora anterior sigue disponible, con asistencia de IA opcional mediante la propia clave API del usuario.

## Cambios en v3.0.0

Una cuenta de Google y una suscripción dan acceso a los asistentes de codificación e interpretación. Ambos usan **GPT-6 Luna**. En conversaciones largas, la aplicación resume el contexto previo para las preguntas siguientes. Las fórmulas del Sumario Estructural no han cambiado respecto a la v2, por lo que esta versión, por sí sola, no exige recalcular registros anteriores.

Las [notas de v3.0.0](./v3-web/releases/v3.0.0/README.es.md) explican las funciones y los límites clínicos. La [comparación de modelos](./v3-web/benchmarks/2026-09-23/) y la [evaluación posterior](./v3-web/benchmarks/2026-09-24/) describen los métodos, resultados y costos. Las verificaciones automáticas de casos sintéticos no son tasas de precisión clínica.

## Código fuente y versiones anteriores

Este repositorio contiene el [código publicado de v2](./v2-nextjs/source/), el [código publicado de v1](./v1-gas/current/) y el [historial completo de versiones](./CHANGELOG.es.md). Todavía no hemos publicado todo el código de producción de v3. Prevemos publicar el código y las instrucciones de IA revisados tras comprobar secretos, registros clínicos y derechos de terceros, conservando los avisos de derechos de autor existentes.

MOW planifica y opera el servicio. El Seoul Institute of Clinical Psychology (SICP) contribuyó a comprobar los primeros resultados de cálculo y a revisar el uso clínico. Véanse también los [agradecimientos y referencias del aprendizaje inicial](./ACKNOWLEDGEMENTS.es.md).

El [aviso de v3](./v3-web/NOTICE.md) explica la atribución y el alcance de publicación de los nuevos registros de v3. Se conservan los avisos de derechos de autor de v1 y v2.
