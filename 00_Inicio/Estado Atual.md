# Estado atual

Revisão de contexto **CTX-2026-10-20-01** · 20/10/2026.

## Entrega do jogo

Último código de produto: **be1bfaf**. Repositório canônico: https://github.com/MiguelAraujodeAlmeida/HuntACreature, branch `main`. Lugar **[Testing] Hunt a Creature**, placeId **102310424634629**. Caça polida em Edit e lugar salvo na Roblox pelo Studio; **aguarda playtest do desenvolvedor**.

- Creatures, Creature Market, Creature Index, Hunting Shop e Settings usam a família MenuTheme/MenuKit, retratos e componentes glossy.
- Reset configurado em geração fixa `20261019_menu_reset_01`. Todas as contas que entrarem nesta versão começam novas; progresso posterior deve persistir. Dados antigos preservados em outro namespace.
- **Não publicado**: servidores antigos continuam com seu código. Publicação não foi realizada.
- **Exportação recuperável .rbxl ainda pendente.** O comando “Salvar na Roblox” foi acionado no Studio para o lugar de teste; não houve reabertura independente para comprovar restauração.

## Entrega da caça · 20/10/2026

- Mira mostra estados discretos de alvo distante, possível, alinhado, bloqueado e ocupado; carga central cresce até MAX e comunica alcance. Voo/retorno diferem por rastro, cor e resposta ao contato, sem avisos para falhas normais.
- Disputa mantém a zona controlada pelo jogador e alterna resistência/abertura em 3,6 s; ganho-base passa de 0,29 para 0,18/s, com meta limitada em passos. Lumito reage no lugar; HUD e corda indicam fase e poção.
- Recompensa usa retrato, primeira descoberta/variante/Gold/tamanho e valores de ouro e XP **por segundo quando equipada na base**; volta sozinha em até 2,35 s.
- Os 11 fontes Luau alterados foram compilados estaticamente no Studio Edit, sem execução. O Studio já estava em Play ao início desta solicitação; essa sessão foi encerrada para aplicar os fontes. Nenhum novo Play, emulação ou benchmark foi iniciado. O lugar foi salvo na Roblox via interface; código remoto confirmado em `be1bfafb13c42787906157a77829f3eec961848a`.

**Pendente:** desenvolvedor avaliar precisão, ritmo, sensação sonora/visual e celular/PC. Salvamento em nuvem não equivale a publicação; exportação .rbxl e teste de restauração seguem pendentes.

Regras dos sistemas preservados: [[01_Produto/Sistemas Atuais]]. Padrão visual: [[01_Produto/Design UI UX]].

## Entrega anterior de menus

53 fontes de runtime iguais entre Studio e disco e compilados; 21 verificações isoladas passaram. Prévia estática em Edit inspecionada para Shop, Index, Settings e mercado; componentes comuns usados em Creatures. Objetos temporários removidos.

Na entrega anterior não houve Play, emulação ou benchmark. DataStore real, reconexão, input remoto completo, toque e mix de som continuam sem confirmação. Verificação técnica não aprova estética, ritmo ou diversão.

Artefatos no checkout do jogo: `contexto/menus-2026-10-19/` contém mapa de fontes, hashes, verificações e backup. Não estão neste repositório de contexto.

## Contexto compartilhado

Cofre consolidado em um conjunto vigente, histórico único e manifesto verificável. Especificações contraditórias substituídas; referências visuais copiadas para o próprio cofre. Instruções de leitura inicial enxuta e manutenção por solicitação registradas. O histórico antigo integral está no backup externo descrito em [[00_Inicio/Historico de Contexto]].

Git é a fonte operacional dos arquivos versionados; comparações integrais Studio/disco não fazem parte do fluxo rotineiro. O Studio aplica e salva mudanças no lugar. A leitura inicial do cofre usa base curta e grupos por domínio.

## Próximos passos

1. Desenvolvedor avalia a sequência da caça em PC e celular, incluindo arremessos vazios/bloqueados, disputa normal/Gold, poção, falha e descoberta.
2. Desenvolvedor executa [[04_Validacao/Playtest Atual]], incluindo duas contas, reset e reconexão.
3. Exportar uma cópia .rbxl recuperável e testar restauração em outra máquina. Corrigir feedback por domínio antes de expandir conteúdo; prioridades em [[02_Planejamento/Backlog]].

O cofre e o código são portáveis por Git; o lugar ainda não foi exportado integralmente. Isso continua impedindo restaurar o **jogo** apenas pelos clones.
