# Estado atual

Revisão de contexto **CTX-2026-10-19-03** · 19/10/2026.

## Entrega do jogo

Último código: **90045a0**, branch local `codex/menu-system-reset`. Lugar **[Testing] Hunt a Creature**, placeId **102310424634629**. Cinco menus refeitos e reset por geração implementados; **aguardam playtest do desenvolvedor**.

- Creatures, Creature Market, Creature Index, Hunting Shop e Settings usam a família MenuTheme/MenuKit, retratos e componentes glossy.
- Reset configurado em geração fixa `20261019_menu_reset_01`. Todas as contas que entrarem nesta versão começam novas; progresso posterior deve persistir. Dados antigos preservados em outro namespace.
- **Não publicado**: servidores antigos continuam com seu código. Publicação não foi realizada.
- **Salvamento completo do lugar (.rbxl/nuvem) não confirmado.** Código local commitado e fontes aplicados não substituem esse salvamento.

Regras dos sistemas preservados: [[01_Produto/Sistemas Atuais]]. Padrão visual: [[01_Produto/Design UI UX]].

## Evidência da entrega de menus

53 fontes de runtime iguais entre Studio e disco e compilados; 21 verificações isoladas passaram. Prévia estática em Edit inspecionada para Shop, Index, Settings e mercado; componentes comuns usados em Creatures. Objetos temporários removidos.

Nenhum Play, emulação ou benchmark iniciado. Sem teste de DataStore real, reconexão, input remoto completo, toque ou mix de som nesta rodada. Verificação técnica não aprova estética, ritmo ou diversão.

Artefatos no checkout do jogo: `contexto/menus-2026-10-19/` contém mapa de fontes, hashes, verificações e backup. Não estão neste repositório de contexto.

## Entrega de contexto desta rodada

Cofre consolidado em um conjunto vigente, histórico único e manifesto verificável. Especificações contraditórias substituídas; referências visuais copiadas para o próprio cofre. Instruções de leitura integral inicial e manutenção por solicitação registradas. O histórico antigo integral está no backup externo descrito em [[00_Inicio/Historico de Contexto]].

Esta rodada altera documentação e organização; não altera gameplay nem gera nova validação do Studio.

## Próximos passos

1. Confirmar/salvar o lugar integral e manter código/lugar identificados.
2. Desenvolvedor executa [[04_Validacao/Playtest Atual]], começando por duas contas, reset e reconexão.
3. Corrigir o feedback por domínio antes de expandir conteúdo. Prioridades em [[02_Planejamento/Backlog]].

O cofre é portável; o código ainda não tem remote configurado e o lugar não foi exportado integralmente. Esses são impedimentos reais para restaurar o **jogo** apenas com este clone.
