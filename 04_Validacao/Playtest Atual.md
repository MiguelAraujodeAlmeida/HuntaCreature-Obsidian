# Playtest atual

Build de referência: **2c74752**, lugar **102310424634629** (`[Testing] Hunt a Creature`). **Todos os itens abaixo aguardam validação humana.** O assistente não inicia Play/emulação sem pedido explícito. Estado da entrega: [[00_Inicio/Estado Atual]].

## 1. Reset e persistência (`P01`–`P04`)

- [ ] **P01 · Primeira entrada na geração `20261019_menu_reset_01`:** testar em duas contas que ouro/XP/força iniciam em `0`, coleção vazia, melhorias nível `1`, `Training Lasso` e `1` unidade de cada consumível.
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
- [ ] **A02 · Contorno contextual e colisão (`Corpo`):** contorno reflete distância, alinhamento e bloqueio; colisão contínua no novo Lumito v01 tem precisão natural sem capturar através de obstáculos.
- [ ] **A03 · Disputa (`3,6 s`) e recompensa:** avaliar ritmo das fases (normal, resistência, abertura), uso da poção sem cancelar captura e cartão final de vitória (`2,35 s`) exibindo taxas de `ouro/s` e `XP/s` na base.
- [ ] **A04 · IA selvagem:** passeio, pausa, detecção visual, fuga em pânico (`5 s`) e cansaço (`7 s`) respeitam as bordas da ilha sem travar em obstáculos.

## 4. Menus, loja, treino e preferências (`M01`–`M04`, `L01`–`L03`, `B01`–`B02`, `S01`)

- [ ] **M01 · Cinco menus (`MenuKit`):** abrir/fechar uma janela por vez, botão `X` acessível, seleção e rolagem estáveis durante os ticks de renda de `1 s`.
- [ ] **M02 · Responsividade PC e celular:** layout lateral (`>= 740 px`) e empilhado (`< 740 px`), botões confortáveis ao toque e textos legíveis em inglês.
- [ ] **L01 · Hunting Shop e cota individual:** duas contas veem a mesma rotação de `5 min`, mas a compra de uma não consome a cota da outra; cota persiste ao reconectar na mesma rotação.
- [ ] **L02 · Ferramentas e `Backpack` nativo:** apenas itens com estoque `> 0` aparecem; isca atrai, armadilha desacelera (`35%`) em solo válido e poção atua na disputa; respawn não duplica `Tools`.
- [ ] **B01 · Placas de melhoria e treino no manequim:** texto clicável nas duas faces apenas na própria base; treino prende avatar laçando o manequim a cada `2 s` e sair/morrer restaura o movimento.
- [ ] **S01 · Settings (`Sound` e `Base creatures`):** desligar som silencia efeitos locais; ocultar criaturas esconde modelos atuais e futuros nas bases sem parar a renda de `1 s`.

## Ordem sugerida de execução

Iniciar por **P01–P02**, **C01–C02**, **A01–A03** e **B01**. Ao registrar falha, anotar código do item, dispositivo, passos, esperado vs. observado e print/Output.
