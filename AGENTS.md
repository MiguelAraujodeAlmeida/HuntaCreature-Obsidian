# Instruções para qualquer IA ou colaborador

Banco de contexto do **Hunt A Creature** (política permanente definida pelo desenvolvedor em 19/10/2026).

- Repositório: https://github.com/MiguelAraujodeAlmeida/HuntaCreature-Obsidian
- Raiz local: `C:\Users\melg_\OneDrive\Documents\Hunt A Creature\Hunt A Creature` (ou a raiz deste clone em outra máquina; nunca criar segundo cofre silenciosamente).

## 1. Leitura obrigatória por escopo

1. **Novo chat ou dispositivo:** ler `README.md`, `AGENTS.md` e os arquivos de `bootstrap` em `context-manifest.json`, na ordem declarada. Não substituir essa base por resumo de chat.
2. **Roteamento por domínio:** antes de editar, ler apenas os arquivos de `domains` correspondentes à tarefa (`gameplay`, `ui_ux`, `engineering`, `decisions` ou `validation`). Ler `reference` somente quando precisar de histórico, modelo de registro, métricas ou comparação visual específica.
3. **Mesma sessão:** reler apenas o que mudou e os domínios afetados. Se algum arquivo, repositório ou instância do Studio estiver inacessível, explicitar a lacuna.

## 2. Regras de execução no projeto

- **Proibições sem pedido explícito:** não iniciar Play, emulação, benchmarks, QA extenso nem subagentes. Verificações estáticas leves em modo Edit são permitidas.
- **Código vs. Studio:** Git (`main`) é a referência operacional dos scripts versionados; o Studio aplica mudanças, e **somente o desenvolvedor aciona o salvamento do lugar** (`.rbxl` / nuvem). Não usar acesso ao computador para salvar por conta própria. Se não houver confirmação humana, registrar o save como pendente. Não fazer varredura integral Studio ↔ disco por rotina — investigar apenas divergência concreta.

## 3. Manutenção obrigatória ao concluir uma entrega

1. Sincronizar e preservar alterações locais conforme [[03_Engenharia/Fluxo de Desenvolvimento]].
2. Atualizar a **nota dona** de cada regra alterada, [[00_Inicio/Estado Atual]] e [[02_Planejamento/Backlog]], removendo afirmações superadas sem duplicar conteúdo entre notas.
3. Registrar a entrega em [[00_Inicio/Historico de Contexto]] (`CTX-AAAA-MM-DD-NN`) distinguindo proposta, implementado, verificado e aprovado.
4. Incrementar `context_revision` em `context-manifest.json`, executar `python tools/check_context.py --refresh`, revisar o diff e validar com `python tools/check_context.py`.
5. Commitar e enviar (`git push origin main`), confirmando o SHA remoto (ou declarar **sincronização pendente** se offline).
