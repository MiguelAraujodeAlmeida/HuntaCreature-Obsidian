# Sistemas atuais

Regras e parâmetros de gameplay implementados no código de referência (**8c0da86**). Validação humana pendente conforme [[04_Validacao/Playtest Atual]]. Apresentação visual e UI: [[01_Produto/Design UI UX]].

## Laço e captura

- **Arremesso livre e reto:** dispara para qualquer ponto mirado (inclusive céu, chão ou parede), sem gravidade nem assistência de mira. A carga máxima (`100%`) atinge o alcance total; cargas menores reduzem o alcance proporcionalmente.
- **Parâmetros do Training Lasso (`CaptureConfig`):** alcance mínimo `18` / máximo `73` studs, tempo máximo de carga `1,4 s`, velocidade de voo `100 studs/s`, retorno `145 studs/s`, cooldown `0,12 s`.
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
- **Curva de ouro e expansão:** o catálogo define livremente renda/venda por espécie e preço por item/melhoria; não há faixas obrigatórias de equipamento por rank. Cada espécie futura pode definir `CaptureXP`, `FirstSpeciesXP`, `FirstVariantXP`, `ResearchXP` e multiplicador de pesquisa Gold para sustentar ranks altos. A escalada extrema depende de espécies e compras futuras; preços iniciais não foram inflados sem fontes de renda correspondentes. Cada item pode declarar `RequiredHunterRank` individualmente. Os itens atuais permanecem disponíveis no rank 1.
- **Treino automático no manequim (`WorldPresentation`):** posiciona o avatar imóvel laçando o manequim a cada `2 s`, somando força conforme nível de treino × eficiência. Sair, pular ou morrer restaura a movimentação imediatamente.
- **Placas físicas da base (`UpgradeBoards`):** único local para comprar melhorias (validação de dono, distância de `16 studs` e saldo no servidor; `SurfaceGui` nas duas faces).

| Melhoria | Valores por nível (1 → 4) | Custos (níveis 2 / 3 / 4) |
|---|---|---|
| Base (`baseLevel`) | 3 / 4 / 5 / 6 criaturas | 40 / 100 / 220 |
| Bolsa (`bagLevel`) | 3 / 4 / 5 / 6 criaturas | 25 / 70 / 160 |
| Treino (`trainingLevel`) | +1 / +2 / +3 / +4 força | 30 / 90 / 180 |
| Eficiência (`efficiencyLevel`) | 1× / 1,25× / 1,5× / 2× | 50 / 140 / 300 |
| Velocidade (`speedLevel`) | 16 / 18 / 20 / 22 walkSpeed | 35 / 100 / 240 |

## Mercado, loja e ferramentas

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
