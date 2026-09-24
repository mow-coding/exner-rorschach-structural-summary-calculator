# Exner v3.0.0: selección de GPT-6 Luna y pruebas en el entorno de producción — 2026-09-24

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Este informe continúa la [comparación del 2026-09-23](../2026-09-23/) de GPT-5.6 Terra, GPT-6 Sol, GPT-6 Luna y Jev. v3.0.0 usa **solo GPT-6 Luna, razonamiento `medium` y nivel estándar (`default`)**. No se utilizan Jev ni cambios automáticos a otro modelo generativo. Los casos sintéticos no demuestran precisión clínica ni equivalencia entre modelos.

La primera comparación utilizó 260 casos sintéticos y 290 llamadas por modelo GPT, con 280 pruebas de respuestas y resúmenes. Al reevaluar las respuestas guardadas con un detector de expresiones corregido, GPT-5.6 Terra obtuvo **257/280**, GPT-6 Sol **254/280** y GPT-6 Luna **255/280**. Son resultados de una prueba automática, no porcentajes de acierto clínico. El uso multiplicado por los precios públicos dio un costo de generación de **US$3.553828**, **US$2.304015** y **US$0.130514**, respectivamente. Se utilizaron tres fragmentos de referencia fijos, distintos de la búsqueda del producto. La [comparación anterior](../2026-09-23/) conserva las pruebas de Jev, los errores HTTP 503 y los costos estimados.

Al revisar las 280 respuestas y 10 resúmenes guardados de GPT-6 Luna descubrimos que una primera revisión omitía parte del resumen anterior y que una entrada de Claude dañaba el texto UTF-8. No usamos esos juicios como prueba final. Con las entradas corregidas, la clasificación exploratoria fue: **217 normales, 35 seguras pero incompletas, 15 falsos fallos del detector, 12 sin fundamento suficiente para decidir y 1 error leve de atribución de la fuente**. Claude Fable 5.1 discrepó en algunas clasificaciones y pasó por alto ese error. Ninguna revisión de IA es una revisión clínica independiente.

## Búsqueda, velocidad y costo

| Ensayo | Observación | Límite |
|---|---|---|
| Siete reglas con búsqueda real de las ocho referencias principales | GPT-6 Luna explicó la regla aportada en **7/7**; búsqueda y generación **US$0.002352** | Preguntas seleccionadas; no incluye todo el chat, resumen o cobro |
| Cinco idiomas × una pregunta de codificación y otra de interpretación, GPT-5.6 Terra/GPT-6 Luna estándar | Ambos pasaron **10/10** pruebas automáticas. Búsqueda y generación: GPT-5.6 Terra **US$0.226730**, GPT-6 Luna **US$0.011580**. Mediana de primera respuesta **2.392 s** frente a **7.314 s** | GPT-6 Luna no alcanzó el objetivo inicial de velocidad en esta pequeña muestra |
| Generación GPT-6 Luna estándar/Fast, 20 respuestas cada uno | Primera respuesta **5.582 s → 2.994 s**; costo **US$0.010000 → US$0.035559** | Fast fue más rápido y caro; no se eligió para el lanzamiento |
| 30 casos originales repetidos tres veces, con búsqueda real: GPT-5.6 Terra estándar/GPT-6 Luna Fast | **90** respuestas por modelo. Búsqueda y generación **US$1.372149 → US$0.064049**, reducción del **95.33%**. Mediana **2.024 s → 2.652 s** y percentil 95 **5.744 s → 6.846 s** para la primera respuesta | La rama GPT-6 Luna usó Fast; estos valores no son mediciones del nivel estándar lanzado |

Claude Fable 5.1 revisó por separado la primera repetición de esos 30 casos. Quedaron por debajo de 80 puntos **0/30** respuestas GPT-5.6 Terra y **4/30** GPT-6 Luna Fast. Los fallos GPT-6 Luna correspondieron a explicaciones de bajo número de respuestas en coreano e inglés, interpretación general en inglés e interpretación general en portugués. La IA no marcó errores críticos en ninguno, pero solo se revisó la primera repetición de casos de desarrollo ya observados.

## Ajustes por idioma y resúmenes

- En `v4`, GPT-6 Luna Fast produjo **60** respuestas y Fable hizo **20** revisiones; una respuesta española recibió **76** puntos. Búsqueda y generación **US$0.062212**; precio de lista estimado de Fable **US$10.129531**.
- En `v5`, **30** respuestas GPT-6 Luna Fast y **10** revisiones Fable elevaron el mínimo español de **76 a 82**. Generación **US$0.034716**; Fable **US$4.982458**. No se aplicó el cambio a todos los idiomas.
- En los límites `v7`, hubo **60** respuestas GPT-6 Luna Fast y **20** revisiones Fable. Las **30** respuestas candidatas alcanzaron al menos **80** puntos, con mínimo **82**, pero una mostró el nombre de un campo interno. Búsqueda y generación **US$0.081067**; Fable **US$9.822691**.
- Tres temas originales en cinco idiomas produjeron **30** resúmenes GPT-5.6 Terra/GPT-6 Luna y **15** revisiones Fable. GPT-6 Luna omitió el historial de retractación en inglés y portugués. Generación **US$0.033595**; Fable **US$3.20503725**. También se probaron **15** respuestas posteriores por modelo y **15** revisiones Fable; una respuesta coreana de GPT-6 Luna mezcló otro sistema de escritura.
- En `v9`, GPT-6 Luna estándar produjo **90** resúmenes y Fable hizo **15** revisiones. La media de puntuación de IA pasó de **86.80 a 88.64**; ambas condiciones mantuvieron **3/45** por debajo de 80 y aún omitían algunas preguntas abiertas. GPT-6 Luna **US$0.011541**; Fable **US$4.194821**.

Una primera ejecución multilingüe se detuvo tras **43/60** llamadas por una colisión en el identificador de instrucciones; conservamos sus **US$0.051947** de costo conocido. Otras seis preparaciones de búsqueda carecen de costo registrado (**desconocido**); el límite conservador calculado fue **US$0.006390**. Cinco traducciones de un caso original cuentan como un solo caso original, no cinco casos independientes.

El flujo con proveedor simulado completó 13 solicitudes de chat, 13 inserciones de búsqueda, 2 resúmenes y 13 generaciones. En `exner.app`, cuentas sintéticas completaron **una respuesta de codificación y una de interpretación**; dos búsquedas y dos generaciones costaron **US$0.000892** según uso y precios configurados. Se creó un pago Live, pero **no se comprobó una compra real ni la activación, cancelación o devolución**. Dos respuestas de producción no establecen un promedio de calidad o costo por respuesta útil.

El [inventario sin datos identificables](./luna-cost-inventory.json) incluye **26** conjuntos de ejecuciones GPT-6 Luna: **US$2.369002** calculados a partir de uso de OpenAI y **US$117.300407** como precio de lista mostrado por Claude CLI. No son cargos confirmados ni deben sumarse como gasto total de investigación. Quedan fuera pruebas anteriores GPT/Jev, llamadas de costo desconocido, servidores y pagos. No completamos la evaluación final prevista de 30 casos originales nuevos × cinco idiomas repetida dos veces ni una revisión clínica independiente. El [registro técnico en coreano](./README.md) detalla los límites de los ensayos.
