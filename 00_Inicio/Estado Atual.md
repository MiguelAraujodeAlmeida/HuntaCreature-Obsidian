# Estado atual

Revisão de contexto **CTX-2026-10-21-03** · 21/10/2026.

## Entrega vigente do jogo

- **Código enviado:** commit **42ca28a** (`main` em https://github.com/MiguelAraujodeAlmeida/HuntACreature; SHA remoto confirmado).
- **Lugar de teste:** **[Testing] Hunt a Creature**, placeId **102310424634629** (Studio em `Edit`; protótipo aplicado e “Novas alterações salvas ... na Roblox” confirmado).
- **Não publicado:** servidores públicos continuam na versão anterior; publicação exige pedido explícito.

### O que está implementado e integrado

0. **Protótipo Hunter Rank (`42ca28a`, aplicado e salvo no Studio):** dez ranks de XP acumulado em curva ampla; XP imediato por captura/descoberta e XP passivo reduzido por criatura ativa; bônus pequenos de ouro e treino por rank; verificação opcional `RequiredHunterRank` por item, sem restringir ilhas nem bloquear itens atuais. Interface inclui rank no HUD e página a partir do Index. Novo namespace de save `20261021_hunter_rank_01` reinicia todos os perfis quando esta versão for executada, preservando gerações antigas. Módulos centrais carregaram e verificações isoladas passaram em Edit, sem Play novo; playtest humano pendente.

1. **Modelo e atuação do Lumito base v01 (`2c74752`):**
   - Modelado no Blender (`C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Art\Lumito\Lumito_Base_v01.blend` e `.fbx`) seguindo os princípios de [[06_Referencias/Estudo visual Steal an Egg]] e [[01_Produto/Design UI UX]].
   - Construído no Studio em `ReplicatedStorage.HACLumitoTemplate` (33 `UnionOperation`s CSG + `Root` + `Corpo` invisível de colisão) e reconstruído em `ReplicatedStorage.HACCreaturePreviews` (`Lumito:Normal` e `Lumito:Dourado`).
   - `CreatureFactory.luau` clona e escala `HACLumitoTemplate` (com fallback procedural compacto) aplicando as paletas Normal e Gold por `ColorRole`.
   - `LumitoAnimator` dá atuação rígida articulada ao modelo: respiração, passada com contato alternado, balanço de cabeça/orelhas/cauda/braços, piscada, reações de susto/cansaço/captura, gestos ociosos e saudação a jogador próximo na base. `Root` e `Corpo` permanecem autoritativos e não recebem o deslocamento visual.
   - Cada contato de pé emite um puff cartunesco ciano/branco em flipbook 2×2 (`rbxassetid://118477338697511`); corrida/pânico habilita um rastro ciano curto. O atlas-fonte está em `art/vfx/lumito-run-puff-flipbook-v01.png`.
   - O salvamento integral do lugar foi confirmado nesta entrega. Exportar cópia `.rbxl` recuperável ainda é pendente.
2. **Escala contínua de criaturas (`ac385ae`) e ajuste local pendente:**
   - Multiplicador individual oculto de `1×` a `5×` substituiu as classes Small/Normal/Large, com migração `0.85× → 1×`.
   - **Divergência local preservada sem commit:** `studio/shared/GameplayConfig.luau` (no checkout e no lugar salvo no Studio) contém o ajuste `BaseChance = 0.7, Curve = 12` (70% de chance para `1×` e cauda rara até `5×`). O salvamento integral desta entrega incluiu o ajuste; sua confirmação como regra versionada ainda depende do desenvolvedor.
3. **Sequência de caça (`be1bfaf`) e família de menus + reset (`90045a0`):**
   - Contorno contextual de mira, carga até MAX, trilha de voo/retorno, disputa em fases de 3,6 s (ganho-base `0,18/s`, limite `22 s`) e recompensa com retrato, XP imediato e potencial de ouro/s na base.
   - Menus `Creatures`, `Creature Market`, `Creature Index`, `Hunting Shop`, `Settings` com `MenuTheme`/`MenuKit`; a nova página `Hunter Rank` foi aplicada junto do protótipo.

## Próximos passos do desenvolvedor

1. Exportar cópia `.rbxl` recuperável do lugar salvo (`P0 · PROC-01`).
2. Decidir se confirma e commita o ajuste `BaseChance = 0.7, Curve = 12` em `GameplayConfig.luau` (`P1 · HAC-15`).
3. Executar [[04_Validacao/Playtest Atual]] em PC e celular (novo reset em duas contas, Hunter Rank/economia, sensação da caça, menus e avaliação visual/animação/VFX do Lumito v01 em campo, base e retratos).

Para continuidade por outro agente: ler `README.md`, `AGENTS.md` e o `bootstrap` de `context-manifest.json`; carregar os domínios da tarefa. O commit de código `42ca28a` está no GitHub, o lugar de teste foi salvo mas não publicado, e a alteração local de tamanho em `GameplayConfig.luau` mais `art/lumito-base-v01/` e `art/lumito-base-v02/` não pertencem a esse commit. Não usar resumos de chat como especificação vigente.
