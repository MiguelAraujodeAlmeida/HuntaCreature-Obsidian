# Estado atual

Revisão **CTX-2026-10-23-12** · 23/10/2026. Código canônico: `main` do [HuntACreature](https://github.com/MiguelAraujodeAlmeida/HuntACreature), commit `f528e6d`. O lugar de teste é **[Testing] Hunt a Creature** (`102310424634629`). O último código de gameplay aplicado no Studio corresponde a `37a01c9`; commits posteriores acrescentaram apenas arte e skills. Não há publicação nova confirmada.

## O que existe

- Fase jogável com **Lumito** como única espécie integrada. Caça com mira e arremesso livres, disputa de captura, variação `Gold`, escala individual `1×–5×`, bolsa/base, renda por segundo, treino AFK, upgrades, ferramentas, Index e Hunter Rank. Detalhes e números: [[01_Produto/Sistemas Atuais]].
- Lumito facetado e animado em `HACLumitoTemplate`; as demais criaturas modeladas **não** foram adicionadas ao jogo. Menus usam `MenuKit` e `MenuTheme`. Implementação e contratos: [[03_Engenharia/Arquitetura Atual]].
- Zonas de entrada abrem treino, Hunting Shop e Creature Market. Loja/mercado fecham ao sair da zona; treino fica fora da base, com quatro manequins evolutivos. A base ocupada mostra foto/nome do dono; base livre não tem texto.
- Três artes para revisão em `art/chicken-base-v01/`, `art/pug-base-v01/` e `art/lumito-ornate-v01/`, todas com Blender/FBX/pranchas. A aprovação visual está pendente. A skill `hac-creature-modeler` cria arte; `hac-creature-integrator` prepara integração jogável. Ambas estão no repositório do jogo e instaladas localmente por junction. Seus guias são consultados apenas ao usá-las.

## Estados e pendências que não podem ser confundidos

- **Studio:** a última aplicação de gameplay foi compilada em Edit. O desenvolvedor ainda não confirmou o salvamento integral dessa rodada. O assistente não aciona Save. Playtest humano e exportação `.rbxl` recuperável pendentes. Checklist: [[04_Validacao/Playtest Atual]].
- **Git local:** `studio/shared/GameplayConfig.luau` possui alteração não commitada `BaseChance = 0.7, Curve = 12`, já presente no lugar salvo de rodada anterior. `art/lumito-base-v01/` e `art/lumito-base-v02/` são pastas locais não rastreadas. Preservar esses dados e não presumir que existem em outro clone.
- **Arte:** nenhuma galinha, pug ou Lumito ornamentado está no Studio. Aprovação visual, animação e balanceamento dependem de revisão do desenvolvedor.
- **Próxima ação:** prioridades em [[02_Planejamento/Backlog]]. Feedback recente do desenvolvedor prevalece; verifique domínio e código para detalhes, sem usar o histórico como regra vigente.
