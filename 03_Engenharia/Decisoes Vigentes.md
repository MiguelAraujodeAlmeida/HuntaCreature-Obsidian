# Decisões vigentes

ADRs consolidadas; este arquivo guarda somente decisões atuais e racional. Substituições anteriores: [[00_Inicio/Historico de Contexto]]. Cada nova decisão duradoura recebe ID e data; não duplicar parâmetros do produto.

## ADR-001 — Fontes de verdade e sincronização

**Vigente, consolidada em 19/10/2026.** Pedido humano recente define intenção; cofre registra requisitos; código/Studio inspecionados definem implementação. Até sync verificado, comparar ambos antes de sobrescrever. Git de scripts não cobre todo o lugar. Consequência: preservar backups e registrar separadamente save, aplicação e publicação.

## ADR-002 — Treino no manequim

**Vigente.** Treino automático, jogador imóvel, avatar laçando manequim; melhorias próprias. Substitui a proposta de esteira. O identificador interno legado “Esteira” ainda pode existir em objetos/código; não significa que a decisão voltou atrás. Consequência: input e saída precisam respeitar o estado de treino.

## ADR-003 — Acessos e coleção

**Vigente.** Melhorias nas placas físicas; Creatures centraliza equipar/desequipar e favoritos. Venda só no mercado físico. Backpack nativo para ferramentas possuídas. Substitui menus duplicados, troca automática bolsa/base e venda remota. Consequência: capacidade/posse/distância continuam validadas no servidor.

## ADR-004 — Base viva, idioma e descoberta

**Vigente, 19/10/2026.** Criaturas passeiam na base; preferências locais não suspendem economia. Inglês nativo, sem migração casual dos IDs de dados. Index separa descoberta permanente da posse; variantes e favoritos pertencem ao perfil. Consequência: apresentação pode mudar sem apagar identidade/histórico.

## ADR-005 — Família de menus

**Vigente, 19/10/2026.** Reutilizar MenuTheme/MenuKit e retratos existentes, conforme [[01_Produto/Design UI UX]]. Placas e disputa são exceções pela função, não justificativa para telas genéricas. Consequência: novos menus não reintroduzem UI:Card ou estilos independentes; revisão visual altera o componente comum.

## ADR-006 — Reset por geração fixa

**Vigente, 19/10/2026.** Pedido de zerar todas as contas atendido por novo namespace explícito de save. Geração fixa preserva dados anteriores e permite progresso novo persistente; não resetar a cada entrada. Consequência: só builds atualizados usam a geração nova; teste real e publicação são separados. Não é Rebirth.

## ADR-007 — Contexto portável, enxuto e versionado

**Vigente, 19/10/2026; pedido explícito do desenvolvedor.** Cofre é a memória geral entre IAs/chats/dispositivos, versionada no GitHub. Primeira leitura absorve todo o contexto vigente; depois, leitura incremental dentro da mesma sessão. Histórico de solicitações é único, append-only para novos fatos/correções; regras atuais têm uma nota dona.

Consequência: toda entrega inclui manutenção de contexto, validação de links/manifesto, commit e sincronização ou pendência explícita. Históricos obsoletos completos ficam fora da leitura ativa. Nenhum documento equivale a uma ordem imutável de produto; este processo de manutenção permanece obrigatório até nova instrução humana.
