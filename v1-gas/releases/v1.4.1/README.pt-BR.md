# v1.4.1

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Metadata

| Field | Value |
| --- | --- |
| Version | `v1.4.1` |
| Release date | 2026-01-07 |
| Release type | Correção de erros |
| GAS deployment | [Open GAS app](https://script.google.com/macros/s/AKfycbxMCx13pkrSzFs8f2qXfmxy2LRhkBpZTItFTIfEOoOi-zwurbysnKGfDIYtAeEdQP99/exec) |

## Patch Notes

# Principais correções

## *Visão geral*

> **Erros da v1.4.0 foram corrigidos.**

Os botões mostrados ao acessar o aplicativo web pela primeira vez e ao acessá-lo novamente agora aparecem corretamente.
>
- Antes havia um erro em que o botão "Começar com dados de exemplo" aparecia mesmo em um novo acesso.
    - Primeiro acesso: botão "Começar com dados de exemplo"
    - Novo acesso (com dados salvos): botão "Carregar conteúdo salvo automaticamente"
- A janela modal mostrada em um novo acesso ficou mais limpa.
    - O título "Continuar o trabalho" foi removido e apenas a mensagem "Há conteúdo da última sessão." é mostrada

        em letra grande e em negrito (para não dizer a mesma coisa duas vezes)


> Outras melhorias
>
- Um efeito mais perceptível foi adicionado ao passar o mouse sobre os cartões da aba Mais.
    - A sombra fica mais intensa
    - A imagem de fundo atrás do cartão fica mais nítida
    - O texto do cartão fica desfocado para que a imagem de fundo se destaque
- Os estilos que deveriam estar em `styles.html` mas ainda estavam parcialmente em `index.html` foram todos movidos,

    deixando o código mais organizado.


Essas mudanças também estão refletidas no [chatbot Gems](https://gemini.google.com/gem/1QDCPHshPvq5J9iIKeV-1Nvy0EFzKPN6Y?usp=sharing).

---

## *Detalhes*

### *Correção da lógica dos botões do modal de primeiro acesso*

> **Implementação**
>
- **Problema**
    - O botão "Começar com dados de exemplo" aparecia tanto no primeiro acesso quanto nos seguintes
    - Em um novo acesso, clicar em "Começar com dados de exemplo" na verdade carregava o conteúdo salvo automaticamente
- **Solução**
    - Com dados salvos: mostrar o botão "Carregar conteúdo salvo automaticamente"
    - Sem dados salvos: mostrar o botão "Começar com dados de exemplo"
    - `updateAllTexts()` não sobrescreve mais o texto enquanto o modal já está visível
    - Funciona igual em todos os idiomas suportados (coreano, inglês, japonês, espanhol, português)

> **Detalhes técnicos**
>
- Adicionada uma proteção em `updateAllTexts()` para não atualizar o texto do modal se ele já estiver visível
- `handleScoringTabFirstLoad()` verifica se há dados salvos e define o texto do modal
- Com dados salvos, `modalLoadBtn.textContent` é definido como `t('modal_welcome_load_saved')`
- Sem dados salvos, `modalLoadBtn.textContent` é definido como `t('modal_welcome_load')`
- `updateAllTexts()` também verifica se há dados salvos e define o texto do modal (caso seja executado antes de o modal aparecer)

**Arquivos**: `index.html` (linhas 2387–2426: função updateAllTexts; linhas 3974–4060: função handleScoringTabFirstLoad)

### *Melhoria da interface do modal de primeiro acesso*

> **Implementação**
>
- **Título removido**
    - Com dados salvos, o título "Continuar o trabalho" é ocultado e apenas a mensagem "Há conteúdo da última sessão." é mostrada
    - Evita dizer a mesma coisa duas vezes
- **Mudança de estilo da mensagem**
    - Com dados salvos, a mensagem aparece em letra grande, em negrito e preta (18px)
    - Antes: letra pequena e cinza
    - Depois: letra grande, em negrito e preta (font-weight: bold, font-size: 18px, color: #212529)
- **Primeiro acesso**
    - Sem dados salvos, título e mensagem são mostrados como antes
    - A mensagem mantém o estilo padrão (pequena, cinza)

> **Detalhes técnicos**
>
- `handleScoringTabFirstLoad()` define `modalTitle.style.display = 'none'` quando há dados salvos
- Com dados salvos, estilos inline (fontWeight, fontSize, color) são aplicados a `modalMessage`
- Sem dados salvos, `modalTitle.style.display = 'block'` é definido e o estilo da mensagem é redefinido
- A mesma lógica é aplicada em `updateAllTexts()`

**Arquivos**: `index.html` (linhas 3987–3993, 4049–4054, 2403–2409, 2413–2424)

### *Refatoração de estilos estáticos*

> **Implementação**
>
- **Problema**
    - Restavam estilos inline em `index.html`, dificultando a manutenção
    - CSS e HTML não estavam separados, então era preciso verificar vários arquivos para alterar um estilo
- **Solução**
    - Todos os estilos estáticos (não controlados dinamicamente por JavaScript) foram movidos para `styles.html`
    - Estilos controlados dinamicamente por JavaScript (`display: none` etc.) permanecem em `index.html`
- **Estilos movidos**
    - `text-align: center` de títulos/mensagens dos modais → adicionado a `#reset-modal-title`, `#reset-modal-message`, `#ai-modal-title`, `#ai-modal-message`
    - Estilo do texto de orientação → adicionado a `#Scoring_Summary > p`
    - Estilo flex do contêiner do info-icon → adicionado a `.row-controls > div`
    - Estilo de hr → adicionado a `#Notice hr`
    - Largura da tabela → adicionada a `#list-table-body table`
    - Largura de colgroup → adicionada a `#list-table-body colgroup col:nth-child()`

> **Detalhes técnicos**
>
- Atributos de estilo inline removidos de `index.html`
- Regras CSS para esses seletores adicionadas a `styles.html`
- Estilos de modais adicionados à seção 8.0
- Estilos da aba Mais adicionados às seções 4.4 e 4.5
- Estilos de componentes comuns adicionados à seção 2.1

**Arquivos**:

- `index.html` (linhas 212–213, 224–225, 263, 271–275, 287, 325: estilos inline removidos)
- `styles.html` (linhas 1306–1311: estilos de modais; 655–666: estilos de tabela; 667–669: estilos de hr; 244–250: estilos de componentes comuns)

### *Organização do sumário e dos comentários*

> **Sumário**
>
- **Mudanças**
    - Entradas duplicadas removidas (10.31 aparecia duas vezes)
    - Ordem do sumário ajustada à ordem real do código
    - Novos estilos refletidos no sumário de `styles.html`
        - `#Scoring_Summary > p` e `.row-controls > div` adicionados a 2.1
        - 4.4 e 4.5 adicionados (largura/colunas da tabela, separador)
        - IDs de modais adicionados a 8.0
- **Verificação**
    - Todos os comentários do sumário coincidem com a posição real do código
    - A estrutura do código pode ser entendida com precisão a partir do sumário

> **Remoção de comentários inline desnecessários**
>
- **Tipos de comentários removidos**
    - Comentários explicativos evidentes só de ler o código
        - ex.: `// 모달이 이미 표시되어 있으면 모달 텍스트는 업데이트하지 않음`
        - ex.: `// (handleScoringTabFirstLoad에서 이미 설정했을 수 있음)`
        - ex.: `// 저장된 데이터 유무에 따라 환영 모달 텍스트 설정`
        - ex.: `// '항목' 열에 내용이 있으면 새 카테고리`
        - ex.: `// "Card (카드)" -> "Card"`
        - ex.: `// Excel에서 한글이 깨지지 않도록 BOM(Byte Order Mark)을 추가합니다.`
- **Comentários importantes mantidos**
    - Comentários de separação de seções (ex.: `// 10.1.5. 모든 텍스트 업데이트 함수`)
    - Comentários que explicam um motivo técnico

**Arquivos**:

- `index.html` (linhas 119–172: sumário; 2387–2426: comentários removidos)
- `styles.html` (linhas 47–107: sumário)

### *Melhoria do efeito hover dos cartões da aba Mais*

> **Implementação**
>
- **Sombra mais forte**
    - Antes: `box-shadow: 0 4px 8px rgba(0,0,0,0.1)`
    - Depois: `box-shadow: 0 8px 24px rgba(0,0,0,0.25)` (sombra mais escura e maior)
- **Imagem de fundo mais nítida**
    - Ao passar o mouse, a opacidade da imagem de fundo sobe de 0.12 para 0.35
    - `filter: saturate(1.2) contrast(1.1)` aplicado para realçar a cor
- **Desfoque do texto**
    - Ao passar o mouse, `filter: blur(2px)` e `opacity: 0.6` são aplicados ao texto do cartão
    - O texto é desfocado para que a imagem de fundo se destaque
- **Transição**
    - `transition` aplicado a todos os efeitos para uma animação suave

> **Detalhes técnicos**
>
- Sombra, opacidade da imagem de fundo e filtro adicionados a `.link-button:hover`
- Filtro adicionado a `.link-button:hover::before` (imagem de fundo mais nítida)
- Filtro e opacidade adicionados a `.link-button:hover > *` (desfoque do texto)
- Propriedade `transition` (0.25s ease) adicionada a todos os efeitos

**Arquivos**: `styles.html` (linhas 1357–1375: efeito hover)

### *Mudanças por arquivo*

> **index.html**
>
- **Principais mudanças**
    - Correção da lógica dos botões do modal de primeiro acesso
    - Melhoria da interface do modal (título removido, estilo da mensagem)
    - Remoção de estilos estáticos inline
    - Organização do sumário e dos comentários
    - Informação de versão sem mudança (permanece v1.4.0)
- **Estatísticas do código**
    - Linhas totais: cerca de 4.839
    - Funções principais: 35
    - Seções do sumário: 35 (todas coincidem com o código)

> **styles.html**
>
- **Principais mudanças**
    - Estilos estáticos adicionados (modais, tabela, hr, componentes comuns)
    - Melhoria do efeito hover dos cartões da aba Mais
    - Sumário atualizado
    - Informação de versão sem mudança (permanece v1.4.1)
- **Estatísticas do código**
    - Linhas totais: cerca de 1.561
    - Variáveis CSS: 33 (cores de grupo)

> **Code.gs**
>
- **Principais mudanças**
    - Sem mudanças
- **Estatísticas do código**
    - Linhas totais: cerca de 1.174

### *Testes e verificação*

> **Testes funcionais**
>
- ✅ No primeiro acesso, o botão "Começar com dados de exemplo" é mostrado
- ✅ Em um novo acesso (com dados salvos), o botão "Carregar conteúdo salvo automaticamente" é mostrado
- ✅ Cada botão executa a ação correta
- ✅ Com dados salvos, o título é ocultado e apenas a mensagem é mostrada
- ✅ Com dados salvos, a mensagem aparece em letra grande, em negrito e preta
- ✅ Funciona igual em todos os idiomas suportados
- ✅ Efeito hover dos cartões da aba Mais verificado (sombra, imagem de fundo, texto)

> **Verificação de UI/UX**
>
- ✅ O texto dos botões do modal muda corretamente conforme o estado de salvamento
- ✅ O estilo da mensagem do modal muda corretamente conforme o estado de salvamento
- ✅ O efeito hover dos cartões da aba Mais funciona com suavidade

> **Verificação da qualidade do código**
>
- ✅ Comentários do sumário coincidem com o código
- ✅ Comentários inline desnecessários removidos
- ✅ Estilos estáticos movidos corretamente para `styles.html`
- ✅ Estilos inline reduzidos ao mínimo
- ✅ Estrutura do código melhorada

---

# Roteiro futuro

O programa continuará sendo monitorado para corrigir os erros que forem encontrados.

## Source files

- `source/Code.gs`
- `source/index.html`
- `source/styles.html`

## How to use

Para reproduzir esta versão, crie em um projeto do Google Apps Script arquivos com os mesmos nomes e cole os arquivos de `source/` como estão.
Ao implantar o projeto do GAS como aplicativo web, é possível executar diretamente a calculadora dessa versão.
