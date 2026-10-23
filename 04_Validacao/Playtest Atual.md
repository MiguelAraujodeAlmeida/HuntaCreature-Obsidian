# Playtest atual

Build de código: **d15f63a**; lugar **102310424634629** (`[Testing] Hunt a Creature`). O polimento da Chicken e o fechamento de menus por saída da zona foram aplicados/compilados em Studio Edit; **o desenvolvedor ainda precisa salvar o lugar**. Todos os itens abaixo aguardam validação humana. O assistente não inicia Play/emulação sem pedido explícito. Estado da entrega: [[00_Inicio/Estado Atual]].

## 1. Reset e persistência (`P01`–`P04`)

- [ ] **P01 · Primeira entrada na geração `20261021_hunter_rank_01`:** testar em duas contas que ouro/XP/força iniciam em `0`, Hunter Rank `1`, coleção vazia, melhorias nível `1`, `Training Lasso` e `1` unidade de cada consumível.
- [ ] **P02 · Persistência em reconexão:** capturar, treinar, comprar melhoria, favoritar e alterar `Settings`; sair e reconectar confirmando que nada reseta novamente.
- [ ] **P03 · Modo de DataStore real:** confirmar que `Workspace.HACStudioMemoryMode` está desativado (`nil`/`false`) ao validar persistência no Studio.
- [ ] **P04 · Proteção contra sobreescrita:** verificar que falha ou bloqueio de sessão não grava perfil vazio sobre progresso existente.

## 2. Novo modelo Lumito v01, escala e base (`C01`–`C06`)

- [ ] **C01 · Leitura visual do `Lumito_Base_v01`:** avaliar silhueta facetada, testa saliente, orelha direita dobrada, crista dorsal com studs e expressão facial (Normal e Gold) na ilha, na base e nos retratos 3D.
- [ ] **C02 · Escala contínua (`1×` a `5×`), atuação e VFX:** conferir contato das solas, passo sincronizado de pé/sola/stud (`FootSide`), respiração, cabeça/orelhas/cauda/braços, piscada, gestos e saudação na base. Em caminhada, validar um puff discreto por contato; em fuga, puff reforçado e rastro curto, sem cobrir a silhueta. Repetir em `1×` e `5×`, PC/celular e diferentes ângulos; confirmar que `Identificacao` não invade as orelhas.
- [ ] **C03 · Passeio na base (`BaseRoamingService`):** criaturas equipadas caminham dentro da plataforma sem empurrar avatares; ticks de `1 s` de renda não reiniciam posição; gigantes sem espaço livre ficam visíveis e imóveis.
- [ ] **C04 · Equip/Unequip (`Creatures`):** move o indivíduo correto e bloqueia destino cheio sem trocar ou perder criaturas.
- [ ] **C05 · Favorito e venda no mercado físico (`Creature Market`):** favorito bloqueia venda; venda exige proximidade (`14 studs`) e confirmação, removendo apenas o exemplar escolhido e creditando ouro uma vez.
- [ ] **C06 · Descoberta permanente (`Creature Index`):** capturar Normal/Gold atualiza retrato colorido e filtros (`All`/`Normal`/`Gold`); itens não descobertos exibem silhueta escura do novo modelo v01; vender não apaga descoberta.

## 3. Caça, laço e IA (`A01`–`A04`)

- [ ] **A01 · Mira e arremesso reto:** tiro segue exatamente a direção escolhida sem arco; carga (`0%` a `100% MAX`) define alcance (`18` a `73 studs`); testar tiro livre para céu/chão/parede e trilha quente/retorno ciano.
- [ ] **A01B · Boleio durante a carga:** em PC e celular, observar de frente, lado e por trás: mão ao lado/acima da cabeça, cotovelo flexionado para fora, braço sem torções ou passagem pela cabeça. Confirmar que braço/pulso preparam o arremesso com laço flexível inclinado que passa por cima e pela lateral, sem aro parado sobre a cabeça. Comparar carga parcial, aceleração até MAX e giro constante depois de MAX; conferir destaque visual/sonoro único, rastro curto e alvo visível. Testar andando e pulando, soltura para pontos diferentes, cancelamento, troca de ferramenta, morte, timeout e visão de um segundo jogador. Verificar que todos os efeitos somem e que a direção/alcance do disparo continuam exatos.
- [ ] **A02 · Contorno contextual e colisão (`Corpo`):** contorno reflete distância, alinhamento e bloqueio; colisão contínua no novo Lumito v01 tem precisão natural sem capturar através de obstáculos.
- [ ] **A03 · Disputa (`3,6 s`) e recompensa:** avaliar ritmo das fases (normal, resistência, abertura), uso da poção sem cancelar captura e cartão final de vitória (`2,35 s`) exibindo XP imediato e potencial de `ouro/s` na base.
- [ ] **A04 · IA selvagem:** passeio, pausa, detecção visual, fuga em pânico (`5 s`) e cansaço (`7 s`) respeitam as bordas da ilha sem travar em obstáculos.

## 4. Hunter Rank e economia (`R01`–`R05`)

- [ ] **R01 · XP de captura:** primeira captura de Lumito Normal `1×` paga `100 XP` e leva ao rank 2; repetição `1×` paga `25 XP`; primeira variante Gold `1×` já descoberta paga `73 XP`. Tamanho maior aumenta apenas a parcela base; conferir o XP anunciado com o crédito real.
- [ ] **R02 · Pesquisa da base:** Lumito Normal equipado paga `1 XP/10 s` no rank 1; Gold paga `2 XP/10 s`; o bônus global acrescenta `1 XP` por rank acima de 1 quando há criatura ativa. Bolsa e base vazia não geram pesquisa. Equipar/dessequipar não deve adiantar o ciclo.
- [ ] **R03 · Bônus:** no rank 2, ouro da base e venda têm `+5%` com resíduos acumulados; treino tem `+3%` sem perder frações após reconexão. Nenhum rank barra acesso à ilha.
- [ ] **R04 · Interface:** botão próprio de Rank na HUD abre/fecha a página; barra/percentual, XP restante exato e próximo rank atualizam; não aparecem custo total, teto nem lista completa. Conferir benefício seguinte, missões `COMING SOON`, silhueta somente quando houver item real bloqueado, celebração não bloqueante e leitura em PC/celular.
- [ ] **R05 · Loja:** todos os itens atuais continuam compráveis no rank 1; para um futuro item com `RequiredHunterRank`, cliente informa requisito e servidor bloqueia a compra abaixo do rank. Validar também saldo, estoque, proximidade e cota.

## 5. Menus, loja, treino e preferências (`M01`–`M04`, `L01`–`L03`, `B01`–`B02`, `S01`)

- [ ] **M01 · Seis menus (`MenuKit`):** incluir `Hunter Rank`; abrir/fechar uma janela por vez, botão `X` acessível, seleção e rolagem estáveis durante os ticks de renda de `1 s`. Index quadrado e Settings circular na topbar devem responder a clique/toque sem sobrepor controles nativos em PC/celular.
- [ ] **M02 · Responsividade PC e celular:** layout lateral (`>= 740 px`) e empilhado (`< 740 px`), botões confortáveis ao toque e textos legíveis em inglês.
- [ ] **L01 · Hunting Shop e cota individual:** duas contas veem a mesma rotação de `5 min`, mas a compra de uma não consome a cota da outra; cota persiste ao reconectar na mesma rotação.
- [ ] **L02 · Ferramentas e `Backpack` nativo:** apenas itens com estoque `> 0` aparecem; isca atrai, armadilha desacelera (`35%`) em solo válido e poção atua na disputa; respawn não duplica `Tools`.
- [ ] **B01 · Placas de melhoria e treino no manequim:** texto clicável nas duas faces apenas na própria base; treino prende avatar laçando o manequim a cada `2 s` e sair/morrer restaura o movimento.
- [ ] **S01 · Settings (`Sound` e `Base creatures`):** desligar som silencia efeitos locais; ocultar criaturas esconde modelos atuais e futuros nas bases sem parar a renda de `1 s`.

## Ordem sugerida de execução

Iniciar por **P01–P02**, **C01–C02**, **A01–A03** e **B01**. Ao registrar falha, anotar código do item, dispositivo, passos, esperado vs. observado e print/Output.

## Economia e upgrades (GOLD-01)

- [ ] Conferir placa Base com apenas expansão, placa própria de Speed e placa de treino com duas opções.
- [ ] Abrir Creatures com bolsa vazia e cheia; comprar 3→5→9→16, observar atualização imediata e MAX.
- [ ] Comprar Base, Training, Efficiency e Speed; conferir custo, saldo, próximo benefício e resposta visual.
- [ ] Tentar compras sem ouro, no nível máximo e longe de cada placa; compra da bolsa pelo menu deve funcionar sem proximidade.
- [ ] Verificar captura com bolsa cheia, equipar/desequipar e progresso antigo após reconectar. Medir tempos dos primeiros níveis com 1–6 ouro/s.

## Treino AFK evolutivo (TRAIN-01)

- [ ] Em quatro níveis, comparar silhueta, cor, peças, reação e estação; subir eficiência separadamente e verificar acessórios.
- [ ] Assistir a vários minutos de ciclos de 2 s; conferir gesto do avatar, corda, impacto, recuperação e variação sem efeitos cansativos.
- [ ] Confirmar ganho real, `+Strength` e som no pagamento, sem pagamentos extras nem perda de frações.
- [ ] Testar dois jogadores, PC/celular, saída, pulo, morte, respawn e troca de manequim durante treino; poses/corda desaparecem.

## Zonas de interação (INTERACT-01)

- [ ] Entrar nas zonas de treino, loja e venda por direções diferentes; confirmar raio amplo (`4,5 studs`) e disparo único sem tecla ou prompt nativo.
- [ ] Loja e mercado abrem ao entrar e fecham automaticamente ao sair, inclusive ao morrer ou sair durante interação. Fechar pelo `X` dentro da área não reabre até sair e retornar. Abrir outra página e depois sair da área não deve fechá-la. Conferir PC/celular e dois jogadores.
- [ ] Treino na própria base inicia pela zona; entrar na estação de outra base não inicia; sair pelo controle de treino restaura movimento. Confirmar que nenhum texto flutua acima ou fora da área.
- [ ] Placa de treino não tem botão TRAIN; melhorias continuam clicáveis. Manequim/estação estão claramente ao lado da base, sobre piso próprio, sem cortar borda do hub.
- [ ] Base vazia sem nome/placa; ocupada com retrato e nome central acima das criaturas, sem sobreposição. Sair/desconectar limpa identificação, nova posse troca retrato.

## Chicken Base v01 (EXP-01)

- [ ] Confirmar Chicken comum em `Ponto4` após iniciar e em cada respawn, com os outros três pontos ainda ocupados por Lumito; Normal e Gold têm cor/silhueta próprias.
- [ ] Observar frente, perfil e três quartos: pés tocam o chão sem deslizar, cabeça bica e inclina, asas e cauda acompanham; pausas e gestos variam entre indivíduos. Conferir passeio, alerta, fuga, cansaço e resistência ao laço.
- [ ] Comparar passeio (`2,8 studs/s`), fuga (`9 studs/s`) e base (`1,65 studs/s`): arrancada/frenagem e curvas suaves, passada acompanhando deslocamento, salto atrapalhado e susto ocasionais sem tremor. Puff igual ao Lumito alterna junto aos pés só quando caminha/corre; nenhuma fumaça parada ou na captura.
- [ ] Mirar e capturar a Chicken; bolsa cheia e força mínima, vitória, XP, nome e retrato corretos. Conferir Index antes/depois, silhuetas, favoritos, venda protegida e equipar/desequipar.
- [ ] Na base, verificar passeio, saudação ocasional, renda provisória de 1 ouro/s em 1× Normal, ocultar criaturas sem interromper renda e reconectar sem perder o indivíduo.
- [ ] Testar tamanhos 1× e grandes, Gold, PC/celular, dois jogadores, som desligado e regressão do Lumito. Anotar clips/prints de animações estranhas para polimento.
