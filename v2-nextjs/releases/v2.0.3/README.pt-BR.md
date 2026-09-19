# [2026-06-11] v2.0.3 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.0.3 corrige a abertura lenta da tela de documentos de referência e erros de conexão de IA. A disposição das telas, o uso e o escopo das respostas de IA não mudam; a tela de documentos de referência abre mais rápido e os dados de conexão de IA inválidos são tratados com segurança.

## Resumo

- A tela de documentos de referência abre mais rápido.
- Os endereços existentes dos 1.015 documentos públicos em cinco idiomas são mantidos.
- Dados de conexão de IA inválidos ou expirados são tratados com segurança como estado desconectado, em vez de uma tela de erro.
- O resultado da verificação do estado da conexão de IA não é armazenado separadamente.
- Os problemas de segurança do aplicativo web conhecidos na época foram resolvidos.

## Tela de documentos de referência

Até a v2.0.2, a primeira tela dos documentos de referência podia demorar a aparecer dependendo da velocidade da conexão.

A calculadora, os resultados do Sumário Estrutural e a tela de conversa com a IA não eram afetados, e o conteúdo e os links dos documentos de referência não mudaram. No entanto, a primeira tela dos documentos de referência podia demorar a aparecer dependendo da velocidade da conexão.

## O que mudou

A tela de documentos de referência abre mais rápido, e os endereços dos documentos públicos existentes são mantidos.

Dados de conexão de IA inválidos ou expirados são tratados como estado desconectado sem exibir uma tela de erro. O resultado da verificação do estado da conexão de IA não é armazenado separadamente.

Os problemas de segurança do aplicativo web conhecidos na época foram resolvidos.
