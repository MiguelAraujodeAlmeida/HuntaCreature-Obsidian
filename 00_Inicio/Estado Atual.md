# Estado atual

Revisão **CTX-2026-10-28-01** · 28/10/2026. Código canônico: `main` do [HuntACreature](https://github.com/MiguelAraujodeAlmeida/HuntACreature), commit `2855b50`. O lugar de teste é **[Testing] Hunt a Creature** (`102310424634629`). Há uma área isolada de comparação **Original × Rig** aplicada em Studio Edit; o Lumito jogável continua com o animador anterior. O lugar aguarda Save humano e playtest. Nenhum clipe foi publicado como asset permanente.

## O que existe

- Fase jogável com **Lumito** e **Chicken** comum (segunda espécie, pendente de playtest). Caça com mira e arremesso livres, disputa de captura, variação `Gold`, escala individual `1×–5×`, bolsa/base, renda por segundo, treino AFK, upgrades, ferramentas, Index e Hunter Rank. Detalhes e números: [[01_Produto/Sistemas Atuais]].
- Lumito e Chicken têm templates facetados e animadores próprios; Chicken usa `HACChickenTemplate` importado do FBX. Pug e Lumito ornamentado seguem apenas como arte. Menus usam `MenuKit` e `MenuTheme`. Implementação e contratos: [[03_Engenharia/Arquitetura Atual]].
- Zonas de entrada abrem treino, Hunting Shop e Creature Market. Loja/mercado têm receptor cliente e vínculo da janela à zona para fechamento ao sair, pendente de playtest; treino fica fora da base, com quatro manequins evolutivos. A base ocupada mostra foto/nome do dono; base livre não tem texto.
- Três fontes de arte em `art/chicken-base-v01/`, `art/pug-base-v01/` e `art/lumito-ornate-v01/`. Chicken foi integrada tecnicamente; sua aparência e atuação no jogo ainda dependem de revisão humana. A skill `hac-creature-modeler` cria arte; `hac-creature-integrator` prepara integração jogável. Ambas estão no repositório do jogo e instaladas localmente por junction. Seus guias são consultados apenas ao usá-las.

## Estados e pendências que não podem ser confundidos

- **Studio:** o comparativo temporário tem duas cópias do mesmo template, em pistas separadas. A cópia Rig usa Motor6D e oito clipes locais reproduzíveis; toda a crista segue a cabeça e as solas ficam acima da pista nas poses amostradas. Quatro scripts compilaram em Edit. Fluidez, contato durante o ciclo completo, visibilidade de outro cliente e desempenho ainda exigem Playtest. O desenvolvedor ainda não confirmou Save; o assistente não aciona Save. Checklist: [[04_Validacao/Playtest Atual]].
- **Git local:** `art/lumito-base-v01/` e `art/lumito-base-v02/` continuam pastas locais não rastreadas. Preservar esses dados e não presumir que existem em outro clone.
- **Arte:** Chicken está no Studio Edit, com FBX convertido em 25 MeshParts; Pug e Lumito ornamentado não foram integrados. Atuações revisadas, passada/aceleração e puff compartilhado ainda aguardam avaliação visual humana; balanceamento provisório aguarda playtest.
- **Migração de animação:** o Rig é somente demonstração no lugar de teste; não participa de caça, catálogo, base, economia ou saves. Os clipes usam IDs temporários de prévia por sessão do Studio; publicação e promoção para o jogo real dependem de avaliação posterior. A implementação vigente do Lumito permanece reversível.
- **Próxima ação:** prioridades em [[02_Planejamento/Backlog]]. Feedback recente do desenvolvedor prevalece; verifique domínio e código para detalhes, sem usar o histórico como regra vigente.
