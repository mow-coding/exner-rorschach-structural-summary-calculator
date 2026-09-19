# [2026-07-13] v2.1.10 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Antes de continuar

A v2.1.10 corrige problemas da busca de documentos de referência que permaneciam após a v2.1.9.

As telas do aplicativo e as fórmulas não mudam. Os códigos Rorschach ligados a frases em japonês são preservados, e perguntas de interpretação amplas usam apenas documentos de interpretação. A IA não determina o código final nem substitui o julgamento do clínico.

## Resumo

- Um código Rorschach seguido de japonês, como em `FQ+の...`, `v/+の...` ou `3r+(2)/Rの...`, é reconhecido como o código completo.
- Perguntas de interpretação amplas formuladas de forma natural também recebem os documentos de interpretação relacionados, e perguntas amplas recebem apenas documentos de interpretação.
- O mesmo documento de referência não aparece mais repetido nos resultados de busca.

A IA não determina automaticamente os códigos nem emite diagnósticos; o julgamento final cabe ao clínico.

## Limites que permanecem

- Dependendo da formulação da pergunta, um documento de interpretação relacionado pode ser deixado de fora.
- A melhoria da busca e da forma de responder não comprova exatidão clínica.
- A utilidade clínica real, a qualidade das frases multilíngues e a segurança devem ser avaliadas por profissionais qualificados.
