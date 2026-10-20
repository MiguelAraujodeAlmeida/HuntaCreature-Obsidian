# Instruções para qualquer IA ou colaborador

Este é o banco de contexto do Hunt A Creature. Política permanente solicitada pelo desenvolvedor em 19/10/2026; alterações de produto continuam revisáveis.

- Repositório: https://github.com/MiguelAraujodeAlmeida/HuntaCreature-Obsidian
- Cofre nesta máquina: `C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Hunt A Creature`.
- Em outra máquina, o diretório é a raiz deste clone. Não criar um segundo cofre silenciosamente.

## Primeira leitura / novo chat ou dispositivo

**Antes de editar qualquer domínio do projeto, absorver integralmente o contexto vigente:** ler README.md, estas instruções e todos os arquivos de `current` em `context-manifest.json`, na ordem declarada. Consultar as imagens indicadas ao trabalhar em visual. Não substituir essa leitura apenas por Estado Atual ou resumo de chat. Se algum arquivo estiver ausente/inacessível, explicitar a lacuna e não assumir uma versão antiga.

Histórico, modelos e relatórios estão classificados à parte. Não são especificação vigente; consultar quando a tarefa exigir proveniência, registrar trabalho ou avaliar propostas.

## Manutenção obrigatória em toda solicitação

1. Conferir estado Git e divergências; atualizar com segurança conforme [[03_Engenharia/Fluxo de Desenvolvimento]].
2. Confrontar pedido humano, documentação e implementação. Registrar divergências; não aplicar propostas antigas como ordens.
3. Atualizar a nota dona de cada regra alterada, Estado Atual e Backlog. Remover ou substituir afirmações superadas, sem duplicar conteúdo entre notas.
4. Acrescentar uma entrada em [[00_Inicio/Historico de Contexto]] com revisão, pedido, resultado, evidência, pendências e autoria/ambiente conhecidos. Nunca inventar aprovação ou teste.
5. Incrementar a revisão no manifesto; executar `python tools/check_context.py --refresh`, revisar o diff, depois `python tools/check_context.py`.
6. Commitar e sincronizar com GitHub. Confirmar o SHA remoto. Se offline ou sem permissão, registrar **sincronização pendente**, conservar o trabalho e informar a limitação; nunca declarar publicação sem evidência.
7. Na mesma sessão, reler somente o que mudou e os domínios afetados. Novo chat/dispositivo exige novamente toda a leitura vigente.

Não iniciar Play, emulação, benchmarks ou QA extenso nem usar agentes auxiliares sem pedido explícito. Revisões e verificações leves são permitidas. Ao alterar o jogo, comparar Studio/disco antes de sobrescrever e registrar o salvamento do lugar separadamente do commit de scripts. Não afirmar que o Git do cofre salva o jogo.
