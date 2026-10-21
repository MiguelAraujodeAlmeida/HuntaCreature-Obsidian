# Arquitetura atual

Referência: código enviado **ee6e901** (`main`, 54 fontes Luau). Ajuste local `BaseChance = 0.7, Curve = 12` em `studio/shared/GameplayConfig.luau` permanece preservado sem commit até decisão do desenvolvedor.

## 1. Mapa de responsabilidade

| Pasta no repositório | Destino no Roblox Studio | Papel |
|---|---|---|
| `studio/shared` (9) | `ReplicatedStorage.HACShared` | Configurações (`GameplayConfig`, `CaptureConfig`, `AudioConfig`), geometria (`LassoAim`, `LassoVisuals`) e estilo (`VisualStyle`, `MenuTheme`, `WorldStyle`) |
| `studio/server` (15) | `ServerScriptService.HACServer` | Autoridade de jogo, fábrica/IA de criaturas, captura, loja, base viva e persistência |
| `studio/client` (28) | `StarterPlayer.StarterPlayerScripts.HACClient` | Input, HUD, mira, menus (`MenuKit`, `*Page`), retratos e preferências locais |
| `studio/HuntACreature.server.luau` | `ServerScriptService.HuntACreature` | Bootstrap do servidor, loops de tick e roteamento de eventos |
| `studio/HuntACreature.client.luau` | `StarterPlayerScripts.HuntACreatureClient` | Bootstrap do cliente e recepção de snapshots |

| Domínio técnico | Módulos principais |
|---|---|
| Catálogo, economia e tamanhos | `GameplayConfig` |
| Modelo 3D, variantes e retratos de criatura | `CreatureFactory`, `CatalogPresentation`, `CreaturePortrait` + `ReplicatedStorage.HACLumitoTemplate` e `HACCreaturePreviews` |
| IA selvagem e passeio na base | `CreatureProfiles`, `CreatureBehaviorService`, `LumitoBehavior`, `BaseRoamingService` |
| Laço, colisão e disputa | `CaptureConfig`, `LassoAim`, `LassoCollision`, `LassoVisuals`, `LassoFeedback`, `CaptureService`, `CaptureController`, `CaptureHUD` |
| Perfil e DataStore | `ProfileData`, `ProfileService`, `PersistenceConfig` |
| Ferramentas e loja | `HuntingTools`, `ToolInventory`, `ToolPlacement`, `ToolPlacementPreview`, `ShopPage` |
| Mundo, treino e placas | `WorldPresentation`, `WorldStations`, `UpgradeBoards` |
| HUD, menus e áudio | `HUD`, `CollectionUI`, `MenuKit`, `GlossyButton`, `RewardPresentation`, `LocalPreferences`, `AudioFeedback` |

*Legado inativo:* `BuildWorld.luau`, `studio/archive` e `UpgradePage.luau` (sem rota ativa) são históricos; não executá-los nem reativá-los. `QuickSlot.luau` apenas reserva espaço invisível para a hotbar nativa.

## 2. Contrato do modelo 3D (`HACLumitoTemplate` e `CreatureFactory`)

- **Template no Studio (`ReplicatedStorage.HACLumitoTemplate`):** gerado a partir de `C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Art\Lumito\Lumito_Base_v01.blend` (33 `UnionOperation`s CSG com `UsePartColor = true` + `Root` + `Corpo`).
- **Pivô e contato com o chão:** `Root` (`PrimaryPart`, invisível) fica na origem `(0, 0, 0)` do template na escala `1.0`, com a base das solas em `Y = -1.625 * scale` (compatível com `RootHeight = 1.68` na ilha e `1.625` na base).
- **Colisão do laço (`Corpo`):** `Part` invisível (`Transparency = 1`, `CanCollide/CanTouch/CanQuery = false`, `CastShadow = false`) de tamanho `Vector3.new(3.3, 2.8, 2.6) * scale` centrada em `Root`, garantindo que `LassoCollision` mantenha o mesmo elipsoide de captura enquanto `LassoAim`/`Highlight` atingem as peças visíveis.
- **Paletas e animação:** cada peça possui o atributo `ColorRole` (`Main`, `Secondary`, `Accent`, `Ink`, `Glint`) colorido por `CreatureFactory` conforme variante (`Normal` ou `Golden`), e as peças dos pés (`Pe`, `Sole_*`, `Stud_Foot_*`) possuem `FootSide = "L" | "R"` para passo sincronizado em `LumitoBehavior`. Se `HACLumitoTemplate` não existir no lugar, `CreatureFactory` usa o fallback procedural compacto de 33 partes.

## 3. Contratos de autoridade e rede

- **Cliente envia intenções; servidor decide:** nenhum saldo, preço, captura ou posse vem do cliente. Servidor valida tipos, valores finitos (`finiteVector`), distância, dono, cooldown, estoque e capacidade. Rate limit: balde de `40` requisições com reposição de `20/s`.
- **Snapshots não destrutivos:** atualizações de renda (`1 s`) atualizam textos via `valueRefreshers` sem destruir seleção de menu, ordem do `Backpack` ou posição das criaturas na base.

## 4. Persistência e geração de save (`PersistenceConfig`)

- **Schema `1`** com migração aditiva (converte `size = 0.85` antigo para `1`). Lease de sessão de `180 s`, margem de `45 s` e autosave a cada `45 s`. Falha de leitura bloqueia sobreescrita para nunca zerar perfil existente.
- **Geração fixa atual:** `20261019_menu_reset_01` (DataStore Studio: `HAC_Profiles_Studio_20261019_menu_reset_01`; Publicado: `HAC_Profiles_20261019_menu_reset_01`; geração anterior `_v1` preservada intacta).
- `Workspace.HACStudioMemoryMode = true` usa memória volátil apenas no Studio; testes de persistência real exigem `nil`/`false`.
