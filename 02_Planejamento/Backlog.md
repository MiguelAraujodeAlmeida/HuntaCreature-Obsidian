# Backlog

**Implementado não significa testado nem aprovado.** Detalhes de mecânica e arte ficam nas notas donas; este arquivo guarda somente a próxima ação.

## Prioridade imediata

| ID | Próxima ação | Estado |
|---|---|---|
| STUDIO-SAVE / PROC-01 | Desenvolvedor confirma Save do lugar após a última aplicação e exporta `.rbxl` recuperável | Save e backup ainda sem confirmação; assistente não salva |
| VALID-01 | Playtest manual de caça, boleio, captura, treino, upgrades, zonas e menus em PC/celular, com duas contas e reconexão | Atuação Lumito/Chicken e receptor de saída da zona verificados em Edit; experiência não aprovada. Usar [[04_Validacao/Playtest Atual]] |
| ART-01 | Desenvolvedor avalia atuação Chicken e Lumito em jogo, além das pranchas de pug e Lumito ornamentado | Animadores revisados no Studio Edit; outras artes só no Git |

## Próximas fatias de implementação

| ID | Próxima ação | Dependência |
|---|---|---|
| EXP-01 | Playtest Lumito/Chicken: braços/asas, expressões, gestos, estados, velocidade, suavidade, puff, captura, base, retratos, Gold e persistência | Integração e polimento técnico feitos; Save e aprovação humana pendentes. Se a taxa visual ou juntas continuarem duras, planejar rig/clipes e apresentação cosmética local |
| ANIM-RIG-01 | Proposta para discussão: pilotar rig e clipes autorais no Lumito, preservando `Root`/`Corpo`, estados e modelo atual como fallback; criar pranchas de poses e integrar após revisão visual | Viabilidade avaliada, sem migração implementada ou decisão final. Chicken pode seguir quando o fluxo estiver validado |
| PROG-02 | Ampliar espécies, rendas, ferramentas e níveis de treino conforme curva de ouro/XP | Conteúdo que sustente os preços, seguido de playtest |
| HAC-07/08 | Criar hub e ilha maiores com teletransporte | Direção/layout do mapa |
| HAC-09M | Criar mutações geométricas no Studio | Aprovação das espécies base |

## Manutenção contínua

Manter código modular e cofre sincronizado a cada solicitação. Não iniciar Play ou QA extenso por rotina; o desenvolvedor testa. Histórico de entregas e IDs antigos: [[00_Inicio/Historico de Contexto]].
