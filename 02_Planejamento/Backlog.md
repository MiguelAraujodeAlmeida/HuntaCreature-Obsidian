# Backlog

**Implementado ≠ testado ≠ aprovado.** Nenhum item recebe aprovação de experiência ou arte apenas por verificações técnicas. Roteiro de validação humana: [[04_Validacao/Playtest Atual]].

## Agora

| Prioridade / ID | Próxima ação | Estado atual |
|---|---|---|
| P0 · STUDIO-SAVE | Desenvolvedor salva o lugar após as aplicações de Index/Settings/XP restante e boleio | Scripts aplicados/compilados em Edit; salvamento integral sem confirmação. Assistente não aciona Save |
| P0 · PROC-01 | Exportar `.rbxl` do lugar salvo e testar restauração | Salvamento de uma versão anterior confirmado em 21/10; rodada atual aguarda save humano. Exportação `.rbxl` pendente |
| P0 · HAC-12 / HAC-33 | Testar reset (`20261021_hunter_rank_01`) em duas contas e persistência após reconexão | Reset salvo na versão anterior; DataStore real e reconexão aguardam playtest |
| P0 · PROG-01 | Validar captura → XP → Hunter Rank 2, pesquisa baixa, bônus de ouro/treino, XP restante e celebração do Rank em PC/celular | Rework e XP restante aplicados em Studio Edit; save e teste humano pendentes |
| P0 · GOLD-01 | Testar Base/Bolsa/Treino/Eficiência/Velocidade em placas e menu, tempos de compra, bag cheia, reconexão e saves antigos | Código e Studio Edit atualizados; save e playtest humano pendentes |
| P1 · PROG-02 | Adicionar espécies, rendas, preços e ferramentas de tiers altos em curva de ouro/XP extrema, conforme conteúdo real | Estrutura flexível e dez ranks criados; catálogo futuro intencionalmente vazio, sem faixas rígidas de ferramentas |
| P1 · HAC-01A / HAC-09 / HAC-10 | Avaliar o Lumito v01 no jogo (silhueta, escala `1×`–`5×`, Gold, atuação, VFX de passada/corrida e retratos) | Modelo e animação/VFX integrados (`2c74752`); aguarda parecer humano sobre ritmo, intensidade e legibilidade em PC/celular |
| P1 · ART-01 | Usar `hac-creature-modeler` em um próximo conceito de espécie e obter revisão visual humana antes de integrar ao Studio | Skill e kit validados tecnicamente em criatura sintética isolada (`f728f3c`); galinha v01, pug v01 e Lumito ornamentado v01 entregues em art/, aguardando aprovação visual |
| P1 · HAC-15 | Confirmar commit da curva de tamanhos raros (`BaseChance = 0.7, Curve = 12`) | Aplicado no checkout local (`GameplayConfig.luau`) e incluído no salvamento integral do Studio; ainda fora do Git aguardando decisão humana |
| P1 · HAC-LASSO-BOLEIO | Avaliar preparação com braço/pulso, laço inclinado/flexível, soltura e visão por dois jogadores em PC/celular | Pose anterior rejeitada. Revisão `a086637` aplicada/compilada; validar mão elevada ao lado da cabeça, cotovelo flexionado e ausência de torção em três ângulos. Save e aprovação visual pendentes |
| P1 · HAC-03 / 03A / 04 / 02 | Avaliar sequência da caça em PC/celular: mira, carga, voo, disputa, poção, falha e vitória | Polimento `be1bfaf` e boleio `6beb403` em código; precisão, ritmo e áudio aguardam playtest humano |
| P1 · HAC-01 / HAC-32 | Avaliar família visual e interação dos seis menus | Implementados com `MenuKit`; Index/Settings refinados em `8c0da86`, save e parecer humano pendentes |
| P0 · INTERACT-01 | Testar entrada/saída em Train, Shop e Sell; fechamento de loja/venda ao sair, reentrada após `X`, preservação de outra página; avaliar raio, estação e nome do dono em PC/celular e duas contas | Correção `37a01c9` aplicada em Studio Edit; Play e save humano pendentes |
| P0 · TRAIN-01 | Avaliar em jogo os quatro manequins, ciclo de 2 s, recompensa, dois jogadores, PC/celular e restauração ao sair/pular/morrer | Código `da8ac18` e Studio Edit prontos; save e validação visual pendentes |
| P1 · TRAIN-02 | Acrescentar níveis visuais/econômicos futuros conforme novas espécies sustentem a renda | Estrutura extensível; conteúdo não liberado |
| P1 · HAC-13 / HAC-06 | Retestar placas de melhoria (duas faces) e início/saída do treino no manequim | Correção aplicada; teste de input real pendente |
| P1 · HAC-16 / 17 / 18 / 31 | Testar Equip/Unequip, venda no mercado físico e proteção de favoritos | Implementados; testar limites de capacidade e cancelamento |
| P1 · HAC-19 / 25 / 14 | Testar Index (Normal/Gold), loja rotativa (cota individual) e Settings | Implementados; validar em duas contas e reconexão |
| P2 · HAC-20 / 21 / 22 / 23 | Testar Backpack nativo, isca, armadilha e poção | Integrados; regressão de respawn e disputa pendente |
| P2 · HAC-05 / 11 / 24 / 28 / 29 / 30 | Avaliar legibilidade, mix de áudio, renda 5× (`1 s`) e força mínima | Regras implementadas; balanceamento de preços aguarda playtest |
| Contínua · HAC-26 / CTX-01 | Manter modularidade do código e cofre sincronizado | Revisão **CTX-2026-10-23-11**; skill de criaturas versionada/instalada, cena interativa do Blender inalterada |

## Depois da validação da base

| IDs | Tema | Situação |
|---|---|---|
| HAC-09M | Mutações visuais dedicadas no Studio (além da paleta Gold) | Adiado para depois da aprovação do Lumito base v01 |
| HAC-07 / HAC-08 | Teletransporte entre hub e ilha + mapa amplo | Direção desejada; ponte atual é provisória |
| EXP-01 | Segunda espécie, novos laços, biomas e eventos | Escopo futuro a especificar |
| HAC-27 | Interferência entre jogadores durante captura | Hipótese não implementada |
| PROC-02 / PROC-03 | Sincronização automatizada Studio ↔ Git e automações extras de contexto | Sem necessidade imediata; fluxo enxuto ativo |

## Ferramentas de produção

- `hac-creature-integrator` pronta estruturalmente; próxima solicitação de integração deve validar o fluxo real em uma espécie escolhida pelo desenvolvedor. Skill não implica aprovação das artes entregues.
