# [2026-07-14] v2.2.0 Versão menor

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

> **Fórmulas atuais:** os extremos de D/AdjD, a condição de exibição de EBPer, a ordem de decisão de GHR/PHR, a omissão de Cn em `FC:CF+C` da Lower Section e o tratamento do denominador zero de WDA% e Afr foram corrigidos na v2.2.1. Na v2.2.2, os cálculos que incluem Cn foram separados dos que não incluem e a classificação GHR/PHR das linhas incompletas com qualidade formal (FQ) vazia foi completada. A calculadora não pede a idade; apenas quando uma interpretação com restrição de idade é solicitada, a conversa de interpretação com IA pergunta a informação necessária. **Consulte a base de cálculo atual na [nota da v2.2.2](../v2.2.2/).**

## Antes de continuar

A v2.2.0 é a primeira versão da série v2.2.x: mantém a calculadora no centro, reúne os menus principais da tela de desktop em uma barra lateral esquerda e reconstrói o assistente de interpretação para se parecer com uma tela comum de chat com IA. A avaliação das respostas de IA não guarda o texto da conversa; escolhe-se apenas um motivo predefinido.

Os itens de cálculo tratados nesta versão que precisaram de correções adicionais foram corrigidos na v2.2.1 e na v2.2.2. O assistente de IA não responde a perguntas fora do Sistema Compreensivo de Exner nem a solicitações de informações não públicas.

## Resumo

### Telas comuns e barra lateral

- Os antigos menus superior e inferior foram integrados em uma barra de ícones fixa no desktop, uma barra lateral que abre sobre o conteúdo e um menu para celular.
- A barra lateral não empurra o conteúdo, permanece aberta ao navegar para outra página e reúne em um só lugar os controles de idioma, tema e sessão de IA.
- Antes do login só aparece "iniciar sessão de IA"; depois, só "encerrar sessão de IA", com uma janela de confirmação antes de encerrar.
- Foi adicionado um guia multilíngue de atalhos que reúne os atalhos da calculadora, os da barra lateral e a forma de ampliar, reduzir e mover a tela de pontuação.
- O fundo e as cores dos modos claro e escuro da calculadora, do assistente de interpretação, dos documentos de referência, da apresentação do serviço, dos termos, da política de privacidade e do arquivo de versões foram unificados.
- A borda externa desnecessária e o botão de copiar a página inteira foram removidos das páginas de serviço, termos e privacidade.

### BYOK e assistente de interpretação

- BYOK (Bring Your Own Key) significa que o usuário conecta a própria chave de API da OpenAI para usar os recursos opcionais de IA.
- A chave de API da OpenAI e a indicação `OpenAI GPT-5.5` ficam na mesma linha, e o título duplicado e o aviso de seleção automática de modelo foram removidos, deixando a janela de conexão de IA mais compacta.
- O aviso de que a chave de API é mantida criptografada por no máximo 24 horas para a conexão de IA e excluída ao encerrar a conexão aparece com mais clareza. A janela não muda mais de tamanho quando o aviso de chave inválida aparece.
- O assistente de interpretação passou a ser um espaço de trabalho completo sem cartão externo, e conversas longas rolam apenas dentro da área de conversa, não na página inteira.
- A rolagem automática que acompanha a resposta da IA para quando a pessoa sobe, e é possível voltar à resposta mais recente quando necessário.
- Foram adicionados parar a resposta, copiar mensagem, localizar a pergunta anterior, uma caixa de entrada translúcida e o estado de colagem do Sumário Estrutural.
- As mensagens do usuário e da IA têm botão de copiar, e as mensagens da IA ganharam "gostei"/"não gostei" com uma janela de motivos predefinidos.
- A avaliação das respostas de IA não guarda o texto da pergunta nem da resposta, nem comentários livres. Apenas se ajudou, o motivo escolhido, o idioma, o modelo, se a resposta foi concluída e o tamanho aproximado são mantidos por no máximo 180 dias.

### Tela de pontuação

- A alça de mover linhas não é mais cortada na borda da tabela.
- A seleção de várias linhas com clique simples, `Shift + clique` e `Ctrl/Command + clique`, e a prévia do movimento de linhas, funcionam de forma estável.
- Caixas de seleção com valor, vazias e desabilitadas mantêm o mesmo tamanho e alinhamento e se distinguem apenas pelo tom.
- As larguras das colunas foram ajustadas para que a tabela caiba em uma tela de desktop comum e, em telas estreitas, role horizontalmente apenas dentro da área de pontuação.
- `Alt + roda do mouse` amplia ou reduz toda a tela de pontuação entre 40% e 125% centrada no ponteiro, e `Ctrl + arrastar` move a tela ampliada.
- A orientação sobre a ordem das linhas aparece na faixa azul logo abaixo da tabela.
- Os botões inferiores foram organizados como adicionar/excluir/ajuda à esquerda e calcular resultados/redefinir entradas ao centro.

### Documentos de referência e arquivo de versões

- A caixa de busca dos documentos de referência não desaparece nos resultados nem no documento detalhado, e o termo de busca é mantido na tela seguinte.
- O aviso de ausência de resultados, os botões de categoria de documentos e o aviso de cópia concluída foram ajustados nos cinco idiomas.
- O corpo dos documentos de referência passou a ser uma vista de leitura sem cartão externo, com a caixa de busca, as categorias e o corpo alinhados no mesmo eixo central.
- Os registros da versão 2 e da versão 1 (GAS) expandem e recolhem ao clicar no título, e a tela não se desloca mais lateralmente quando a barra de rolagem vertical aparece ao expandir.
- As orientações de execução do GAS foram movidas para uma ajuda informativa ao lado do título, que também pode ser aberta pelo teclado.

## Mudanças de cálculo na v2.2.0

Na v2.2.0, os sete itens a seguir foram corrigidos. As fórmulas atuais incluem também as correções posteriores da v2.2.1 e da v2.2.2.

| Item | Correção |
| --- | --- |
| EBPer | Exibido apenas quando `EA >= 4`, M e WSumC são positivos e a proporção é `>= 2.5` |
| Movimento ativo/passivo | `Ma-p`, `FMa-p` e `ma-p` são somados tanto ao lado ativo quanto ao passivo |
| `3r+(2)/R` | O peso das reflexões `Fr+rF` foi corrigido de 2 para o 3 da fórmula padrão |
| HVI | O limite da condição auxiliar de Zd foi corrigido de `> 3.0` para `> 3.5` |
| ZEst | O último limite válido `Zf=50` agora retorna `173` |
| D/AdjD | `0` em vez de `-0` na faixa negativa |
| Lambda | `∞` em vez de 0 quando todas as respostas são F pura |

Para comparar os resultados do cálculo foram usados quatro tipos de material.

- [Sample computerized score reports de Essentials of Rorschach Assessment](https://elmirmohammedmemorypsy.com/wp-content/uploads/2021/04/essentials-of-rorschach-assessment.pdf)
- [Engelman et al., "Why am I so stuck?"](https://www.therapeuticassessment.com/docs/Engelman_et_al_2016_copy.pdf)
- [Caso de síndrome amnésica de Tibon Czopp et al.](https://pubmed.ncbi.nlm.nih.gov/23985019/) e sua [errata](https://www.tandfonline.com/doi/pdf/10.1080/13554794.2014.910345)
- As fórmulas reais da [planilha Excel de 2019 de distribuição pública](https://blog.naver.com/jin_k84/221539279596) consultada no desenvolvimento inicial da v1. A atribuição interna da planilha é `[Scoring Program] _by. Ju-Ri`; nenhum nome real é inferido e o arquivo original não é redistribuído.

Nos dois itens em que as tabelas publicadas e as colunas de escores públicas divergiam, nenhum dos lados foi tomado como única resposta correta.

Médias de grupos nacionais não são gabaritos para a mesma coluna de escores. As diferenças culturais afetam principalmente a codificação, as normas e a aplicação interpretativa, não as fórmulas; por isso os materiais coreanos, japoneses e de língua inglesa foram usados separadamente para verificar a faixa de respostas por cultura e idade.

## Escopo do assistente de IA

- Não responde a interpretações gerais de R-PAS nem de MMPI, a perguntas sem relação nem a solicitações de informações não públicas.
- Perguntas válidas de comparação ou diferenciação com Exner são permitidas apenas na medida de explicar o limite, sem se estender à interpretação geral de outros sistemas.
- A interpretação do S-CON aplica-se a pessoas com 15 anos ou mais. A calculadora não pede a idade; apenas quando lhe pedem uma interpretação do S-CON, o assistente de IA confirma a idade na conversa se necessário.
- Diante de uma pergunta direta sobre Popular (`P`), o documento de referência sobre respostas populares é apresentado primeiro.

O uso do GPT-5.5 com a própria chave de API é mantido. As conversas com a IA são mantidas apenas enquanto a janela atual do navegador está em uso e não são guardadas como registros de conta de longo prazo. A IA não substitui o julgamento final do clínico nem garante a exatidão de todas as respostas.

## Limites que permanecem

- Este escopo de cálculo não comprova matematicamente todas as combinações de respostas possíveis.
- Como a calculadora não pede a idade, a suspensão da interpretação do S-CON para pessoas com 14 anos ou menos deve ser verificada pelo clínico que a utiliza.
- A utilidade clínica real, a qualidade das frases multilíngues e a segurança devem ser avaliadas por profissionais qualificados.
