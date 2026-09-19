# [2026-04-27] v2.0.1 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.0.1 corrige problemas de uso encontrados após a publicação da v2.0.0. O escopo do produto — cálculo do Sumário Estrutural, documentos de referência e assistentes de codificação e interpretação baseados em BYOK — é mantido.

## Resumo

- O fluxo de entrada do assistente de interpretação passou de anexar arquivos para inserir os valores do Sumário Estrutural.
- Nos assistentes de codificação e interpretação, foram reduzidas as respostas longas demais da IA e os movimentos de tela difíceis de controlar.
- O fluxo de preenchimento automático por IA foi removido. Codificação e interpretação são revisadas apenas conversando com a IA.
- Corrigidas as telas de conexão e desconexão da chave de API que se sobrepunham ou não mostravam as orientações necessárias.
- Corrigidos os avisos e balões de mensagem do sistema que apareciam transparentes ou difíceis de ler no modo escuro.
- Corrigido o problema de páginas de documentos de referência que não abriam ao clicar em códigos como `+`, `-` ou `v/+`.
- A apresentação do serviço, os termos de serviço e a política de privacidade foram atualizados para refletir os recursos atuais.

## Inserir os dados do Sumário Estrutural no assistente de interpretação

Na v2.0.0, o assistente de interpretação era descrito como um fluxo em que se anexava um arquivo CSV do Sumário Estrutural. Anexar arquivos podia deixar dúvidas sobre qual arquivo usar, e a IA podia não ler o conteúdo do arquivo de forma estável e uniforme.

Na v2.0.1, o fluxo consiste em colar os valores do Sumário Estrutural copiados da tela de resultados em um campo específico do assistente de interpretação. Depois de copiar os valores do Sumário Estrutural na tela de resultados, cole-os no pequeno campo de valores à esquerda da caixa de entrada do assistente de interpretação e comece a perguntar.

Ao colar os valores, aparece `Inserido` em vez do texto completo. Enquanto a mesma janela do navegador estiver em uso, a entrada é mantida até que o usuário a apague ou a substitua por novos valores.

Além disso, para que o assistente de interpretação não aceite qualquer material, usa-se apenas a entrada no formato dos valores do Sumário Estrutural copiados da tela de resultados. Se o usuário inserir um texto sem relação e tentar iniciar a conversa, um aviso pede que use a função de copiar valores do Sumário Estrutural da tela de resultados.

## Respostas do assistente de interpretação

As respostas do assistente de interpretação foram ajustadas a um tamanho e formato que permitem continuar a conversa. Logo após a v2.0.0, as respostas podiam ficar longas demais, ser cortadas no meio ou listar valores demais em uma linha, dificultando a leitura.

O assistente de interpretação não abre mais muitos temas em uma única resposta e mostra separadamente os `valores de referência` e as `hipóteses interpretativas`.

O assistente de interpretação usa expressões mais intuitivas, como `dados do teste`, `dados das respostas` e `dados do Sumário Estrutural`, em vez de `protocolo`.

## Assistente de codificação

O assistente de codificação ajuda por meio de conversa enquanto o usuário codifica as respostas na tela de pontuação. Na v2.0.1, o fluxo em que o assistente preenchia linhas automaticamente ou aplicava campos com um botão foi removido.

Agora o assistente de codificação apenas explica na conversa os candidatos e seus fundamentos com base na linha selecionada e no contexto de toda a planilha. O usuário pode tomar a explicação da IA como referência, mas deve revisar e inserir por si mesmo os valores de codificação.

A abertura do assistente de codificação com `Ctrl/Cmd+J` na tela de pontuação foi mantida. Sem nenhuma linha selecionada, usa-se apenas a planilha inteira como contexto, sem linha central; com uma linha selecionada, essa linha é tratada como contexto mais importante.

## Remoção do preenchimento automático por IA

O recurso `Preenchimento automático por IA` foi removido. Ele tentava preencher de uma vez os campos de codificação da linha atual a partir das notas da resposta e das informações da prancha.

A codificação Rorschach exige a revisão e o julgamento do clínico. O preenchimento automático foi removido para evitar que as sugestões da IA sejam aceitas sem revisão suficiente; a entrada final é decidida pelo clínico.

Como resultado, os recursos de IA da v2.0.1 ficaram mais simples. A IA do aplicativo web oferece apenas dois auxílios conversacionais: o assistente de codificação e o assistente de interpretação.

## Tela de conexão da chave de API

A chave de API é usada apenas enquanto a conexão de IA está ativa e é excluída ao encerrar a conexão.

Se uma chave de API do Google for colocada no campo da OpenAI, ou uma chave da OpenAI no campo do Google, o campo correto é indicado.

A sobreposição entre o botão de encerrar a conexão de API e a janela de entrada da chave também foi corrigida. Ao abrir o assistente de interpretação sem uma chave de API conectada, os passos necessários são indicados.

## Seleção do modelo de IA

O usuário não escolhe o modelo. O aplicativo web usa automaticamente o modelo mais recente definido pelo serviço entre os modelos lançados há pelo menos um mês cuja estabilidade foi confirmada.

As orientações sobre a seleção do modelo aparecem apenas nas telas necessárias, para que não pareça que o usuário precisa escolher um modelo.

## Avisos no modo escuro

No modo escuro, os balões de aviso do sistema ou os avisos do canto superior direito podiam aparecer transparentes ou se misturar ao fundo e ficar difíceis de ler. Na v2.0.1, a cor de fundo, a borda e a cor do texto dos avisos e das mensagens de orientação do chat aparecem com mais clareza.

Os avisos de sucesso, alerta e sistema foram ajustados para não ficarem escondidos por outros elementos da tela nem se misturarem ao fundo.

## Tela de conversa com a IA

Tanto no assistente de codificação quanto no de interpretação, textos de orientação desnecessários e mensagens duplicadas foram reduzidos. Elementos que interrompiam o fluxo da conversa ou pareciam recursos excessivos, como o nome do modelo de IA, a lista de documentos de referência e os botões de aplicar campos, foram removidos.

O problema de a tela descer continuamente de forma forçada enquanto a IA respondia, dificultando o controle da rolagem, também foi reduzido. Agora a rolagem automática não intervém em excesso quando o usuário está lendo conteúdo anterior.

O movimento dos pontos do balão mostrado enquanto se espera a resposta foi suavizado para incomodar menos. Uma ferramenta conversacional é uma tela que o usuário observa por muito tempo, e até um movimento pequeno pode cansar.

## Documentos de referência que não abriam

Alguns documentos de referência têm códigos como `+`, `-` e `v/+` no nome. Na v2.0.0, alguns links com esses códigos não abriam.

Agora, ao clicar em itens como `[Codificação/Qualidade evolutiva] v`, `[Codificação/Qualidade evolutiva] v/+`, `[Codificação/Qualidade formal] +` e `[Codificação/Qualidade formal] -`, o documento correto é aberto.

## Informações do serviço

A apresentação do serviço, os termos de serviço e a política de privacidade foram atualizados para refletir os recursos realmente oferecidos. Orientações erradas que faziam parecer que o aplicativo oferecia créditos de IA, pagamentos ou uma loja também foram corrigidas.
