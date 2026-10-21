# Estudo visual: criaturas e mundo de Steal an Egg

**Estado:** princípios gerais aprovados pelo desenvolvedor em 20/10/2026, consolidados em [[01_Produto/Design UI UX]] e aplicados na modelagem do `Lumito_Base_v01` ([[06_Referencias/Referencias Visuais]]). Este estudo documenta a leitura visual da referência; nenhuma malha, textura ou criatura de *Steal an Egg* deve ser copiada.

## Fontes observadas

- [Página do jogo no Roblox](https://www.roblox.com/games/107778070777162/Steal-An-Egg) e imagens promocionais: [dinossauro e ovo](https://tr.rbxcdn.com/180DAY-875b2a6dc156ce6dd64eb637e73238ce/768/432/Image/Png/noFilter), [serpente](https://tr.rbxcdn.com/180DAY-79e666901b2c722b06310d267bc6c152/768/432/Image/Png/noFilter), [dragão](https://tr.rbxcdn.com/180DAY-7dd435aafd4a769f634a333a47f99735/768/432/Image/Png/noFilter).
- Capturas de gameplay: [base e criaturas grandes](https://files.bo3.gg/uploads/image/129278/image/webp-d456cb4a1beeb999c5591b272c0282da.webp), [área inicial](https://stealanegg-wiki.com/images/progression/forest-guardian.png), [três áreas e criaturas](https://i.ibb.co/fzCyTt2v/094b3efdf27d.jpg) e anexos de referência enviados pelo desenvolvedor.

![Divulgação: dinossauro de volumes facetados, cabeça dominante e grandes zonas de cor](https://tr.rbxcdn.com/180DAY-875b2a6dc156ce6dd64eb637e73238ce/768/432/Image/Png/noFilter)

![Captura de jogo: escala dos pets, textura regular no piso e em corpos, cercas e áreas amplas](https://files.bo3.gg/uploads/image/129278/image/webp-d456cb4a1beeb999c5591b272c0282da.webp)

![Área inicial: criatura simples, ovos, piso verde com studs e muro ocre](https://stealanegg-wiki.com/images/progression/forest-guardian.png)

## Síntese dos princípios observados

### Criaturas
1. **Silhueta imediata:** cada espécie tem proporções e massas dominantes próprias (cabeça/mandíbula grande, corpo em cunha ou dorso marcado), legíveis mesmo sem detalhe fino.
2. **Construção por blocos e facetas:** cabeça, focinho, torso, patas, placas e cristas parecem peças encaixadas com chanfros simples e planos visíveis, nunca esferas lisas genéricas.
3. **Zonas amplas de cor e studs pontuais:** barriga clara, dorso contrastante e marcações seguem a geometria; relevo de studs conecta a criatura ao material do mundo Roblox.
4. **Personalidade pela pose e escala:** inclinação de cabeça, olhos/boca simples e contraste de escala (`1×` a gigantes) sustentam o apelo visual sem depender de partículas constantes.

### Mundo
1. **Superfícies modulares e saturadas:** pisos planos com grade de studs, muros em blocos quentes e cercas simples que delimitam bases e caminhos.
2. **Espaço limpo para o foco:** áreas de circulação sem ruído deixam criaturas, alvos e recompensas dominarem a leitura em câmera distante ou tela móvel.

## Aplicação no Hunt A Creature

| Adotar como princípio | Adaptar ao nosso jogo | Evitar |
|---|---|---|
| Silhueta forte em 360°, volumes grandes facetados/chanfrados, material toy/studs, cenário modular | Paleta ciano e traços próprios por espécie (ex.: testa saliente, orelha dobrada e crista dorsal do `Lumito_Base_v01`), escala `1×`–`5×` | Copiar espécies/malhas existentes, importar mecânica de ovos, usar neon/VFX constante em criatura base ou repetir esferas lisas |
