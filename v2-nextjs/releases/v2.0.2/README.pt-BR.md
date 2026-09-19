# [2026-05-21] v2.0.2 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

A v2.0.2 corrige problemas do CSV do Sumário Estrutural encontrados após a v2.0.1. A direção geral do produto e a forma de usar os recursos de IA não mudaram; os dados copiados ou baixados da tela de resultados agora refletem com mais precisão o Sumário Estrutural mostrado na tela.

**Os valores do Sumário Estrutural em si não mudaram, portanto não é necessário recalcular.** No entanto, se você fez uma interpretação com IA a partir de um CSV do Sumário Estrutural copiado na v2.0.1, alguns itens podem ter faltado ou o mesmo nome pode ter aparecido repetido; confira essa interpretação com valores copiados novamente na v2.0.2 ou posterior. Pelo mesmo motivo, é mais seguro gerar de novo os CSV baixados que você guarda.

## Resumo

- Na janela de download de dados, o nome do item em coreano `입력값 원자료 CSV` foi corrigido para `점수계열 원자료 CSV`.
- Corrigido um problema em que a string CSV gerada pelo botão `Copiar valores do Sumário Estrutural` podia conter cabeçalhos duplicados e itens ausentes.
- Copiar e baixar agora fornecem os mesmos itens do Sumário Estrutural.
- Corrigido o pop-up de início de sessão que reaparecia repetidamente após um erro da chave do provedor de IA em uma sessão iniciada com chave de API.
- O modelo de conversa padrão da OpenAI foi atualizado de GPT-5.4 para GPT-5.5.
- A confirmação de colagem dos valores do Sumário Estrutural no assistente de interpretação agora aparece como `Inserido ✅`.

## O que conferir no assistente de interpretação

Na v2.0.1, o assistente de interpretação é usado copiando os valores da tela de resultados com o botão `Copiar valores do Sumário Estrutural`, colando-os no campo de valores do Sumário Estrutural da tela de IA de interpretação e iniciando a conversa.

Na v2.0.1, nomes usados em várias seções, como `D`, `Zf`, `Zd`, `GHR` e `PHR`, podiam aparecer duplicados nos dados copiados. Alguns itens visíveis na tela, como `Single`, `Contents`, `Form Quality`, `Special Scores`, `Approach` e `Blends`, também podiam faltar.

Não era um problema da conexão com a chave de API nem da conversa com a IA, mas os dados do Sumário Estrutural entregues ao assistente de interpretação podiam ser incompletos ou ambíguos.

## O que mudou

Copiar e baixar agora fornecem o mesmo conjunto completo de itens, e os itens com o mesmo nome são mostrados de forma que possam ser distinguidos.

O CSV de dados brutos da série de escores inclui apenas as linhas de pontuação realmente usadas no cálculo. Linhas provisórias com a prancha vazia e linhas incompletas são excluídas.

O assistente de interpretação aceita os dados do Sumário Estrutural copiados da tela de resultados e não trata frases comuns sem relação como dados do Sumário Estrutural.
