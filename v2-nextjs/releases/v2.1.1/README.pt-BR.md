# [2026-06-27] v2.1.1 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.1.1 corrige problemas da tela de entrada de pontuação e do processo de conexão de IA. A conexão com Gemini/Google AI foi removida e o processo foi simplificado para OpenAI com a sua própria chave de API.

## Resumo

- Corrigido: arrastar texto com o mouse dentro da janela de notas da resposta era interpretado como clique no fundo e fechava a janela.
- Selecionar outra linha durante uma conversa com o assistente de codificação não apaga mais a conversa existente nem a resposta em andamento.
- Os recursos de IA aceitam apenas uma chave de API da OpenAI; a conexão com o Google Gemini não é mais oferecida.
- Na janela da chave de API, o nome do modelo e as orientações sobre a chave aparecem em uma única linha fácil de ler.

## Conexão de IA e tela de pontuação

Os recursos de IA agora aceitam apenas uma chave de API da OpenAI. Se uma antiga chave do Google/Gemini for inserida, é exibido um aviso de que é necessária uma chave da OpenAI. A chave de API é usada de forma criptografada para a conexão de IA; a conexão dura no máximo 24 horas e, ao encerrá-la, a chave também é excluída.

O assistente de codificação toma como referência a linha selecionada, mas mudar para outra linha não apaga as mensagens existentes. Você pode manter a conversa e continuar perguntando com outra linha como referência.

A correção da janela de notas da resposta não afeta os resultados do cálculo; apenas a condição para fechar a janela durante a entrada foi ajustada com mais precisão.
