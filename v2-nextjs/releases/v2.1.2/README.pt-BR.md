# [2026-06-28] v2.1.2 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.1.2 ajusta a forma de responder do assistente de codificação e do assistente de interpretação: eles respondem o necessário, não são cortados no meio e não ultrapassam o âmbito de julgamento do clínico. Além de um pequeno ajuste de alinhamento na janela da chave de API, as telas não mudam.

## Resumo

- Os assistentes de codificação e interpretação se comportam de forma mais consistente no tamanho e na apresentação das respostas.
- O assistente de codificação indica com mais clareza os códigos candidatos e o limite do que o clínico deve revisar. Respostas que poderiam ser confundidas com preenchimento ou aplicação automática na linha são bloqueadas e, quando faltam evidências, ele pede mais informações de observação.
- Os limites do assistente de interpretação foram reforçados para que não determine diagnóstico, tratamento ou questões legais a partir de um único índice. Em perguntas amplas com poucos valores do Sumário Estrutural, ele não inventa índices inexistentes e sugere uma ordem de verificação.
- Na janela da chave de API, o nome do modelo da OpenAI e o campo da chave aparecem em uma única linha fácil de ler.
