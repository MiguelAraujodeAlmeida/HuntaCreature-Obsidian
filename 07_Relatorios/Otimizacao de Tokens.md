# Otimização de tokens — opções para o projeto

19/10/2026. **Relatório para discussão**, não autorização para instalar ferramentas, trocar modelos ou criar infraestrutura. A regra de leitura integral na primeira entrada foi preservada.

## O que foi feito nesta rodada

Cofre com uma nota principal por assunto; especificações obsoletas fora do conjunto vigente; histórico único; manifesto de leitura/hash; mapa de módulos; referências visuais portáveis e checklist único. Isso reduz releitura e reexplicação sem omitir as regras atuais.

Métricas reproduzíveis aparecem abaixo. Caracteres/bytes medem volume de texto; não são contagem exata de tokens nem percentual de economia da assinatura. Tokens variam com tokenizer, idioma, imagens, ferramentas e respostas.

| Medida | Antes | Depois |
|---|---:|---:|
| Notas Markdown no cofre | 44 | 16 |
| Notas da leitura inicial definida | Sem manifesto; 44 notas no acervo | 13 |
| Caracteres: acervo antigo completo vs. novo conjunto inicial | 161.139 | 46.079 |

O novo conjunto inicial tem 71.4% menos caracteres que o acervo antigo completo. A comparação exclui imagens, manifesto e instruções adicionais da plataforma; histórico/modelo/relatório novos são consulta complementar. Não significa que o sistema anterior lia sempre as 44 notas, nem que a economia de tokens será essa porcentagem. Contagem: caracteres Unicode dos Markdown UTF-8; reproduzir o conjunto atual com tools/check_context.py.


## Prioridades recomendadas

| Ação | Esforço | Benefício esperado neste projeto | Cuidado |
|---|---|---|---|
| 1. Ler todo o conjunto vigente uma vez; depois só notas alteradas na mesma sessão | Baixo; regra já registrada | Evita reler dezenas de notas a cada ajuste | Novo chat/dispositivo exige leitura completa |
| 2. Pedido com objetivo, domínio, critério de aceite e limites | Baixo | Menos suposições e refações do HUD/mecânicas | Não transformar cada pedido em formulário longo |
| 3. Uma fatia jogável por entrega | Baixo | Feedback localiza o problema; menor diff e regressão | Não fragmentar uma mudança inseparável |
| 4. Buscar símbolo/arquivo e ler trechos relevantes, não todos os scripts | Baixo | Menos saída de ferramentas e contexto de código | Ampliar leitura quando há dependência real |
| 5. Preferir diff, hashes e resumo de resultados a dumps completos | Baixo | Barato conferir Studio/disco e Git | Hash detecta diferença, não explica comportamento |
| 6. Feedback de bug com passos, esperado, observado, build e imagem certa | Baixo | Evita ciclos tentando adivinhar o erro | Um vídeo curto pode comunicar melhor que muitos screenshots |
| 7. Reusar MenuKit, tokens e componentes | Médio; base existente | Menos código e design refeitos por menu | Padrão deve evoluir quando feedback mostrar defeito |
| 8. Remote do código + export identificável do lugar + sync verificado | Médio; pendente | Evita recuperação de versões divergentes entre máquinas | Introduzir comparação/backup antes de automatizar escrita |
| 9. Checks locais de contexto, lint e contratos pequenos | Médio; validador do cofre pronto | Máquinas detectam repetidamente erros estruturais sem explicações longas | Não substituir teste humano de diversão ou executar QA extenso por rotina |
| 10. Encerrar um chat em marco estável e abrir outro com cofre atualizado | Baixo/médio | Evita carregar tentativas fracassadas por semanas | A nova leitura tem custo; não abrir chat para cada ajuste mínimo |
| 11. Ajustar esforço/modelo à tarefa | Médio; decisão futura | Tarefas mecânicas podem precisar menos raciocínio que rede/persistência | Menor custo por chamada pode gerar mais refações; medir por entrega |
| 12. Retrieval por domínio ou índice de código | Alto; só se crescer muito | Encontra contexto relevante sem varrer o projeto | Não pode omitir a leitura vigente inicial nem recuperar specs antigas como atuais |
| 13. Instrumentação e prompt caching em integração própria por API | Alto; opcional | Pode reduzir custo/latência de prefixos repetidos | Não é configuração automática do Codex desktop |

As práticas de manter AGENTS curto, correto e ligado a documentação específica são coerentes com a orientação oficial de trabalho com Codex. Aqui a leitura inicial completa é uma exigência adicional do desenvolvedor. [OpenAI — boas práticas](https://learn.chatgpt.com/guides/best-practices)

## Aplicação concreta por domínio

**UI/UX:** pedido traz referência e define o alvo (“diminuir mochila, manter proporção da arte, não mudar funções”). Comparar uma imagem antes/depois em resolução informada. Ajustar componente comum antes de replicar CSS/Frames/constantes em várias páginas. Gerar arte só quando faltar um asset útil; reutilizar arquivos/IDs existentes.

**Laço/IA:** relatar distância, carga, movimento do alvo, obstáculo e resultado esperado. Ler CaptureConfig/LassoAim/LassoCollision e consumidor relevante; não reler todo o histórico de HUD. Uma correção geométrica deve ter caso de verificação específico, não um benchmark de todo o jogo.

**Persistência/economia:** mudanças exigem mais cuidado. Não economizar omitindo validação de autoridade, transação, migração, reset ou conflitos de sessão. Comparar configuração/contratos e registrar geração/build; o custo de refazer perda de dados é maior.

**Contexto:** atualizar a nota dona, uma linha no backlog quando necessário e uma entrada curta no histórico. Evitar transcrições de chat, logs brutos, pesquisas antigas inteiras e o mesmo relatório repetido em seis páginas.

## API: quando faria sentido

Somente se construirmos uma ferramenta própria de documentação/análise. Prompt caching depende de prefixos idênticos; instruções estáveis antes e conteúdo variável depois favorecem reutilização. Devemos observar métricas de uso/cached tokens antes de prometer economia. Cache não elimina o texto do contexto nem corrige informação antiga. Não há nesta entrega uma integração API ou controle desse mecanismo na interface do Codex. [OpenAI — Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)

Um sistema de retrieval poderia indexar notas vigentes e módulos com versão/estado. Só vale o custo se busca simples e manifesto deixarem de resolver; indexar o legado sem filtragem recriaria justamente as contradições removidas.

## Como medir sem adivinhar

Durante 5–10 entregas comparáveis, registrar: domínio, quantidade de rodadas de correção, tamanho do diff, fontes lidos, caracteres enviados/retornados pelas ferramentas e uso de tokens se a plataforma disponibilizar. Separar imagens, geração de mídia e tempo de trabalho. Comparar **custo por entrega aceita**, não apenas por resposta.

Não há medição completa de tokens históricos nesta tarefa; portanto não se promete porcentagem exata de economia nem equivalência com limite de uso do plano.

## Sequência sugerida para discutirmos

1. Manter a organização/manifesto já entregues e padronizar pedidos/relatos de bug.
2. Resolver portabilidade do código e do lugar, maior fonte atual de retrabalho.
3. Validar o fluxo por algumas entregas; só então avaliar modelo/esforço, CI ou retrieval.
4. Deixar integração API/cache para uma necessidade concreta.

Nenhuma dessas sugestões autoriza agentes auxiliares ou QA pesado: as regras do projeto continuam valendo.
