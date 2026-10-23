# Estado atual

Revisão **CTX-2026-10-23-13** · 23/10/2026. Código canônico: `main` do [HuntACreature](https://github.com/MiguelAraujodeAlmeida/HuntACreature), commit `ab96be0`. O lugar de teste é **[Testing] Hunt a Creature** (`102310424634629`). A integração da Chicken foi aplicada ao Studio Edit nesta rodada; o lugar ainda aguarda Save humano. Não há publicação nova confirmada.

## O que existe

- Fase jogável com **Lumito** e **Chicken** comum (segunda espécie, pendente de playtest). Caça com mira e arremesso livres, disputa de captura, variação `Gold`, escala individual `1×–5×`, bolsa/base, renda por segundo, treino AFK, upgrades, ferramentas, Index e Hunter Rank. Detalhes e números: [[01_Produto/Sistemas Atuais]].
- Lumito e Chicken têm templates facetados e animadores próprios; Chicken usa `HACChickenTemplate` importado do FBX. Pug e Lumito ornamentado seguem apenas como arte. Menus usam `MenuKit` e `MenuTheme`. Implementação e contratos: [[03_Engenharia/Arquitetura Atual]].
- Zonas de entrada abrem treino, Hunting Shop e Creature Market. Loja/mercado fecham ao sair da zona; treino fica fora da base, com quatro manequins evolutivos. A base ocupada mostra foto/nome do dono; base livre não tem texto.
- Três fontes de arte em `art/chicken-base-v01/`, `art/pug-base-v01/` e `art/lumito-ornate-v01/`. Chicken foi integrada tecnicamente; sua aparência e atuação no jogo ainda dependem de revisão humana. A skill `hac-creature-modeler` cria arte; `hac-creature-integrator` prepara integração jogável. Ambas estão no repositório do jogo e instaladas localmente por junction. Seus guias são consultados apenas ao usá-las.

## Estados e pendências que não podem ser confundidos

- **Studio:** a Chicken foi aplicada e seus módulos foram carregados em Edit; o desenvolvedor ainda não confirmou o salvamento integral do lugar. O assistente não aciona Save. Playtest humano e exportação `.rbxl` recuperável pendentes. Checklist: [[04_Validacao/Playtest Atual]].
- **Git local:** a curva local prévia `BaseChance = 0.7, Curve = 12` foi reconciliada no commit `ab96be0`. `art/lumito-base-v01/` e `art/lumito-base-v02/` continuam pastas locais não rastreadas. Preservar esses dados e não presumir que existem em outro clone.
- **Arte:** Chicken está no Studio Edit, com FBX convertido em 25 MeshParts; Pug e Lumito ornamentado não foram integrados. A atuação da Chicken e o balanceamento provisório aguardam playtest.
- **Próxima ação:** prioridades em [[02_Planejamento/Backlog]]. Feedback recente do desenvolvedor prevalece; verifique domínio e código para detalhes, sem usar o histórico como regra vigente.
