# Backlog

**Implementado ≠ testado ≠ aprovado.** Nenhum item recebe aprovação de experiência ou arte apenas por verificações técnicas. Roteiro de validação humana: [[04_Validacao/Playtest Atual]].

## Agora

| Prioridade / ID | Próxima ação | Estado atual |
|---|---|---|
| P0 · PROC-01 | Exportar `.rbxl` do lugar salvo e testar restauração | Salvamento integral na Roblox confirmado em 21/10; exportação `.rbxl` pendente |
| P0 · HAC-12 / HAC-33 | Testar reset (`20261021_hunter_rank_01`) em duas contas e persistência após reconexão | Código aplicado e lugar salvo; DataStore real e reconexão aguardam playtest |
| P0 · PROG-01 | Validar captura → XP → Hunter Rank 2, XP passivo baixo, bônus de ouro/treino e rank visível em PC/celular | Protótipo em código (`42ca28a`) e Studio; verificações isoladas em Edit passaram, teste de experiência/economia humano pendente |
| P1 · PROG-02 | Adicionar espécies, rendas, preços e ferramentas de tiers altos em curva de ouro/XP extrema, conforme conteúdo real | Estrutura flexível e dez ranks criados; catálogo futuro intencionalmente vazio, sem faixas rígidas de ferramentas |
| P1 · HAC-01A / HAC-09 / HAC-10 | Avaliar o Lumito v01 no jogo (silhueta, escala `1×`–`5×`, Gold, atuação, VFX de passada/corrida e retratos) | Modelo e animação/VFX integrados (`2c74752`); aguarda parecer humano sobre ritmo, intensidade e legibilidade em PC/celular |
| P1 · HAC-15 | Confirmar commit da curva de tamanhos raros (`BaseChance = 0.7, Curve = 12`) | Aplicado no checkout local (`GameplayConfig.luau`) e incluído no salvamento integral do Studio; ainda fora do Git aguardando decisão humana |
| P1 · HAC-03 / 03A / 04 / 02 | Avaliar sequência da caça em PC/celular: mira, carga, voo, disputa, poção, falha e vitória | Polimento `be1bfaf` salvo; precisão, ritmo e áudio aguardam playtest humano |
| P1 · HAC-01 / HAC-32 | Avaliar família visual e interação dos seis menus | Implementados com `MenuKit` (incluindo Hunter Rank em `42ca28a`); parecer humano pendente |
| P1 · HAC-13 / HAC-06 | Retestar placas de melhoria (duas faces) e início/saída do treino no manequim | Correção aplicada; teste de input real pendente |
| P1 · HAC-16 / 17 / 18 / 31 | Testar Equip/Unequip, venda no mercado físico e proteção de favoritos | Implementados; testar limites de capacidade e cancelamento |
| P1 · HAC-19 / 25 / 14 | Testar Index (Normal/Gold), loja rotativa (cota individual) e Settings | Implementados; validar em duas contas e reconexão |
| P2 · HAC-20 / 21 / 22 / 23 | Testar Backpack nativo, isca, armadilha e poção | Integrados; regressão de respawn e disputa pendente |
| P2 · HAC-05 / 11 / 24 / 28 / 29 / 30 | Avaliar legibilidade, mix de áudio, renda 5× (`1 s`) e força mínima | Regras implementadas; balanceamento de preços aguarda playtest |
| Contínua · HAC-26 / CTX-01 | Manter modularidade do código e cofre sincronizado | Revisão **CTX-2026-10-21-03**; resumo de passagem registrado, sem alteração de jogo |

## Depois da validação da base

| IDs | Tema | Situação |
|---|---|---|
| HAC-09M | Mutações visuais dedicadas no Studio (além da paleta Gold) | Adiado para depois da aprovação do Lumito base v01 |
| HAC-07 / HAC-08 | Teletransporte entre hub e ilha + mapa amplo | Direção desejada; ponte atual é provisória |
| EXP-01 | Segunda espécie, novos laços, biomas e eventos | Escopo futuro a especificar |
| HAC-27 | Interferência entre jogadores durante captura | Hipótese não implementada |
| PROC-02 / PROC-03 | Sincronização automatizada Studio ↔ Git e automações extras de contexto | Sem necessidade imediata; fluxo enxuto ativo |
