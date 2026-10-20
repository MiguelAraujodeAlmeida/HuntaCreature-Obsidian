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

## Proveniência do acervo anterior

Antes da consolidação: 44 notas Markdown, 161.139 caracteres, 167.066 bytes. Backup ZIP íntegro e cópia das pastas antigas preservados **fora do cofre ativo**, em `contexto/obsidian-2026-10-19/` no checkout do jogo desta máquina.

Esse arquivo legado não é necessário para entender as regras atuais e não foi publicado no repositório público. Uma máquina nova recebe o histórico consolidado acima; detalhes antigos não reconstruíveis são explicitamente desconhecidos. Não alegar que o Git novo contém versões históricas que nunca foram commitadas.
