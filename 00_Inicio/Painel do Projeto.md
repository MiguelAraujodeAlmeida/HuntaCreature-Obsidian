# Painel do projeto

## Leitura inicial enxuta

Em um novo chat/dispositivo, ler README, AGENTS e estes fundamentos na ordem do `bootstrap` do manifesto:

1. [[00_Inicio/Estado Atual]] — entrega, evidência e próximo passo.
2. [[01_Produto/Visao e Escopo]] — identidade, ciclo e limites.
3. [[02_Planejamento/Backlog]] — prioridades e itens adiados.
4. [[03_Engenharia/Fluxo de Desenvolvimento]] — execução, Git e manutenção do cofre.

Depois, carregar apenas o domínio da tarefa:

| Domínio | Ler quando a tarefa envolver |
|---|---|
| `gameplay` | laço, captura, criatura, treino, economia, loja ou ferramentas |
| `ui_ux` | HUD, menu, componente visual, layout, efeitos ou referência de arte |
| `engineering` | módulos, persistência, segurança, rede, Studio ou aplicação do código |
| `decisions` | decisão que pode mudar uma regra duradoura |
| `validation` | playtest, bug, regressão ou checklist humano |

O manifesto contém os arquivos exatos e hashes. Não carregar todos os domínios por padrão.

## Consulta complementar

- [[00_Inicio/Historico de Contexto]]: pedidos e mudanças ao longo do tempo; não sobrepõe regras vigentes.
- [[05_Modelos/Registro de Solicitacao]]: formato de registro.
- [[07_Relatorios/Otimizacao de Tokens]]: opções para discussão, não tarefas automaticamente autorizadas.

## Regra de interpretação

**Pedido humano recente → decisão vigente → requisito do domínio.** Código inspecionado comprova o que existe, não o que o desenvolvedor aprovou. Conflitos entre intenção e código devem ser registrados como lacunas. Pesquisa externa e ideias antigas não são ordens.

As notas têm donos: produto descreve regras; engenharia, implementação; Backlog, andamento; Estado Atual, entrega; Histórico, proveniência. Referenciar em vez de copiar.
