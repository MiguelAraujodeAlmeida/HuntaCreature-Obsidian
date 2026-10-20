# Decisões vigentes

ADRs consolidadas; este arquivo guarda somente decisões atuais e racional. Substituições anteriores: [[00_Inicio/Historico de Contexto]]. Cada nova decisão duradoura recebe ID e data; não duplicar parâmetros do produto.

## ADR-001 — Fontes de verdade e sincronização

**Vigente, consolidada em 19/10/2026.** Pedido humano recente define intenção; cofre registra requisitos; Git é a referência operacional dos fontes versionados e Studio contém o lugar. Investigar Studio/disco diante de divergência concreta ou falha de aplicação, sem comparação integral rotineira. Git de scripts não cobre todo o lugar. Consequência: preservar reversibilidade e registrar separadamente save, aplicação e publicação.

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

**Vigente, 19/10/2026; pedido explícito do desenvolvedor.** Cofre é a memória geral entre IAs/chats/dispositivos, versionada no GitHub. Novo chat lê o bootstrap e os domínios da tarefa; continuação usa revisão/hashes e leitura incremental. Histórico de solicitações é único, append-only para novos fatos/correções; regras atuais têm uma nota dona.

Consequência: toda entrega inclui manutenção de contexto, validação de links/manifesto, commit e sincronização ou pendência explícita. Históricos obsoletos completos ficam fora da leitura ativa. Nenhum documento equivale a uma ordem imutável de produto; este processo de manutenção permanece obrigatório até nova instrução humana.

## ADR-008 — Caça legível pelo mundo e recompensa verdadeira

**Vigente, 20/10/2026; sujeito a playtest humano.** Preservar lançamento livre, reto e sem assistência. Mira, carga, voo, contato, disputa e retorno usam sinais visuais/sonoros curtos e estados distintos; erros normais não viram notificações. Ritmo da disputa é configurado e autoritativo no servidor. Vitória mostra a criatura e o valor real de renda/XP **quando equipada na base**, sem sugerir crédito instantâneo. Consequência: cliente apresenta dados validados e limpa efeitos ao terminar; ajustes de ritmo ficam em CaptureConfig.
