# [2026-07-18] v2.2.4 Corrección de errores

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Antes de continuar

v2.2.4 es una versión de documentos de referencia, búsqueda con IA y seguridad que **no cambia las fórmulas del Resumen Estructural ni la forma de rellenar la hoja de puntuación**. No es necesario recalcular el Resumen Estructural de un protocolo completado. Tampoco hay que introducir nueva información del evaluado cuando se usa solo la calculadora sin clave API.

Esta versión mejora los documentos de referencia y el material de búsqueda de la IA. Los términos clínicos de los cinco idiomas no se ajustaron por traducción literal; se dio prioridad a las expresiones realmente usadas en la literatura profesional y académica de cada idioma. Los títulos y el orden de los documentos también se organizaron para seguir la puntuación y el Resumen Estructural en lugar del orden alfabético.

Los asistentes opcionales de codificación e interpretación responden solo dentro del ámbito del Sistema Comprehensivo (CS) de Exner. No responden a preguntas sobre otros sistemas de evaluación ni a solicitudes de información no pública.

## Documentos de referencia

### Títulos y orden fáciles de leer en pantalla

Los enlaces existentes de los documentos de referencia se mantienen, y los títulos visibles en pantalla siguen ahora los términos clínicos de cada idioma. Los botones muestran títulos con significado, como `Codificación`, `Calidad formal (FQ)` y `Índices especiales`.

Los documentos de nivel superior se ordenan en este flujo.

1. Codificación
2. Interpretación
3. Upper Section
4. Lower Section
5. Special Indices

Los documentos de codificación siguen el orden lámina, localización, calidad evolutiva (DQ), determinantes, calidad formal (FQ), pares, contenidos, populares (P), actividad organizativa (Z), puntuación, GHR/PHR y puntuaciones especiales. El orden alfabético se usa solo para localizar elementos de detalle dentro de una misma categoría.

### Términos clínicos en los cinco idiomas

Los documentos en coreano, inglés, japonés, español y portugués de Brasil usan los términos profesionales naturales en cada idioma. Cada documento explica la definición central, las condiciones de aplicación, las precauciones y los elementos relacionados.

Entre las correcciones más representativas están las siguientes.

- En el documento PHR en inglés se aclara que `ALOG` forma parte de las condiciones iniciales de PHR en el orden de decisión.
- En los códigos de contenido natural en inglés y español se explicita la prioridad por la que, cuando se aplica `Na`, no se codifican `Bt` ni `Ls` en la misma respuesta.
- En el documento en japonés se corrigió la explicación de `Ay` como contenido cultural/histórico en lugar de anatómico.
- En el documento en coreano se distinguió la frecuencia bruta `S-` de la proporción independiente `S-%`.
- En el documento S-CON en coreano se explicitaron el límite de aplicación a partir de los 15 años y los 12 criterios que lo componen.

Estos cambios no sustituyen la codificación que realiza el clínico tras comprobar el registro de respuestas y la fase de encuesta (Inquiry). Los documentos de referencia son material de apoyo para comprobar las definiciones y los criterios de distinción de los códigos; la codificación final de cada respuesta sigue siendo responsabilidad del evaluador humano.

## Búsqueda de documentos de referencia por la IA

El asistente de IA busca en los documentos de referencia actuales el contenido relacionado con la pregunta.

También encuentra las explicaciones relacionadas en preguntas breves como estas.

- Una pregunta breve sobre la relación entre Cn y WSumC recupera ahora tanto el valor en pantalla que incluye Cn como la explicación de WSumC que lo excluye.
- Una pregunta sobre la prioridad de `Na`, `Bt` y `Ls` ya no recupera solo las descripciones generales de los tres códigos de contenido pasando por alto la frase exacta sobre la prioridad.

## Alcance de los asistentes de codificación e interpretación

Ambos asistentes siguen estos principios.

- Responden solo a preguntas de codificación y del Resumen Estructural del Sistema Comprehensivo (CS) de Exner.
- No amplían sus respuestas a sistemas de evaluación distintos, como R-PAS o MMPI, ni a preguntas generales de orientación o diagnóstico.
- Rechazan las solicitudes de revelar información no pública del servicio o la clave API y los datos de conexión del usuario.
- Cuando la edad es realmente necesaria para una interpretación, pueden explicar el motivo y preguntarla dentro de la conversación de IA, pero la calculadora en sí no exige introducir la edad.
- No determinan un diagnóstico ni un riesgo a partir del Resumen Estructural por sí solo, y dan prioridad a la entrevista, la observación conductual, los datos brutos y el juicio del clínico.

Las solicitudes fuera del ámbito del CS de Exner o de información no pública no se responden; en su lugar, se orienta hacia preguntas de codificación o del Resumen Estructural que sí pueden responderse.

## Prevención de la repetición excesiva de solicitudes de IA

Si las solicitudes de conversación con la IA superan 12 por minuto o 120 por hora, se pide esperar un momento. Este límite reduce la repetición accidental de la misma solicitud y los costes mayores de lo previsto. Para limitar el número de solicitudes no se guardan por separado la clave API, las preguntas, las respuestas, el texto del Resumen Estructural ni el contenido clínico.

Las valoraciones con "me gusta" o "no me gusta" no guardan el texto de la conversación y se conservan durante un máximo de 180 días.

## Cambios en las pantallas y en la descripción del servicio

- La barra lateral izquierda tiene un fondo opaco fijo para que el contenido de detrás no se transparente.
- Se corrigió que el menú de idioma quedara recortado o desalineado sobre el contenido al abrirlo con la barra lateral contraída.
- Los botones de documentos de referencia usan los títulos en los cinco idiomas y el orden que sigue la puntuación y la interpretación.
- Se restauró la ventana que pide elegir de nuevo el modo de inicio (datos nuevos, datos de muestra o datos guardados) cada vez que se entra en la pantalla de puntuación.
- Las frases clave de tipo código en los documentos de referencia se muestran en un rojo fácil de distinguir tanto en modo claro como oscuro.
- En el asistente de codificación, la flecha hacia abajo que aparece al subir para leer la conversación anterior se sitúa justo encima del área de entrada. Ya no tapa el centro de la conversación en respuestas largas.
- Los registros de la versión 2 y la versión 1 se muestran contraídos al entrar por primera vez.
- El nombre del servicio se unificó como `Calculadora del Resumen Estructural del Sistema Comprehensivo de Exner para el Rorschach`.
- La presentación del servicio acredita la producción a MOW y la contribución del Seoul Institute of Clinical Psychology (SICP) en la comprobación de los primeros resultados de cálculo y la revisión desde la perspectiva del uso clínico real.

Las columnas, los desplegables, el botón de cálculo y el control de zoom de la hoja de puntuación, así como la pantalla de resultados del Resumen Estructural, no cambian. Las pantallas móviles también se mantienen.

Las respuestas de la IA pueden variar cada vez y no se garantiza su exactitud clínica para todas las preguntas reales. Tampoco se determina la corrección del cálculo del Resumen Estructural a partir de las respuestas de la IA.

## Fuentes públicas de los términos en los cinco idiomas

Se da prioridad al uso profesional de cada idioma y se mantienen tal cual los códigos e identificadores del Sistema Comprehensivo. Ninguna fuente única se toma como respuesta correcta para todos los idiomas.

- Coreano: [KCI - Construction of the Korean Rorschach Comprehensive System for Children based on Exner's Comprehensive System](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001392063), [KCI - Coping and defense of North Korean defectors on the Rorschach](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001391524)
- Inglés: [International Rorschach Institute manuals](https://www.rorschach-institute.org/manuals.html), [Meyer and Viglione, An Introduction to Rorschach Assessment](https://www.utoledo.edu/al/psychology/pdfs/meyer/MeyerViglione2008IntroRorschach.pdf)
- Japonés: [誠信書房 - 包括システムによるロールシャッハ臨床](https://www.seishinshobo.co.jp/book/b88274.html)
- Español: [Sociedad Española de Rorschach y Métodos Proyectivos](https://www.rorschach.es/index.php/programas-de-los-cursos), [CHESSSS](https://rorschachspain.org/chessss/), [Manual de codificación del Rorschach para el Sistema Comprehensivo](https://www.psimatica.com/tienda/psicodiagnostico/23-manual-de-codificacion-del-rorschach-autor-john-exner.html)
- Portugués de Brasil: [SciELO - Localização e qualidade formal do Rorschach-SC no Brasil](https://www.scielo.br/j/pusf/a/kFHxFGKH3qx9gdVtyC6nqWS/), [SciELO - Indícios de validade do déficit relacional no Método de Rorschach](https://www.scielo.br/j/pusf/a/6Xy8zSJGCNq49BWjXRpYNhx/)
- Principios comunes de traducción y adaptación: [International Test Commission Guidelines](https://www.intestcom.org/page/14)
