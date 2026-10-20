# Design, UI e UX

**Padrão vigente, revisável por feedback.** A implementação mais recente ainda não foi aprovada artisticamente. Referências portáveis: [[06_Referencias/Referencias Visuais]].

## Direção de arte

**Padrão vigente após aprovação do estudo visual em 20/10/2026; revisável por feedback.** Referência de leitura: [[06_Referencias/Estudo visual Steal an Egg]]. Usar a lógica visual como inspiração, sem copiar malhas, personagens ou texturas. A meta é uma linguagem de brinquedo/cartoon que pareça nativa do Roblox e una cenário e criaturas.

### Criaturas e objetos

- A espécie deve ser reconhecida pela silhueta antes de detalhes, efeitos ou cor. Cada espécie tem uma massa principal e de 1 a 2 marcas anatômicas próprias em escala exagerada; evitar repetir a mesma esfera com acessórios trocados.
- Construir com volumes grandes e encaixados, formas blocadas ou facetadas e chanfros simples. Curvas podem suavizar cantos, mas não devem apagar os planos e a leitura de peça montável. Evitar superfície uniformemente lisa, detalhamento fino e realismo orgânico.
- Definir cores por áreas amplas: corpo principal, área secundária e poucos acentos de alto contraste. Faixas, barriga, placas, bico, focinho, patas, espinhos ou cristas devem explicar forma ou espécie. Textura de studs pode ser usada quando reforça o material de brinquedo; não cobrir tudo com ruído/relevo sem hierarquia.
- Personalidade vem de proporções, pose e poucos traços faciais legíveis. Olhos e boca simples; exagerar um traço que comunique a criatura. Não depender de partículas para tornar a forma interessante.
- Raridade e mutações podem adicionar forma, paleta, peças e VFX por camadas, preservando a leitura da espécie base. Brilho intenso é reservado a eventos/variantes que o justifiquem; criatura comum continua atraente sem VFX.
- Conferir o modelo em silhueta monocromática, frente/lado/costas e três quartos; testar legibilidade pequena, escala 1× e multiplicadores altos existentes. Pivô, chão e peças animáveis devem servir à integração prevista no Studio.

### Mundo e materiais

- Construir como cenário modular de brinquedo: terreno amplo, caminhos, plataformas, muros, cercas, placas e lojas com formas simples, encaixes claros e limites legíveis.
- Usar superfícies estudadas — studs/grade em chão e peças construídas, madeira estilizada onde fizer sentido — com cores vivas por bioma. Grama, árvores, água, areia, estruturas e criaturas devem compartilhar acabamento e proporção do mesmo mundo.
- Manter áreas de circulação visualmente simples para que criatura, objetivo e recompensa se destaquem. Repetição regular une o espaço, mas não deve competir com pontos de interesse; reservar contraste forte, luz e partículas para locais/ocasiões especiais.
- Mostrar escala com avatar, cercas e props; garantir que cenário e criatura funcionem na câmera e em tela pequena. Evitar realismo, ruído visual, microdetalhes e excesso de neon.

### Lumito base — escopo do próximo estudo

O protótipo atual é ciano, com duas saliências superiores, olhos simples e pés curtos. Esses traços dão reconhecimento à espécie, mas a forma atual quase esférica foi julgada básica demais. No próximo redesign, preservar essa identidade e reinterpretar o corpo segundo as regras acima: silhueta própria, volumes montáveis/facetados e traços anatômicos intencionais. Fazer somente a aparência base; Gold e outras mutações ficam para etapa posterior no Studio. O prompt atual é uma proposta para modelagem e aguarda revisão do modelo, não aprovação antecipada.

Usar componentes glossy originais existentes: ícones grandes o suficiente para leitura, brilho, relevo/contorno e texto branco com sombra escura. Não substituir mochila/moeda/laço por emoji, símbolos de fonte ou retângulos de texto. A referência de botões foi explicitamente escolhida pelo desenvolvedor; manter sua linguagem visual, ajustando escala ao jogo.

Fonte: **Fredoka One** em títulos, números e interface, consistente entre telas. Não adicionar famílias sem justificativa. Inglês, rótulos curtos e hierarquia clara.

## HUD e feedback

- Ações laterais; recursos no canto inferior esquerdo; laço/carga perto do centro inferior, acima da barra nativa. Respeitar áreas seguras e menus do Roblox.
- Ícones de moeda/XP/força proporcionais ao valor; mochila não domina a tela. Recursos não precisam de caixas grandes para existir.
- Sem título permanente do jogo, comandos repetidos, guias contínuos ou mensagens que repetem o que o jogador já viu.
- Priorizar o mundo. Disputa compacta com leitura de progresso e tensão; não uma janela gigante de instruções.
- Hover/foco: brilho e relevo; pressionar: compressão curta; soltar: retorno suave. Mesma resposta por toque sem depender de hover.
- Captura: impacto/celebração e prêmio legível; primeira descoberta/raridade pode ter destaque maior. Compra/upgrade confirma benefício. Renda frequente deve ser sutil.
- Efeitos acompanham o evento, não loops decorativos constantes. Limpar sons, partículas, tweens e conexões. Cancelamento/interrupção precisa encerrar feedback.
- AudioFeedback/AudioConfig limitam vozes e intervalos. Configuração atual: master 0,7, até 8 vozes; som de renda limitado por cooldown, não por tick de 1 s. Mix final pendente.

## Caça e recompensa

- Alvo em foco recebe contorno discreto com estados de distância, possibilidade, alinhamento, bloqueio e disputa alheia. Intensidade e preenchimento acompanham cor; não piscar a cada movimento de câmera. A marca do limite surge durante a carga.
- Carga central acima da barra nativa mostra alcance e ápice MAX, com pulso leve e som limitado. Voo tem trilha curta quente; retorno é ciano e recolhe a corda. Impacto com obstáculo ou tentativa recusada se lê pelo efeito, sem aviso rotineiro.
- Acerto combina som, faísca curta, corda presa e resistência do Lumito. HUD compacta mostra zona móvel, progresso, tempo, resistência/abertura e poção; mantém a visão do mundo livre.
- Vitória tem retrato real, sinal maior para Gold e primeira descoberta de espécie/variante e potencial de renda/XP **na base**. O tamanho aparece no modelo, sem categoria ou multiplicador escrito na interface. Fecha sozinha em até 2,35 s; não bloqueia o retorno ao controle. Renda passiva permanece discreta.

## Família dos menus

Aplica-se a Creatures, Creature Market, Creature Index, Hunting Shop e Settings e a novos menus comparáveis.

- Corpo escuro texturizado, contorno escuro, cabeçalho colorido forte, título grande, **X vermelho** no canto superior direito.
- Ciano: coleção/Index; verde: equipamentos; dourado: mercado/valor/Gold; azul claro: preferências.
- Retrato/objeto antes da ficha textual. Uma ação principal por seleção; preço/capacidade/benefício sempre legíveis.
- Estados explícitos: carregando, vazio, selecionado, indisponível, atualização de dados; confirmação/cancelamento em venda.
- Não inventar recompensas, contadores, urgência, produtos ou catálogo para preencher espaço.
- Textura por ImageLabel em Tile; não milhares de Frames decorativos.
- Menus de coleção usam MenuTheme/MenuKit. Placas físicas e disputa compacta têm composição própria por serem interações no mundo/combate; essa é a exceção atual justificada.

## Layout e acessibilidade

Valores atuais em MenuTheme: cabeçalho 78 px, margens 16, intervalo 12; tamanho máximo 1000 × 660, Settings 800 × 450. Área real é limitada pelo viewport seguro.

A partir de 740 px: galeria esquerda (~62%) e ficha direita (~38%). Abaixo disso: ficha selecionada acima da galeria na rolagem principal. Não reduzir toda a tela até texto/botões ficarem minúsculos.

Rolagem não deve bloquear saída; textos longos não podem sobrepor preço ou ação. Foco/seleção persistem entre atualizações de renda; distinguir estados com texto/forma, não só cor. Compras bloqueadas mostram o motivo real. Feedback visual de clique não comprova compra: snapshot do servidor confirma.

## Componentes e regra para novas páginas

| Camada      | Fonte no código                       | Responsabilidade                                                                        |
| ----------- | ------------------------------------- | --------------------------------------------------------------------------------------- |
| Tokens      | shared/MenuTheme, VisualStyle         | Cor, fonte, proporções e arte                                                           |
| Estrutura   | client/MenuKit                        | Window, Surface, Scroller, Layout, Detail, Grid, Badge, Stat, Action, Selectable, Empty |
| Criaturas   | CreatureCards / CreaturePortrait      | Cartão, ficha, retrato real e silhueta                                                  |
| Ferramentas | ToolPortrait                          | Representação de consumíveis e ícone do laço                                            |
| Interação   | GlossyButton / CollectionUI / páginas | Animação, input, seleção e snapshots                                                    |
| Autoridade  | servidor                              | Posse, custos, favoritos, progressão                                                    |

1. Configurar a página em MenuTheme; módulo Render(ui) e rota necessária em CollectionUI.
2. Definir pageTitle e Tabs; compor com Kit/CreatureCards. Em galeria, Detail vem antes de Grid para calcular largura.
3. Enviar intenções via ui:Send; atualizar valores voláteis via valueRefreshers. Não reconstruir tudo por renda.
4. FocusKey estável por ação/indivíduo; reutilizar bordas, cancelar animações ao destruir.
5. Conferir vazio/cheio, indisponível, confirmação, perda de seleção, texto longo e estreitamento por revisão leve. Teste manual depende do desenvolvedor.
6. Se o padrão não atender, evoluir primeiro o componente compartilhado; registrar exceção e motivo.

O antigo UI:Card(título, parágrafo) foi removido das páginas ativas. UpgradePage é legado sem rota, incompatível com essa remoção: não reativar.

## Tokens e assets de referência

IDs Roblox existentes; não dependem de arquivos temporários da máquina.

| Recurso | Asset ID |
|---|---|
| Coin / XP / Strength | 137147969134175 / 90531108912513 / 111581776806956 |
| Bag / Lasso | 84667354571821 / 117254148917574 |
| SkinTile / Panel | 93505871377958 / 130734564577623 |
| Studs / Wood / Tiles | 133050717017276 / 97810845356536 / 103826263412719 |

Paleta RGB base: Gold 255,203,20; Cyan 12,211,255; Purple 211,108,255; Green 59,246,29; Red 255,72,81; Ink 3,12,40. Menu: Ink 8,14,31; Body 28,35,56; Surface 43,56,78; Muted 178,203,224. Texturas de mundo são amostras, não arte aprovada.

Esta nota é a especificação portável. `studio/MENU_STANDARD.md` é o guia técnico correspondente e deve permanecer alinhado; constantes executáveis ficam nos módulos. Mudança visual exige atualizar os lados afetados na mesma entrega.
