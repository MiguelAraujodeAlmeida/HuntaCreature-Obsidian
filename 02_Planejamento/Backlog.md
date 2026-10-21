# Backlog

**Implementado ≠ testado ≠ aprovado.** Nenhum item recebe aprovação de experiência ou arte apenas por verificações técnicas. Roteiro de validação humana: [[04_Validacao/Playtest Atual]].

## Agora

| Prioridade / ID | Próxima ação | Estado atual |
|---|---|---|
| P0 · PROC-01 | Salvar lugar com `HACLumitoTemplate` na Roblox, exportar `.rbxl` e testar restauração | Mudanças de `ee6e901` aplicadas em Studio Edit; salvamento do lugar e exportação `.rbxl` pendentes |
| P0 · HAC-12 / HAC-33 | Testar reset (`20261019_menu_reset_01`) em duas contas e persistência após reconexão | Implementado (`90045a0`); DataStore real e reconexão aguardam playtest |
| P1 · HAC-01A / HAC-09 / HAC-10 | Avaliar o novo Lumito base v01 no jogo (silhueta, escala `1×`–`5×`, Gold, passeio e retratos) | Modelo v01 criado no Blender e substituído funcionalmente no Studio e código (`ee6e901`); aguarda parecer humano |
| P1 · HAC-15 | Confirmar commit e salvamento da curva de tamanhos raros (`BaseChance = 0.7, Curve = 12`) | Aplicado no checkout local (`GameplayConfig.luau`) e no Studio Edit; sem commit/save confirmado |
| P1 · HAC-03 / 03A / 04 / 02 | Avaliar sequência da caça em PC/celular: mira, carga, voo, disputa, poção, falha e vitória | Polimento `be1bfaf` salvo; precisão, ritmo e áudio aguardam playtest humano |
| P1 · HAC-01 / HAC-32 | Avaliar família visual e interação dos cinco menus | Implementados com `MenuKit` (`90045a0`); parecer humano pendente |
| P1 · HAC-13 / HAC-06 | Retestar placas de melhoria (duas faces) e início/saída do treino no manequim | Correção aplicada; teste de input real pendente |
| P1 · HAC-16 / 17 / 18 / 31 | Testar Equip/Unequip, venda no mercado físico e proteção de favoritos | Implementados; testar limites de capacidade e cancelamento |
| P1 · HAC-19 / 25 / 14 | Testar Index (Normal/Gold), loja rotativa (cota individual) e Settings | Implementados; validar em duas contas e reconexão |
| P2 · HAC-20 / 21 / 22 / 23 | Testar Backpack nativo, isca, armadilha e poção | Integrados; regressão de respawn e disputa pendente |
| P2 · HAC-05 / 11 / 24 / 28 / 29 / 30 | Avaliar legibilidade, mix de áudio, renda 5× (`1 s`) e força mínima | Regras implementadas; balanceamento de preços aguarda playtest |
| Contínua · HAC-26 / CTX-01 | Manter modularidade do código e cofre sincronizado | Revisão **CTX-2026-10-20-09** validada |

## Depois da validação da base

| IDs | Tema | Situação |
|---|---|---|
| HAC-09M | Mutações visuais dedicadas no Studio (além da paleta Gold) | Adiado para depois da aprovação do Lumito base v01 |
| HAC-07 / HAC-08 | Teletransporte entre hub e ilha + mapa amplo | Direção desejada; ponte atual é provisória |
| EXP-01 | Segunda espécie, novos laços, biomas e eventos | Escopo futuro a especificar |
| HAC-27 | Interferência entre jogadores durante captura | Hipótese não implementada |
| PROC-02 / PROC-03 | Sincronização automatizada Studio ↔ Git e automações extras de contexto | Sem necessidade imediata; fluxo enxuto ativo |
