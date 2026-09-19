# [2026-07-18] v2.2.4 Correção de erros

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Antes de continuar

A v2.2.4 é uma versão de documentos de referência, busca com IA e segurança que **não altera as fórmulas do Sumário Estrutural nem a forma de preencher a folha de pontuação**. Não é necessário recalcular o Sumário Estrutural de um protocolo concluído. Também não há novas informações do examinando a inserir quando se usa apenas a calculadora sem chave de API.

Esta versão melhora os documentos de referência e o material de busca da IA. Os termos clínicos dos cinco idiomas não foram ajustados por tradução literal; deu-se prioridade às expressões realmente usadas na literatura profissional e acadêmica de cada idioma. Os títulos e a ordem dos documentos também foram organizados para seguir a pontuação e o Sumário Estrutural em vez da ordem alfabética.

Os assistentes opcionais de codificação e interpretação respondem apenas dentro do escopo do Sistema Compreensivo (CS) de Exner. Não respondem a perguntas sobre outros sistemas de avaliação nem a solicitações de informações não públicas.

## Documentos de referência

### Títulos e ordem fáceis de ler na tela

Os links existentes dos documentos de referência são mantidos, e os títulos visíveis na tela agora seguem os termos clínicos de cada idioma. Os botões mostram títulos com significado, como `Codificação`, `Qualidade formal (FQ)` e `Índices especiais`.

Os documentos de nível superior estão organizados neste fluxo.

1. Codificação
2. Interpretação
3. Upper Section
4. Lower Section
5. Special Indices

Os documentos de codificação seguem a ordem prancha, localização, qualidade evolutiva (DQ), determinantes, qualidade formal (FQ), pares, conteúdos, populares (P), atividade organizacional (Z), escore, GHR/PHR e escores especiais. A ordem alfabética é usada apenas para localizar itens de detalhe dentro de uma mesma categoria.

### Termos clínicos nos cinco idiomas

Os documentos em coreano, inglês, japonês, espanhol e português do Brasil usam os termos profissionais naturais em cada idioma. Cada documento explica a definição central, as condições de aplicação, os cuidados e os itens relacionados.

Entre as correções mais representativas estão as seguintes.

- No documento PHR em inglês, esclarece-se que `ALOG` faz parte das condições iniciais de PHR na ordem de decisão.
- Nos códigos de conteúdo natural em inglês e espanhol, explicita-se a prioridade pela qual, quando `Na` se aplica, `Bt` ou `Ls` não são codificados na mesma resposta.
- No documento em japonês, a explicação de `Ay` foi corrigida para conteúdo cultural/histórico em vez de anatômico.
- No documento em coreano, a frequência bruta `S-` foi distinguida da proporção independente `S-%`.
- No documento S-CON em coreano, foram explicitados o limite de aplicação a partir dos 15 anos e os 12 critérios que o compõem.

Essas mudanças não substituem a codificação que o clínico realiza após conferir o registro de respostas e a fase de inquérito (Inquiry). Os documentos de referência são material de apoio para conferir as definições e os critérios de distinção dos códigos; a codificação final de cada resposta continua sendo responsabilidade do avaliador humano.

## Busca de documentos de referência pela IA

O assistente de IA procura nos documentos de referência atuais o conteúdo relacionado à pergunta.

Também encontra as explicações relacionadas em perguntas curtas como estas.

- Uma pergunta curta sobre a relação entre Cn e WSumC agora recupera tanto o valor na tela que inclui Cn quanto a explicação de WSumC que o exclui.
- Uma pergunta sobre a prioridade de `Na`, `Bt` e `Ls` não recupera mais apenas as descrições gerais dos três códigos de conteúdo deixando de fora a frase exata sobre a prioridade.

## Escopo dos assistentes de codificação e interpretação

Os dois assistentes seguem estes princípios.

- Respondem apenas a perguntas de codificação e do Sumário Estrutural do Sistema Compreensivo (CS) de Exner.
- Não ampliam suas respostas a sistemas de avaliação distintos, como R-PAS ou MMPI, nem a perguntas gerais de aconselhamento ou diagnóstico.
- Recusam solicitações de revelar informações não públicas do serviço ou a chave de API e os dados de conexão do usuário.
- Quando a idade é realmente necessária para uma interpretação, podem explicar o motivo e perguntá-la dentro da conversa de IA, mas a calculadora em si não exige a inserção da idade.
- Não determinam diagnóstico ou risco a partir do Sumário Estrutural sozinho e dão prioridade à entrevista, à observação do comportamento, aos dados brutos e ao julgamento do clínico.

Solicitações fora do escopo do CS de Exner ou de informações não públicas não são respondidas; em vez disso, os assistentes indicam perguntas de codificação ou do Sumário Estrutural que podem responder.

## Prevenção da repetição excessiva de solicitações de IA

Se as solicitações de conversa com a IA ultrapassarem 12 por minuto ou 120 por hora, pede-se aguardar um momento. Esse limite reduz a repetição acidental da mesma solicitação e custos maiores do que o previsto. Para limitar o número de solicitações, não se armazenam separadamente a chave de API, as perguntas, as respostas, o texto do Sumário Estrutural nem o conteúdo clínico.

As avaliações com "gostei" ou "não gostei" não guardam o texto da conversa e são mantidas por no máximo 180 dias.

## Mudanças nas telas e na descrição do serviço

- A barra lateral esquerda tem fundo opaco fixo para que o conteúdo atrás dela não fique transparente.
- Corrigido o menu de idioma que ficava cortado ou desalinhado sobre o conteúdo ao ser aberto com a barra lateral recolhida.
- Os botões de documentos de referência usam os títulos nos cinco idiomas e a ordem que segue a pontuação e a interpretação.
- A janela que pede para escolher novamente o modo de início (dados novos, dados de exemplo ou dados salvos) volta a abrir sempre que se entra na tela de pontuação.
- As frases-chave em formato de código nos documentos de referência aparecem em um vermelho fácil de distinguir tanto no modo claro quanto no escuro.
- No assistente de codificação, a seta para baixo que aparece ao subir para ler a conversa anterior fica logo acima da área de entrada. Ela não cobre mais o centro da conversa em respostas longas.
- Os registros da versão 2 e da versão 1 aparecem recolhidos ao entrar pela primeira vez.
- O nome do serviço foi unificado como `Calculadora do Sumário Estrutural do Sistema Compreensivo de Exner para o Rorschach`.
- A apresentação do serviço credita a produção à MOW e a contribuição do Seoul Institute of Clinical Psychology (SICP) na conferência dos primeiros resultados de cálculo e na revisão sob a perspectiva do uso clínico real.

As colunas, os menus suspensos, o botão de cálculo e o controle de zoom da folha de pontuação, assim como a tela de resultados do Sumário Estrutural, não mudam. As telas de celular também são mantidas.

As respostas da IA podem variar a cada vez e não têm exatidão clínica garantida para todas as perguntas reais. Tampouco a correção do cálculo do Sumário Estrutural é determinada pelas respostas da IA.

## Fontes públicas dos termos nos cinco idiomas

Dá-se prioridade ao uso profissional de cada idioma e os códigos e identificadores do Sistema Compreensivo são mantidos como estão. Nenhuma fonte única é tomada como resposta correta para todos os idiomas.

- Coreano: [KCI - Construction of the Korean Rorschach Comprehensive System for Children based on Exner's Comprehensive System](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001392063), [KCI - Coping and defense of North Korean defectors on the Rorschach](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001391524)
- Inglês: [International Rorschach Institute manuals](https://www.rorschach-institute.org/manuals.html), [Meyer and Viglione, An Introduction to Rorschach Assessment](https://www.utoledo.edu/al/psychology/pdfs/meyer/MeyerViglione2008IntroRorschach.pdf)
- Japonês: [誠信書房 - 包括システムによるロールシャッハ臨床](https://www.seishinshobo.co.jp/book/b88274.html)
- Espanhol: [Sociedad Española de Rorschach y Métodos Proyectivos](https://www.rorschach.es/index.php/programas-de-los-cursos), [CHESSSS](https://rorschachspain.org/chessss/), [Manual de codificación del Rorschach para el Sistema Comprehensivo](https://www.psimatica.com/tienda/psicodiagnostico/23-manual-de-codificacion-del-rorschach-autor-john-exner.html)
- Português do Brasil: [SciELO - Localização e qualidade formal do Rorschach-SC no Brasil](https://www.scielo.br/j/pusf/a/kFHxFGKH3qx9gdVtyC6nqWS/), [SciELO - Indícios de validade do déficit relacional no Método de Rorschach](https://www.scielo.br/j/pusf/a/6Xy8zSJGCNq49BWjXRpYNhx/)
- Princípios comuns de tradução e adaptação: [International Test Commission Guidelines](https://www.intestcom.org/page/14)
