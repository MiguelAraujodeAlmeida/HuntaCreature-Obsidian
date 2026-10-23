# Backlog

**Implementado não significa testado nem aprovado.** Detalhes de mecânica e arte ficam nas notas donas; este arquivo guarda somente a próxima ação.

## Prioridade imediata

| ID | Próxima ação | Estado |
|---|---|---|
| STUDIO-SAVE / PROC-01 | Desenvolvedor confirma Save do lugar após a última aplicação e exporta `.rbxl` recuperável | Save e backup ainda sem confirmação; assistente não salva |
| VALID-01 | Playtest manual de caça, boleio, captura, treino, upgrades, zonas e menus em PC/celular, com duas contas e reconexão | Scripts aplicados/compilados em Edit; experiência não aprovada. Usar [[04_Validacao/Playtest Atual]] |
| ART-01 | Desenvolvedor avalia Lumito em jogo e as pranchas de galinha, pug e Lumito ornamentado | Artes novas só no Git; nenhuma integrada |
| HAC-15 | Resolver a alteração local da curva de tamanhos (`BaseChance = 0.7`, `Curve = 12`) sem perder o trabalho existente | Fora do Git; presente no checkout e no Studio salvo anteriormente |

## Próximas fatias de implementação

| ID | Próxima ação | Dependência |
|---|---|---|
| EXP-01 | Integrar segunda espécie com `hac-creature-integrator`, após escolha e raridade do desenvolvedor | Revisão da arte escolhida; primeira utilização da skill exige avaliação humana |
| PROG-02 | Ampliar espécies, rendas, ferramentas e níveis de treino conforme curva de ouro/XP | Conteúdo que sustente os preços, seguido de playtest |
| HAC-07/08 | Criar hub e ilha maiores com teletransporte | Direção/layout do mapa |
| HAC-09M | Criar mutações geométricas no Studio | Aprovação das espécies base |

## Manutenção contínua

Manter código modular e cofre sincronizado a cada solicitação. Não iniciar Play ou QA extenso por rotina; o desenvolvedor testa. Histórico de entregas e IDs antigos: [[00_Inicio/Historico de Contexto]].
