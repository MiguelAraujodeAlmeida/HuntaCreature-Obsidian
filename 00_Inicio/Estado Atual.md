# Estado atual

Revisão de contexto **CTX-2026-10-21-01** · 21/10/2026.

## Entrega vigente do jogo

- **Código enviado:** commit **2c74752** (`main` em https://github.com/MiguelAraujodeAlmeida/HuntACreature).
- **Lugar de teste:** **[Testing] Hunt a Creature**, placeId **102310424634629** (Studio em modo `Edit`).
- **Não publicado:** servidores públicos continuam na versão anterior; publicação exige pedido explícito.

### O que está implementado e integrado

1. **Modelo e atuação do Lumito base v01 (`2c74752`):**
   - Modelado no Blender (`C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Art\Lumito\Lumito_Base_v01.blend` e `.fbx`) seguindo os princípios de [[06_Referencias/Estudo visual Steal an Egg]] e [[01_Produto/Design UI UX]].
   - Construído no Studio em `ReplicatedStorage.HACLumitoTemplate` (33 `UnionOperation`s CSG + `Root` + `Corpo` invisível de colisão) e reconstruído em `ReplicatedStorage.HACCreaturePreviews` (`Lumito:Normal` e `Lumito:Dourado`).
   - `CreatureFactory.luau` clona e escala `HACLumitoTemplate` (com fallback procedural compacto) aplicando as paletas Normal e Gold por `ColorRole`.
   - `LumitoAnimator` dá atuação rígida articulada ao modelo: respiração, passada com contato alternado, balanço de cabeça/orelhas/cauda/braços, piscada, reações de susto/cansaço/captura, gestos ociosos e saudação a jogador próximo na base. `Root` e `Corpo` permanecem autoritativos e não recebem o deslocamento visual.
   - Cada contato de pé emite um puff cartunesco ciano/branco em flipbook 2×2 (`rbxassetid://118477338697511`); corrida/pânico habilita um rastro ciano curto. O atlas-fonte está em `art/vfx/lumito-run-puff-flipbook-v01.png`.
   - **Pendente no Studio:** acionar salvamento do lugar (`Ctrl+S` / Salvar na Roblox) para persistir `HACLumitoTemplate` e `HACCreaturePreviews` na nuvem, além de exportar cópia `.rbxl` recuperável.
2. **Escala contínua de criaturas (`ac385ae`) e ajuste local pendente:**
   - Multiplicador individual oculto de `1×` a `5×` substituiu as classes Small/Normal/Large, com migração `0.85× → 1×`.
   - **Divergência local preservada sem commit:** `studio/shared/GameplayConfig.luau` (no checkout e no Studio Edit) contém o ajuste `BaseChance = 0.7, Curve = 12` (70% de chance para `1×` e cauda rara até `5×`), cuja confirmação de salvamento foi interrompida pelo usuário anteriormente.
3. **Sequência de caça (`be1bfaf`) e família de menus + reset (`90045a0`):**
   - Contorno contextual de mira, carga até MAX, trilha de voo/retorno, disputa em fases de 3,6 s (ganho-base `0,18/s`, limite `22 s`) e recompensa com retrato e ganho na base (`ouro/s` e `XP/s`).
   - Cinco menus (`Creatures`, `Creature Market`, `Creature Index`, `Hunting Shop`, `Settings`) com `MenuTheme`/`MenuKit` e geração fixa de save `20261019_menu_reset_01`.

## Próximos passos do desenvolvedor

1. Salvar o lugar no Roblox Studio e exportar cópia `.rbxl` recuperável (`P0 · PROC-01`).
2. Decidir se confirma e commita o ajuste `BaseChance = 0.7, Curve = 12` em `GameplayConfig.luau` (`P1 · HAC-15`).
3. Executar [[04_Validacao/Playtest Atual]] em PC e celular (persistência em duas contas, sensação da caça, menus e avaliação visual/animação/VFX do Lumito v01 em campo, base e retratos).
