# [2026-02-15] v2.0.0 Versão principal

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.0.0 é a primeira versão 2: leva a v1.4.1 para um novo aplicativo web. Mantém o núcleo da v1, o fluxo de cálculo do Sumário Estrutural do sistema Exner (CS) do Rorschach, e adiciona telas multilíngues, busca de documentos de referência e assistência de IA baseada em BYOK.

A maior mudança desta versão é o modo BYOK (Bring Your Own Key): o usuário conecta sua própria chave de API da OpenAI ou do Google para usar os recursos de IA. Os custos de uso da IA são gerados na conta conectada, e a chave de API é usada apenas enquanto a conexão de IA está ativa.

## O que foi mantido da v1.4.1

O propósito central da v1.4.1 foi mantido. O usuário insere as respostas Rorschach linha por linha, organiza os valores necessários para o Sumário Estrutural, como prancha, localização, qualidade evolutiva, determinantes, qualidade formal, conteúdos e escores especiais, e então calcula os resultados.

O fluxo de cálculo do Sumário Estrutural, a revisão de resultados, a exportação CSV e o suporte multilíngue da v1 passam para a v2. As telas de entrada e de resultados foram reconstruídas como telas de aplicativo web fáceis de usar no celular e no desktop.

## Modo de uso

As telas principais são a tela de pontuação, o assistente de interpretação, os documentos de referência, o gerenciamento da conta e o arquivo de versões. As funções básicas de cálculo e a busca de documentos de referência podem ser usadas sem login; para usar os recursos de IA é preciso fazer login e conectar uma chave de API.

## Conexão de IA com BYOK

Os recursos de IA da v2 funcionam apenas com BYOK. O aplicativo não vende créditos nem assinaturas de IA; o usuário pode conectar uma chave de API da OpenAI ou do Google.

A chave de API é usada apenas enquanto a conexão de IA está ativa e é excluída ao sair da conta ou quando a conexão expira. Se uma chave da OpenAI ou do Google for colocada no campo errado, o aviso é imediato.

O usuário não escolhe o modelo. O aplicativo web usa automaticamente o modelo mais recente definido pelo serviço entre os modelos cuja estabilidade foi confirmada algum tempo após o lançamento. Na v2.0.0, os modelos padrão são GPT-5.4 para a OpenAI e Gemini 2.5 Pro para o Google.

Quando o provedor de IA recusa uma solicitação, os erros não são agrupados em um só. O aplicativo distingue uma chave de API incorreta, um problema de cobrança ou de limite de uso, e um modelo que não pode ser usado com aquela chave de API, e informa ao usuário qual é o caso.

## Assistente de codificação

A IA da tela de pontuação é organizada como assistente de codificação. Aqui "codificação" não significa programação, mas o processo de codificar as respostas Rorschach nos símbolos e categorias do sistema Exner (CS).

O assistente de codificação abre com o atalho Ctrl/Cmd+J. Toda a planilha inserida na tela de pontuação atual é passada como contexto padrão e, se uma linha estiver selecionada, essa linha é destacada como contexto mais importante. Sem nenhuma linha selecionada, usa-se apenas o contexto da planilha inteira, sem linha central.

O assistente de codificação não determina a resposta automaticamente. Ao revisar a localização, os determinantes, a qualidade formal e as categorias de conteúdo de uma resposta, ele explica os candidatos possíveis e seus fundamentos com base nos documentos de referência e nos dados inseridos.

A v2.0.0 não oferece botão de preenchimento automático. A IA apenas explica candidatos e fundamentos; a codificação final é decidida pelo clínico após revisar o contexto da resposta.

## Assistente de interpretação

O assistente de interpretação é uma tela de IA para conduzir uma conversa de interpretação com base em um CSV com os valores do Sumário Estrutural. O usuário anexa o arquivo CSV com os valores do Sumário Estrutural, acrescenta idade, sexo, contexto de observação e as hipóteses ou perguntas que o clínico já tem em mente, e pede à IA que as revise.

O assistente de interpretação tem papel de apoio: explica os padrões dos resultados do Sumário Estrutural e confere as hipóteses formuladas pelo usuário. Não substitui um diagnóstico oficial nem a interpretação final; o julgamento final cabe ao clínico.

## Documentos de referência

A v2 também oferece uma coleção de documentos explicativos curtos consultados pelo aplicativo web e pelos assistentes de IA. Esses documentos explicam os principais conceitos do cálculo do Sumário Estrutural, da codificação e do processo de interpretação, e podem ser pesquisados diretamente na tela de documentos de referência.

Os documentos de referência foram elaborados a partir de material produzido e organizado em conjunto pelo Seoul Institute of Clinical Psychology e pela MOW. O objetivo de publicá-los é permitir que o usuário verifique em que conhecimento a IA se baseia para responder. Isso se liga ao princípio de projeto de não deixar os recursos de IA como uma caixa-preta, para que o usuário possa conferir os fundamentos e julgar por si mesmo.

Documentos de referência cujo nome contém códigos como `+`, `-` e `v/+` abrem corretamente.

## A IA não substitui o julgamento do clínico

A v2 não pretende ser um sistema em que a IA julga no lugar do profissional, mas um sistema que ajuda psicólogos clínicos e pessoas em formação a revisar e julgar sobre fundamentos mais claros. Por isso restam apenas dois recursos de IA: o assistente de codificação na tela de pontuação e o assistente de interpretação em uma tela de chat separada.

As respostas da IA são de referência e apoio; a codificação e a interpretação finais são julgadas pelo clínico.

## Segurança e privacidade

Chaves de API e o texto das conversas com a IA não são guardados como dados de conta de longo prazo. A chave de API é usada apenas enquanto a IA está conectada e é excluída ao sair da conta ou quando a conexão expira.

Os custos de uso da IA são gerados na conta do provedor de API conectada pelo usuário; o aplicativo não tem funções próprias de pagamento nem de assinatura.

## Telas e facilidade de uso

O menu superior, a seleção de idioma, o modo claro/escuro, o gerenciamento da conta, o arquivo de versões e a tela de busca de documentos de referência foram reorganizados.

Na tela de pontuação, a seleção de linhas, a adição/exclusão de linhas, os atalhos e o fluxo de desfazer/refazer foram ajustados. As linhas selecionadas permanecem destacadas, e o contexto recebido pelo assistente de codificação muda conforme a seleção.

Na tela do assistente de interpretação foram adicionados um botão para anexar CSV e a possibilidade de arrastar e soltar. Além de colar texto, é possível anexar um CSV com os valores do Sumário Estrutural e usar seu conteúdo como contexto da conversa com a IA. Apenas um anexo é aceito por vez, o que reduz a chance de a IA ler um contexto errado a partir de materiais misturados.

## Suporte multilíngue

A v2 oferece telas em coreano, inglês, japonês, espanhol e português. O idioma é escolhido em um menu suspenso, e a disposição se mantém estável mesmo com tamanhos de tela e comprimentos de texto diferentes em cada idioma.

## Escopo do produto

O escopo central da v2.0.0 é o cálculo do Sumário Estrutural, os documentos de referência e os assistentes de codificação e interpretação baseados em BYOK. Não inclui créditos de IA, pagamentos nem assinaturas oferecidos pelo serviço.
