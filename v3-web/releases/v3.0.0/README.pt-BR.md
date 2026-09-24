# [2026-09-24] v3.0.0 versão principal — Aplicativo web pago com assistentes de IA

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

O Exner v3.0.0 permite conversar livremente com assistentes de IA ao revisar a codificação e a interpretação do Sumário Estrutural do Sistema Compreensivo de Rorschach. O novo aplicativo está disponível em [exner.app](https://exner.app). As respostas da IA são informações de apoio; a codificação e interpretação finais, baseadas na resposta original e no registro do inquérito, são responsabilidade do profissional clínico.

## O que mudou?

- É possível criar uma conta com o Google e consentir separadamente com o envio de informações à IA antes de usar os assistentes de codificação e interpretação. Ambos usam GPT-6 Luna com raciocínio `medium` e a classe de serviço padrão. Avaliamos o Jev, mas ele não integra a geração de respostas da v3.0.0.
- O aplicativo busca referências relevantes para a pergunta e resume o conteúdo anterior para perguntas seguintes em conversas longas. Nem o resumo nem a resposta da IA alteram o protocolo original ou um resultado verificado pela calculadora. O assistente pode pedir informações ausentes.
- A interface e o material de referência estão disponíveis em coreano, inglês, japonês, espanhol e português brasileiro. Continuaremos a melhorar as respostas em cada idioma; não afirmamos que todos os julgamentos clínicos estejam igualmente completos nos cinco.
- A assinatura custa **US$3.99 por mês** ou **US$42.99 por ano**. O valor cobrado em outra moeda e os tributos dependem da tela de pagamento e das condições do cartão. O uso é controlado por um orçamento de custo de processamento de IA, não por um número fixo de perguntas. O aplicativo mostra o uso restante e o estado da assinatura.

## Preciso recalcular um protocolo anterior?

Esta versão não altera as fórmulas do Sumário Estrutural da v2 nem os cálculos já concluídos. Não é necessário recalcular um protocolo da v2 por causa deste lançamento. Códigos e explicações sugeridos pela IA não são uma pontuação definitiva: para uso clínico, confronte-os com a resposta original, o inquérito e o conjunto dos dados clínicos.

## Evidências e limites

Antes do lançamento, comparamos GPT-5.6 Terra, GPT-6 Sol, GPT-6 Luna e Jev em **casos sintéticos**. Examinamos separadamente codificação, interpretação, resumos, busca real de referências, tempo de resposta e uso por idioma. Também fizemos uma revisão separada por IA com Claude Fable 5.1. Não tratamos verificações automáticas de redação como precisão clínica nem apresentamos uma revisão por IA como revisão clínica independente. Os nomes exatos dos modelos, números, cálculos de custo, falhas e respostas incompletas estão na [comparação inicial](../../benchmarks/2026-09-23/) e no [relatório posterior da configuração de lançamento](../../benchmarks/2026-09-24/).

![Custos de geração e resultados de verificações automáticas de redação para três modelos GPT com as mesmas entradas sintéticas](../../benchmarks/2026-09-23/model-comparison.svg)

As verificações automáticas acima **não medem precisão clínica**. A comparação seguinte inclui busca real de referências, mas usou GPT-6 Luna **Fast**; ela não descreve a velocidade nem o custo da classe padrão lançada.

![Custo calculado de busca e geração e tempo até o primeiro texto de GPT-5.6 Terra padrão e GPT-6 Luna Fast](../../benchmarks/2026-09-24/retrieval-trial.svg)

No site de produção, contas sintéticas obtiveram respostas dos dois assistentes e criaram uma tela de pagamento Live. **No lançamento, ainda não havíamos concluído uma transação real que abrangesse novo cadastro, pagamento, concessão de acesso, cancelamento e reembolso.** Compararemos os registros de transações e acesso e corrigiremos qualquer problema encontrado. A revisão clínica independente das respostas e algumas respostas multilíngues incompletas também permanecem pendentes.

Os Termos de uso e a Política de privacidade entram em vigor em **2026-09-24**. O consentimento para enviar informações à IA é separado da assinatura e pode ser retirado. Publicaremos o código e os prompts da v3 em partes revisadas após verificar segredos, registros clínicos e direitos de terceiros. Estas notas e os relatórios de benchmark não significam que todo o código de produção já tenha sido publicado.
