# Estado atual

Revisão de contexto **CTX-2026-10-23-02** · 23/10/2026.

## Entrega vigente do jogo

- **Código enviado:** commit **da8ac18** (`main` em https://github.com/MiguelAraujodeAlmeida/HuntACreature; SHA remoto confirmado).
- **Lugar de teste:** **[Testing] Hunt a Creature**, placeId **102310424634629**. A rodada de Index/Settings/XP restante e os cinco módulos do boleio do laço estão aplicados e compilados em Studio Edit. **Salvamento integral pendente de confirmação pelo desenvolvedor; o assistente não aciona Save.**
- **Não publicado:** servidores públicos continuam na versão anterior; publicação exige pedido explícito.

### Treino AFK evolutivo — 23/10/2026

`TrainingDummies` constrói quatro silhuetas de oficina por nível: Hay Scout, Wood Ranger, Iron Guard e Clockwork Champion. Melhorias de eficiência acrescentam equipamento à estação. `TrainingPresentation` apresenta o ciclo localmente para jogadores próximos, com boleio, corda, reação do manequim e +Strength no pagamento. `HuntACreature.server` continua autoritativo para 2 s e ganho; sinaliza início e pagamento por atributos. Cinco fontes aplicados/compilados em Studio Edit; construção dos quatro níveis verificada em árvore temporária. Sem Play, parecer visual ou save humano.

### Economia e upgrades — 23/10/2026

Curva inicial de ouro revisada no código: Base 3→4→5→6, Bolsa 3→5→9→16, treino e eficiência com custos crescentes; velocidade mantém números antigos. Bolsa é comprada em Creatures, Base tem placa exclusiva, velocidade ganhou placa própria e treino mantém placa com dois upgrades. Servidor valida placa/proximidade para Base, Velocidade e Treino, e compra Bolsa pelo menu. Quatro scripts compilados em Studio Edit e instâncias das placas atualizadas; save humano e playtest pendentes. Projeção até bilhões registrada em Sistemas Atuais, sem liberar níveis sem espécies que sustentem a renda. IDs de perfil preservados; nenhuma geração de save nova.

### O que está implementado e integrado

0. **Hunter Rank (`977fbce` + `8c0da86`):** dez limiares iniciais de XP acumulado; captura/descoberta principais, com bônus por tamanho/Gold, e pesquisa menor por criatura equipada. Bônus de ouro/treino por rank; `RequiredHunterRank` opcional por item, sem bloquear ilhas ou itens atuais. HUD tem botão/emblema/progresso próprios; a página revela rank atual, percentual, **XP restante exato**, próximo marco, benefícios e silhuetas de equipamento real quando aplicável. Missões futuras sinalizadas. Custo total, teto e lista de ranks não aparecem. Namespace `20261021_hunter_rank_01` preservado.
   - **Navegação visual (`8c0da86`):** Index tem ícone original e placa quadrada glossy; Settings é engrenagem circular discreta posicionada pela área livre da topbar. Os scripts e o XP restante foram aplicados/compilados em Studio Edit, com save integral ainda pendente.
   - **Boleio do laço (`a086637`, revisão de pose):** o Training Lasso prepara o arremesso com ombro/cotovelo/pulso, laço flexível inclinado que passa pela região da cabeça e desce pela lateral, aceleração durante `1,4 s`, giro estável ao atingir MAX, destaque único e gesto breve de soltura. Outros clientes acompanham início/fim aceitos pelo servidor, sem posições por quadro; mira, alcance, voo e movimento não mudaram. A pose anterior foi rejeitada pelo desenvolvedor. Revisão atual levanta o braço com ombro/cotovelo configuráveis, corrige os eixos e evita acúmulo/interferência da animação da Tool no braço direito. Aplicada e compilada em Edit; aparência ainda não aprovada. Save e playtest humano pendentes. Prompt alternativo: `studio/prompts/LASSO_ANIMATION_AGENT.md` no repositório de código.

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

1. **Desenvolvedor:** salvar o lugar no Studio e confirmar o salvamento. O assistente não aciona Save; até a confirmação, as aplicações de Index/Settings/XP restante e boleio são apenas o estado em Edit.
2. Exportar cópia `.rbxl` recuperável do lugar salvo (`P0 · PROC-01`).
3. Decidir se confirma e commita o ajuste `BaseChance = 0.7, Curve = 12` em `GameplayConfig.luau` (`P1 · HAC-15`).
4. Executar [[04_Validacao/Playtest Atual]] em PC e celular, incluindo boleio parcial/MAX, soltura/cancelamento, troca de ferramenta, morte e dois jogadores.

Para continuidade por outro agente: ler `README.md`, `AGENTS.md` e o `bootstrap` de `context-manifest.json`; carregar os domínios da tarefa. O código `da8ac18` está no GitHub; o lugar de teste recebeu os scripts em Edit e aguarda salvamento humano, sem publicação. A alteração local de tamanho em `GameplayConfig.luau` mais `art/lumito-base-v01/` e `art/lumito-base-v02/` não pertencem a esse commit. Não usar resumos de chat como especificação vigente.
