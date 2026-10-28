# Receita de ilhas e cenários

**Estado:** direção de design proposta em 28/10/2026; revisável após bloco visual e playtest. Nenhuma ilha, barco ou teletransporte desta proposta está implementado. Esta nota orienta qualquer agente que criar ou revisar mapas; regras de interface ficam em [[01_Produto/Design UI UX]], mecânicas vigentes em [[01_Produto/Sistemas Atuais]].

## 1. Experiência pretendida

- O mundo pode receber novas ilhas por atualização ou evento, sem número final pré-definido. Isso significa **estrutura expansível**, não geração procedural infinita prometida ao jogador.
- Cada ilha comunica seu tema em poucos segundos pela silhueta do terreno, um marco dominante, vegetação, paleta, materiais e ambientação. O jogador deve reconhecer onde chegou antes de ler qualquer placa.
- O destino é um lugar de caça e descoberta, não apenas um fundo. Caminhos, relevos e pontos de interesse criam pequenos momentos de curiosidade, mas preservam visão limpa das criaturas e espaço para mirar o laço.
- A mesma linguagem de **brinquedo montável** une criaturas, prédios e cenário: volumes grandes, planos/facetas ou blocos bem encaixados, chanfros controlados, cor por peças e studs onde reforçam material/escala. Não forçar studs em toda superfície; água, areia, folhagem e efeitos podem precisar de tratamentos próprios.
- Referências de *Steal an Egg*, *Grow a Garden* e *Steal a Brainrot* ajudam a avaliar leitura, ritmo e acabamento. Criar composições, modelos, silhuetas e biomas próprios; não copiar uma ilha ou prop específico.

## 2. Brief inicial das ilhas

| Ilha | Primeira impressão e função | Elementos de direção, ainda ajustáveis |
|---|---|---|
| **Base** | Refúgio amigável e pacífico onde o jogador administra sua coleção e se prepara para caçar | Bases, lojas e treino organizados em percursos legíveis; vegetação comum, praia contornando a área principal e porto com barco. A costa e o relevo devem dar identidade sem esconder ações essenciais. |
| **Fazenda** | Primeira ilha de caça: fazenda tranquila, fértil e acolhedora | Celeiro como marco, plantações e vegetação rural, cercas, caminhos de terra e detalhes agrícolas com escala de brinquedo. Criaturas precisam de espaço e visibilidade para caça; não fixar ainda distribuição ou economia definitiva. |

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
- A interação para viajar deve ser descoberta pelo próprio porto/barco e apresentar destinos claramente. Entrada, destino, retorno e cancelamento precisam ser previsíveis em PC e celular. Não colocar um tutorial permanente na tela.
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

Escolher escala e mapa de rotas, organização dos destinos no barco, posição definitiva de bases/treino/lojas, catálogo de props, espécies por ilha e seus requisitos de força, e abordagem técnica do teletransporte. Validar cada ilha em bloco antes de produzir a arte final. Esta receita não aprova modelos específicos nem substitui feedback visual do desenvolvedor.
