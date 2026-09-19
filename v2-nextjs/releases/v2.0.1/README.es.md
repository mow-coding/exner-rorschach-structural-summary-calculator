# [2026-04-27] v2.0.1 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.1 corrige problemas de uso detectados tras la publicación de v2.0.0. El alcance del producto —cálculo del Resumen Estructural, documentos de referencia y asistentes de codificación e interpretación basados en BYOK— se mantiene.

## Resumen

- El flujo de entrada del asistente de interpretación pasó de centrarse en adjuntar archivos a centrarse en introducir los valores del Resumen Estructural.
- En los asistentes de codificación e interpretación se redujeron las respuestas demasiado largas de la IA y los movimientos de pantalla difíciles de controlar.
- Se eliminó el flujo de autocompletado con IA. La codificación y la interpretación se revisan únicamente conversando con la IA.
- Se corrigieron las pantallas de conexión y desconexión de la clave API que se superponían o no mostraban las indicaciones necesarias.
- Se corrigieron los avisos emergentes y las burbujas de aviso del sistema que se veían transparentes o eran difíciles de leer en modo oscuro.
- Se corrigió que no se abrieran las páginas de documentos de referencia al pulsar códigos como `+`, `-` o `v/+`.
- La presentación del servicio, los términos del servicio y la política de privacidad se actualizaron para reflejar las funciones actuales.

## Introducir los datos del Resumen Estructural en el asistente de interpretación

En v2.0.0, el asistente de interpretación se describía como un flujo en el que se adjuntaba un archivo CSV del Resumen Estructural. Adjuntar archivos podía crear dudas sobre qué archivo usar, y la IA podía no leer el contenido del archivo de forma estable y uniforme.

En v2.0.1, el flujo consiste en pegar los valores del Resumen Estructural copiados desde la pantalla de resultados en un campo específico del asistente de interpretación. Tras copiar los valores del Resumen Estructural en la pantalla de resultados, se pegan en el pequeño campo de valores situado a la izquierda del cuadro de entrada del asistente de interpretación y se empieza a preguntar.

Al pegar los valores, se muestra `Introducido` en lugar del texto completo. Mientras se use la misma ventana del navegador, la entrada se conserva hasta que el usuario la borre o la sustituya por nuevos valores.

Además, para que el asistente de interpretación no acepte cualquier material, solo se usa la entrada que tenga el formato de los valores del Resumen Estructural copiados desde la pantalla de resultados. Si el usuario introduce un texto sin relación e intenta iniciar la conversación, un aviso le indica que use la función de copiar valores del Resumen Estructural de la pantalla de resultados.

## Respuestas del asistente de interpretación

Las respuestas del asistente de interpretación se ajustaron a una longitud y un formato que permiten continuar la conversación. Justo después de v2.0.0, las respuestas podían alargarse en exceso, cortarse a mitad o enumerar demasiados valores en una línea, lo que dificultaba la lectura.

El asistente de interpretación ya no abre demasiados temas en una sola respuesta y muestra por separado los `valores de referencia` y las `hipótesis interpretativas`.

El asistente de interpretación usa expresiones más intuitivas, como `datos de la prueba`, `datos de las respuestas` y `datos del Resumen Estructural`, en lugar de `protocolo`.

## Asistente de codificación

El asistente de codificación ayuda mediante conversación mientras el usuario codifica las respuestas en la pantalla de puntuación. En v2.0.1 se eliminó el flujo por el que el asistente rellenaba filas automáticamente o aplicaba campos con un botón.

Ahora el asistente de codificación solo explica en la conversación los candidatos y sus fundamentos a partir de la fila seleccionada y del contexto de toda la hoja. El usuario puede tomar como referencia la explicación de la IA, pero debe revisar e introducir por sí mismo los valores de codificación.

Se mantiene la posibilidad de abrir el asistente de codificación con `Ctrl/Cmd+J` en la pantalla de puntuación. Sin ninguna fila seleccionada, solo se usa la hoja completa como contexto, sin fila central; si hay una fila seleccionada, esa fila se trata como contexto más importante.

## Eliminación del autocompletado con IA

Se eliminó la función `Autocompletar con IA`. Esta función intentaba rellenar de una vez los campos de codificación de la fila actual a partir de las notas de la respuesta y la información de la lámina.

La codificación Rorschach requiere la revisión y el juicio del clínico. Se eliminó el autocompletado para evitar que las sugerencias de la IA se acepten sin una revisión suficiente; la entrada final la decide el clínico.

Como resultado, las funciones de IA de v2.0.1 son más sencillas. La IA de la aplicación web ofrece solo dos ayudas conversacionales: el asistente de codificación y el asistente de interpretación.

## Pantalla de conexión de la clave API

La clave API se usa solo mientras la conexión de IA está activa y se elimina al finalizar la conexión.

Si se introduce una clave API de Google en el campo de OpenAI o una clave API de OpenAI en el campo de Google, se indica el campo correcto.

También se corrigió la superposición entre el botón de finalizar la conexión API y la ventana de entrada de la clave. Al abrir el asistente de interpretación sin una clave API conectada, se indican los pasos necesarios.

## Selección del modelo de IA

El usuario no elige el modelo. La aplicación web usa automáticamente el modelo más reciente definido por el servicio entre los modelos publicados hace al menos un mes cuya estabilidad se ha confirmado.

Las indicaciones sobre la selección del modelo se muestran solo en las pantallas necesarias, para que no parezca que el usuario debe elegir un modelo.

## Avisos en modo oscuro

En modo oscuro, las burbujas de aviso del sistema o los avisos emergentes de la esquina superior derecha podían verse transparentes o mezclarse con el fondo y ser difíciles de leer. En v2.0.1, el color de fondo, el borde y el color del texto de los avisos emergentes y de los mensajes de aviso del chat se muestran con más claridad.

Los avisos de éxito, advertencia y sistema se ajustaron para que no queden ocultos por otros elementos de la pantalla ni se mezclen con el fondo.

## Pantalla de conversación con la IA

Tanto en el asistente de codificación como en el de interpretación se redujeron los textos de ayuda innecesarios y los mensajes duplicados. Se eliminaron elementos que interrumpían el flujo de la conversación o parecían funciones excesivas, como el nombre del modelo de IA, la lista de documentos de referencia y los botones de aplicar campos.

También se redujo el problema de que la pantalla bajara continuamente de forma forzada mientras la IA respondía, lo que dificultaba controlar el desplazamiento. Ahora el desplazamiento automático no interviene en exceso cuando el usuario está leyendo contenido anterior.

El movimiento de los puntos de la burbuja que se muestra mientras se espera la respuesta se suavizó para que moleste menos. Una herramienta conversacional es una pantalla que el usuario mira durante mucho tiempo, y hasta un movimiento pequeño puede resultar cansado.

## Documentos de referencia que no se abrían

Algunos documentos de referencia tienen códigos como `+`, `-` y `v/+` en su nombre. En v2.0.0, algunos enlaces con estos códigos no se abrían.

Ahora, al pulsar elementos como `[Codificación/Calidad evolutiva] v`, `[Codificación/Calidad evolutiva] v/+`, `[Codificación/Calidad formal] +` y `[Codificación/Calidad formal] -`, se abre el documento correcto.

## Información del servicio

La presentación del servicio, los términos del servicio y la política de privacidad se actualizaron para reflejar las funciones realmente ofrecidas. También se corrigieron indicaciones erróneas que hacían parecer que la aplicación ofrecía créditos de IA, pagos o una tienda.
