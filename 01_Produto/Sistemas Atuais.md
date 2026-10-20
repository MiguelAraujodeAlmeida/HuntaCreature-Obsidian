# Sistemas atuais

Estado: implementados, com validação humana pendente conforme [[04_Validacao/Playtest Atual]]. Valores abaixo são referência da entrega 90045a0; ao alterar configuração, atualizar esta nota na mesma solicitação. Código inspecionado decide o valor executado; documento registra a intenção e a versão.

## Laço e captura

- Lançamento livre para o ponto escolhido pelo jogador, inclusive céu/chão/locais sem criatura. Sem mensagens rotineiras de “mira inválida” ou “laço errou”.
- Direção reta, sem gravidade ou correção automática para o alvo. A 100% segue exatamente a direção da mira, respeitando obstáculos e alcance real. Carga menor reduz alcance.
- Cada laço tem seus parâmetros. Training Lasso: alcance mínimo 18/máximo 73 studs, carga máxima 1,4 s; voo 100 studs/s e retorno 145; cooldown 0,12 s. Barra de força central, acima da barra nativa, sem ocupar permanentemente a tela.
- Criatura elegível na mira/alcance recebe contorno. A elegibilidade e o acerto são revalidados no servidor.
- Colisão contínua considera movimento relativo da criatura e volume do laço/corpo; bloqueios do mundo também são considerados. Isso não equivale a colisão por pixel da orelha. Precisão percebida precisa de teste.
- Disputa compacta, sem modal gigante/tutorial. Parâmetros atuais: duração-base 22 s e ganho-base 0,29/s; força beneficia com retorno decrescente. Não considerar esse ritmo aprovado.
- Uma disputa possui dono exclusivo; validação de força mínima no início e na recompensa. Lumito exige 0. Não permitir segunda captura simultânea ou prêmio duplicado.
- Poção pode ser usada durante a disputa; trocar a ferramenta não deve cancelar o estado por deixar de segurar o laço.

## Criaturas e coleção

Lumito é a única espécie atual. Passeia, pausa, percebe jogador com linha de visão, foge e se cansa. IA delimitada ao cenário atual; não é navegação universal para qualquer mapa.

- Indivíduo tem ID próprio, espécie, raridade, tamanho, mutações, local (bolsa/base), posição lógica e favorito.
- Tamanhos atuais 0,85/1/1,2 com pesos 25/55/20. Gold é mutação: chance 18%, multiplicador de valor 3 e dificuldade 1,2; não é raridade separada.
- Raridades: Common, Rare, Epic, Mythic, Legendary, Secret, Divine. IDs internos legados em português permanecem estáveis.
- Creatures permite selecionar, filtrar favoritos e **Equip/Unequip**. Destino precisa ter espaço; sem troca implícita, exclusão ou perda de criatura. Bloqueios de treino/disputa continuam válidos.
- Favorito persiste por indivíduo e bloqueia venda no servidor, inclusive se o cliente tentar ignorar a interface.
- Index registra descobertas permanentes, independentes da posse; variantes All/Normal/Gold, raridade, progresso, silhuetas e ficha. Paginação de 18. Não há recompensas de coleção implementadas.
- Criaturas equipadas passeiam dentro do piso da base, com pausas/separação. Não ficam em pedestais. Visuais ancorados sem colisão/toque/query; a atualização de renda não reinicia sua posição. Área atual de passeio: 18 × 17 studs.

## Economia, treino e melhorias

- Renda de ouro e XP a cada **1 segundo**, mantendo o valor que antes era pago a cada 5 s: aceleração **5× expressamente escolhida pelo desenvolvedor**.
- Lumito normal: referência-base 1 ouro/s, 1 XP/s e venda 12; variações/mutações influenciam valor. Preços antigos mantidos, balanceamento pendente.
- Treino automático no manequim: avatar imóvel, animação de laçar; não exige jogar um minigame. Tick de 2 s; ganho combina nível de treino e eficiência. Sair/morrer/interromper deve restaurar movimento.
- Gerenciar melhorias **apenas nas placas da própria base**, com botão clicável. Treino e sua eficiência junto ao manequim. Sem acesso duplicado por menu.
- Placas exibem nível atual/próximo, custo e estado máximo; proprietário, distância e saldo validados no servidor. Texto nas duas faces e descoberta tardia dos objetos não devem deixar a placa vazia.

| Melhoria | Valores por nível | Custos das três compras |
|---|---|---|
| Base | 3 / 4 / 5 / 6 criaturas | 40 / 100 / 220 |
| Bolsa | 3 / 4 / 5 / 6 criaturas | 25 / 70 / 160 |
| Treino | 1 / 2 / 3 / 4 | 30 / 90 / 180 |
| Eficiência | 1 / 1,25 / 1,5 / 2 | 50 / 140 / 300 |
| Velocidade | 16 / 18 / 20 / 22 | 35 / 100 / 240 |

## Mercado, loja e ferramentas

**Venda:** somente no mercado físico próximo ao jogador (14 studs). Selecionar indivíduo de bolsa/base, confirmar ou cancelar. Remoção e crédito atômicos; favorito protegido. Sem botão de venda remota no Creatures.

**Hunting Shop:** proximidade de 18 studs; abas Tools/Lassos. Rotação determinística de 5 minutos com ofertas comuns entre servidores e **cota individual persistida**. Não é um estoque global consumido por todos os jogadores. Mostrar itens e motivo de indisponibilidade. Training Lasso é o único laço, já possuído inicialmente.

| Ferramenta / ID interno | Preço | Função atual | Estoque por rotação |
|---|---:|---|---|
| Bait / Isca | 8 | Atrai por 15 s, raio 18; cooldown 8 s | 2–5, recorrente |
| Trap / Armadilha | 12 | Arma em 1 s, dura 25 s, raio 3; velocidade a 35% (redução de 65%) por 6 s, cooldown 10 s | 1–3, chance 70% |
| Potion / Pocao | 10 | Durante disputa, alvo da disputa a 65% da velocidade (redução de 35%) por 6 s, cooldown 12 s | 1–4, chance 60% |

Posição, cota, propriedade, quantidade, cooldown e contexto são validados pelo servidor; consumir apenas quando a ação for válida. Inventário usa **Backpack nativo do Roblox**, com reordenação padrão. Só existem Tools possuídos; quantidade zero remove o Tool. Atualização passiva não deve recriar ferramentas. Ordem não tem persistência personalizada.

## Preferências, idioma e início

- Inglês como idioma nativo da apresentação. Documentação em português. Não renomear IDs de save para traduzir.
- Settings: Sound e Base creatures. Preferências persistentes; efeito local. Ocultar criaturas das bases não suspende renda e se aplica também às que surgirem depois.
- Perfil novo: ouro/XP/força zerados, coleção/descobertas vazias, melhorias iniciais, Training Lasso e uma unidade de cada consumível; preferências ligadas.
- Reset excepcional atual e proteção de dados: [[03_Engenharia/Arquitetura Atual]]. Não confundir reset de teste com mecânica de progressão.
