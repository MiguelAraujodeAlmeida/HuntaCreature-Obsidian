# Decisões vigentes

ADRs ativas do projeto (histórico de substituições em [[00_Inicio/Historico de Contexto]]). Parâmetros detalhados ficam em [[01_Produto/Sistemas Atuais]] e [[03_Engenharia/Arquitetura Atual]].

## ADR-001 — Fontes de verdade e sincronização (19/10/2026)
Pedido humano recente define a intenção; o cofre registra as regras vigentes; o repositório Git (`main`) é a referência operacional dos scripts Luau e o Roblox Studio detém o lugar (`102310424634629`). Não fazer varredura integral Studio ↔ disco por rotina — investigar apenas divergência concreta. Salvar scripts no Git, salvar o lugar no Studio (`.rbxl`/nuvem) e publicar o jogo são operações independentes.

## ADR-002 — Treino automático no manequim (18/10/2026)
O treino de força é automático, mantendo o avatar imóvel laçando o manequim da base (substituindo a ideia antiga de correr em esteira, embora o nome interno `Esteira` permaneça no modelo da estação por compatibilidade). Sair, pular ou morrer deve restaurar o movimento imediatamente.

## ADR-003 — Acessos físicos e gestão de coleção (18/10/2026)
Melhorias são compradas exclusivamente nas placas físicas da própria base; vendas ocorrem apenas no mercado físico; ferramentas usam o `Backpack` nativo do Roblox; e a janela `Creatures` centraliza `Equip`/`Unequip` (sem troca implícita quando cheio) e proteção por favorito.

## ADR-004 — Base viva, idioma inglês e descoberta permanente (19/10/2026)
Criaturas equipadas passeiam livremente no piso da base; ocultá-las em `Settings` é preferência visual local e não interrompe a renda. Toda a interface visível ao jogador é em inglês, mantendo IDs internos de save estáveis. O `Creature Index` registra variantes descobertas (`Normal`/`Gold`) de forma permanente, mesmo após venda.

## ADR-005 — Família unificada de menus (19/10/2026)
Todos os menus de tela (`Creatures`, `Creature Market`, `Creature Index`, `Hunting Shop`, `Settings`) compartilham `MenuTheme`, `MenuKit`, `GlossyButton` e retratos `ViewportFrame` ([[01_Produto/Design UI UX]]). Apenas as placas físicas do mundo e a HUD compacta de disputa possuem layout próprio pela função espacial.

## ADR-006 — Reset global por geração fixa de DataStore (19/10/2026)
O reset global solicitado foi implementado trocando o namespace fixo em `PersistenceConfig` para `20261019_menu_reset_01`, preservando os dados antigos (`_v1`) sem exclusão física e permitindo que o novo progresso persista normalmente entre sessões.

## ADR-007 — Contexto portável, enxuto e com dono único (19/10/2026)
O cofre Obsidian é versionado no GitHub com manifesto de leitura (`bootstrap` + `domains`) e validador determinístico (`tools/check_context.py`). Cada regra tem uma única nota dona; mudanças atualizam a nota dona e acrescentam uma entrada curta em [[00_Inicio/Historico de Contexto]].

## ADR-008 — Caça legível pelo mundo e recompensa transparente (20/10/2026)
O laço mantém disparo reto, livre e sem assistência. Estados de mira, carga, voo, impacto, fases da disputa (`3,6 s`) e uso de poção são comunicados por feedback visual/sonoro curto sem popups de erro. O cartão de vitória informa o ganho real (`ouro/s` e `XP/s` ao equipar na base), sem sugerir pagamento instantâneo na captura.

## ADR-009 — Escala contínua (`1×`–`5×`) e Lumito base facetado v01 (20/10/2026)
O tamanho das criaturas é um multiplicador individual contínuo de `1×` a `5×` sem rótulos textuais de classe na UI. O modelo provisório esférico do Lumito foi substituído pela construção facetada de brinquedo (`Lumito_Base_v01` em `ReplicatedStorage.HACLumitoTemplate` + `CreatureFactory` + `LumitoBehavior`, commit `ee6e901`), seguindo a direção de [[06_Referencias/Estudo visual Steal an Egg]] e mantendo o pivô (`Root`), o volume de colisão do laço (`Corpo`) e a paleta por `ColorRole` (`Normal` e `Gold`). Mutações com geometria adicional ficam para etapa posterior à aprovação humana do modelo base.
