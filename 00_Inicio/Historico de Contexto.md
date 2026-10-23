# Histórico de contexto e solicitações

Registro independente de IA/chat/dispositivo. **Não é especificação vigente**; consultar o manifesto para o presente. Novas entradas são acrescentadas; correções históricas devem indicar o que foi corrigido, sem apagar a mudança de direção.

## Convenções

- CTX-AAAA-MM-DD-NN identifica uma revisão de contexto; Git fornece o conteúdo exato.
- Entradas anteriores à consolidação foram reconstruídas de documentos e mensagens disponíveis. Quando não há rastreio, autoria/dispositivo/commit = **não registrado**; não inferir.
- Código, contexto, lugar salvo, aplicação e publicação são evidências diferentes.
- Aprovação humana deve conter feedback explícito e escopo; checks técnicos não a substituem.
- Modelo: [[05_Modelos/Registro de Solicitacao]].

## HIST-001 — Concepção e primeiro protótipo · data exata não registrada

**Pedido:** caça com laço, criaturas gerando recursos, base e evolução; referências em jogos de coleção/treino Roblox.
**Evolução:** feedback rejeitou HUD genérico, captura iniciada só por E, treino em esteira, criaturas imóveis e mapa pequeno com ponte. Direção passou a mira/carga livres, treino automático no manequim, base/mundo vivos, arte toy/studs e recompensas expressivas.
**Situação atual:** regras vigentes nos domínios; mapa amplo/teletransporte e arte final ainda adiados. IA, dispositivo e commit originais não registrados.

## HIST-002 — Revisões de HUD e laço · até 17/10/2026

**Pedido:** remover título permanente/tutorial excessivo; ícones reais, família glossy e fonte semelhante à referência; recursos proporcionais e carga central. Lançamento exato na mira sem gravidade, alcance real, tiro livre e contorno elegível.
**Resultado registrado:** HUD modular, áudio configurável, lançamento/colisão revisados e amostras de textura. Críticas de imprecisão/rigidez motivaram sucessivas correções.
**Limite:** não tratar primeira melhora visual como aprovação final. Artistas/modelos via IA foram discutidos como necessidade futura. Rastreamento individual das rodadas não disponível.

## HIST-003 — HUD/áudio e Lumito · 17/10/2026

**Resultado registrado:** revisão de responsividade/áudio; passeio, percepção, fuga, cansaço e pausas; colisão contínua relativa para alvo móvel e projétil a 100 studs/s.
**Evidência histórica:** nota de QA relata desktop/emulação e som de lançamento na versão daquela data; não valida a versão atual. Houve parecer inicial positivo sobre comportamento do Lumito, sem aprovação global.
**Regra posterior:** testes extensos/Play e subagentes passaram a exigir pedido explícito. Não repetir a antiga rotina automaticamente. IA/dispositivo/commit não registrados.

## HIST-004 — Base mecânica · 17–18/10/2026

**Pedido:** preparar sistemas extensíveis e persistência antes de expandir conteúdo.
**Resultado:** identidade individual, perfil versionado, capacidades/upgrades independentes, inventário, ferramentas, loja e descobertas; remoção gradual de regras espalhadas.
**Evidência registrada:** entrega com 31 fontes, 36 checks puros e 5 de UI; não era teste de DataStore real.
**Superado:** auditoria que dizia “persistência/loja/index ausentes” descrevia código anterior. IA/dispositivo/commit não registrados.

## HIST-005 — Loja, Index e recuperação entre dispositivos · 18/10/2026

**Pedido:** comparar referências e integrar oferta rotativa, progressão e coleção.
**Resultado:** estoque por rotação com cota pessoal, categorias e registro de descoberta. Comparação local/Studio recuperou versões divergentes (notas registram 34/37 fontes em momentos distintos).
**Limite:** pesquisa histórica não garante preços/regras atuais dos jogos externos. Rebirth e troca implícita sugeridos em documentos antigos não são decisões vigentes. Autoria/dispositivo não registrados.

## HIST-006 — Placas, gestão, renda e inventário · 18/10/2026

**Pedido:** remover redundâncias, upgrade em placa física, Creatures com Equip/Unequip, venda em loja física, Backpack nativo e renda por segundo.
**Decisão humana explícita:** acelerar renda **5×**, não manter o total antigo por minuto.
**Resultado:** acessos centralizados, troca implícita removida, Tools só possuídos, 42 fontes registrados na entrega. Recuperação de local antigo versus Studio recente precedeu aplicação; referência histórica de baseline 7b2649a.
**Pendente:** balanceamento dos preços e teste humano. Dispositivo/IA não registrados.

## HIST-007 — Placas vazias e interações · 18/10/2026

**Feedback:** placas pretas/sem clique e interações desaparecidas, inclusive treino e venda.
**Correção:** descoberta tardia das placas, texto nas duas faces, inicialização de eventos independente, prompts e acesso ao mercado/treino.
**Evidência:** cinco fontes iguais/compilados e 18 checks isolados em Edit; sem perfil gasto/DataStore real.
**Limite:** mouse/toque e ciclo completo ainda precisavam de reteste. Checklist atual incorpora essa regressão.

## CTX-2026-10-19-01 — Base, coleção e inglês · reconstruída

**Pedido:** criaturas livres na base, Settings, HUD menos genérico, inglês, loja Tools/Lassos, força mínima, Index por variantes e favoritos.
**Resultado:** implementado; 48 fontes/33 checks registrados. Código de referência 4c381d9.
**Limite:** IA/layout/som/reconexão aguardavam avaliação. Lumito continuou único catálogo. Autoria/dispositivo originais não registrados.

## CTX-2026-10-19-02 — Menus e reset global · reconstruída

**Pedido:** zerar progresso de todas as contas e refazer menus com referências de Index/Shop/Settings, mantendo padrão para telas futuras.
**Resultado:** MenuTheme/MenuKit/CreatureCards/ToolPortrait e cinco menus; reset por geração fixa 20261019_menu_reset_01, dados anteriores preservados. Commit de código **90045a0**.
**Evidência:** 53 fontes idênticos/compilados, 21 checks isolados, prévias em Edit inspecionadas e removidas. Sem Play iniciado, DataStore real ou publicação.
**Limite:** lugar integral não confirmado salvo; duas contas/reconexão e experiência aguardam teste. Entrega registrada nesta sessão Codex, computador Windows; modelo exato não registrado.

## CTX-2026-10-19-03 — Consolidação e GitHub · 19/10/2026

**Pedido:** limpar resíduos/contradições/repetições, tornar o cofre autossuficiente entre chats/máquinas, manter design/UI/UX, histórico independente de IA, GitHub e leitura integral inicial obrigatória; apresentar opções de redução de tokens.
**Resultado:** conjunto vigente reescrito por domínio, histórico único, manifesto com hashes/validador, referências visuais locais, processo de sincronização e instruções AGENTS no cofre e no checkout. Relatório de tokens separado como proposta.
**Correções de contexto:** Settings/Index deixaram de aparecer como futuro; esteira/swap/venda remota/5 s identificados como superados; namespaces de reset e limites de validação explicitados. Sem mudança de gameplay.
**Autor/ambiente:** Codex, Windows, workspace do projeto; sem agentes auxiliares. Modelo exato não registrado.
**Evidência:** validação estrutural e revisão de diff desta entrega; commit/estado remoto consultáveis pelo Git, sem SHA autorreferente nesta nota. Se o envio falhar, registrar pendência na entrega.
**Pendências do jogo:** permanecem em Estado Atual/Backlog; otimizações avançadas são propostas, não infraestrutura implementada.

## CTX-2026-10-19-04 — Código no GitHub e fluxo enxuto · 19/10/2026

**Pedido:** associar os fontes atuais ao repositório HuntACreature e eliminar comparações rotineiras Studio ↔ disco, avaliando desperdícios de tokens em todo o fluxo.
**Resultado:** o histórico local foi publicado como `main` em https://github.com/MiguelAraujodeAlmeida/HuntACreature. Git passa a ser a referência operacional dos fontes versionados. AGENTS, arquitetura, README e fluxo deixam de exigir varredura integral Studio/disco; o Studio permanece para aplicar/salvar o lugar e investigar divergência concreta.
**Otimizações aplicadas:** leitura incremental na mesma sessão, saída de ferramenta limitada a trechos/diffs, validações somente após entrega alterada e confirmação remota somente após push. A leitura completa do contexto em novo chat/dispositivo foi preservada por pedido explícito do desenvolvedor.
**Evidência:** repositório remoto vazio confirmado antes do envio; push de `main` e SHA remoto conferidos. Não houve exportação integral do lugar, mudança de gameplay, Play ou QA.
**Autor/ambiente:** Codex, Windows, workspace do projeto; sem agentes auxiliares. Modelo exato não registrado.

## CTX-2026-10-19-05 — Leitura de contexto por domínio · 19/10/2026

**Pedido:** reduzir a leitura inicial do Obsidian ao contexto básico e carregar arquivos adicionais somente quando a tarefa exigir — por exemplo, regras e referências visuais em trabalho de UI.
**Resultado:** o manifesto separa `bootstrap` de `domains`. Todo novo chat/dispositivo lê somente README, AGENTS e cinco notas-base; depois roteia a tarefa para gameplay, ui_ux, engineering, decisions ou validation. Histórico, modelos e relatório de tokens continuam sob consulta explícita.
**Evidência:** instruções no cofre, checkout e README técnico atualizadas; validador ajustado para essa estrutura. Sem mudança de gameplay, Studio ou Play.
**Autor/ambiente:** Codex, Windows, workspace do projeto; sem agentes auxiliares. Modelo exato não registrado.

## CTX-2026-10-20-01 — Polimento da caça · 20/10/2026

**Pedido:** tornar mira, carga, lançamento, acerto, disputa e vitória uma sequência curta, fluida e recompensadora, preservando laço reto/livre, parâmetros do Training Lasso, servidor autoritativo e UI compacta. Anexo de texto do desenvolvedor detalhou estados visuais, ritmo e recompensa.
**Resultado:** contorno contextual, carga até MAX, trilha de voo/retorno, distinção de obstáculo/alcance/contato recusado, hit confirm, reação do Lumito, fases previsíveis de resistência/abertura, poção contextual e vitória com retrato/Gold/Index/tamanho e potencial real de renda/XP na base. Ganho-base 0,18/s; limite 22 s e ritmo 3,6 s. Nenhuma alteração de alcance/velocidade/gravidade/assistência do laço.
**Evidência:** código `be1bfafb13c42787906157a77829f3eec961848a` enviado e SHA remoto conferido; 11 fontes aplicados e compilados estaticamente em Studio Edit no placeId 102310424634629; “Salvar na Roblox” acionado pela interface. Studio estava em Play antes da solicitação e foi encerrado para edição; nenhum novo Play, emulação ou benchmark iniciado. Sem publicação.
**Pendências:** playtest humano de precisão, ritmo, Gold/descoberta, som e PC/celular; DataStore/reconexão da entrega anterior; exportação .rbxl e restauração independente. Salvamento em nuvem e código Git não demonstram essas verificações.
**Autoria/ambiente:** Codex, Windows, Studio MCP e interface local; sem agentes auxiliares. Modelo exato não registrado.

## CTX-2026-10-20-02 — Briefing para agente Blender · 20/10/2026

**Pedido:** criar um prompt para outro agente conectar-se ao servidor MCP do Blender e receber as regras e referências visuais atuais do projeto.
**Resultado:** briefing textual entregue com leitura inicial enxuta do cofre, domínio `ui_ux`, direção toy/cartoon, coerência de materiais e silhuetas, distinção entre referências e arte aprovada, e inspeção inicial da cena sem alteração presumida.
**Evidência e limites:** prompt preparado; esta sessão não se conectou ao Blender, não editou cena, não modelou nem exportou assets. O agente executor deverá informar o estado real da conexão e aguardar um objeto concreto para modelar.
**Autoria/ambiente:** Codex, Windows; sem agentes auxiliares nesta sessão. Modelo exato não registrado.

## CTX-2026-10-20-03 — Prompt de redesign do Lumito · 20/10/2026

**Pedido:** formular um prompt completo para outro agente redesenhar o Lumito no Blender segundo as referências dos jogos e a direção visual própria do projeto.
**Resultado:** briefing de asset com identidade visual original, silhueta, expressão, estados de caça, variações de tamanho e Gold, uso do modelo no mundo e retratos, e critérios de integração com pivô/volume/partes animáveis.
**Evidência e limites:** inspeção dos documentos vigentes e de CreatureFactory, CreatureProfiles, GameplayConfig e CatalogPresentation; prompt textual entregue. Nenhum modelo, arquivo de arte ou código do jogo alterado nesta sessão.
**Autoria/ambiente:** Codex, Windows; sem agentes auxiliares. Modelo exato não registrado.

## CTX-2026-10-20-04 — Escala contínua e redesign restrito ao Lumito base · 20/10/2026

**Pedido:** substituir classes Small/Normal/Large por multiplicador oculto de 1× a 5×; após feedback de gigantes frequentes, tornar 1× muito mais comum e os tamanhos maiores progressivamente raros. Reformular o prompt de modelagem só para a aparência base, com mais detalhes e fidelidade à identidade ciano/arredondada da imagem anexada. Mutações ficam para depois no Studio.
**Resultado confirmado:** código `ac385aed7c62a8eb4c4e43f18c342363ca86fbe0` enviado para escala contínua; oito scripts aplicados/compilados em Studio Edit, limites e migração 0,85× → 1× verificados e status “Novas alterações salvas ... na Roblox” visto. A imagem do Lumito provisório foi copiada para as referências do cofre e a direção de arte vigente foi refinada.
**Pendente separado:** o ajuste adicional de raridade (`BaseChance = 0.7`, `Curve = 12`) foi aplicado no checkout local e no script em Studio Edit, com limites 1×/5× conferidos. O usuário interrompeu o controle da interface com Esc antes da confirmação de salvamento; esta parte está sem commit no repositório do jogo e sem salvamento do lugar comprovado. Não houve Play novo, publicação, modelagem ou integração do Lumito. Exemplares existentes preservam tamanho.
**Correção de registro:** CTX-2026-10-20-03 marcou um prompt como entregue, mas o turno correspondente foi interrompido antes da resposta final. O primeiro prompt efetivamente entregue foi mais curto e foi rejeitado pelo desenvolvedor; esta solicitação o substitui por instruções visuais concretas.
**Autoria/ambiente:** Codex, Windows, Studio MCP e interface local. Sem agentes auxiliares. Aprovação artística e avaliação no jogo pendentes.

## CTX-2026-10-20-05 — Estudo visual Steal an Egg · 20/10/2026

**Pedido:** estudar formato, textura, personalidade das criaturas e construção do mundo de Steal an Egg antes de escolher nova direção para Hunt A Creature; entregar relatório ao desenvolvedor para concordância ou correção.
**Resultado:** análise separada em observação e inferência em [[06_Referencias/Estudo visual Steal an Egg]], com links de imagens de divulgação, capturas de jogo e limitações das fontes. A proposta anterior de volumes lisos para Lumito foi retirada da posição de direção vigente; nenhuma nova forma específica foi aprovada.
**Evidência:** fontes visuais e comparação com a imagem do Lumito provisório na nota. Sem edição de Studio/Blender, Play, exportação ou teste. Estudo aguardando parecer humano; não altera regra de jogo.
**Autoria/ambiente:** Codex, Windows e pesquisa web; sem agentes auxiliares. Modelo exato não registrado.

## CTX-2026-10-20-06 — Regras visuais e novo prompt do Lumito · 20/10/2026

**Pedido:** adotar um padrão visual mais próximo dos princípios observados em Steal an Egg e preparar um novo prompt para redesign da aparência base do Lumito.
**Resultado:** regras de criatura e mundo atualizadas em [[01_Produto/Design UI UX]]; distinção mantida entre direção aprovada e modelo ainda sujeito a revisão. O estudo foi atualizado para refletir aprovação dos princípios gerais. Prompt de modelagem focado no Lumito base entregue no chat.
**Evidência/limites:** validação do cofre e commit Git. Nenhuma alteração de Studio, Blender, jogo ou asset; modelo aguarda geração e aprovação do desenvolvedor.
**Autoria/ambiente:** Codex, Windows, continuidade de contexto do projeto; sem agentes auxiliares. Modelo exato não registrado.

## CTX-2026-10-20-07 — Conexão dos MCPs de Blender e Studio · 20/10/2026

**Pedido:** conectar aos servidores MCP do Roblox Studio e Blender e seguir a leitura padrão das regras Markdown para criação de modelo 3D.
**Resultado:** conexões confirmadas; bootstrap do cofre, domínio `ui_ux`, decisões aplicáveis, modelo de registro e guias técnicos foram lidos. A regra operacional para o Lumito continua: somente aparência base, identidade ciano/arredondada preservada, silhueta e volumes toy/facetados, validação em ângulos/escala; mutações posteriores.
**Evidência/limites:** Studio conectado ao placeId 102310424634629 em Play, portanto sem mudança no lugar. Blender conectado à cena-padrão não salva (Cube/Camera/Light), sem criação, exportação ou modificação. O checkout do jogo possui alterações locais pré-existentes em `studio/shared/GameplayConfig.luau` e `art/`, preservadas sem inspeção ou edição.
**Autoria/ambiente:** Codex, Windows, Roblox Studio MCP e Blender MCP; sem agentes auxiliares. Nenhuma aprovação artística, modelo ou commit de código do jogo.

## CTX-2026-10-20-08 — Modelagem do Lumito base v01 e substituição funcional no Studio · 20/10/2026

**Pedido:** redesenhar a aparência base do Lumito em Blender segundo as regras visuais de `Design UI UX.md` e `Estudo visual Steal an Egg.md` e, em seguida, substituir completamente o modelo antigo do Lumito pelo novo de forma funcional.
**Resultado:** modelo `Lumito_Base_v01` criado e salvo em `C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Art\Lumito\Lumito_Base_v01.blend` (e `.fbx` + prancha de vistas), construído no Studio em `ReplicatedStorage.HACLumitoTemplate` (33 `UnionOperation`s CSG fiéis à geometria facetada do Blender + `Root` + `Corpo` invisível para colisão do laço) e integrado em `CreatureFactory.luau` (com fallback procedural compacto e suporte às paletas Normal e Dourado via `ColorRole`) e `LumitoBehavior.luau` (passo sincronizado de pé/sola/stud via `FootSide`). `ReplicatedStorage.HACCreaturePreviews` (`Lumito:Normal` e `Lumito:Dourado`) foi reconstruído no Studio Edit.
**Evidência/limites:** commit `ee6e901c99aa9855e5b84f1d8a87c3a05fe569a0` enviado para `main` no repositório de código; scripts `CreatureFactory` e `LumitoBehavior` atualizados e compilados em Studio Edit; prévia inspecionada por captura de tela em Edit e removida. Nenhum Play iniciado; salvamento do lugar na nuvem Roblox e aprovação estética final em playtest permanecem com o desenvolvedor.
**Autoria/ambiente:** Antigravity, Windows, Blender 5.4 (porta 9876) e Roblox Studio MCP; sem agentes auxiliares.

## CTX-2026-10-20-09 — Otimização integral do cofre Obsidian e remoção de contradições · 21/10/2026

**Pedido:** atualizar e otimizar o cofre Obsidian removendo repetições, contradições e informações desatualizadas, consolidando todas as mudanças recentes sem prejudicar o raciocínio do leitor.
**Resultado:** todas as notas de `bootstrap` e `domains` foram revisadas e enxugadas sem perda de regras ou links. Contradições corrigidas: remoção do texto residual em `Estado Atual` que dizia que Blender/Studio não tinham modelo criado; alinhamento do build de referência (`ee6e901`) em `Sistemas Atuais`, `Arquitetura Atual` e `Playtest Atual`; atualização de `ADR-009` em `Decisoes Vigentes` para refletir o modelo facetado `Lumito_Base_v01` em vez da descrição antiga; documentação do contrato técnico de `ReplicatedStorage.HACLumitoTemplate` (`ColorRole`, `FootSide`, `Corpo`) em `Arquitetura Atual`; e inclusão da captura em Studio (`assets/lumito-v01-studio-2026-10-20.jpg`) em `Referencias Visuais` e no manifesto. O volume da leitura inicial (`entrypoints` + `bootstrap`) caiu de 24.049 para 16.696 caracteres (~30,6% menor que a revisão anterior e ~89,6% menor que o acervo original).
**Evidência/limites:** validação determinística `python tools/check_context.py` sem erros e sincronização Git (`main`). Nenhuma alteração adicional de código ou Studio nesta etapa.
**Autoria/ambiente:** Antigravity, Windows; sem agentes auxiliares.

## CTX-2026-10-21-01 — Atuação e VFX cartunesco do Lumito · 21/10/2026

**Pedido:** dar vida ao novo Lumito facetado, que parecia rígido, e depois substituir a fumaça genérica de movimento por partículas cartunescas discretas inspiradas em uma prancha de nuvens de poeira, sem copiar seus desenhos.
**Resultado:** `LumitoAnimator` e `LumitoMotionConfig` passaram a compartilhar atuação entre ilha e base: respiração, passada proporcional a velocidade/escala, balanço de cabeça/orelhas/cauda/braços, piscada, susto, cansaço, resistência, gestos ociosos e saudação a jogador próximo. Cada contato de pé dispara um flipbook original 2×2 em ciano/branco com contorno teal; corrida/pânico habilita um rastro ciano curto. Atlas-fonte versionado em `art/vfx/lumito-run-puff-flipbook-v01.png` e publicado como `rbxassetid://118477338697511`.
**Evidência:** commit de código **2c74752a9759051b232d628798e5d6555ab0cc32** enviado e SHA remoto confirmado; quatro módulos aplicados no Studio Edit; compilação estática e verificação isolada de estados, flipbook, rastro e estabilidade de `Root`/`Corpo` passaram. O Studio encontrado em Play foi apenas encerrado; nenhum novo Play, emulação ou benchmark foi iniciado.
**Limites/pendências:** ritmo, intensidade, leitura em PC/celular e escalas `1×`/`5×` aguardam playtest humano. `game:SavePlace()` não está disponível no contexto Edit do conector e o controle nativo de janelas não estava exposto; portanto o salvamento integral do lugar continua sem confirmação. A alteração local anterior de `GameplayConfig.luau` e os diretórios de arte do Lumito foram preservados fora do commit.
**Autoria/ambiente:** Codex, Windows, Studio MCP e ImageGen integrado; sem agentes auxiliares. A imagem anexada foi tratada apenas como referência visual.

## CTX-2026-10-21-02 — Protótipo de Hunter Rank e reset autorizado · 21/10/2026

**Pedido:** implementar o rework de progressão acordado como protótipo ajustável, com liberdade para resetar o progresso de todos os jogadores para evitar migração.
**Resultado:** dez Hunter Ranks por XP total em curva crescente; XP imediato por captura e descoberta, XP passivo pequeno por criatura ativa na base, bônus de ouro/treino por rank, requisito opcional individual `RequiredHunterRank` para itens futuros e página de rank ligada ao Index. Ouro/preços iniciais preservados; novas espécies podem trazer XP/renda e preços extremos sem faixas rígidas de ferramenta. Namespace de save novo `20261021_hunter_rank_01` zera perfis quando a versão for executada, sem excluir dados anteriores. Ilhas não foram bloqueadas.
**Evidência:** commit de código **42ca28ae1133f7d63c1000c976cca2a3858ff62c** enviado e SHA remoto confirmado; 15 scripts aplicados/criados em Studio Edit, backup dos 13 substituídos em `ServerStorage.HACBeforeHunterRank20261021`; módulos centrais carregaram, verificações isoladas de XP/rank/bonificação/perfil passaram e a interface do Studio confirmou “Novas alterações salvas ... na Roblox”. Sessão Play preexistente foi encerrada após autorização do usuário; nenhum Play novo ou publicação. O ajuste local de tamanho em `GameplayConfig.luau` foi incluído no salvamento do lugar, mas preservado fora do commit; as pastas de arte não rastreadas também ficaram fora.
**Pendências:** playtest humano em PC/celular, reset e reconexão de duas contas no DataStore real, curva de ouro/XP com espécies futuras e exportação `.rbxl` recuperável. O reset ainda não atinge servidores públicos sem publicação explícita.
**Autoria/ambiente:** Codex, Windows, Studio MCP e interface local; sem agentes auxiliares.

## CTX-2026-10-21-03 — Resumo de continuidade para outro agente · 21/10/2026

**Pedido:** resumir o que foi combinado, o que já foi feito e o que falta, para continuidade por outro agente.
**Resultado:** estado e backlog conferidos contra os commits remotos; resumo de passagem registrado em [[00_Inicio/Estado Atual]]. Nenhuma regra ou script do jogo alterado.
**Evidência/limites:** código `42ca28ae1133f7d63c1000c976cca2a3858ff62c` e cofre `9036d0efb4c237027ee7fe1e1e8c8f366aad1a19` estavam sincronizados com `origin/main` na abertura desta solicitação. Lugar salvo, mas não publicado; validação humana de experiência, reset real e reconexão continuam pendentes. `GameplayConfig.luau` e duas pastas locais de arte permanecem fora do commit por escolha prévia.
**Autoria/ambiente:** Codex, Windows; leitura de Git/cofre, sem Studio, Play ou agentes auxiliares.

## CTX-2026-10-21-04 — Rework do Hunter Rank e sua apresentação · 21/10/2026

**Pedido:** concluir e refazer o protótipo de progressão discutido no chat compartilhado; tornar Hunter Rank visível, interessante e recompensador. Botão próprio semelhante ao da mochila, página com rank/progresso/próximo desbloqueio, silhuetas de ferramentas reais e missões apenas sinalizadas. Ocultar teto, limiares de XP, lista completa e textos supérfluos.
**Resultado:** `HunterRankHUD` ganhou botão glossy com emblema original, barra curta, brilho/partículas/som e celebração não bloqueante de rank; `HunterRankPage` apresenta o marco atual, percentual e benefícios do próximo. O Index deixou de servir como atalho duplicado; a caixa isolada de XP saiu do HUD. A página só desenha silhueta quando um item real tem `RequiredHunterRank`; missões permanecem `COMING SOON`, sem mecânica implementada. Captura passou a calcular XP base por tamanho/Gold e descoberta; pesquisa passiva deriva da espécie/variante equipada e continua menor que XP ativo. O servidor segue autoritativo. Namespace de save foi mantido.
**Evidência:** commit de código `977fbcea97d0071e45c8c3cdeae03bec9ed9b288` enviado a `origin/main` e SHA remoto conferido; 18 scripts alterados/carregados compilaram estaticamente em Studio Edit, com recompilação da correção final do HUD. O Studio confirmou “Novas alterações salvas ... na Roblox” após aplicação; atalho de salvamento acionado novamente após a correção final. Nenhum Play, benchmark ou publicação. Arte do emblema versionada e enviada ao Studio como `rbxassetid://94003376835794`.
**Pendências:** playtest humano em PC/celular, impacto visual e ritmo percebido, cálculo real em DataStore/reconexão, introdução futura de equipamentos com requisito e sistema de missões. `GameplayConfig.luau` mantém somente a alteração pré-existente de curva de tamanho fora do commit; duas pastas locais de arte do Lumito permanecem intocadas. Exportação `.rbxl` recuperável ainda pendente.
**Autoria/ambiente:** Codex, Windows, Studio MCP, ImageGen e interface local; sem agentes auxiliares.

## CTX-2026-10-21-05 — Botões Index e Settings · 21/10/2026

**Pedido:** redesenhar Index para acompanhar os botões de Mochila/Rank; tornar Configurações pequeno e discreto na topbar esquerda, como na imagem enviada.
**Resultado:** ícone original de bestiário azul/dourado gerado com ImageGen, salvo em `studio/assets/creature-index-book-v1.png` e enviado ao Roblox como `rbxassetid://112115433096189`. Index recebeu placa quadrada glossy; Settings recebeu variante circular escura de `GlossyButton` em `ScreenGui` próprio, posicionada por `GuiService.TopbarInset`. Layout lateral foi reorganizado e os dois botões passaram a fechar a janela ao segundo clique.
**Evidência/limite:** `VisualStyle`, `GlossyButton` e `HUD` aplicados/compilados em Studio Edit. O salvamento foi acionado, mas a verificação do status foi interrompida por Esc físico do desenvolvedor; nenhuma confirmação final de salvamento ou playtest. As mudanças entraram no commit de código `8c0da860df2821bda03ff441a1e6f925431d0b29`, SHA remoto confirmado. Sem publicação.
**Autoria/ambiente:** Codex, Windows, Studio MCP, ImageGen e interface local; sem agentes auxiliares.

## CTX-2026-10-21-06 — XP restante no Hunter Rank · 21/10/2026

**Pedido:** mostrar quanto XP falta para alcançar o próximo Hunter Rank.
**Resultado:** `HunterProgression.Progress` passou a retornar XP restante; `HunterRankPage` mostra o valor exato formatado com separadores de milhar, atualizado por snapshot, e preserva a porcentagem na barra. Custo total e lista de ranks continuam ocultos.
**Evidência/limite:** código incluído no mesmo commit `8c0da860df2821bda03ff441a1e6f925431d0b29` e SHA remoto confirmado; diff revisado. Na solicitação atual, `list_roblox_studios` retornou lista vazia duas vezes; a nova indicação de XP ainda não foi aplicada ao lugar nem compilada em Studio Edit. Play, publicação e teste humano não ocorreram. O ajuste local pré-existente de curva de tamanho e as pastas de arte do Lumito ficaram fora do commit.
**Autoria/ambiente:** Codex, Windows, checkout Git e cofre; sem agentes auxiliares.

## CTX-2026-10-22-01 — Boleio corrigido e salvamento reservado ao desenvolvedor · 22/10/2026

**Pedido:** preparar o arremesso com movimento cinematográfico de braço e pulso, não com um aro fixo girando acima da cabeça; manter corda flexível, ciclo enquanto segura, soltura em chicote e precisão anterior. O desenvolvedor proibiu o assistente de salvar o lugar pelo acesso ao computador.
**Resultado:** `LassoChargePresentation` foi separado de `LassoFeedback`; `LassoChargeStyle` define visual por laço. O Training Lasso inicia localmente e, após aceitação do servidor, a carga é vista pelos demais via atributos de início/fim no personagem. O braço direito/cotovelo/pulso e o tronco acompanham um pequeno boleio; a corda segmentada ondula em plano inclinado (`38°` inicial ajustável), movendo-se com a mão pela região superior e lateral. Entrada, destaque único em MAX, rastro curto, cancelamento e soltura cosmética têm transições. O servidor limpa o sinal em arremesso, cancelamento, troca, morte e timeout. Nenhum parâmetro de `LassoAim`, alcance, física ou locomoção foi modificado. A regra de salvamento humano foi registrada em `AGENTS.md`, [[03_Engenharia/Fluxo de Desenvolvimento]] e ADR-014.
**Evidência/limites:** commits de código `6beb403` e `a5e62ab` enviados, SHA remoto final `a5e62ab8f1e03111557cc55c6ab9b6f53b1b87cb` confirmado. Cinco módulos aplicados e compilados por `loadstring` em Studio Edit; a revisão final de estilo/apresentação também compilou. Sem Play, emulação, teste de animação real ou publicação. **Salvamento integral do lugar ainda depende do desenvolvedor**, assim como playtest visual, PC/celular e dois jogadores. A curva local de tamanhos em `GameplayConfig.luau` e as duas pastas de arte não rastreadas foram preservadas fora dos commits.
**Autoria/ambiente:** Codex, Windows, checkout Git e Roblox Studio MCP; sem agentes auxiliares.

## Proveniência do acervo anterior

Antes da consolidação: 44 notas Markdown, 161.139 caracteres, 167.066 bytes. Backup ZIP íntegro e cópia das pastas antigas preservados **fora do cofre ativo**, em `contexto/obsidian-2026-10-19/` no checkout do jogo desta máquina.

Esse arquivo legado não é necessário para entender as regras atuais e não foi publicado no repositório público. Uma máquina nova recebe o histórico consolidado acima; detalhes antigos não reconstruíveis são explicitamente desconhecidos. Não alegar que o Git novo contém versões históricas que nunca foram commitadas.

## CTX-2026-10-22-02 — braço erguido na preparação do laço

- Solicitação: corrigir novamente a pose rejeitada e entregar prompt completo para teste por outro agente.
- Autoria/ambiente: Codex, Windows local, Studio MCP no lugar 102310424634629.
- Resultado: ombro elevado (115°), cotovelo flexionado (65°), pulso pequeno; parâmetros por laço, conversão para eixos da articulação e restauração antes de Animator. Braço direito mistura para pose definida em vez de somar ao gesto de Tool. Reconhecimento também por membro conectado.
- Evidência: dois módulos aplicados/compilados em Edit; verificação matemática estática de elevação/conversão de eixos passou. Rig observado usa AnimationConstraint. Nenhum Play iniciado pelo assistente; o desenvolvedor encerrou seu teste para aplicação. Isso não comprova qualidade visual.
- Código: a086637b2f5b2260dd26f71526a6eeb4aa93f0ed enviado a main; prompt em studio/prompts/LASSO_ANIMATION_AGENT.md. Nenhum agente auxiliar executado.
- Pendências: aprovação visual, regressões manuais PC/celular/dois jogadores e salvamento pelo desenvolvedor. Soltura direcionada dos observadores permanece fora desta correção. Nenhum salvamento acionado ou publicação feita. Alterações locais de GameplayConfig e art preservadas.

- Encerramento em 23/10/2026: retomada solicitada pelo desenvolvedor; código remoto a086637 confirmado, verificador do cofre executado e sincronização desta revisão concluída. Sem nova aplicação no Studio ou confirmação de salvamento humano.

## CTX-2026-10-23-01 — progressão de ouro e localização de upgrades

- Solicitação: executar plano de curva inicial, bolsa crescente e compras separadas. Autoria: Codex no Windows local; lugar de teste 102310424634629.
- Resultado: custos e capacidades jogáveis revisados; projeção futura condicionada a novo conteúdo. Base, velocidade, treino e bolsa receberam pontos de compra distintos, com validação de servidor.
- Evidência: quatro scripts compilados em Studio Edit; atributos das três placas conferidos após atualização. Sem Play pelo assistente, sem aprovação de balanceamento.
- Estado: commit de código 7c9e9d8; save humano e playtest pendentes. Alteração preexistente na curva de tamanhos e pastas de arte locais preservadas, sem incluí-las no commit de código.

## CTX-2026-10-23-02 — treino AFK evolutivo

- Solicitação: treinar automaticamente com cena mais viva e quatro manequins de oficina visualmente distintos, preparando futuros níveis sem liberá-los. Autoria: Codex, Windows local; lugar de teste 102310424634629.
- Resultado: `TrainingDummies`, `TrainingPresentation`, atualização de `WorldPresentation` e atributos de ciclo/pagamento no servidor. Ganho e custo atuais preservados.
- Evidência: cinco scripts compilados/aplicados em Studio Edit; construção dos quatro níveis verificada sem Play. Código `da8ac180aa9f9414ef9453f4495ce2e2ed807100` enviado ao GitHub.
- Pendências: teste visual/funcional humano, salvamento do lugar pelo desenvolvedor e expansão econômica/visual futura. Alterações locais de tamanho/arte preservadas. Sem publicação.

## CTX-2026-10-23-03 — zonas de interação e bases

- Solicitação: substituir prompts por áreas de entrada no treino e lojas; remover TRAIN da placa, mover manequim para fora, retirar Totem/Free base e mostrar retrato/nome central do dono. Autoria: Codex, Windows local; lugar de teste 102310424634629.
- Resultado: zonas de entrada com trava de reativação, estações externas, identificação condicional. Código `5d3b37282c01f4e2802e13884700b52c46e1065a` enviado a main.
- Evidência: cinco scripts do Studio compilaram; no Edit, Totem ausente, estação fora e zonas Train/Sell com rótulo verificadas. ShopZone surge junto da loja em runtime; sem Play.
- Pendências: validar interação e layout em PC/celular, dois jogadores, save humano. Alteração local de GameplayConfig e arte preservadas.

## CTX-2026-10-23-04 — correção de escala e posição das zonas

- Solicitação: ampliar consideravelmente as áreas de interação, remover textos que flutuavam sobre elas, elevar nome/retrato do dono e colocar manequim/estação claramente ao lado e fora da base. Autoria: Codex, Windows local; lugar de teste 102310424634629.
- Resultado: zonas de treino, venda e loja com raio `4,5 studs` e sem `ZoneLabel`; detecção do servidor lê o raio da instância. Estação deslocada para `z = ±43,5`, apoiada em anexo provisório; marcador do dono elevado `6 studs` em relação à revisão anterior. Código `a6b138b38d02cc24679d638327d2aaed332f390d` enviado a `main`.
- Evidência: três fontes compilados/aplicados em Studio Edit; quatro estações em `z = ±43,5`, quatro marcadores elevados, quatro zonas de treino e zona de venda com raio `4,5`, sem `ZoneLabel`. Sem Play ou avaliação visual humana.
- Pendências: salvar o lugar pelo desenvolvedor; validar escala, leitura e interações em PC/celular; rever a composição final quando o hub definitivo existir. Alteração local de GameplayConfig e pastas de arte preservadas; sem publicação.

## CTX-2026-10-23-05 — fechamento ao sair da área

- Solicitação: janelas abertas por área de interação devem fechar ao sair, além do `X`. Autoria: Codex, Windows local; lugar de teste 102310424634629.
- Resultado: servidor sinaliza saída das zonas de Hunting Shop e Creature Market; cliente fecha apenas a página correspondente se ela ainda estiver visível. Reentrada continua necessária após fechamento manual dentro da zona. Código `37a01c9` enviado a `main`.
- Evidência: scripts de servidor e cliente compilados/aplicados em Studio Edit; `git diff --check` passou. Sem Play iniciado pelo assistente, nem teste funcional de movimento.
- Pendências: salvar o lugar pelo desenvolvedor; testar entrada, saída, `X`, troca de página, morte e dois jogadores em PC/celular. Ajuste local de GameplayConfig e arte preservados; sem publicação.

## CTX-2026-10-23-06 — conexão do MCP do Blender

- Solicitação: conectar ao MCP do Blender aberto no PC. Autoria/ambiente: Codex, Windows local, Blender MCP.
- Resultado: conexão confirmada por consulta não destrutiva de informações do arquivo aberto. A cena respondeu ao MCP; o arquivo está sem caminho, não salvo e sem alterações pendentes.
- Evidência/limites: nenhuma cena, objeto ou arquivo foi modificado; nenhuma operação de salvar, renderizar ou exportar foi acionada. O MCP permanece disponível para solicitações futuras de arte 3D.

## CTX-2026-10-23-07 — skill de modelagem de criaturas

- Solicitação: criar `hac-creature-modeler` a partir do guia e seis conceitos enviados, com entrega de arte para revisão e sem importação no Studio.
- Resultado: skill portável em `skills/hac-creature-modeler/` no repositório do jogo, instalada por junction local em `~/.codex/skills/hac-creature-modeler`; referência técnica, seis pranchas, kit de geometria/materiais/exportação e renderização de 12 vistas/escala. Convenções: `1 BU = 1 stud`, frente `-Y`, raiz no chão, `ColorRole`/`FootSide`; espécies preservam anatomia própria e usam studs discretos em 1–3 áreas.
- Evidência: `quick_validate.py` passou na cópia instalada; execução Blender 5.4 isolada construiu criatura sintética, gerou prancha/silhuetas/comparação com avatar e FBX, conferindo escala, eixos, metadados e composição visual. Commit de código `3ade45d67dd68bf089e83d00293765f0459afa43` enviado e SHA remoto confirmado. A cena Blender interativa e o lugar Roblox não foram alterados; nenhum Play ou Save acionado.
- Limites: validação do kit não aprova qualidade de uma criatura real. Modelo conceitual do Lumito no jogo permanece intacto. Artistas devem revisar cada entrega; a adaptação ao `Root`/colisão atual do Studio requer outra solicitação.
- Autoria/ambiente: Codex, Windows, Blender em processo separado, Git; sem agentes auxiliares. Alterações locais anteriores em `GameplayConfig.luau` e `art/lumito-base-v01/`/`v02/` preservadas fora do commit.
