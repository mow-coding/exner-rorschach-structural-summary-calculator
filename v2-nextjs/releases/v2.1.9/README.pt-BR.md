# [2026-07-12] v2.1.9 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Antes de continuar

A v2.1.9 melhora o método de busca para que o assistente de codificação e o assistente de interpretação encontrem de forma mais confiável os documentos de referência adequados a uma pergunta antes de responder.

As telas do aplicativo não mudam. Os documentos de referência relacionados a uma pergunta são encontrados com mais precisão nos cinco idiomas, e o assistente de codificação toma como referência apenas as linhas selecionadas pelo usuário.

## Resumo

- Reduz-se a confusão de palavras de uma só letra com códigos Rorschach, preservando os códigos explícitos pelo contexto, como `Card I`, `Content A` e o determinante em minúscula `m`.
- Perguntas com partículas e terminações do coreano ou com japonês, e índices compostos como `3r+(2)/R`, são reconhecidos com mais precisão.
- Os documentos relacionados à pergunta são encontrados com mais precisão.
- Resultados com significado fraco demais são excluídos, e o mesmo documento de referência não aparece mais várias vezes.
- O assistente de codificação toma como referência apenas a linha selecionada e as linhas que o usuário selecionou junto com ela.

Esta versão melhora a busca de documentos de referência, mas a IA não determina automaticamente o código final nem emite diagnósticos. O julgamento final cabe ao clínico.

## Limites que permanecem

- A melhoria da busca não comprova exatidão clínica.
- As respostas do GPT-5.5 são probabilísticas, portanto nem todas as respostas futuras são garantidas.
- A utilidade clínica real, a qualidade das frases multilíngues e a segurança devem ser avaliadas por profissionais qualificados.
