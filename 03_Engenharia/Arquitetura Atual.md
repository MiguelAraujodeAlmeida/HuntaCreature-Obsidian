# Arquitetura atual

Referência: código **90045a0**, 53 fontes runtime. Este cofre registra arquitetura e contratos, não duplica os fontes.

## Mapa de responsabilidade

| Pasta do jogo | Destino no Studio | Domínio |
|---|---|---|
| studio/shared (9) | ReplicatedStorage.HACShared | Configurações, geometria e estilo |
| studio/server (15) | ServerScriptService.HACServer | Regras e persistência autoritativas |
| studio/client (27) | StarterPlayer.StarterPlayerScripts.HACClient | Input, apresentação e preferências locais |
| HuntACreature.server.luau | ServerScriptService.HuntACreature | Bootstrap e validação dos acessos |
| HuntACreature.client.luau | StarterPlayerScripts.HuntACreatureClient | Inicialização e snapshots |

| Alteração desejada | Fontes principais |
|---|---|
| Catálogo, renda, melhorias, ferramentas, força mínima | GameplayConfig |
| Laço e disputa | CaptureConfig, LassoAim, LassoCollision, CaptureService, CaptureController |
| IA selvagem | CreatureProfiles, CreatureBehaviorService, LumitoBehavior |
| Construção / retrato de criatura | CreatureFactory, CatalogPresentation, CreaturePortrait |
| Regras de perfil / transações | ProfileData; integração via ProfileService |
| Gravação / reset | ProfileService, PersistenceConfig |
| Ferramentas / posicionamento | HuntingTools, ToolInventory, ToolPlacement, ToolPlacementPreview |
| Base viva / mundo / placas | BaseRoamingService, WorldPresentation, WorldStations, UpgradeBoards |
| HUD / menus / preferências | HUD, CollectionUI, módulos de página, LocalPreferences |
| Aparência / som | VisualStyle, MenuTheme, MenuKit, GlossyButton, WorldStyle, AudioConfig, AudioFeedback |

Os nomes acima são módulos, salvo bootstraps explícitos. Consultar o arquivo no checkout antes de editar; não inferir uma API só pelo nome.

## Contratos que precisam sobreviver às refatorações

- Cliente envia intenções, nunca saldo, prêmio, preço ou posse final. Servidor valida tipos, valores finitos, distância, proprietário, contexto, cooldown e capacidades.
- Captura tem dono exclusivo, força mínima e entrega única; transações de coleção/venda/compra são autoritativas.
- Perfil é a única fonte de estado do jogador. Snapshots atualizam apresentação; renda passiva não deve destruir seleção, Tools ou posições dos visuais da base.
- Favorito, Settings e descobertas de variantes pertencem ao perfil; esconder visuais é somente preferência local.
- Eventos de rede devem ser conectados sem esperar indefinidamente por placas/inventário. UpgradeBoards descobre placas tardias e usa SurfaceGui no PlayerGui com Adornee; duas faces.
- Limite de pedidos atual: balde de 40 com reposição 20/s; isso complementa validação das ações, não a substitui.
- Separar parâmetros, regras, entrada e arte. Evitar expandir os bootstraps monolíticos ao criar um domínio.

## Persistência e reset excepcional

Schema atual 1; migrações aditivas preservam IDs internos. ProfileService usa lease de 180 s, margem de bloqueio de 45 s e autosave de 45 s. Falha de leitura **não** pode virar perfil novo gravado sobre o anterior.

Geração explícita em PersistenceConfig: **20261019_menu_reset_01**.

| Ambiente | Store desta versão |
|---|---|
| Studio | HAC_Profiles_Studio_20261019_menu_reset_01 |
| Publicado | HAC_Profiles_20261019_menu_reset_01 |

Stores anteriores: HAC_Profiles_Studio_v1 / HAC_Profiles_v1. Foram preservados; o reset não foi exclusão física. Não derivar a geração da data atual, de cada boot ou de cada login. Alterar novamente somente com pedido explícito de reset.

Workspace.HACStudioMemoryMode = true habilita memória temporária **apenas no Studio**. Nil/false usa DataStore. Verificações em memória não demonstram persistência. Um rollback precisa considerar código e geração juntos, sem fundir silenciosamente saldos de gerações diferentes.

## Versões, código e lugar

- Checkout atual: C:/Users/melg_/OneDrive/Documents/ChatGPT/Hunt A Creature.
- Branch local: codex/menu-system-reset; commit base anterior 4c381d9, entrega de menus 90045a0.
- Sincronização automática Studio/disco **não configurada/verificada**. Comparar antes de sobrescrever qualquer lado.
- O lugar contém modelos/Tools/propriedades não integralmente exportados. Salvar fontes no Git não salva o lugar; publicação e salvamento são operações distintas.
- BuildWorld.luau e studio/archive são históricos; não executar o construtor antigo sobre o cenário atual.
- UpgradePage não possui rota ativa e depende do antigo UI:Card removido. QuickSlot só reserva espaço invisível; inventário visível é nativo.
- Backup da última rodada: contexto/menus-2026-10-19 no checkout. Não disponível pelo clone deste cofre.

Uma máquina nova precisa do cofre **e** checkout correto **e** acesso ao lugar atual. Configurar remote do código, export do lugar e sync verificado continua pendente.
