# Calculadora do Sumário Estrutural do Sistema Compreensivo de Rorschach de Exner

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Exner é um aplicativo web que ajuda a revisar a codificação e o Sumário Estrutural do Sistema Compreensivo de Rorschach. A versão atual, **v3.0.0**, reúne a calculadora e assistentes de IA que aceitam perguntas de acompanhamento. Os códigos e as explicações sugeridos são informações de apoio; a decisão final cabe ao profissional, com base na resposta original e no registro do inquérito.

## Acessar o aplicativo

- [Aplicativo web v3 pago](https://exner.app): disponível em coreano, inglês, japonês, espanhol e português brasileiro. A assinatura custa **US$3.99 por mês** ou **US$42.99 por ano**.
- [Aplicativo web v2 gratuito](https://exner.yesucan.co.kr): a calculadora anterior continua disponível, com assistência opcional de IA usando a própria chave de API do usuário.

## O que mudou na v3.0.0

Uma conta Google e uma assinatura dão acesso aos assistentes de codificação e interpretação. Ambos usam **GPT-6 Luna**. Em conversas longas, o aplicativo resume o contexto anterior para as perguntas seguintes. As fórmulas do Sumário Estrutural não mudaram em relação à v2; portanto, esta versão, por si só, não exige recalcular registros anteriores.

As [notas da v3.0.0](./v3-web/releases/v3.0.0/README.pt-BR.md) explicam os recursos e os limites clínicos. A [comparação de modelos](./v3-web/benchmarks/2026-09-23/) e a [avaliação posterior](./v3-web/benchmarks/2026-09-24/) descrevem os métodos, resultados e custos. Verificações automáticas com casos sintéticos não são taxas de precisão clínica.

## Código-fonte e versões anteriores

Este repositório contém o [código publicado da v2](./v2-nextjs/source/), o [código publicado da v1](./v1-gas/current/) e o [histórico completo de versões](./CHANGELOG.pt-BR.md). O código completo de produção da v3 ainda não foi publicado. Pretendemos publicar o código e as instruções de IA revisados após verificar segredos, registros clínicos e direitos de terceiros, preservando os avisos de direitos autorais existentes.

A MOW planeja e opera o serviço. O Seoul Institute of Clinical Psychology (SICP) contribuiu para conferir os primeiros resultados de cálculo e revisar o uso clínico. Consulte também os [agradecimentos e referências do aprendizado inicial](./ACKNOWLEDGEMENTS.pt-BR.md).

O [aviso da v3](./v3-web/NOTICE.md) explica a atribuição e o escopo de publicação dos novos registros da v3. Os avisos de direitos autorais da v1 e v2 são preservados.
