# Processo de criação de mundos Roblox

Pesquisa de 29/10/2026. Referência complementar para tarefas de cenário; não carregar no bootstrap.

## Evidência e limites

Os casos abaixo possuem documentação pública dos criadores da plataforma. Não foi verificado o pipeline interno de Steal an Egg, Blox Fruits, Grow a Garden ou Steal a Brainrot. A aparência desses jogos não permite concluir qual plugin, programa ou técnica usaram. Não apresentar nossas inferências visuais como bastidores confirmados.

## Casos documentados

**Beyond the Dark:** a equipe começou com Parts e formas simples, importou algumas malhas de ferramentas como Blender/Maya e ajustou escala e rotas antes da arte final. O cenário foi organizado em módulos com encaixe consistente e Packages para propagar revisões. Uma biblioteca pequena de trim sheets e SurfaceAppearance serviu a muitos objetos. Photoshop e Substance aparecem no relato da produção de mapas. É um exemplo de método modular, não uma direção estética para nosso jogo. [Relato de arquitetura](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture).

**Modern City:** o exemplo reutiliza paredes, janelas, portas e materiais. Pivôs em posições coerentes e dimensões compatíveis com a grade permitem encaixar peças rotacionadas sem corrigir cada junção à mão. A variação vem de combinações, cores, materiais e props. A grade específica do exemplo não é uma exigência universal. [Tutorial de ambientes modulares](https://create.roblox.com/docs/tutorials/use-case-tutorials/modeling/assemble-modular-environments).

**Currículo Environment Art:** parte do greybox para validar espaço, escala do avatar, acessos e linhas de visão. Depois trabalha direção de arte, texturas repetíveis, trim sheets, módulos e props. Texturas sem emendas ainda podem revelar repetição se houver manchas muito reconhecíveis. A iteração entre modelo e composição é prevista. O tutorial inclui Mystery of Duvall como exemplo de como detalhes muito marcantes numa textura repetida denunciam o reuso. [Greybox](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment), [assets](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets), [construção](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/construct-your-world).

## Ferramentas e responsabilidades

| Etapa | Ferramentas possíveis | Resultado |
|---|---|---|
| Intenção e mapa | Esboço, referências e documento curto | Percurso, funções, marcos e áreas livres |
| Bloco | Studio Parts/Wedges, Move/Rotate snapping, Pivot Tools | Escala e circulação revisáveis |
| Relevo | Terrain Editor quando sua linguagem serve ao bioma; Parts ou malhas para formas deliberadamente construídas | Silhueta e superfície navegável |
| Modelos | Studio para peças simples; Blender/Maya para silhuetas, chanfros, UVs e malhas mais elaboradas | Kit com pivôs, escala e colisões planejados |
| Materiais | MaterialService/MaterialVariant; SurfaceAppearance para malhas com UV; editores de imagem, Blender ou Substance para mapas | Biblioteca por função, reutilizável |
| Montagem | Models, Packages, ferramentas de transformação e scripts reproduzíveis | Variações controladas e revisões propagáveis |
| Luz | Lighting, fontes locais e efeitos de pós-processamento | Leitura de formas e clima sem brilho agressivo |
| Validação | Câmeras em Edit; depois playtest autorizado e dispositivos alvo | Legibilidade, circulação e custo reais |

SurfaceAppearance usa mapas de cor, normal, metalness e roughness em MeshParts; uma Texture sobre um Part não oferece o mesmo controle de rugosidade. Reflectance zerado sozinho também não elimina toda resposta especular. Consultar [materiais](https://create.roblox.com/docs/parts/materials) antes de escolher o recurso. A demonstração [Intro to World Building](https://events.roblox.com/en/public/videos/intro-to-world-building-roblox-staff-streams-2024-05-20) reúne Parts, meshes, materiais, terreno e luz no mesmo fluxo.

## Aplicação proposta ao Hunt A Creature

1. Fixar o escopo da rodada: cenário e lotes reservados. Mar, bases construídas, treino, lojas e barco aguardam etapa própria com sistemas consistentes.
2. Definir a impressão desejada e três pontos de observação: chegada, praça e caminhada junto aos lotes. Usar escala do avatar, não apenas vista aérea.
3. Fazer uma pequena amostra: árvore, pedra, chão e trecho de caminho. Comparar silhueta, materiais e luz antes de replicar pela ilha.
4. Usar massas tranquilas no chão e vegetação; textura reforça material. Brinquedo é reconhecido por proporção, construção, cores e acabamento, sem exigir studs em tudo.
5. Montar biblioteca com grama suave, areia, terra de barranco, pedra, madeira e pintura. Cada item declara função, escala de repetição, contraste, acabamento e variantes compatíveis. Começar com poucos materiais bem distintos; expandir por necessidade do bioma.
6. Variar árvores por silhueta e agrupamento, com áreas vazias intencionais. Não preencher cada lacuna com flores ou postes. Manter caminhos e lotes livres.
7. Revisar junções e coplanaridade de perto. Interseção interna oculta que une peças não equivale automaticamente a defeito; frestas, faces competindo, volumes expostos atravessados e encaixes incoerentes exigem correção.
8. Revisar luz no material final: brilho controlado, plantas opacas, iluminação local discreta, foco no que importa. Não compensar material ruim apenas reduzindo toda a luz.
9. Submeter a amostra e a ilha à avaliação humana. Só consolidar como fórmula o que for aprovado; pesquisa técnica não aprova a estética.

Não adicionar textos flutuantes para explicar reservas. A identificação técnica pode ficar em nomes e atributos no Explorer. Portos, lojas e bases ainda não construídos não devem ganhar sinalização de uma interação inexistente.
