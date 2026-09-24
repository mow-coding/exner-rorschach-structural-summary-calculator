# Comparación de modelos de IA para Exner v3 — estudio del 2026-09-23

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Comparamos GPT-5.6 Terra, GPT-6 Sol y GPT-6 Luna con los mismos **casos sintéticos** para orientar la elección del modelo de asistencia en codificación y conversación interpretativa de Exner v3. Evaluamos Jev por separado como modelo de decisiones estructuradas. Los resultados describen el **estudio previo al lanzamiento del 2026-09-23**. Después se lanzó v3.0.0 con GPT-6 Luna estándar `medium` solamente, a US$3.99 al mes o US$42.99 al año. Consulte también las [pruebas posteriores y cuestiones pendientes](../2026-09-24/).

## Qué se comparó

Cada modelo GPT recibió **260 casos**: 61 en coreano, 64 en inglés, 47 en japonés, 44 en español y 44 en portugués. Hay 143 casos de asistencia en codificación y 117 de interpretación: 136 preguntas normales, 95 ataques de instrucciones o solicitudes fuera de alcance, 19 conversaciones de varios turnos y 10 resúmenes de conversaciones largas. Cada modelo completó 280 comprobaciones de respuestas y 290 llamadas a la API, incluidas las de resumen. Los modelos recibieron las mismas instrucciones del producto, registros sintéticos y extractos de referencia. Todos usaron un esfuerzo de razonamiento medium: GPT-5.6 Terra lo configuró expresamente; GPT-6 Sol y GPT-6 Luna usaron el valor predeterminado de la API.

| Modelo generativo | Costo calculado por uso, 290 llamadas | Frente a GPT-5.6 Terra | Latencia mediana / percentil 95 | Comprobación original → nueva evaluación de respuestas guardadas |
|---|---:|---:|---:|---:|
| GPT-5.6 Terra | US$3.553828 | Referencia | 3.061 s / 10.469 s | 250/280 → 257/280 |
| GPT-6 Sol | US$2.304015 | 35.2% menor | 3.125 s / 6.681 s | 242/280 → 254/280 |
| GPT-6 Luna | US$0.130514 | 96.3% menor | 3.357 s / 11.365 s | 247/280 → 255/280 |

Tras corregir las pruebas de formato numérico, negación, expresiones de rechazo y formulaciones equivalentes de la regla Na/Bt/Ls, volvimos a evaluar las **mismas 840 respuestas guardadas**. Veintisiete fallos del contrato automático pasaron a aprobados; esto no demuestra que las 27 respuestas sean clínicamente correctas. A la izquierda de la flecha está la puntuación original; a la derecha, la obtenida con la prueba corregida. La tabla por idioma muestra los valores corregidos. No hubo nuevas llamadas a modelos y estas cifras no son tasas de exactitud clínica.

| Comprobaciones automáticas corregidas por idioma | GPT-5.6 Terra | GPT-6 Sol | GPT-6 Luna |
|---|---:|---:|---:|
| Coreano | 57/64 | 57/64 | 57/64 |
| Inglés | 66/72 | 68/72 | 67/72 |
| Japonés | 43/50 | 43/50 | 42/50 |
| Español | 47/47 | 42/47 | 45/47 |
| Portugués | 44/47 | 44/47 | 44/47 |

El costo resulta de aplicar las [tarifas publicadas de OpenAI](https://developers.openai.com/api/docs/pricing) al uso de tokens informado por la API; no es un importe verificado en una factura. Excluye búsqueda, servidor, pagos y tratamiento de solicitudes fallidas. La latencia mide llamadas de prueba, no la experiencia completa en la aplicación web. Como el número de casos varía por idioma, no deben compararse directamente sus porcentajes. El [resumen original](./results.json) y el [resumen corregido](./results-rescored.json) incluyen el desglose por tarea y tipo de caso.

## Cómo interpretar los números

Algunas comprobaciones automáticas **rechazaron respuestas de significado correcto** por no contener una expresión exigida. Por ejemplo, una frase japonesa que decía «no registrar ambos códigos» coincidió con una expresión prohibida; `Lambda: 0.25` tampoco cumplió una prueba que exigía el signo igual. En otros casos, la selección de referencias de la prueba omitió una regla necesaria y el modelo aplazó correctamente el juicio. Por eso, cifras como 250/280 **no son tasas de exactitud clínica ni una clasificación de modelos**. Contrastamos respuestas representativas sobre el límite de cálculo de Cn, el rechazo de mezclas entre sistemas de evaluación, las conclusiones diagnósticas excesivas y las preguntas de seguimiento con los registros y las reglas. Las 840 respuestas generadas no han recibido una revisión clínica independiente completa.

En 30 preguntas sobre el determinante M, 30 respuestas válidas de Jev coincidieron con las **expectativas provisionales del autor**, no con una clave validada por profesionales clínicos. 3 solicitudes con 10 decisiones cada una funcionaron a través de Gateway; 2 intentos de enviar 30 decisiones en una sola solicitud devolvieron HTTP 503. No sabemos si el error se originó en Gateway o en TypeSafe. La [promoción gratuita de Jev en Vercel](https://vercel.com/ai-gateway/models/jev) termina, según lo anunciado, el 2026-09-25; el cargo de prueba de US$0 no sirve como costo permanente. La [tarifa directa publicada por TypeSafe](https://docs.typesafe.ai/models) es US$0.042 por millón de tokens de entrada, con salida gratuita. Aplicarla a los 42341 tokens de entrada de 30 llamadas individuales válidas da **US$0.001778322**: una estimación, no un cargo.

## Prueba pequeña de Jev junto con GPT

Después ejecutamos **2 preguntas sintéticas en cada uno de los cinco idiomas**: 10 preguntas y 40 respuestas GPT en cuatro configuraciones. GPT-6 Solo examinamos la regla Na/Bt/Ls y los límites de evidencia para conclusiones diagnósticas, terapéuticas y forenses. Jev evaluó el alcance, la suficiencia de datos y la relevancia de referencias una vez por pregunta; GPT conservó el registro y los cálculos originales. Son costos para 10 respuestas calculados a partir del uso de GPT, con **US$0.001746** estimados para Jev según la [tarifa directa de TypeSafe](https://docs.typesafe.ai/models) en cada configuración combinada. Los costos de fallos se indican por separado.

| Configuración, razonamiento GPT medium | Costo de 10 respuestas | Pruebas automáticas superadas |
|---|---:|---:|
| GPT-6 Solo GPT-6 Sol | US$0.163943 | 9/10 |
| GPT-6 Solo GPT-6 Luna | US$0.008627 | 9/10 |
| Jev + GPT-6 Sol | US$0.172066 | 8/10 |
| Jev + GPT-6 Luna | US$0.010538 | 8/10 |

**Esta combinación no reduce el costo en su forma actual.** El verificador rechazó 1 respuesta Jev sin conservar el original, por lo que se desconoce la causa; también hubo 2 errores HTTP 503. Los registramos sin reintentos automáticos y completamos las respuestas faltantes en ensayos manuales separados. Las pruebas automáticas todavía rechazan algunas explicaciones correctas en varios idiomas; las cifras no son tasas de exactitud clínica. Con las mismas decisiones de Jev y razonamiento GPT `low`, una respuesta japonesa de Jev + GPT-6 Luna clasificó S-CON como criterio no cumplido sin conocer la edad. Por ello excluimos el razonamiento reducido como candidato de lanzamiento. El [agregado por solicitud](./results-hybrid-pilot.json) no contiene respuestas originales, claves ni datos de clientes.

## Validación con otros grupos de reglas

Obtuvimos 20 respuestas por configuración, 80 en total, en 20 casos sintéticos separados de los usados para ajustar la prueba. Cubren cálculos Cn, pares de niveles de puntuaciones especiales, proporciones GHR/PHR y mezcla de sistemas de evaluación. Los costos combinados suman US$0.002616 estimados para Jev con su tarifa pública directa al costo calculado del uso de GPT. Estos 20 casos estaban separados del ajuste de la combinación, pero ya formaban parte del conjunto anterior de 260 casos de GPT solo; no son preguntas ocultas completamente nuevas.

| Configuración, razonamiento GPT medium | Costo total de 20 respuestas | Pruebas automáticas superadas |
|---|---:|---:|
| GPT-6 Solo GPT-6 Sol | US$0.216957 | 15/20 |
| GPT-6 Solo GPT-6 Luna | US$0.011021 | 17/20 |
| Jev + GPT-6 Sol | US$0.289299 | 19/20 |
| Jev + GPT-6 Luna | US$0.017494 | 19/20 |

La combinación superó más pruebas automáticas, pero no demuestra mayor exactitud clínica. En un caso Cn en coreano, ambas respuestas explicaron correctamente los límites y solo la respuesta sin Jev falló por una exigencia de redacción. Nuestro verificador también rechazó erróneamente una respuesta Jev cuyas probabilidades redondeadas sumaban 0.99. Reutilizamos la respuesta guardada y generamos solo las respuestas GPT faltantes. No fue un fallo del servicio Jev. El [agregado por solicitud](./results-hybrid-holdout.json) excluye respuestas originales, credenciales y datos de clientes.

Nuestra revisión con IA comparó las 80 respuestas originales con reglas limitadas: Cn 20/20, GHR/PHR 20/20, mezcla de sistemas 20/20 y DV 16/20 cumplieron esos criterios. Las respuestas coreanas de DV 4/20 se abstuvieron prudentemente porque faltó la regla en la búsqueda, pero no resolvieron la pregunta. Esta revisión interna encontró 0/80 errores críticos. **Es una revisión de IA, no una evaluación clínica independiente ni exactitud en casos reales.** No se estableció una ventaja de contenido entre configuraciones.

Estos casos sintéticos por sí solos no bastaban para elegir entre GPT-6 Sol y GPT-6 Luna. Después añadimos ensayos con la búsqueda real del producto y su contabilización de uso, y aplazamos Jev. Siguen pendientes una revisión clínica independiente y una conciliación completa de los costos de fallos.

El [informe del 2026-09-24](../2026-09-24/) recoge los ensayos posteriores y la configuración publicada. Ampliaremos la publicación de los prompts, las instrucciones de IA, el código de conexión de modelos y las herramientas de evaluación de v3 después de revisar secretos, ajustes operativos, datos de clientes y derechos de terceros. Este documento conserva las condiciones y los fallos de los ensayos iniciales.
