# Otimização de tokens — diretrizes e métricas do cofre

Relatório de referência sobre a estrutura enxuta do cofre (regras operacionais ativas estão em `AGENTS.md` e [[03_Engenharia/Fluxo de Desenvolvimento]]).

## 1. Como o cofre economiza contexto

1. **Leitura em duas camadas (`context-manifest.json`):** todo novo chat lê apenas a base inicial (`entrypoints` + `bootstrap`, 7 arquivos) e carrega sob demanda somente o grupo `domains` exigido pela tarefa (`gameplay`, `ui_ux`, `engineering`, `decisions` ou `validation`).
2. **Dono único por informação:** parâmetros de jogo ficam apenas em [[01_Produto/Sistemas Atuais]], regras visuais em [[01_Produto/Design UI UX]], arquitetura em [[03_Engenharia/Arquitetura Atual]] e estado de entrega em [[00_Inicio/Estado Atual]], evitando repetição entre notas.
3. **Sem varredura cega Studio ↔ disco:** o repositório Git (`main`) é a fonte operacional dos scripts Luau; o Studio é usado para aplicar/salvar o lugar e verificar itens visuais ou divergências concretas.
4. **Leitura incremental na mesma sessão:** após a leitura inicial, reler apenas arquivos que mudaram e usar busca dirigida (`grep`/trechos) em vez de despejar todos os scripts no contexto.

## 2. Evolução das métricas do cofre

Os valores exatos da revisão atual são calculados deterministicamente por `python tools/check_context.py`:

| Medida | Acervo antigo (antes de 19/10/2026) | Cofre consolidado (19/10/2026) | Cofre otimizado (**CTX-2026-10-20-09**) |
|---|---:|---:|---:|
| Notas Markdown no cofre | 44 | 16 | 17 (incluindo estudo visual) |
| Notas na leitura inicial (`bootstrap`) | 44 (sem filtro) | 7 | 7 |
| Caracteres na leitura inicial | 161.139 | 20.585 | 16.696 (redução de ~89,6% vs. acervo antigo e ~30,6% vs. CTX-08) |

*Nota:* caracteres e bytes UTF-8 medem volume de texto reproduzível; o consumo real de tokens varia conforme modelo, imagens e chamadas de ferramentas.

## 3. Boas práticas por tipo de tarefa

- **UI / Arte 3D (`ui_ux`):** consultar [[01_Produto/Design UI UX]] e [[06_Referencias/Referencias Visuais]]; ao ajustar menus, editar `MenuTheme`/`MenuKit` antes de páginas individuais.
- **Gameplay / Laço / IA (`gameplay`):** ler [[01_Produto/Sistemas Atuais]] e apenas os módulos envolvidos na mecânica alterada.
- **Persistência / Segurança (`engineering`):** nunca economizar contexto omitindo validação de autoridade, migração de schema ou proteção de DataStore em `ProfileService`/`PersistenceConfig`.
