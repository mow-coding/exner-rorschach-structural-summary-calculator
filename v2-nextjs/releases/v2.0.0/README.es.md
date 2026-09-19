# [2026-02-15] v2.0.0 Versión mayor

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.0 es la primera versión 2: traslada v1.4.1 a una nueva aplicación web. Mantiene el núcleo de v1, el flujo de cálculo del Resumen Estructural del sistema Exner (CS) del Rorschach, y añade pantallas multilingües, búsqueda de documentos de referencia y asistencia de IA basada en BYOK.

El mayor cambio de esta versión es el modo BYOK (Bring Your Own Key): el usuario conecta su propia clave API de OpenAI o de Google para usar las funciones de IA. Los costes de uso de la IA se generan en la cuenta conectada, y la clave API se usa solo mientras la conexión de IA está activa.

## Lo que se conserva de v1.4.1

El propósito central de v1.4.1 se mantiene. El usuario introduce las respuestas Rorschach fila por fila, organiza los valores necesarios para el Resumen Estructural, como lámina, localización, calidad evolutiva, determinantes, calidad formal, contenidos y puntuaciones especiales, y luego calcula los resultados.

El flujo de cálculo del Resumen Estructural, la revisión de resultados, la exportación CSV y el soporte multilingüe de v1 pasan a v2. Las pantallas de entrada y de resultados se reconstruyeron como pantallas de aplicación web fáciles de usar en móvil y en escritorio.

## Modo de uso

Las pantallas principales son la pantalla de puntuación, el asistente de interpretación, los documentos de referencia, la gestión de la cuenta y el archivo de versiones. Las funciones básicas de cálculo y la búsqueda de documentos de referencia se pueden usar sin iniciar sesión; para usar las funciones de IA hay que iniciar sesión y conectar una clave API.

## Conexión de IA con BYOK

Las funciones de IA de v2 funcionan solo con BYOK. La aplicación no vende créditos ni suscripciones de IA; el usuario puede conectar una clave API de OpenAI o de Google.

La clave API se usa solo mientras la conexión de IA está activa y se elimina al cerrar sesión o cuando la conexión caduca. Si se introduce una clave de OpenAI o de Google en el campo equivocado, se avisa de inmediato.

El usuario no elige el modelo. La aplicación web usa automáticamente el modelo más reciente definido por el servicio entre los modelos cuya estabilidad se ha confirmado pasado un tiempo desde su lanzamiento. En v2.0.0, los modelos predeterminados son GPT-5.4 para OpenAI y Gemini 2.5 Pro para Google.

Cuando el proveedor de IA rechaza una solicitud, los errores no se agrupan en uno solo. La aplicación distingue una clave API incorrecta, un problema de facturación o de límite de uso, y un modelo que no se puede usar con esa clave API, e informa al usuario de cuál es.

## Asistente de codificación

La IA de la pantalla de puntuación se organiza como asistente de codificación. Aquí "codificación" no significa programación, sino el proceso de codificar las respuestas Rorschach en los símbolos y categorías del sistema Exner (CS).

El asistente de codificación se abre con el atajo Ctrl/Cmd+J. Se le pasa como contexto por defecto toda la hoja introducida en la pantalla de puntuación actual y, si hay una fila seleccionada, esa fila se destaca como contexto más importante. Sin ninguna fila seleccionada, se usa solo el contexto de la hoja completa, sin fila central.

El asistente de codificación no determina la respuesta automáticamente. Al revisar la localización, los determinantes, la calidad formal y las categorías de contenido de una respuesta, explica los candidatos posibles y sus fundamentos a partir de los documentos de referencia y de los datos introducidos.

v2.0.0 no ofrece un botón de autocompletado. La IA solo explica candidatos y fundamentos; la codificación final la decide el clínico tras revisar el contexto de la respuesta.

## Asistente de interpretación

El asistente de interpretación es una pantalla de IA para mantener una conversación de interpretación a partir de un CSV con los valores del Resumen Estructural. El usuario adjunta el archivo CSV con los valores del Resumen Estructural, añade la edad, el sexo, el contexto de observación y las hipótesis o preguntas que el clínico ya tiene en mente, y pide a la IA que las revise.

El asistente de interpretación cumple una función de apoyo: explica los patrones de los resultados del Resumen Estructural y contrasta las hipótesis planteadas por el usuario. No sustituye un diagnóstico oficial ni la interpretación final; el juicio final corresponde al clínico.

## Documentos de referencia

v2 ofrece además una colección de breves documentos explicativos que consultan la aplicación web y los asistentes de IA. Estos documentos explican los conceptos principales del cálculo del Resumen Estructural, la codificación y el proceso de interpretación, y se pueden buscar directamente en la pantalla de documentos de referencia.

Los documentos de referencia se elaboraron a partir de material producido y organizado conjuntamente por el Seoul Institute of Clinical Psychology y MOW. El objetivo de publicarlos es que el usuario pueda comprobar en qué conocimiento se basa la IA para responder. Esto se relaciona con el principio de diseño de no dejar las funciones de IA como una caja negra, para que el usuario pueda comprobar los fundamentos y juzgar por sí mismo.

Los documentos de referencia cuyo nombre contiene códigos como `+`, `-` y `v/+` se abren correctamente.

## La IA no sustituye el juicio del clínico

v2 no pretende ser un sistema en el que la IA juzgue en lugar del profesional, sino un sistema que ayude a psicólogos clínicos y a personas en formación a revisar y juzgar sobre fundamentos más claros. Por eso solo se conservan dos funciones de IA: el asistente de codificación en la pantalla de puntuación y el asistente de interpretación en una pantalla de chat aparte.

Las respuestas de la IA son de referencia y apoyo; la codificación y la interpretación finales las juzga el clínico.

## Seguridad y privacidad

Las claves API y el texto de las conversaciones con la IA no se conservan como datos de cuenta a largo plazo. La clave API se usa solo mientras la IA está conectada y se elimina al cerrar sesión o cuando la conexión caduca.

Los costes de uso de la IA se generan en la cuenta del proveedor de API conectada por el usuario; la aplicación no tiene funciones propias de pago ni de suscripción.

## Pantallas y facilidad de uso

Se reorganizaron el menú superior, la selección de idioma, el modo claro/oscuro, la gestión de la cuenta, el archivo de versiones y la pantalla de búsqueda de documentos de referencia.

En la pantalla de puntuación se ajustaron la selección de filas, la adición/eliminación de filas, los atajos y el flujo de deshacer/rehacer. Las filas seleccionadas se mantienen resaltadas, y el contexto que recibe el asistente de codificación cambia según la selección.

En la pantalla del asistente de interpretación se añadieron un botón para adjuntar CSV y la posibilidad de arrastrar y soltar. Además de pegar texto, se puede adjuntar un CSV con los valores del Resumen Estructural y usar su contenido como contexto de la conversación con la IA. Solo se admite un archivo adjunto a la vez, lo que reduce el riesgo de que la IA lea un contexto equivocado a partir de materiales mezclados.

## Soporte multilingüe

v2 ofrece pantallas en coreano, inglés, japonés, español y portugués. El idioma se elige en un desplegable, y la disposición se mantiene estable aunque varíen el tamaño de la pantalla y la longitud de los textos en cada idioma.

## Alcance del producto

El alcance central de v2.0.0 es el cálculo del Resumen Estructural, los documentos de referencia y los asistentes de codificación e interpretación basados en BYOK. No incluye créditos de IA, pagos ni suscripciones ofrecidos por el servicio.
