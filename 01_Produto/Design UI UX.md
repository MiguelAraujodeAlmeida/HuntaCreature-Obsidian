# Design, UI e UX

**Padrão visual vigente, revisável por feedback.** Princípios gerais aprovados a partir de [[06_Referencias/Estudo visual Steal an Egg]]; imagens de apoio em [[06_Referencias/Referencias Visuais]]. Regras mecânicas e parâmetros: [[01_Produto/Sistemas Atuais]].

## 1. Direção de arte: criaturas e mundo

### Criaturas
- **Silhueta em primeiro lugar:** cada espécie deve ser reconhecível em silhueta monocromática (frente, lado, costas e 3/4) antes de cor ou efeito, combinando uma massa dominante e 1–2 traços anatômicos próprios em escala exagerada.
- **Construção de brinquedo montável:** poucos volumes grandes e bem encaixados, planos visíveis, facetas e chanfros simples. Cantos podem ser suavizados, mas sem voltar à esfera lisa com bolinhas soltas.
- **Cor por zonas amplas:** cor principal, área secundária (barriga/focinho) e acentos de contraste seguindo a geometria. Studs discretos apenas onde reforçarem o material de brinquedo.
- **Expressão sem ruído:** personalidade dada por proporção, inclinação da cabeça e rosto simples (olhos/boca legíveis), sem depender de partículas ou neon em criaturas comuns.

### Modelo vigente: Lumito base v01 (`Lumito_Base_v01`)
- **Identidade preservada e reinterpretada:** substituiu o protótipo esférico no código (`ee6e901`) e no Studio (`ReplicatedStorage.HACLumitoTemplate`).
- **Anatomia e silhueta:**
  - **Cabeça (~50% da altura):** cápsula facetada em três faixas com **testa larga projetada sobre o rosto** (traço próprio nº 1), inclinada com curiosidade (`14°` roll, `10°` yaw, `6°` pitch).
  - **Orelhas em duas folhas facetadas:** esquerda ereta e **direita dobrada para fora** (traço próprio nº 2, assimétrico em 360°), com interior em teal escuro.
  - **Tronco, pés e crista:** tronco trapezoidal curto com placa de barriga aqua acompanhando o chanfro frontal; pés em cunha com sola teal e 1 stud; **crista dorsal teal com 3 studs** conectando topo, nuca e ponta da cauda.
  - **Expressão:** olho esquerdo aberto com brilho branco, olho direito semicerrado, boca torta e um único dente triangular.
- **Paleta aplicada por `ColorRole` (`SmoothPlastic`, sem neon):**
  - `Normal`: `Main` Cyan `12,211,255` · `Secondary` Pale Aqua `196,248,255` · `Accent` Deep Teal `0,112,168` · `Ink` `3,12,40` · `Glint` `255,255,255`.
  - `Gold` (`Dourado`): `Main` `255,220,86` · `Secondary` `255,252,240` · `Accent` `214,142,28` · `Ink` `3,12,40` · `Glint` `255,255,255`.

### Mundo e materiais
- Cenário modular de brinquedo: pisos amplos com studs/grade, plataformas, cercas e estruturas simples com cores vivas por bioma. Áreas de circulação permanecem limpas para destacar criaturas, alvos e recompensas.

### Movimento e VFX de criaturas
- A atuação deve sugerir curiosidade e travessura com poucos movimentos grandes: inclinação e balanço de cabeça, orelhas/cauda responsivas, passada com peso, piscada e pausas gestuais. O `Root` de gameplay e o volume `Corpo` não acompanham oscilações cosméticas.
- Poeira de passada usa massas gráficas de leitura cartunesca, contorno teal e preenchimento branco/ciano, em rajadas curtas sincronizadas ao contato do pé. Corrida pode usar rastro ciano curto e afilado; evitar fumaça contínua, nuvens grandes sobre o personagem, excesso de brilho ou partículas que substituam a animação corporal.

## 2. HUD, caça e feedback

- **HUD limpo:** ouro/força no canto inferior esquerdo; Criaturas, Index e Hunter Rank em botões quadrados glossy com arte original, agrupados na lateral no desktop e reorganizados em telas menores. Configurações usa engrenagem circular escura na área livre da topbar nativa, acompanhando `GuiService.TopbarInset`. Barra de carga central acima da hotbar. XP aparece no contexto de Rank, sem terceira caixa de recurso. Sem título fixo ou avisos para falhas comuns.
- **Botões glossy (`GlossyButton`):** ícones reais, brilho, contorno escuro e fonte **Fredoka One** em inglês; compressão curta ao clicar/tocar (`0.94×`) e leve expansão em hover (`1.06×`).
- **Leitura da caça no mundo (`LassoFeedback` / `CaptureHUD` / `RewardPresentation`):**
  - Contorno (`Highlight`) muda cor e opacidade conforme estado do alvo; voo do laço usa trilha quente e retorno usa trilha ciano.
  - Disputa exibe barra compacta de progresso, zona móvel, fase (normal/resistência/abertura) e indicador de poção.
  - Vitória mostra cartão curto (`2,35 s`) com retrato 3D real (`ViewportFrame`), destaque de Gold/primeira descoberta, XP ganho na captura e potencial de `ouro/s` na base (sem rótulo textual de tamanho).
- **Boleio do laço (`LassoChargePresentation`):** a preparação deve ser lida primeiro no corpo do avatar: braço direito claramente elevado, mão ao lado e ligeiramente acima da cabeça, cotovelo flexionado para fora e pulso em ciclo curto, tronco acompanhando discretamente e braço esquerdo recolhido. A corda aberta acompanha a mão em plano inclinado de `30–45°`, cruzando a região superior da cabeça e descendo na lateral; não deve parecer um aro estático flutuando acima do avatar. Ondulação pequena, rastro dourado curto e um único acento em MAX dão vida sem esconder o alvo. A soltura sugere extensão rápida do braço rumo à mira, sem alterar o voo real. Parâmetros visuais pertencem a `LassoChargeStyle` por laço.
- **Hunter Rank:** botão roxo de acesso direto com emblema de licença, rank e progresso curto. A página abre com emblema, rank atual, **XP restante exato até o próximo rank** e percentual na barra; abaixo, somente os benefícios do próximo marco e silhuetas dos equipamentos reais com `RequiredHunterRank` correspondente. Missões aparecem como `COMING SOON` até existir sistema próprio. Não mostrar custo total de XP, lista completa de ranks, cap, ferramenta fictícia, tutorial ou bloqueio de ilha. Subida de rank usa brilho/partículas/som e cartão curto não bloqueante.
- **Áudio (`AudioConfig` / `AudioFeedback`):** master `0,7`, limite de `8` vozes simultâneas e cooldown no som de renda para não tocar a cada segundo.

## 3. Família de menus (`MenuTheme` / `MenuKit`)

Aplica-se a `Creatures`, `Creature Market`, `Creature Index`, `Hunter Rank`, `Hunting Shop` e `Settings` (guia técnico espelhado em `studio/MENU_STANDARD.md`). Placas físicas do mundo e HUD de disputa são as únicas exceções justificadas.

- **Estrutura visual:** fundo escuro em tile (`ImageLabel`), borda escura, cabeçalho colorido por função (**ciano** = coleção/Index, **roxo** = Hunter Rank, **verde** = loja, **dourado** = mercado, **azul claro** = Settings) e botão **X vermelho** no canto superior direito.
- **Responsividade:** janelas até `1000 × 660` (`Settings` `800 × 450`). Em `>= 740 px`, galeria à esquerda (`~62%`) e ficha à direita (`~38%`); abaixo disso, ficha selecionada acima da grade.
- **Comportamento:** retrato 3D/ícone antes do texto; uma ação principal por ficha; seleção e rolagem preservadas durante atualizações de `valueRefreshers`; confirmação visual depende do snapshot do servidor.

| Camada | Módulo no código | Papel |
|---|---|---|
| Tokens e paleta | `shared/MenuTheme`, `shared/VisualStyle` | Cores, fontes, tamanhos e asset IDs |
| Componentes de janela | `client/MenuKit` | `Window`, `Surface`, `Scroller`, `Detail`, `Grid`, `Badge`, `Stat`, `Action`, `Selectable`, `Empty` |
| Retratos | `client/CreatureCards`, `client/CreaturePortrait`, `client/ToolPortrait` | Cartões, `ViewportFrame` 3D (colorido ou silhueta `12,18,40`) e ícones de ferramentas |
| Controle e páginas | `client/GlossyButton`, `client/CollectionUI`, `*Page.luau` | Navegação, foco (`FocusKey`) e envio via `ui:Send` |

## 4. Tokens e Asset IDs (`VisualStyle`)

| Recurso | Asset ID (`rbxassetid://`) |
|---|---|
| `Coin` / `XP` / `Strength` | `137147969134175` / `90531108912513` / `111581776806956` |
| `Bag` / `Lasso` | `84667354571821` / `117254148917574` |
| `HunterRank` | `94003376835794` |
| `Index` | `112115433096189` |
| `SkinTile` / `Panel` (`SliceCenter 150,140,874,200`) | `93505871377958` / `130734564577623` |
| `Studs` / `Wood` / `Tiles` (amostras de mundo) | `133050717017276` / `97810845356536` / `103826263412719` |

Paleta RGB UI/Menu: `Gold` `255,203,20` · `Cyan` `12,211,255` · `Purple` `211,108,255` · `Green` `59,246,29` · `Red` `255,72,81` · `Ink` `3,12,40` · `MenuBody` `28,35,56` · `MenuSurface` `43,56,78` · `MenuMuted` `178,203,224`.

## Treino AFK

O manequim deve evoluir em silhueta, material e personalidade, seguindo a oficina de caçador: espantalho, madeira articulada, guarda blindado e autômato. O ciclo automático deve mostrar preparação, arremesso, resistência cômica, impacto e recuperação, com variações discretas e `+Strength` apenas após crédito real. A cena precisa continuar legível após minutos de repetição; brilho e som são acentos, sem cobrir o alvo. Eficiência acrescenta equipamento próprio à estação sem multiplicar combinações de modelos.
