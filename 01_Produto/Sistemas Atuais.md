# Sistemas atuais

Regras e parâmetros de gameplay implementados no código de referência (**ee6e901**). Validação humana pendente conforme [[04_Validacao/Playtest Atual]]. Apresentação visual e UI: [[01_Produto/Design UI UX]].

## Laço e captura

- **Arremesso livre e reto:** dispara para qualquer ponto mirado (inclusive céu, chão ou parede), sem gravidade nem assistência de mira. A carga máxima (`100%`) atinge o alcance total; cargas menores reduzem o alcance proporcionalmente.
- **Parâmetros do Training Lasso (`CaptureConfig`):** alcance mínimo `18` / máximo `73` studs, tempo máximo de carga `1,4 s`, velocidade de voo `100 studs/s`, retorno `145 studs/s`, cooldown `0,12 s`.
- **Elegibilidade e colisão (`LassoAim` / `LassoCollision`):** o cliente exibe contorno contextual por estado (distante, no alcance, alinhado, bloqueado por obstáculo, ocupado ou sem força mínima), mas o servidor revalida tudo. A colisão contínua varre o deslocamento relativo entre projétil e o volume elipsoidal de `Corpo` (`3,3 × 2,8 × 2,6 * scale`), bloqueando capturas através de paredes.
- **Disputa autoritativa (`CaptureService`):** dono exclusivo e validação de força mínima no início e na entrega (`Lumito` exige `0`). Limite de `22 s`, ganho-base `0,18/s` na zona e perda `0,075/s` fora dela. Ciclo de `3,6 s` alterna fase normal, resistência (mais movimento, menos ganho) e abertura (menos movimento, mais ganho); meta desloca em passos limitados de `0,25` e força amplia a zona com retorno decrescente.
- **Uso de Poção na disputa:** reduz a velocidade do alvo em `35%` (para `65%`) por `6 s`; alternar para a ferramenta da poção não cancela a captura.
- **Recompensa:** credita o indivíduo na bolsa, atualiza descobertas do Index (`Normal` / `Gold`) e exibe o potencial de **ouro/s e XP/s quando equipado na base** (a captura não paga ouro/XP instantâneos).

## Criaturas e coleção

- **Espécie atual (`Lumito`):** passeia na ilha, pausa, detecta jogadores no cone de visão (`28 studs`, `110°`), foge em pânico (`14 studs/s` por `5 s`), cansa (`1,8 studs/s` por `7 s`) e retoma o passeio (`3,5 studs/s`). Modelo 3D facetado (`HACLumitoTemplate` / `CreatureFactory`) com pivô `Root` a `1,68 * scale` do chão na ilha e `1,625 * scale` na base, animando os conjuntos de pés (`FootSide = "L" / "R"`) em fase oposta.
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

- **Renda passiva (aceleração 5× aprovada):** paga a cada **1 segundo** o valor das criaturas equipadas na base. Referência do Lumito `1×` Normal: `1 ouro/s`, `1 XP/s` e venda por `12 ouro` (escalados por tamanho e mutação).
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
