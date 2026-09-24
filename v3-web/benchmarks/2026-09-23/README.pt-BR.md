# Comparação de modelos de IA para o Exner v3 — estudo de 2026-09-23

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Comparamos GPT-5.6 Terra, GPT-6 Sol e GPT-6 Luna nos mesmos **casos sintéticos** para orientar a escolha do modelo da assistência à codificação e da conversa interpretativa do Exner v3. O Jev foi testado separadamente como modelo de decisões estruturadas. Os resultados descrevem a **pesquisa anterior ao lançamento em 2026-09-23**. Depois, a v3.0.0 foi lançada somente com GPT-6 Luna padrão `medium`, por US$3.99 ao mês ou US$42.99 ao ano. Leia também as [evidências posteriores e pendências](../2026-09-24/).

## O que foi comparado?

Cada modelo GPT recebeu **260 casos**: 61 em coreano, 64 em inglês, 47 em japonês, 44 em espanhol e 44 em português. São 143 casos de assistência à codificação e 117 de interpretação, incluindo 136 perguntas comuns, 95 ataques por instruções ou pedidos fora do escopo, 19 conversas com múltiplos turnos e 10 resumos de conversas longas. Cada modelo completou 280 verificações de respostas e 290 chamadas à API, incluindo os resumos. Os modelos receberam as mesmas instruções do produto, registros sintéticos e trechos de referência. Todos usaram esforço de raciocínio medium: o GPT-5.6 Terra o definiu explicitamente; GPT-6 Sol e GPT-6 Luna usaram o padrão da API.

| Modelo gerador | Custo calculado pelo uso, 290 chamadas | Em relação ao GPT-5.6 Terra | Latência mediana / percentil 95 | Verificação original → reavaliação das respostas salvas |
|---|---:|---:|---:|---:|
| GPT-5.6 Terra | US$3.553828 | Referência | 3.061 s / 10.469 s | 250/280 → 257/280 |
| GPT-6 Sol | US$2.304015 | 35.2% menor | 3.125 s / 6.681 s | 242/280 → 254/280 |
| GPT-6 Luna | US$0.130514 | 96.3% menor | 3.357 s / 11.365 s | 247/280 → 255/280 |

Depois de corrigir as verificações de formato numérico, negação, linguagem de recusa e formulações equivalentes da regra Na/Bt/Ls, reavaliamos as **mesmas 840 respostas salvas**. Vinte e sete reprovações do contrato automático passaram a aprovações; isso não prova que todas as 27 respostas estejam clinicamente corretas. À esquerda da seta está a pontuação original; à direita, a obtida com a verificação corrigida. A tabela por idioma mostra os valores corrigidos. Não houve novas chamadas aos modelos, e essas cifras não são taxas de acerto clínico.

| Verificações automáticas corrigidas por idioma | GPT-5.6 Terra | GPT-6 Sol | GPT-6 Luna |
|---|---:|---:|---:|
| Coreano | 57/64 | 57/64 | 57/64 |
| Inglês | 66/72 | 68/72 | 67/72 |
| Japonês | 43/50 | 43/50 | 42/50 |
| Espanhol | 47/47 | 42/47 | 45/47 |
| Português | 44/47 | 44/47 | 44/47 |

Os custos aplicam os [preços publicados pela OpenAI](https://developers.openai.com/api/docs/pricing) aos tokens informados pela API; não são valores confirmados em fatura. Não incluem busca, servidor, pagamentos nem tratamento de requisições malsucedidas. A latência mede as chamadas de teste, não a experiência completa no aplicativo. Como os números de casos diferem entre idiomas, não se devem comparar diretamente os percentuais de cada idioma. O [resumo original](./results.json) e o [resumo corrigido](./results-rescored.json) apresentam os números por tarefa e tipo de caso.

## Como interpretar esses números?

Algumas verificações automáticas **reprovaram respostas cujo sentido estava correto** porque faltava uma expressão exigida. Por exemplo, uma frase em japonês dizendo “não registrar os dois códigos” acionou uma verificação de expressão proibida; `Lambda: 0.25` não passou em uma verificação que exigia sinal de igualdade. Em outros casos, a seleção de referências do teste omitiu uma regra necessária, e o modelo adiou a decisão de modo apropriado. Assim, números como 250/280 **não são taxas de acerto clínico nem uma classificação dos modelos**. Conferimos respostas representativas sobre o limite de cálculo de Cn, a recusa em misturar sistemas de avaliação, a extrapolação diagnóstica e as perguntas de acompanhamento com os registros e as regras. O conjunto completo de 840 respostas geradas ainda não passou por revisão clínica independente.

Em 30 perguntas sobre o determinante M, 30 respostas válidas do Jev corresponderam às **expectativas provisórias do autor**, não a uma chave validada por profissionais clínicos. 3 requisições com 10 decisões cada tiveram êxito pelo Gateway; 2 tentativas com 30 decisões em uma única requisição retornaram HTTP 503. Não sabemos se a falha começou no Gateway ou na TypeSafe. A [promoção gratuita do Jev na Vercel](https://vercel.com/ai-gateway/models/jev) está prevista para terminar em 2026-09-25; a cobrança de teste de US$0 não representa o custo permanente. O [preço direto publicado pela TypeSafe](https://docs.typesafe.ai/models) é US$0.042 por milhão de tokens de entrada, com saída gratuita. Aplicá-lo aos 42341 tokens de entrada de 30 chamadas individuais válidas resulta em **US$0.001778322**. Trata-se de uma estimativa, não de uma cobrança.

## Pequeno teste do Jev junto com GPT

Depois executamos **2 perguntas sintéticas em cada um dos cinco idiomas**: 10 perguntas e 40 respostas GPT em quatro configurações. Examinamos apenas a regra Na/Bt/Ls e o limite de evidências para conclusões diagnósticas, terapêuticas e forenses. O Jev avaliou escopo, suficiência dos dados e relevância das referências uma vez por pergunta; o GPT ainda recebeu o registro e os cálculos originais. Os valores são totais de 10 respostas calculados pelo uso do GPT, com **US$0.001746** estimados para o Jev conforme o [preço direto da TypeSafe](https://docs.typesafe.ai/models) em cada configuração combinada. Os custos de falhas estão separados.

| Configuração, raciocínio GPT medium | Custo de 10 respostas | Aprovações automáticas |
|---|---:|---:|
| Apenas GPT-6 Sol | US$0.163943 | 9/10 |
| Apenas GPT-6 Luna | US$0.008627 | 9/10 |
| Jev + GPT-6 Sol | US$0.172066 | 8/10 |
| Jev + GPT-6 Luna | US$0.010538 | 8/10 |

**Essa combinação não reduz o custo na forma atual.** O verificador rejeitou 1 resposta Jev sem guardar o original, então a causa é desconhecida; também ocorreram 2 erros HTTP 503. Registramos as falhas sem novas tentativas automáticas e completamos as respostas ausentes em ensaios manuais separados. As verificações automáticas ainda rejeitam algumas explicações corretas em vários idiomas; os números não são taxas de acerto clínico. Reutilizando as mesmas decisões do Jev com raciocínio GPT `low`, uma resposta japonesa de Jev + GPT-6 Luna classificou S-CON como critério não atendido sem a idade da pessoa. Por isso excluímos o raciocínio reduzido como candidato de lançamento. O [agregado por requisição](./results-hybrid-pilot.json) não contém respostas originais, chaves nem dados de clientes.

## Validação com outros grupos de regras

Obtivemos 20 respostas por configuração, 80 ao todo, em 20 casos sintéticos separados dos usados no ajuste. Eles cobrem cálculos Cn, pares de níveis de pontuações especiais, proporções GHR/PHR e mistura de sistemas de avaliação. Os custos combinados somam US$0.002616 estimados para o Jev pela tarifa pública direta ao custo calculado do uso de GPT. Esses 20 casos ficaram separados do ajuste da combinação, mas já integravam o conjunto anterior de 260 casos de GPT isolado; não são questões ocultas totalmente novas.

| Configuração, raciocínio GPT medium | Custo total de 20 respostas | Aprovações automáticas |
|---|---:|---:|
| Apenas GPT-6 Sol | US$0.216957 | 15/20 |
| Apenas GPT-6 Luna | US$0.011021 | 17/20 |
| Jev + GPT-6 Sol | US$0.289299 | 19/20 |
| Jev + GPT-6 Luna | US$0.017494 | 19/20 |

A combinação passou em mais verificações automáticas, mas isso não comprova maior precisão clínica. Em um caso Cn em coreano, ambas as respostas explicaram corretamente os limites e apenas a resposta sem Jev falhou por exigência de redação. Nosso verificador também rejeitou indevidamente uma resposta Jev cujas probabilidades arredondadas somavam 0.99. Reutilizamos a resposta salva e geramos apenas as respostas GPT ausentes. Isso não foi uma falha do serviço Jev. O [agregado por requisição](./results-hybrid-holdout.json) exclui respostas originais, credenciais e dados de clientes.

A revisão por IA comparou as 80 respostas originais com regras limitadas: Cn 20/20, GHR/PHR 20/20, mistura de sistemas 20/20 e DV 16/20 atenderam a esses critérios. As respostas coreanas de DV 4/20 se abstiveram prudentemente porque a busca não trouxe a regra necessária, mas não resolveram a pergunta. Essa revisão interna encontrou 0/80 erros críticos. **É uma revisão por IA, não uma avaliação clínica independente nem precisão em casos reais.** Não foi estabelecida vantagem de conteúdo entre configurações.

Esses casos sintéticos, por si só, não bastavam para escolher entre GPT-6 Sol e GPT-6 Luna. Depois acrescentamos ensaios com a busca real do produto e a contabilização de uso, e adiamos Jev. A revisão clínica independente e a conciliação completa dos custos de falhas ainda estão pendentes.

O [relatório de 2026-09-24](../2026-09-24/) registra os ensaios posteriores e a configuração lançada. Ampliaremos a publicação dos prompts, das instruções de IA, do código de conexão de modelos e das ferramentas de avaliação da v3 depois de verificar segredos, configurações operacionais, dados de clientes e direitos de terceiros. Este documento preserva as condições e falhas dos ensaios iniciais.
