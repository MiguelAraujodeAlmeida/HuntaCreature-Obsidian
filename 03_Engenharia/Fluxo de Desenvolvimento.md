# Fluxo de desenvolvimento e manutenção do contexto

Política permanente do projeto. Toda IA, chat ou dispositivo deve segui-la; alterações exigem pedido explícito do desenvolvedor.

## 1. Sincronizar antes de editar

- **Repositório de contexto:** https://github.com/MiguelAraujodeAlmeida/HuntaCreature-Obsidian (`main`).
- **Repositório de código:** https://github.com/MiguelAraujodeAlmeida/HuntACreature (`main`).
- Conferir `git status --short --branch` e `git fetch origin`. Com árvore limpa, usar `git pull --ff-only`.
- **Proibido:** `reset --hard`, `clean`, `push --force` ou descartar mudanças locais sem ordem explícita. Se houver modificações locais pré-existentes (como `GameplayConfig.luau`), preservá-las intactas.
- Evitar rodar Git simultaneamente em duas máquinas sobre pastas sincronizadas pelo OneDrive.

## 2. Implementar uma fatia por vez

- Trabalhar a partir do código no Git e aplicar no Studio Edit quando a tarefa envolver o jogo.
- Manter servidor autoritativo, configuração isolada, componentes compartilhados (`MenuTheme`/`MenuKit`) e textos de UI em inglês.
- Distinguir claramente quatro estados: **proposta**, **implementado**, **verificado tecnicamente** (compilação/inspeção em Edit) e **aprovado pelo desenvolvedor** (após playtest/revisão visual).

## 3. Nota dona de cada informação

| Assunto | Única nota dona |
|---|---|
| Identidade, pilares, ciclo principal e escopo futuro | [[01_Produto/Visao e Escopo]] |
| Regras de gameplay, economia, IA e parâmetros | [[01_Produto/Sistemas Atuais]] |
| Direção de arte, anatomia de criaturas, HUD e padrão de menus | [[01_Produto/Design UI UX]] |
| Módulos Luau, templates do Studio, contratos e persistência | [[03_Engenharia/Arquitetura Atual]] |
| Decisões arquiteturais e de produto duradouras (ADRs) | [[03_Engenharia/Decisoes Vigentes]] |
| Estado da entrega atual, pendências de save e próximos passos | [[00_Inicio/Estado Atual]] |
| Prioridades e fila de trabalho | [[02_Planejamento/Backlog]] |
| Checklist de validação humana | [[04_Validacao/Playtest Atual]] |
| Registro cronológico de solicitações e entregas | [[00_Inicio/Historico de Contexto]] |

Substituir informações superadas diretamente na nota dona; nunca manter duas versões contraditórias no cofre.

## 4. Validar e publicar o contexto

1. Atualizar as notas donas afetadas e acrescentar a entrada `CTX-AAAA-MM-DD-NN` em [[00_Inicio/Historico de Contexto]] (modelo em [[05_Modelos/Registro de Solicitacao]]).
2. Atualizar `context_revision` e `code_reference` em `context-manifest.json`, `README.md` e [[00_Inicio/Estado Atual]].
3. Executar `python tools/check_context.py --refresh`, inspecionar o diff e rodar `python tools/check_context.py` (deve retornar `"ok": true`).
4. Revisar `git diff --check`, commitar apenas arquivos rastreados do cofre e executar `git push origin main`, confirmando o SHA remoto.
