# Arquitetura atual

Referência: código enviado **a5e62ab** (`main`). Ajuste local `BaseChance = 0.7, Curve = 12` em `studio/shared/GameplayConfig.luau` permanece no lugar salvo anteriormente no Studio, mas fora do commit até decisão do desenvolvedor. A linha `ResearchXP = 1` do mesmo arquivo foi commitada separadamente. XP restante e boleio foram aplicados/compilados em Studio Edit; salvamento integral da rodada depende do desenvolvedor.

## 1. Mapa de responsabilidade

| Pasta no repositório | Destino no Roblox Studio | Papel |
|---|---|---|
| `studio/shared` (12) | `ReplicatedStorage.HACShared` | Configurações (`GameplayConfig`, `CaptureConfig`, `LassoChargeStyle`, `AudioConfig`, `LumitoMotionConfig`), geometria (`LassoAim`, `LassoVisuals`) e estilo (`VisualStyle`, `MenuTheme`, `WorldStyle`) |
| `studio/server` (16) | `ServerScriptService.HACServer` | Autoridade de jogo, fábrica/IA/animação de criaturas, captura, loja, base viva e persistência |
| `studio/client` (31) | `StarterPlayer.StarterPlayerScripts.HACClient` | Input, HUD, mira, boleio do laço, menus (`MenuKit`, `*Page`), retratos e preferências locais |
| `studio/HuntACreature.server.luau` | `ServerScriptService.HuntACreature` | Bootstrap do servidor, loops de tick e roteamento de eventos |
| `studio/HuntACreature.client.luau` | `StarterPlayerScripts.HuntACreatureClient` | Bootstrap do cliente e recepção de snapshots |

| Domínio técnico | Módulos principais |
|---|---|
| Catálogo, economia e tamanhos | `GameplayConfig`; `HunterProgression` concentra curva de XP, bônus e ritmo passivo |
| Modelo 3D, variantes e retratos de criatura | `CreatureFactory`, `CatalogPresentation`, `CreaturePortrait` + `ReplicatedStorage.HACLumitoTemplate` e `HACCreaturePreviews` |
| IA, atuação e passeio na base | `CreatureProfiles`, `CreatureBehaviorService`, `LumitoBehavior`, `LumitoAnimator`, `LumitoMotionConfig`, `BaseRoamingService` |
| Laço, colisão e disputa | `CaptureConfig`, `LassoChargeStyle`, `LassoAim`, `LassoCollision`, `LassoVisuals`, `LassoFeedback`, `LassoChargePresentation`, `CaptureService`, `CaptureController`, `CaptureHUD` |
| Perfil e DataStore | `ProfileData`, `ProfileService`, `PersistenceConfig` |
| Ferramentas e loja | `HuntingTools`, `ToolInventory`, `ToolPlacement`, `ToolPlacementPreview`, `ShopPage` |
| Mundo, treino e placas | `WorldPresentation`, `TrainingDummies`, `TrainingPresentation`, `WorldStations`, `UpgradeBoards` |
| HUD, menus e áudio | `HUD`, `HunterRankHUD`, `CollectionUI`, `HunterRankPage`, `MenuKit`, `GlossyButton`, `RewardPresentation`, `LocalPreferences`, `AudioFeedback` |

*Legado inativo:* `BuildWorld.luau`, `studio/archive` e `UpgradePage.luau` (sem rota ativa) são históricos; não executá-los nem reativá-los. `QuickSlot.luau` apenas reserva espaço invisível para a hotbar nativa.

## 2. Contrato do modelo 3D (`HACLumitoTemplate` e `CreatureFactory`)

- **Template no Studio (`ReplicatedStorage.HACLumitoTemplate`):** gerado a partir de `C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Art\Lumito\Lumito_Base_v01.blend` (33 `UnionOperation`s CSG com `UsePartColor = true` + `Root` + `Corpo`).
- **Pivô e contato com o chão:** `Root` (`PrimaryPart`, invisível) fica na origem `(0, 0, 0)` do template na escala `1.0`, com a base das solas em `Y = -1.625 * scale` (compatível com `RootHeight = 1.68` na ilha e `1.625` na base).
- **Colisão do laço (`Corpo`):** `Part` invisível (`Transparency = 1`, `CanCollide/CanTouch/CanQuery = false`, `CastShadow = false`) de tamanho `Vector3.new(3.3, 2.8, 2.6) * scale` centrada em `Root`, garantindo que `LassoCollision` mantenha o mesmo elipsoide de captura enquanto `LassoAim`/`Highlight` atingem as peças visíveis.
- **Paletas e animação:** cada peça possui o atributo `ColorRole` (`Main`, `Secondary`, `Accent`, `Ink`, `Glint`) colorido por `CreatureFactory` conforme variante (`Normal` ou `Golden`), e as peças dos pés (`Pe`, `Sole_*`, `Stud_Foot_*`) possuem `FootSide = "L" | "R"` para passo sincronizado em `LumitoBehavior`. Se `HACLumitoTemplate` não existir no lugar, `CreatureFactory` usa o fallback procedural compacto de 33 partes.
- **Apresentação rígida (`LumitoAnimator`):** captura os `CFrame`s de repouso e aplica poses absolutas por grupos nomeados, compartilhadas entre a IA selvagem e `BaseRoamingService`. Cria `StepPuff` com atlas 2×2 (`rbxassetid://118477338697511`) e `RunSwoosh`; o asset-fonte versionado está em `art/vfx/lumito-run-puff-flipbook-v01.png`. Nenhum efeito altera `Root`, `Corpo`, autoridade do servidor ou tamanho do indivíduo.

## 3. Contratos de autoridade e rede

- **Carga e boleio:** `CaptureController` inicia a apresentação local imediatamente; `CaptureService` valida `ChargeStart` e sinaliza `HACLassoCharging` + `HACLassoChargeStartedAt` no personagem para os demais clientes. Sinal limpo em arremesso, cancelamento, troca de laço, morte e timeout. `LassoChargePresentation` cria corda cosmética sem colisão, aplica pose aditiva em `AnimationConstraint`/`Motor6D` quando disponível e destrói os objetos ao encerrar. Nenhuma posição é enviada por quadro; `LassoAim` e o projétil autoritativo mantêm a trajetória original. Estilo ajustável por laço em `LassoChargeStyle`.

- **Cliente envia intenções; servidor decide:** nenhum saldo, preço, captura ou posse vem do cliente. Servidor valida tipos, valores finitos (`finiteVector`), distância, dono, cooldown, estoque e capacidade. Rate limit: balde de `40` requisições com reposição de `20/s`.
- **Snapshots não destrutivos:** atualizações de renda (`1 s`) atualizam textos via `valueRefreshers` sem destruir seleção de menu, ordem do `Backpack` ou posição das criaturas na base.
- **Progressão autoritativa:** `ProfileData.Capture` soma XP de captura/descoberta em transação; `HunterProgression` calcula o rank, XP de captura por espécie/tamanho/Gold e pesquisa por espécie/variante; `ProfileData.Action` valida `RequiredHunterRank` na compra. `HuntACreature.server` aplica bônus ao ouro/treino e pesquisa apenas com criatura equipada, e envia evento `HunterRankUp` quando o rank sobe. `goldCarry` e `strengthCarry` preservam frações. `HunterRank` é atributo/leaderstat de apresentação, não entrada do cliente nem campo independente de save.
- **Progresso apresentado:** `HunterProgression.Progress` também retorna o XP restante, sem transmitir o custo total como texto; `HunterRankPage` o formata e atualiza via `valueRefreshers`. `HUD` posiciona Settings num `ScreenGui` separado com `DeviceSafeInsets` e acompanha `GuiService.TopbarInset`.

## 4. Persistência e geração de save (`PersistenceConfig`)

- **Schema `1`** em uma nova geração limpa; lease de sessão de `180 s`, margem de `45 s` e autosave a cada `45 s`. Falha de leitura bloqueia sobreescrita para nunca zerar perfil existente.
- **Geração fixa atual:** `20261021_hunter_rank_01` (DataStore Studio: `HAC_Profiles_Studio_20261021_hunter_rank_01`; Publicado: `HAC_Profiles_20261021_hunter_rank_01` quando a versão for publicada). As gerações anteriores continuam intactas, sem exclusão física.
- `Workspace.HACStudioMemoryMode = true` usa memória volátil apenas no Studio; testes de persistência real exigem `nil`/`false`.

- **Treino AFK:** `HuntACreature.server` mantém ciclo e ganho autoritativos, publicando `Treinando`, `TrainingStartedAt`, `TrainingPulse` e `TrainingGain`. `WorldPresentation` fixa/restaura avatar; `TrainingDummies` define modelos por nível sem tocar na economia; `TrainingPresentation` cria a apresentação local, limpa poses/corda ao terminar e limita detalhe a 110 studs.

- **Zonas de entrada:** `WorldStations` constrói os indicadores; `HuntACreature.server` testa entrada a cada 0,15 s e guarda presença por jogador até saída. `WorldPresentation` cria a zona da loja após criar o balcão. A lógica de compra/venda e validações existentes permanecem no servidor. `WorldStations.Prepare` move treino, remove Totem e cria identificação da base antes da construção dos dummies.
