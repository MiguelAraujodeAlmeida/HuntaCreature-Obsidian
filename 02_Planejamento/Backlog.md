# Backlog

**Implementado não significa testado nem aprovado.** Detalhes de mecânica e arte ficam nas notas donas; este arquivo guarda somente a próxima ação.

## Prioridade imediata

| ID | Próxima ação | Estado |
|---|---|---|
| STUDIO-SAVE / PROC-01 | Desenvolvedor confirma Save do lugar após a última aplicação e exporta `.rbxl` recuperável | Save e backup ainda sem confirmação; assistente não salva |
| VALID-01 | Playtest manual de caça, boleio, captura, treino, upgrades, zonas e menus em PC/celular, com duas contas e reconexão | Rigs jogáveis de Lumito e Chicken e receptor de saída da zona verificados em Edit; integrações ainda não aprovadas. Usar [[04_Validacao/Playtest Atual]] |
| ART-01 | Desenvolvedor avalia atuação Chicken e Lumito em jogo, além das pranchas de pug e Lumito ornamentado | Animadores revisados no Studio Edit; outras artes só no Git |

## Próximas fatias de implementação

| ID | Próxima ação | Dependência |
|---|---|---|
| EXP-01 | Playtest Lumito/Chicken: braços/asas, expressões, gestos, estados, velocidade, suavidade, puff, captura, base, retratos, Gold e persistência | Integração em Edit; Save e aprovação humana do jogo pendentes |
| ANIM-RIG-01 | Validar o Rig aplicado ao Lumito selvagem e na base: pés, crista, transições, captura, escala, Gold, dois clientes e custo; ajustar defeitos observados | Promovido após preferência humana no comparativo; não houve Play automático nem teste de rede/desempenho. O Original segue disponível como retorno seguro |
| ANIM-RIG-02 | Validar o Rig da Chicken: bicada, estranhamento, tropeço, asas, cauda, pés, captura, escala, Gold, dois clientes e custo; ajustar defeitos observados | Aplicado em Studio Edit e compilado; sem Play automático, teste de rede/desempenho ou Save. `ChickenAnimator` é retorno seguro |
| PROG-02 | Ampliar espécies, rendas, ferramentas e níveis de treino conforme curva de ouro/XP | Conteúdo que sustente os preços, seguido de playtest |
| HAC-07/08 | Desenvolvedor revisa a prévia v02 da Ilha Base; corrigir visual e então integrar cercados, treinos, lojas e viagem | Mar, seis cercados, seis treinos visuais, duas lojas e barco em `PreviewV02`; sem gameplay novo, Save ou Play. Menu e técnica de viagem abertos. [[01_Produto/Receita de Ilhas e Cenarios]] |
| HAC-09M | Criar mutações geométricas no Studio | Aprovação das espécies base |

## Manutenção contínua

Manter código modular e cofre sincronizado a cada solicitação. Não iniciar Play ou QA extenso por rotina; o desenvolvedor testa. Histórico de entregas e IDs antigos: [[00_Inicio/Historico de Contexto]].
