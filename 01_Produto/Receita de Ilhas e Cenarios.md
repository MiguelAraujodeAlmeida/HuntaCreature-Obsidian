# Receita de ilhas e cenários

**Estado:** direção de design proposta em 28/10/2026; revisável após bloco visual e playtest. A Ilha Base tem um **bloco v01.1 em Studio Edit** (seção 2.1, escala `1.1×` e polimento geométrico), sem aprovação humana final, água ou funcionalidades; barco, teletransporte e Fazenda não estão implementados. Esta nota orienta qualquer agente que criar ou revisar mapas; regras de interface ficam em [[01_Produto/Design UI UX]], mecânicas vigentes em [[01_Produto/Sistemas Atuais]].

## 1. Experiência pretendida

- O mundo pode receber novas ilhas por atualização ou evento, sem número final pré-definido. Isso significa **estrutura expansível**, não geração procedural infinita prometida ao jogador.
- Ilhas podem ter **tamanhos diferentes**. Como referência de sensação, a ilha média deve comportar tema e descobertas próprias sem caminhada longa ou espaços vazios, comparável a uma ilha média de *Blox Fruits*; não fixar studs ou um tempo de travessia antes do bloco em câmera jogável. Ilhas especiais podem ser menores ou maiores por função.
- Cada ilha comunica seu tema em poucos segundos pela silhueta do terreno, um marco dominante, vegetação, paleta, materiais e ambientação. O jogador deve reconhecer onde chegou antes de ler qualquer placa.
- O destino é um lugar de caça e descoberta, não apenas um fundo. Caminhos, relevos e pontos de interesse criam pequenos momentos de curiosidade, mas preservam visão limpa das criaturas e espaço para mirar o laço.
- A mesma linguagem de **brinquedo montável** une criaturas, prédios e cenário: volumes grandes, planos/facetas ou blocos bem encaixados, chanfros controlados, cor por peças e studs onde reforçam material/escala. Não forçar studs em toda superfície; água, areia, folhagem e efeitos podem precisar de tratamentos próprios.
- Referências de *Steal an Egg*, *Grow a Garden* e *Steal a Brainrot* ajudam a avaliar leitura, ritmo e acabamento. Criar composições, modelos, silhuetas e biomas próprios; não copiar uma ilha ou prop específico.

## 2. Brief inicial das ilhas

| Ilha | Primeira impressão e função | Elementos de direção, ainda ajustáveis |
|---|---|---|
| **Base** | Refúgio amigável e pacífico onde o jogador administra sua coleção e se prepara para caçar | Seis bases futuras como **cercados habitáveis** para criaturas, treino ao lado das bases, duas lojas na parte norte e porto/barco no norte da costa; vegetação comum e praia contornando a área principal. O esquema abaixo fixa apenas essa distribuição inicial, não o contorno nem a arte final. |
| **Fazenda** | Primeira ilha de caça: fazenda tranquila, fértil e acolhedora | Celeiro como marco, plantações e vegetação rural, cercas, caminhos de terra e detalhes agrícolas com escala de brinquedo. Criaturas precisam de espaço e visibilidade para caça; não fixar ainda distribuição ou economia definitiva. |

Distribuição inicial da Base, conforme o esquema do desenvolvedor: **duas bases à esquerda, duas à direita e duas na parte inferior**; áreas de treino próximas às bases, **duas lojas na parte superior** e barco/porto na costa superior. A distribuição é relativa: não determina forma da ilha, posição exata, orientação dos caminhos nem arte final. A ilha de teste ainda não foi substituída. Espécies residentes, requisitos de força e demais regras de gameplay de cada ilha serão estudados numa etapa própria; não inventar esses números ao desenhar cenário.

### 2.1 Ilha Base — bloco v01.1 e guia de continuidade (Studio Edit, 28/10/2026)

**Estado:** implementado e polido em Edit como `Workspace.HAC_IlhaBase` (Model, `1.445` BaseParts / `2.710` descendentes, `WorldPivot = (0, 0, −430)`, escala `1.1×` via `HACEscala = 1.1`), sem Save confirmado, Play ou aprovação visual final. Fica a ~430 studs ao norte (`−Z`) da ilha de teste (`Workspace.HuntACreature`), que segue intacta; nenhum script referencia `HAC_IlhaBase`. **Norte = `−Z` = porto**. Guia avulso completo também salvo em `../Handoff - Ilha Base v01.1.md` (fora do cofre).

- **Terreno e orientação de cilindros (`Terreno`):** contorno orgânico por 5 `UnionOperation`s de cilindros rotacionados `90°` em Z (`RightVector = +Y`, espessura vertical em `Size.X` e textura de topo em `Face = Enum.NormalId.Right`): `Fundacao` (topo `−2,20`), `AreiaRasa` (topo `2,75`), `Praia` (topo `4,40`), `Barranco` (topo `7,70`) e `Gramado` (topo **`8,80`**). Quatro colinas decorativas nos cantos e farol listrado na colina NE.
- **Circulação e hierarquia de alturas sem Z-fighting (`Caminhos`):** todas as superfícies horizontais sobrepostas mantêm diferença mínima de `>= 0,05` studs no topo (`topY`, zero pares coplanares): `Gramado` (`8,800`) → `Acesso_Loja1..2` (`8,860`) → `Acesso_Base5..6` (`8,866`) → `Lote_Treino.Borda` (`8,910`) → `Acesso_Base1..4` (`8,932`) → `Lote_Base/Loja.Piso` (`8,950`) → `Lote_Treino.Piso` (`8,976`) → `Avenida_Porto/Oeste/Leste` (`9,020`) → `PracaBorda` (`9,108`) → `Lote.Marcador/IndicadorFrente` (`9,130`) → `Praca` (`9,196`). Píer em `T` no norte com tábuas em `5,280`/`5,302`.
- **Lotes reservados (`Lotes`, coordenadas globais em escala `1.1×`):** cada lote é um Model desimpedido com `Piso` (`PrimaryPart`, cuja frente é `Piso.CFrame.LookVector`), cantoneiras brancas sem sobreposição nos cantos, `Volume` invisível (`CanCollide/CanQuery/CanTouch = false`) e atributos `HACReserva`, `HACIndice`, `HACTamanho`/`HACRaio`:
  - `Lote_Base1..4`: `37,4 × 19,8 × 30,8` em `(−70,4, 8,73, −456,4)`, `(−70,4, 8,73, −412,4)`, `(70,4, 8,73, −456,4)` e `(70,4, 8,73, −412,4)`, frente para a praça (`±X`).
  - `Lote_Base5..6`: `30,8 × 19,8 × 37,4` em `(−22,0, 8,73, −361,8)` e `(22,0, 8,73, −361,8)`, frente norte (`−Z`).
  - `Lote_Treino1..6`: raio `7,15` (diâmetro `14,3`) ao lado de cada base (`HACBaseVinculada = 1..6`).
  - `Lote_Loja1..2`: `28,6 × 26,4 × 22,0` em `(−37,4, 8,73, −498,2)` e `(37,4, 8,73, −498,2)`, voltadas na diagonal para a avenida/praça.
  - `Lote_Barco1`: `Volume` `50,6 × 15,4 × 22,0` em `(0, 5,5, −635,7)` ao norte do píer e `AreaInteracao` `33,0 × 8,8 × 8,8` em `(0, 9,68, −618,1)` sobre a cabeça do píer.
- **Kit, paleta e regras anti-bug:** `SmoothPlastic` em tudo exceto luzes funcionais (`Neon` apenas em `Farol_Lampada` e `Poste.Lanterna`). Texturas preservadas em `StudsPerTile = 4` (studs `133050717017276` e madeira `97810845356536`) e `12` (caminho `103826263412719`) — sempre restaurar `StudsPerTileU/V` após usar `:ScaleTo()`. Copas de árvores, arbustos, palmeiras, flores, monumento e vigas do píer usam empilhamento real sem interpenetração interna; auditoria via `OverlapParams` confirmou `0` invasões nos 15 lotes e `0` faces de topo coplanares.
- **Pendências para continuar:** nível da água (recomendado `Y = 2,0` a `2,6`), `SpawnLocation`, conversão dos 15 lotes em cercados/treinos/lojas/barco, colisões em Play, custo em celular e aprovação visual humana.

Outras ilhas podem ser fantásticas, sazonais ou surpreendentes. Devem manter legibilidade e qualidade da família visual, não repetir floresta/grama por obrigação. As imagens abaixo demonstram como uma linguagem de blocos e studs suporta árvore, lava, cânion e ruína com identidades diferentes; **não são o mapa que deve ser copiado**.

| Referência enviada pelo desenvolvedor | Leitura útil |
|---|---|
| ![[assets/ilhas-referencia-arvore.png]] | Árvore em massas escalonadas e textura de studs; contraste entre copa, tronco, solo e água. |
| ![[assets/ilhas-referencia-lava.png]] | Formas modulares escuras com um foco luminoso forte, sem precisar cobrir tudo de brilho. |
| ![[assets/ilhas-referencia-canyon.png]] | Grandes planos de rocha em camadas, borda verde e caminho que orienta a exploração. |
| ![[assets/ilhas-referencia-templo.png]] | Marco arquitetônico dominante, escadaria e vegetação que contam o tema de longe. |

## 3. Viagem por barco — contrato de experiência proposto

- Toda ilha tem um porto/embarcação de chegada e saída. O barco funciona como acesso por **teletransporte** entre ilhas; não exige viagem física longa.
- **Nenhuma ilha exige Hunter Rank ou nível mínimo para entrar.** O limite de progressão vem da força das criaturas e de seus requisitos de captura, definidos por espécie quando o conteúdo existir. O jogador pode visitar uma ilha difícil e entender visualmente que ainda precisa evoluir.
- Ao entrar na **área de interação do barco**, o jogador abre um menu de destinos; escolhe a ilha e confirma. **O teletransporte acontece imediatamente após a confirmação**, sem animação de viagem que imponha espera. Sair da área, fechar o menu e cancelar não deslocam o jogador. O retorno deve ser claro em PC e celular; não colocar tutorial permanente na tela.
- A implementação pode usar áreas separadas no mesmo lugar ou lugares Roblox distintos. Escolher depois conforme escala, carregamento, multiplayer e custo; a experiência acima não depende dessa decisão técnica. Não alterar spawn, save ou permissões antes de especificar o fluxo.

## 4. Receita de produção para qualquer agente

1. **Escrever um brief curto por ilha:** emoção, função no loop, leitura em três segundos, marco principal, dois ou três motivos visuais, fauna pretendida, zonas de caça, porto, contraste com ilhas vizinhas. Registrar o que está decidido e o que ainda é hipótese.
2. **Fazer bloco de volumes antes de detalhar:** topografia, costa, caminhos, porto, marcos e áreas jogáveis com caixas simples. Conferir da altura normal da câmera e em tela pequena: o tema e a direção de viagem são óbvios? O avatar consegue alcançar lojas/treino/spawns sem desvios irritantes?
3. **Definir kit modular da ilha:** família de chão, bordas/encostas, vegetação, rochas, arquitetura, cercas/props e sinais do porto. Cada objeto usa a linguagem toy comum, mas tem forma, cor e material que contam o bioma. Criar variantes de escala/rotação/composição sem parecer cópia repetida.
4. **Aplicar materiais por função:** massas principais simples e legíveis; studs ou grade em áreas selecionadas; textura fina com parcimônia; brilho/néon somente para foco funcional, magia ou evento. A grama, árvores, rochas e edifícios da mesma ilha devem parecer produzidos pela mesma direção de arte, mesmo com superfícies diferentes.
5. **Fazer três passagens de ambientação:** primeiro marcos e horizonte; depois caminhos, grupos de vegetação e props médios; por último detalhes próximos, movimento ambiental, áudio e acentos de VFX. Cada passagem deve melhorar a leitura, não apenas aumentar a quantidade de objetos.
6. **Testar a caça no layout:** linhas de visão, espaço para arremesso e fuga, bordas seguras, terrenos navegáveis e colisões coerentes. Evitar que decoração atrapalhe a mira, esconda criaturas ou cause presos entre peças.
7. **Revisar de vários pontos:** chegada pelo barco, rota principal, área de caça, base/lojas quando aplicável, câmera baixa e alta, PC e celular. Mostrar capturas gerais e detalhes de props; corrigir silhueta, escala, repetição e vazios antes de polir mais.
8. **Entregar de forma reproduzível:** mapa de blocos/layout, paleta e materiais usados, kit de props com nomes claros, evidência visual e pendências. Separar configuração de ilhas/viagem dos assets e das regras de captura; cada nova ilha deve entrar sem editar uma lista espalhada por menus e scripts.

## 5. Como avaliar sem engessar

- **Tema imediato:** ao chegar, uma pessoa reconhece a identidade da ilha sem explicação? O marco aparece antes dos detalhes?
- **Variedade com parentesco:** a Fazenda e a Base compartilham qualidade de formas e acabamento, mas não precisam ter a mesma paleta, árvores ou materiais. Uma futura ilha de lava ou ruínas pode usar blocos escuros e efeitos fortes sem quebrar o estilo.
- **Densidade útil:** há coisas interessantes para descobrir ao andar, com pausas visuais onde as criaturas e interações importam? Quantidade de props nunca é uma meta por si só.
- **Movimento e atmosfera:** vegetação, água, partículas e áudio dão vida ao tema com acentos localizados. Efeitos não substituem topografia, composição e modelos bons.
- **Jogo funcionando:** caminhos, portos, zonas e criaturas são legíveis, acessíveis e não geram colisões inesperadas. O custo visual permanece adequado ao celular; medir quando houver mapa jogável, sem fixar agora um orçamento arbitrário de peças.
- **Originalidade:** qualquer exceção ao kit comum é bem-vinda se comunicar melhor o tema e preservar leitura, desempenho e coerência. Registrar a decisão no brief da ilha em vez de transformar uma exceção em regra global.

## 6. Pendências para a etapa de implementação

Escolher no bloco jogável as dimensões e o contorno de cada ilha, caminhos definitivos entre pontos, catálogo de props e abordagem técnica do teletransporte. A distribuição inicial da Base e o fluxo de interação do barco já estão descritos; a UI concreta do menu de destinos ainda exige design. Espécies por ilha e seus requisitos de força ficam para um estudo de gameplay separado. Validar cada ilha em bloco antes da arte final. Esta receita não aprova modelos específicos nem substitui feedback visual do desenvolvedor.
