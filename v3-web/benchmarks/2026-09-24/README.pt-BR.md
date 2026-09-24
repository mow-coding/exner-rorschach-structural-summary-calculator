# Exner v3.0.0: escolha do GPT-6 Luna e evidências do serviço em produção — 2026-09-24

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Este relatório continua a [comparação de 2026-09-23](../2026-09-23/) entre GPT-5.6 Terra, GPT-6 Sol, GPT-6 Luna e Jev. A v3.0.0 usa **somente GPT-6 Luna, raciocínio `medium` e classe padrão (`default`)**. Jev e a troca automática para outro modelo generativo não integram o produto. Casos sintéticos não demonstram precisão clínica nem equivalência entre modelos.

A comparação inicial usou 260 casos sintéticos e 290 chamadas por modelo GPT, incluindo 280 verificações de respostas e resumos. Reavaliando as respostas salvas com um verificador de expressões corrigido, GPT-5.6 Terra obteve **257/280**, GPT-6 Sol **254/280** e GPT-6 Luna **255/280**. São resultados de uma verificação automática, não taxas de acerto clínico. O uso multiplicado pelos preços públicos deu custos de geração de **US$3.553828**, **US$2.304015** e **US$0.130514**, respectivamente. Foram usados três trechos fixos de referência, diferentes da busca do produto. O [relatório anterior](../2026-09-23/) mantém os testes com Jev, os erros HTTP 503 e os custos estimados.

Ao reler as 280 respostas e 10 resumos salvos do GPT-6 Luna, descobrimos que uma primeira revisão não incluía parte do resumo anterior e que um caminho de entrada do Claude corrompia texto UTF-8. Excluímos esses julgamentos como prova final. Com as entradas corrigidas, a classificação exploratória foi **217 normais, 35 seguras mas incompletas, 15 falsos erros do verificador, 12 sem base suficiente para decidir e 1 erro leve de atribuição de fonte**. Claude Fable 5.1 discordou de algumas classificações e não percebeu esse erro. Nenhuma revisão por IA equivale à revisão clínica independente.

## Busca, velocidade e custo

| Ensaio | Observação | Limite |
|---|---|---|
| Sete regras com busca real das oito principais referências | GPT-6 Luna explicou a regra fornecida em **7/7**; busca e geração **US$0.002352** | Perguntas selecionadas; não abrange todo o chat, resumo ou cobrança |
| Cinco idiomas × uma pergunta de codificação e uma de interpretação, GPT-5.6 Terra/GPT-6 Luna padrão | Ambos passaram **10/10** verificações automáticas. Busca e geração: GPT-5.6 Terra **US$0.226730**, GPT-6 Luna **US$0.011580**. Mediana do primeiro texto **2.392 s** contra **7.314 s** | GPT-6 Luna não atingiu a meta inicial de velocidade nessa amostra pequena |
| Geração GPT-6 Luna padrão/Fast, 20 respostas cada | Primeiro texto **5.582 s → 2.994 s**; custo **US$0.010000 → US$0.035559** | Fast foi mais rápido e caro; não foi escolhido para o lançamento |
| 30 casos originais repetidos três vezes, com busca real: GPT-5.6 Terra padrão/GPT-6 Luna Fast | **90** respostas por modelo. Busca e geração **US$1.372149 → US$0.064049**, redução de **95.33%**. Mediana **2.024 s → 2.652 s** e percentil 95 **5.744 s → 6.846 s** para o primeiro texto | O braço GPT-6 Luna usou Fast; esses valores não são medições da classe padrão lançada |

Claude Fable 5.1 revisou separadamente a primeira repetição dos 30 casos. Ficaram abaixo de 80 pontos **0/30** respostas GPT-5.6 Terra e **4/30** GPT-6 Luna Fast. As falhas GPT-6 Luna envolveram baixo número de respostas em coreano e inglês, interpretação geral em inglês e interpretação geral em português. A IA não marcou erros críticos em nenhum dos grupos, mas só a primeira repetição de casos de desenvolvimento já conhecidos foi revisada.

## Ajustes por idioma e resumos

- Em `v4`, GPT-6 Luna Fast gerou **60** respostas e Fable fez **20** revisões; uma resposta espanhola recebeu **76** pontos. Busca e geração **US$0.062212**; estimativa de preço de lista Fable **US$10.129531**.
- Em `v5`, **30** respostas GPT-6 Luna Fast e **10** revisões Fable elevaram o mínimo espanhol de **76 para 82**. Geração **US$0.034716**; Fable **US$4.982458**. A mudança não foi aplicada indiscriminadamente aos outros idiomas.
- Nos limites `v7`, houve **60** respostas GPT-6 Luna Fast e **20** revisões Fable. Todas as **30** candidatas obtiveram ao menos **80** pontos, mínimo **82**, mas uma exibiu o nome de um campo interno. Busca e geração **US$0.081067**; Fable **US$9.822691**.
- Três temas originais em cinco idiomas produziram **30** resumos GPT-5.6 Terra/GPT-6 Luna e **15** revisões Fable. GPT-6 Luna omitiu um histórico de retratação em inglês e português. Geração **US$0.033595**; Fable **US$3.20503725**. Também foram testadas **15** respostas seguintes por modelo e **15** revisões Fable; uma resposta coreana do GPT-6 Luna misturou outro sistema de escrita.
- Em `v9`, GPT-6 Luna padrão produziu **90** resumos e Fable fez **15** revisões. A média de avaliação da IA passou de **86.80 para 88.64**; ambas as condições tiveram **3/45** abaixo de 80 e ainda omitiram algumas perguntas em aberto. GPT-6 Luna **US$0.011541**; Fable **US$4.194821**.

Uma primeira execução multilíngue parou após **43/60** chamadas por colisão no identificador das instruções; preservamos seu custo conhecido de **US$0.051947**. Outras seis preparações de busca têm custo registrado **desconhecido**, com limite conservador estimado de **US$0.006390**. Cinco traduções do mesmo caso original contam como um caso original, não cinco casos independentes.

O fluxo com provedor simulado completou 13 solicitações de chat, 13 buscas, 2 resumos e 13 gerações. Em `exner.app`, contas sintéticas concluíram **uma resposta de codificação e uma de interpretação**; duas buscas e duas gerações custaram **US$0.000892** pelos preços e uso registrados. Uma tela de pagamento Live foi criada, mas **compra real, acesso, cancelamento e reembolso não foram comprovados**. Duas respostas de produção não estabelecem média de qualidade ou custo por resposta útil.

O [inventário sem dados identificáveis](./luna-cost-inventory.json) inclui **26** conjuntos de execução GPT-6 Luna: **US$2.369002** calculados do uso OpenAI e **US$117.300407** como preço de lista exibido pelo Claude CLI. Não são cobranças confirmadas e não devem ser somados como gasto total de pesquisa. Testes anteriores GPT/Jev, chamadas de custo desconhecido, servidores e pagamentos ficaram fora. Não concluímos a avaliação final prevista de 30 casos originais novos × cinco idiomas repetida duas vezes nem a revisão clínica independente. O [registro técnico em coreano](./README.md) detalha os limites dos ensaios.
