# Sistemas atuais

Regras e parâmetros de gameplay implementados no código de referência (**a5e62ab**). Validação humana pendente conforme [[04_Validacao/Playtest Atual]]. Apresentação visual e UI: [[01_Produto/Design UI UX]].

## Laço e captura

- **Arremesso livre e reto:** dispara para qualquer ponto mirado (inclusive céu, chão ou parede), sem gravidade nem assistência de mira. A carga máxima (`100%`) atinge o alcance total; cargas menores reduzem o alcance proporcionalmente.
- **Parâmetros do Training Lasso (`CaptureConfig`):** alcance mínimo `18` / máximo `73` studs, tempo máximo de carga `1,4 s`, velocidade de voo `100 studs/s`, retorno `145 studs/s`, cooldown `0,12 s`.
- **Preparação visual (`LassoChargePresentation`):** enquanto o botão fica pressionado, o avatar ergue o braço e boleia o laço em plano inclinado, passando pela região da cabeça e descendo pela lateral. O movimento acelera até `100%` e permanece em ciclo depois disso. Soltar produz um gesto cosmético breve de chicote; cancelar recolhe o efeito. Isso não muda mira, alcance, trajetória ou locomoção. Outros jogadores veem a preparação confirmada pelo servidor. A pose usa eixos locais da articulação, prioridade no braço direito e restauração antes do Animator para evitar acúmulo. Ombro/flexão/pulso são configuráveis em LassoChargeStyle. A soltura direcionada é local; observadores atualmente recebem o encerramento e recolhimento, sem o mesmo gesto direcionado. A revisão visual ainda depende de aprovação humana.
- **Elegibilidade e colisão (`LassoAim` / `LassoCollision`):** o cliente exibe contorno contextual por estado (distante, no alcance, alinhado, bloqueado por obstáculo, ocupado ou sem força mínima), mas o servidor revalida tudo. A colisão contínua varre o deslocamento relativo entre projétil e o volume elipsoidal de `Corpo` (`3,3 × 2,8 × 2,6 * scale`), bloqueando capturas através de paredes.
- **Disputa autoritativa (`CaptureService`):** dono exclusivo e validação de força mínima no início e na entrega (`Lumito` exige `0`). Limite de `22 s`, ganho-base `0,18/s` na zona e perda `0,075/s` fora dela. Ciclo de `3,6 s` alterna fase normal, resistência (mais movimento, menos ganho) e abertura (menos movimento, mais ganho); meta desloca em passos limitados de `0,25` e força amplia a zona com retorno decrescente.
- **Uso de Poção na disputa:** reduz a velocidade do alvo em `35%` (para `65%`) por `6 s`; alternar para a ferramenta da poção não cancela a captura.
- **Recompensa:** credita o indivíduo na bolsa, atualiza descobertas do Index (`Normal` / `Gold`) e concede XP de caçador imediatamente. O cartão exibe XP recebido e potencial de ouro/s ao equipar na base; captura não paga ouro instantâneo.

## Criaturas e coleção

- **Espécie atual (`Lumito`):** passeia na ilha, pausa, detecta jogadores no cone de visão (`28 studs`, `110°`), foge em pânico (`14 studs/s` por `5 s`), cansa (`1,8 studs/s` por `7 s`) e retoma o passeio (`3,5 studs/s`). Modelo 3D facetado (`HACLumitoTemplate` / `CreatureFactory`) com pivô `Root` a `1,68 * scale` do chão na ilha e `1,625 * scale` na base.
- **Atuação visual (`LumitoAnimator`):** os conjuntos nomeados de cabeça, corpo, orelhas, braços, cauda e pés usam poses absolutas sobre o `Root`; passada acompanha velocidade e escala, e os estados AtBase/Wandering/Panicking/Tired/Capturing alteram postura e reação. Inclui piscada, gestos ociosos e atenção curta a jogadores próximos na base, sem alterar navegação, colisão ou regras de captura.
- **VFX de movimento:** contato alternado dos pés dispara puff cartunesco ciano/branco em flipbook 2×2; corrida/pânico habilita rastro ciano de `0,13 s`. São efeitos de apresentação discretos, sem emissão contínua.
- **Atributos por indivíduo:** `id`, `species`, `rarity`, `size`, `mutations`, `location` (`bag` ou `base`) e `favorite`.
- **Escala contínua (`1×` a `5×`, duas casas):** atributo numérico oculto na UI; exemplares existentes preservam seu tamanho.
  - Em `ee6e901` (Git): `1 + 4 × u^5`.
  - No checkout local e Studio Edit (pendente de confirmação/commit): `BaseChance = 0.7` para `1×` e `1 + 4 × u^12` nos `30%` restantes.
- **Mutação `Dourado` (`Gold`):** chance `18%`, multiplicador de valor/renda `3×` e dificuldade `1,2×`.
- **Raridades suportadas:** `Common`, `Rare`, `Epic`, `Mythic`, `Legendary`, `Secret`, `Divine` (IDs internos legados preservados para compatibilidade de save).
- **Gestão (`Creatures` e `Index`):**
  - `Creatures`: filtrar favoritos e acionar `Equip`/`Unequip` (exige vaga livre no destino; sem substituição implícita). Favorito persiste no perfil e bloqueia venda no servidor.
  - `Index`: registro permanente de variantes descobertas (`All` / `Normal` / `Gold`), independente de venda posterior, com paginação de `18` itens e sem recompensa de reivindicação (`Claim`).
- **Base viva (`BaseRoamingService`):** criaturas equipadas (escala visual `0,72 × size`) caminham livremente sobre a plataforma (`18 × 17 studs`) sem colisão física com avatares. Espécimes grandes demais para caminhar sem colidir ficam visíveis e estacionários. Ticks de renda não reiniciam a posição das criaturas.

## Economia, treino e melhorias

- **Renda passiva:** paga ouro a cada **1 segundo** pelo valor das criaturas equipadas. Lumito `1×` Normal rende `1 ouro/s` e vende por `12 ouro` antes do bônus de rank (ouro escala por tamanho/mutação). Pesquisa da base é separada e deliberadamente menor: Lumito Normal gera `1 XP/10 s`, Gold gera `2 XP/10 s`; soma-se `1 XP` global por rank acima de 1 apenas quando há criatura ativa. Espécies futuras definem `ResearchXP`; base vazia e bolsa não geram pesquisa.
- **Hunter Rank (sem rebirth):** dez tiers iniciais calculados pelo XP **total acumulado**, sem gasto de XP ou reivindicação manual. Limiares internos para ranks 1–10: `0`, `100`, `700`, `5.000`, `40.000`, `400.000`, `5 milhões`, `80 milhões`, `1,5 bilhão`, `30 bilhões`. A UI revela apenas o rank atual, percentual até o próximo e benefícios seguintes, sem expor limiares ou cap.
- **XP da caça:** captura de Lumito `1×` Normal rende `25 XP`; tamanho maior multiplica a base em até `1,6×`, Gold multiplica em `1,5×` (arredondado). Primeira descoberta de espécie soma `75`; primeira variante subsequente soma `35`, sem dupla bonificação na primeira captura. Cada rank acima de 1 acrescenta `+5%` ao ouro de base/venda e `+3%` à força do treino; resíduos fracionários persistem. Nenhuma ilha é bloqueada por rank.
- **Curva de ouro e expansão:** valores jogáveis estão na tabela abaixo. Estágios posteriores são metas de design dependentes de novas espécies com renda correspondente, sem preços ou níveis fictícios liberados agora. Custos miram cerca de 30–240 s da renda típica do estágio; a validação real é playtest. Ouro de base e venda recebem bônus de Hunter Rank, tamanho e Gold conforme regra vigente. Itens futuros mantêm `RequiredHunterRank` individual e não há bloqueio de ilha por rank.
- **Treino automático no manequim:** servidor imobiliza o avatar e paga força a cada `2 s` conforme nível de treino × eficiência; `TrainingDummies` troca a silhueta e reação do alvo nos quatro níveis atuais e adiciona equipamento de estação conforme eficiência. `TrainingPresentation` mostra o ciclo de boleio, impacto, reação e `+Strength` para clientes próximos a partir dos atributos de início/pagamento. Sair, pular ou morrer restaura a movimentação imediatamente. A cena depende de avaliação visual humana.
- **Compras de upgrades:** Base apenas na placa Base; Treino e Multiplicador na placa do manequim; Velocidade na placa própria; Bolsa no menu Creatures. Servidor valida saldo/nível para todos e proximidade da placa para os upgrades físicos.

| Melhoria | Valores por nível (1 → 4) | Custos (níveis 2 / 3 / 4) |
|---|---|---|
| Base (`baseLevel`) | 3 / 4 / 5 / 6 criaturas | 40 / 150 / 600 |
| Bolsa (`bagLevel`) | 3 / 4 / 5 / 6 criaturas | 25 / 180 / 1400 |
| Treino (`trainingLevel`) | +1 / +2 / +3 / +4 força | 30 / 120 / 480 |
| Eficiência (`efficiencyLevel`) | 1× / 1,25× / 1,5× / 2× | 50 / 200 / 800 |
| Velocidade (`speedLevel`) | 16 / 18 / 20 / 22 walkSpeed | 35 / 100 / 240 |

## Mercado, loja e ferramentas

### Tabela de balanceamento jogável

Tempos aproximados usam renda total de referência de 1, 3 e 6 ouro/s para os níveis pagos 1, 2 e 3, sem bônus de rank, venda ou saldo prévio.

| Upgrade | Nível 1 | Nível 2 | Nível 3 | Tempo de referência |
|---|---:|---:|---:|---|
| Base | 4 por 40 | 5 por 150 | 6 por 600 | 40 / 50 / 100 s |
| Bolsa | 5 por 25 | 9 por 180 | 16 por 1400 | 25 / 60 / 233 s |
| Manequim | 2 por 30 | 3 por 120 | 4 por 480 | 30 / 40 / 80 s |
| Eficiência | 1,25× por 50 | 1,5× por 200 | 2× por 800 | 50 / 67 / 133 s |
| Velocidade | 18 por 35 | 20 por 100 | 22 por 240 | 35 / 33 / 40 s |

**Projeção não liberada:** crescimento 10–100 ouro/s; avançado 1 mil–20 mil/s; raro 1 milhão–80 milhões/s. Planejar Base 8/10/12 e Bolsa 28/45/70 somente ao introduzir criaturas, ferramentas e preços coerentes com esses estágios.

- **Creature Market (venda física):** exige proximidade (`14 studs`), seleção explícita e confirmação; remove o indivíduo e credita ouro atomicamente (bloqueado se favorito).
- **Hunting Shop (`18 studs`):** abas `Tools` e `Lassos`. Rotação determinística a cada `5 minutos` compartilhada por horário, mas com **cota de compra individual persistida no perfil**. `Training Lasso` já inicia possuído.

| Ferramenta / ID interno | Preço | Efeito validado no servidor | Estoque por rotação |
|---|---:|---|---|
| Bait / `Isca` | 8 | Atrai criaturas por `15 s` em raio de `18 studs`; cooldown `8 s` | 2–5 (100%) |
| Trap / `Armadilha` | 12 | Arma em `1 s`, dura `25 s`, raio `3 studs`; reduz velocidade a `35%` por `6 s`, cooldown `10 s` | 1–3 (70%) |
| Potion / `Pocao` | 10 | Na disputa ativa, reduz velocidade do alvo a `65%` por `6 s`, cooldown `12 s` | 1–4 (60%) |

- **Inventário (`ToolInventory`):** usa o `Backpack` nativo do Roblox apenas para ferramentas com quantidade `> 0`; zerar estoque remove a `Tool`, e ticks de renda não recriam nem reordenam ferramentas.

## Preferências, idioma e perfil inicial

- **Idioma:** interface em inglês; documentação e IDs legados de save em português.
- **Settings:** `Sound` (áudio local) e `Base creatures` (oculta/mostra modelos nas bases localmente sem interromper a renda).
- **Perfil inicial (`ProfileData`):** ouro, XP e força `0`, coleção/descobertas vazias, melhorias no nível `1`, `Training Lasso` e `1` unidade de cada consumível (`Isca`, `Armadilha`, `Pocao`).
