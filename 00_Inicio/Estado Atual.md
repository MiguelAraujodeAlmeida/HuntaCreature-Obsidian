# Estado atual

Revisão **CTX-2026-10-28-02** · 28/10/2026. Código canônico: `main` do [HuntACreature](https://github.com/MiguelAraujodeAlmeida/HuntACreature), commit `f146eda`. O lugar de teste é **[Testing] Hunt a Creature** (`102310424634629`). Após o desenvolvedor preferir o Rig, ele foi aplicado ao Lumito jogável na ilha e na base em Studio Edit; o animador anterior permanece como retorno seguro. O lugar aguarda Save humano e playtest da integração.

## O que existe

- Fase jogável com **Lumito** e **Chicken** comum (segunda espécie, pendente de playtest). Caça com mira e arremesso livres, disputa de captura, variação `Gold`, escala individual `1×–5×`, bolsa/base, renda por segundo, treino AFK, upgrades, ferramentas, Index e Hunter Rank. Detalhes e números: [[01_Produto/Sistemas Atuais]].
- Lumito e Chicken têm templates facetados e animadores próprios; Chicken usa `HACChickenTemplate` importado do FBX. Pug e Lumito ornamentado seguem apenas como arte. Menus usam `MenuKit` e `MenuTheme`. Implementação e contratos: [[03_Engenharia/Arquitetura Atual]].
- Zonas de entrada abrem treino, Hunting Shop e Creature Market. Loja/mercado têm receptor cliente e vínculo da janela à zona para fechamento ao sair, pendente de playtest; treino fica fora da base, com quatro manequins evolutivos. A base ocupada mostra foto/nome do dono; base livre não tem texto.
- Três fontes de arte em `art/chicken-base-v01/`, `art/pug-base-v01/` e `art/lumito-ornate-v01/`. Chicken foi integrada tecnicamente; sua aparência e atuação no jogo ainda dependem de revisão humana. A skill `hac-creature-modeler` cria arte; `hac-creature-integrator` prepara integração jogável. Ambas estão no repositório do jogo e instaladas localmente por junction. Seus guias são consultados apenas ao usá-las.

## Estados e pendências que não podem ser confundidos

- **Studio:** o Lumito selvagem e o da base agora usam rig Motor6D com oito fontes de clipe versionadas. O servidor move `Root`/colisão, publica estado/velocidade e emite puff/rastro; cada cliente apresenta poses, gestos, olhar e piscada. O comparativo ficou desativado por padrão e sua arena foi removida do Edit. Scripts compilaram; clones 1× Normal, 3× Gold e base foram inspecionados em Edit, com crista ligada à cabeça e solas acima do piso. Fluidez, captura real, dois clientes e desempenho exigem Playtest. Save do lugar ainda sem confirmação; o assistente não aciona Save. Checklist: [[04_Validacao/Playtest Atual]].
- **Git local:** `art/lumito-base-v01/` e `art/lumito-base-v02/` continuam pastas locais não rastreadas. Preservar esses dados e não presumir que existem em outro clone.
- **Arte:** Chicken está no Studio Edit, com FBX convertido em 25 MeshParts; Pug e Lumito ornamentado não foram integrados. Atuações revisadas, passada/aceleração e puff compartilhado ainda aguardam avaliação visual humana; balanceamento provisório aguarda playtest.
- **Migração de animação:** a preferência humana pelo Rig no comparativo autorizou a integração. O reprodutor jogável usa as fontes de pose versionadas em runtime, sem depender dos IDs temporários de prévia e sem alterar saves/economia. A qualidade final da integração ainda não foi aprovada. `CreatureProfiles.Lumito.Animator` pode voltar a `LumitoAnimator` se necessário. A skill de integração foi atualizada para exigir rig/clipes reproduzíveis quando adequados à anatomia.
- **Próxima ação:** prioridades em [[02_Planejamento/Backlog]]. Feedback recente do desenvolvedor prevalece; verifique domínio e código para detalhes, sem usar o histórico como regra vigente.
