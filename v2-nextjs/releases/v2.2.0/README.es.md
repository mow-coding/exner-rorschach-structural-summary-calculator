# [2026-07-14] v2.2.0 Versión menor

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

> **Fórmulas actuales:** los extremos de D/AdjD, la condición de visualización de EBPer, el orden de decisión de GHR/PHR, la omisión de Cn en `FC:CF+C` de la Lower Section y el tratamiento del denominador cero de WDA% y Afr se corrigieron en v2.2.1. En v2.2.2 se separaron los cálculos que incluyen Cn de los que no lo incluyen y se completó la clasificación GHR/PHR de las filas incompletas con calidad formal (FQ) vacía. La calculadora no pide la edad; solo cuando se solicita una interpretación con restricción de edad, la conversación de interpretación con IA pregunta la información necesaria. **Consulte la base de cálculo actual en la [nota de v2.2.2](../v2.2.2/).**

## Antes de continuar

v2.2.0 es la primera versión de la serie v2.2.x: mantiene la calculadora en el centro, agrupa los menús principales de la pantalla de escritorio en una barra lateral izquierda y reconstruye el asistente de interpretación para que se parezca a una pantalla habitual de chat con IA. La valoración de las respuestas de IA no guarda el texto de la conversación; solo se elige un motivo predefinido.

Los elementos de cálculo tratados en esta versión que necesitaban correcciones adicionales se corrigieron en v2.2.1 y v2.2.2. El asistente de IA no responde a preguntas fuera del Sistema Comprehensivo de Exner ni a solicitudes de información no pública.

## Resumen

### Pantallas comunes y barra lateral

- Los antiguos menús superior e inferior se integraron en una barra de iconos fija en escritorio, una barra lateral que se abre sobre el contenido y un menú para móvil.
- La barra lateral no desplaza el contenido, se mantiene abierta al navegar a otra página y reúne en un solo lugar los controles de idioma, tema y sesión de IA.
- Antes de iniciar sesión solo se muestra "iniciar sesión de IA"; después, solo "finalizar sesión de IA", con una ventana de confirmación antes de finalizar.
- Se añadió una guía multilingüe de atajos que reúne los atajos de la calculadora, los de la barra lateral y la forma de ampliar, reducir y desplazar la pantalla de puntuación.
- Se unificaron el fondo y los colores de los modos claro y oscuro de la calculadora, el asistente de interpretación, los documentos de referencia, la presentación del servicio, los términos, la política de privacidad y el archivo de versiones.
- Se eliminaron el borde exterior innecesario y el botón de copiar toda la página en las páginas de servicio, términos y privacidad.

### BYOK y asistente de interpretación

- BYOK (Bring Your Own Key) significa que el usuario conecta su propia clave API de OpenAI para usar las funciones opcionales de IA.
- La clave API de OpenAI y la indicación `OpenAI GPT-5.5` se colocan en la misma línea, y se eliminaron el título duplicado y el aviso de selección automática de modelo, de modo que la ventana de conexión de IA es más compacta.
- Se muestra con más claridad el aviso de que la clave API se conserva cifrada durante un máximo de 24 horas para la conexión de IA y se elimina al finalizar la conexión. La ventana ya no cambia de tamaño cuando aparece el aviso de clave incorrecta.
- El asistente de interpretación pasó a ser un espacio de trabajo completo sin tarjeta exterior, y las conversaciones largas se desplazan solo dentro del área de conversación, no en toda la página.
- El desplazamiento automático que sigue la respuesta de la IA se detiene cuando la persona sube, y se puede volver a la última respuesta cuando haga falta.
- Se añadieron detener la respuesta, copiar mensaje, localizar la pregunta anterior, un cuadro de entrada translúcido y el estado de pegado del Resumen Estructural.
- Los mensajes del usuario y de la IA tienen botón de copiar, y los mensajes de la IA incorporan "me gusta"/"no me gusta" con una ventana de motivos predefinidos.
- La valoración de las respuestas de IA no guarda el texto de la pregunta ni de la respuesta ni comentarios libres. Solo se conservan, durante un máximo de 180 días, si ayudó, el motivo elegido, el idioma, el modelo, si la respuesta se completó y su longitud aproximada.

### Pantalla de puntuación

- El asa para mover filas ya no se recorta en el borde de la tabla.
- La selección de varias filas con clic normal, `Mayús + clic` y `Ctrl/Comando + clic`, y la vista previa del movimiento de filas, funcionan de forma estable.
- Los cuadros de selección con valor, vacíos y deshabilitados mantienen el mismo tamaño y alineación y se distinguen solo por el tono.
- Se ajustaron los anchos de columna para que la tabla quepa en una pantalla de escritorio habitual y, en pantallas estrechas, se desplace horizontalmente solo dentro del área de puntuación.
- `Alt + rueda del ratón` amplía o reduce toda la pantalla de puntuación entre el 40 % y el 125 % centrada en el puntero, y `Ctrl + arrastrar` desplaza la pantalla ampliada.
- La indicación del orden de las filas se muestra en la franja azul justo debajo de la tabla.
- Los botones inferiores se ordenaron como añadir/eliminar/ayuda a la izquierda y calcular resultados/restablecer entradas en el centro.

### Documentos de referencia y archivo de versiones

- El cuadro de búsqueda de documentos de referencia no desaparece en los resultados ni en el documento detallado, y el término de búsqueda se conserva en la siguiente pantalla.
- El aviso de ausencia de resultados, los botones de categoría de documentos y el aviso de copia completada se ajustaron en los cinco idiomas.
- El cuerpo de los documentos de referencia pasó a ser una vista de lectura sin tarjeta exterior, con el cuadro de búsqueda, las categorías y el cuerpo alineados en el mismo eje central.
- Los registros de la versión 2 y de la versión 1 (GAS) se despliegan y contraen pulsando el título, y la pantalla ya no se desplaza lateralmente cuando aparece la barra de desplazamiento vertical al desplegarlos.
- Las indicaciones de ejecución de GAS se trasladaron a una ayuda informativa junto al título, que también se puede abrir con el teclado.

## Cambios de cálculo en v2.2.0

En v2.2.0 se corrigieron los siete elementos siguientes. Las fórmulas actuales incluyen además las correcciones posteriores de v2.2.1 y v2.2.2.

| Elemento | Corrección |
| --- | --- |
| EBPer | Se muestra solo cuando `EA >= 4`, M y WSumC son positivos y la proporción es `>= 2.5` |
| Movimiento activo/pasivo | `Ma-p`, `FMa-p` y `ma-p` se suman tanto al lado activo como al pasivo |
| `3r+(2)/R` | El peso de las reflexiones `Fr+rF` se corrigió de 2 al 3 de la fórmula estándar |
| HVI | El límite de la condición auxiliar de Zd se corrigió de `> 3.0` a `> 3.5` |
| ZEst | El último límite válido `Zf=50` devuelve ahora `173` |
| D/AdjD | `0` en lugar de `-0` en el rango negativo |
| Lambda | `∞` en lugar de 0 cuando todas las respuestas son F pura |

Para comparar los resultados del cálculo se usaron cuatro tipos de materiales.

- [Sample computerized score reports de Essentials of Rorschach Assessment](https://elmirmohammedmemorypsy.com/wp-content/uploads/2021/04/essentials-of-rorschach-assessment.pdf)
- [Engelman et al., "Why am I so stuck?"](https://www.therapeuticassessment.com/docs/Engelman_et_al_2016_copy.pdf)
- [Caso de síndrome amnésico de Tibon Czopp et al.](https://pubmed.ncbi.nlm.nih.gov/23985019/) y su [fe de erratas](https://www.tandfonline.com/doi/pdf/10.1080/13554794.2014.910345)
- Las fórmulas reales del [libro de Excel de 2019 de distribución pública](https://blog.naver.com/jin_k84/221539279596) consultado en el desarrollo inicial de v1. La atribución interna del libro es `[Scoring Program] _by. Ju-Ri`; no se infiere ningún nombre real ni se redistribuye el archivo original.

En los dos elementos en que las tablas publicadas y las columnas de puntuación públicas discrepaban, no se tomó ninguna de las dos como única respuesta correcta.

Las medias de grupos nacionales no son claves de corrección para una misma columna de puntuaciones. Las diferencias culturales afectan sobre todo a la codificación, las normas y la aplicación interpretativa, no a las fórmulas, por lo que los materiales coreanos, japoneses y de habla inglesa se usaron por separado para comprobar el rango de respuestas por cultura y edad.

## Alcance del asistente de IA

- No responde a interpretaciones generales de R-PAS ni de MMPI, a preguntas sin relación ni a solicitudes de información no pública.
- Las preguntas válidas de comparación o diferenciación con Exner se permiten solo en la medida de explicar el límite, sin extenderse a la interpretación general de otros sistemas.
- La interpretación del S-CON se aplica a personas de 15 años o más. La calculadora no pide la edad; solo cuando se le solicita una interpretación del S-CON, el asistente de IA confirma la edad en la conversación si es necesario.
- Ante una pregunta directa sobre Popular (`P`), se presenta primero el documento de referencia de respuestas populares.

Se mantiene el uso de GPT-5.5 con la clave API propia. Las conversaciones con la IA solo se conservan mientras se usa la ventana actual del navegador y no se guardan como registros de cuenta a largo plazo. La IA no sustituye el juicio final del clínico ni garantiza la exactitud de todas las respuestas.

## Límites que persisten

- Este alcance de cálculo no demuestra matemáticamente todas las combinaciones de respuestas posibles.
- Como la calculadora no pide la edad, el clínico que la use debe comprobar la suspensión de la interpretación del S-CON en personas de 14 años o menos.
- La utilidad clínica real, la calidad de las frases multilingües y la seguridad deben ser evaluadas por profesionales cualificados.
