# [2026-06-22] v2.1.0 Versão menor

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.1.0 permite abrir o aplicativo web como um aplicativo instalado nos navegadores compatíveis, credita o projeto público RorScore e melhora a forma como a IA procura primeiro os documentos de referência adequados a uma pergunta de codificação.

## Resumo

- Em navegadores compatíveis, como Chrome e Edge, o aplicativo web pode ser aberto como um aplicativo instalado.
- O recurso de instalação não inclui armazenamento off-line, notificações push nem sincronização em segundo plano, e não guarda separadamente no dispositivo dados de avaliação sensíveis nem respostas de IA.
- Diante de uma pergunta de codificação como `DQ+`, a IA consulta primeiro os documentos de entrada de pontuação relacionados.
- O projeto público RorScore é creditado como material de referência.

## Instalação e guarda de dados

O recurso de instalação não muda a forma como o aplicativo guarda os dados nem o princípio de proteção da chave de API. A chave de API é usada de forma criptografada para a conexão de IA; a conexão dura no máximo 24 horas e, ao encerrá-la, a chave também é excluída.

O aplicativo instalado também é usado com conexão à internet e não guarda off-line dados de avaliação sensíveis nem respostas de IA.

Esta mudança não afeta os resultados do cálculo. Quando o assistente de codificação recebe uma pergunta como "Quando DQ+ deve ser codificado em vez de DQo ou DQv/+?", ele consulta os documentos de entrada de pontuação relacionados antes dos documentos de interpretação.

## Crédito ao RorScore

O projeto público RorScore é creditado como material de referência.
