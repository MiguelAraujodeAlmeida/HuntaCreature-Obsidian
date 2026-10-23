# Painel do projeto

## Roteiro de leitura (`reference`, sob demanda)

O manifesto é a fonte da ordem atual; esta nota explica o propósito de cada grupo.

1. [[00_Inicio/Estado Atual]] — última entrega, estado do Studio/Git e pendências imediatas.
2. [[01_Produto/Visao e Escopo]] — identidade, pilares, ciclo principal e limites da versão.
3. [[02_Planejamento/Backlog]] — prioridades ativas e itens adiados.
4. [[03_Engenharia/Fluxo de Desenvolvimento]] — sincronização Git, dono de cada informação e validação do cofre.

## Leitura sob demanda (`domains` e `reference`)

| Grupo | Arquivos | Quando carregar |
|---|---|---|
| `gameplay` | [[01_Produto/Sistemas Atuais]] | Laço, captura, criatura, IA, treino, economia, loja ou ferramentas |
| `ui_ux` | [[01_Produto/Design UI UX]] | HUD, menus, componentes visuais, modelagem 3D ou direção de arte |
| `engineering` | [[03_Engenharia/Arquitetura Atual]] | Módulos Luau, templates em `ReplicatedStorage`, persistência, rede ou Studio |
| `decisions` | [[03_Engenharia/Decisoes Vigentes]] | Decisão arquitetural ou de produto duradoura (ADRs) |
| `validation` | [[04_Validacao/Playtest Atual]] | Roteiro de playtest humano, regressão ou relato de bug |
| `reference` | [[00_Inicio/Historico de Contexto]], [[05_Modelos/Registro de Solicitacao]], [[07_Relatorios/Otimizacao de Tokens]], [[06_Referencias/Referencias Visuais]], [[06_Referencias/Estudo visual Steal an Egg]] | Proveniência, métricas ou comparação visual específica |

## Hierarquia de autoridade

**Pedido humano mais recente → decisão vigente ([[03_Engenharia/Decisoes Vigentes]]) → especificação do domínio → código inspecionado.**
Código comprova o que está implementado, não o que o desenvolvedor aprovou. Cada informação tem uma única nota dona; referenciar em vez de duplicar.
