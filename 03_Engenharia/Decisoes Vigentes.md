# Decisões vigentes

ADRs ativas do projeto (histórico de substituições em [[00_Inicio/Historico de Contexto]]). Parâmetros detalhados ficam em [[01_Produto/Sistemas Atuais]] e [[03_Engenharia/Arquitetura Atual]].

## ADR-001 — Fontes de verdade e sincronização (19/10/2026)
Pedido humano recente define a intenção; o cofre registra as regras vigentes; o repositório Git (`main`) é a referência operacional dos scripts Luau e o Roblox Studio detém o lugar (`102310424634629`). Não fazer varredura integral Studio ↔ disco por rotina — investigar apenas divergência concreta. Salvar scripts no Git, salvar o lugar no Studio (`.rbxl`/nuvem) e publicar o jogo são operações independentes.

## ADR-002 — Treino automático no manequim (18/10/2026)
O treino de força é automático, mantendo o avatar imóvel laçando o manequim da base (substituindo a ideia antiga de correr em esteira, embora o nome interno `Esteira` permaneça no modelo da estação por compatibilidade). Sair, pular ou morrer deve restaurar o movimento imediatamente.

## ADR-003 — Acessos físicos e gestão de coleção (18/10/2026)
Melhorias físicas usam placas da base, velocidade e treino; a Bolsa é comprada no menu Creatures (ADR-015). Vendas ocorrem apenas no mercado físico; ferramentas usam o `Backpack` nativo do Roblox; e a janela `Creatures` centraliza `Equip`/`Unequip` (sem troca implícita quando cheio) e proteção por favorito.

## ADR-004 — Base viva, idioma inglês e descoberta permanente (19/10/2026)
Criaturas equipadas passeiam livremente no piso da base; ocultá-las em `Settings` é preferência visual local e não interrompe a renda. Toda a interface visível ao jogador é em inglês, mantendo IDs internos de save estáveis. O `Creature Index` registra variantes descobertas (`Normal`/`Gold`) de forma permanente, mesmo após venda.

## ADR-005 — Família unificada de menus (19/10/2026)
Todos os menus de tela (`Creatures`, `Creature Market`, `Creature Index`, `Hunter Rank`, `Hunting Shop`, `Settings`) compartilham `MenuTheme`, `MenuKit` e `GlossyButton`; menus de criaturas usam retratos `ViewportFrame` ([[01_Produto/Design UI UX]]). Apenas as placas físicas do mundo e a HUD compacta de disputa possuem layout próprio pela função espacial.

## ADR-006 — Reset global por geração fixa de DataStore (atualizado 21/10/2026)
O reset global autorizado para o protótipo de Hunter Rank troca o namespace fixo em `PersistenceConfig` para `20261021_hunter_rank_01`. Todas as contas começam novas ao carregar esta versão; dados das gerações anteriores continuam preservados, sem exclusão física. Não trocar a geração novamente sem decisão explícita: cada troca reinicia também o progresso criado desde este reset.

## ADR-007 — Contexto portável, enxuto e com dono único (19/10/2026)
O cofre Obsidian é versionado no GitHub com manifesto de leitura (`bootstrap` + `domains`) e validador determinístico (`tools/check_context.py`). Cada regra tem uma única nota dona; mudanças atualizam a nota dona e acrescentam uma entrada curta em [[00_Inicio/Historico de Contexto]].

## ADR-008 — Caça legível pelo mundo e recompensa transparente (atualizado 21/10/2026)
O laço mantém disparo reto, livre e sem assistência. Estados de mira, carga, voo, impacto, fases da disputa (`3,6 s`) e uso de poção são comunicados por feedback visual/sonoro curto sem popups de erro. O cartão de vitória informa XP pago imediatamente na captura e potencial de ouro/s na base; XP passivo não é anunciado como XP/s.

## ADR-009 — Escala contínua (`1×`–`5×`) e Lumito base facetado v01 (20/10/2026)
O tamanho das criaturas é um multiplicador individual contínuo de `1×` a `5×` sem rótulos textuais de classe na UI. O modelo provisório esférico do Lumito foi substituído pela construção facetada de brinquedo (`Lumito_Base_v01` em `ReplicatedStorage.HACLumitoTemplate` + `CreatureFactory` + `LumitoBehavior`, commit `ee6e901`), seguindo a direção de [[06_Referencias/Estudo visual Steal an Egg]] e mantendo o pivô (`Root`), o volume de colisão do laço (`Corpo`) e a paleta por `ColorRole` (`Normal` e `Gold`). Mutações com geometria adicional ficam para etapa posterior à aprovação humana do modelo base.

## ADR-010 — Hunter Rank cumulativo, loja flexível e progresso sem bloqueio espacial (21/10/2026)
O Hunter Rank é um tier derivado de XP total, com dez limiares iniciais muito crescentes, sem rebirth. Captura e descoberta dão XP imediato; criaturas equipadas dão XP passivo pequeno. Rank melhora levemente ouro e treino; cada item futuro pode optar por `RequiredHunterRank`, sem faixas prescritas de equipamentos. O rank não bloqueia visita a ilhas. A economia de ouro pode crescer livremente por renda/preço de futuras espécies e itens; o conteúdo inicial não é inflado artificialmente. Parâmetros são prototípicos e revisáveis após playtest, sem migração de dados antigos por causa do reset autorizado.

## ADR-011 — Hunter Rank como marco visível e descoberta gradual (21/10/2026)
Hunter Rank tem botão próprio na HUD, progresso percentual e celebração breve. A página revela o XP restante para o próximo rank e seus benefícios; custo total, lista de ranks e teto configurado permanecem internos. Equipamento só aparece como silhueta se existir no catálogo com `RequiredHunterRank`. Missões são sinalizadas como futuras, sem regras simuladas. XP de captura considera espécie, tamanho, Gold e descoberta; pesquisa passiva vem da espécie/variante equipada. Essas regras pertencem a `HunterProgression`; apresentação pertence a `HunterRankHUD`/`HunterRankPage`, para permitir ajuste separado.

## ADR-012 — Navegação principal ilustrada e Configurações na topbar (21/10/2026)
Criaturas, Index e Hunter Rank compartilham a placa quadrada glossy e ícones próprios. Configurações é um controle circular auxiliar, pequeno e sem legenda permanente, na região da topbar desocupada pelo Roblox. A posição acompanha `GuiService.TopbarInset`, evitando deslocamentos fixos que colidam com controles nativos. Clique/foco/brilho continuam centralizados em `GlossyButton`.

## ADR-013 — Boleio de preparação separado do disparo (22/10/2026)
Segurar o arremesso faz o avatar preparar o laço com braço e pulso, corda flexível inclinada que passa pela região superior da cabeça e desce pela lateral. O laço não fica como aro estático acima do personagem. O ciclo acelera com a carga e segue estável em MAX; soltar sugere um chicote breve. `LassoChargePresentation` e `LassoChargeStyle` contêm apenas a apresentação, com início/fim replicados após validação do servidor; `LassoAim`, alcance e trajetória permanecem independentes. Ritmo e pose aguardam aprovação em playtest.

## ADR-014 — Salvamento do lugar é ação do desenvolvedor (22/10/2026)
O assistente pode editar scripts no Studio Edit via MCP, mas não aciona Save pelo acesso ao computador. Após aplicar, informa ao desenvolvedor que ele deve salvar o lugar e registra o estado como pendente até receber confirmação. Commit de código, compilação e lugar salvo são estados distintos.

## ADR-015 — Distribuição dos upgrades e curva de ouro (23/10/2026)
A placa Base compra somente expansão da base. A bolsa cresce no menu Creatures; treino e eficiência ficam na placa do manequim; velocidade tem placa própria até o rework. IDs de perfil não mudam. A curva jogável usa apenas níveis sustentados pelo conteúdo atual; escalas até bilhões são projeção condicionada a novas espécies e ferramentas. Saldo, nível e proximidade de placas físicas são validados no servidor.

## ADR-016 — Treino AFK evolutivo (23/10/2026)
O treino permanece totalmente automático com pagamento de força pelo servidor a cada 2 s. Os quatro níveis atuais têm modelos de manequim distintos; eficiência altera componentes da estação de forma independente. Construção visual, animação cliente e economia são módulos separados. Níveis futuros podem adicionar novo modelo e custo quando houver renda correspondente; esta rodada não cria níveis nem altera ganho/custo.

## ADR-017 — Zonas de interação e bases silenciosas (23/10/2026)
Treino e lojas usam áreas de entrada amplas e visíveis, sem texto flutuando sobre elas, com disparo único por entrada; fechar menu dentro da área exige sair e voltar para reabrir. O treino fica claramente ao lado e fora da plataforma, sobre piso provisório próprio, e continua exclusivo do dono. Totem e texto de base livre foram retirados. A identidade do dono é retrato e nome no centro, elevados acima das criaturas, apenas enquanto ocupada. Placas de upgrade permanecem ações por clique. A posição exata será revista com o hub definitivo.
