# Playtest atual

Build de referência: **90045a0**, lugar **102310424634629**. **Todos os itens abaixo aguardam confirmação humana nesta versão.** O assistente não deve iniciar Play/emulação por rotina. Evidência técnica existente: [[00_Inicio/Estado Atual]].

## Primeiro: reset e persistência

- [ ] P01 · Entrar em duas contas: ouro/XP/força zerados, coleção vazia, níveis iniciais, Training Lasso e uma unidade de cada consumível. Se a conta já jogou nesta geração, ela deve manter o progresso novo, não zerar novamente.
- [ ] P02 · Capturar, treinar, comprar/melhorar, favoritar e alterar Settings; sair e reconectar. Dados novos preservados, sem reset repetido.
- [ ] P03 · Confirmar ambiente: Studio e publicado usam stores distintos; HACStudioMemoryMode precisa estar desativado para testar persistência real. Não inferir que teste em memória aprovou save.
- [ ] P04 · Se houver erro de leitura/perfil ocupado, nenhum perfil vazio deve ser gravado por cima do anterior.

## Menus e interação

- [ ] M01 · Abrir/fechar Creatures, Index, Shop e Settings; mercado pelo ponto físico. Uma janela por vez, X acessível, sem sobreposição com barra/controles Roblox.
- [ ] M02 · Selecionar itens, rolar e receber renda: seleção/foco/posição de rolagem estáveis; valores atualizam sem piscar/recriar tudo.
- [ ] M03 · Conferir vazio, texto longo, indisponível, página cheia e seleção removida. Ícone/retrato comunica antes do texto.
- [ ] M04 · PC e celular: botões legíveis/tocáveis, rolagem e saída funcionam. Ficha vai acima da grade em largura pequena.
- [ ] M05 · Hover/pressão/retorno, brilho e som agradáveis; sem repetição irritante, travamento ou excesso de efeitos. Registrar avaliação visual separada dos bugs.
- [ ] M06 · Texto visível em inglês; sem guias permanentes, título fixo do jogo ou avisos redundantes.

## Criaturas, base e mercado

- [ ] C01 · Equip/Unequip move o indivíduo correto. Destino cheio bloqueia sem trocar, duplicar ou perder.
- [ ] C02 · Equipadas passeiam dentro da base, sem colisões/bordas atravessadas. Renda não reinicia posição. Desequipar/remove visual certo.
- [ ] C03 · Favoritar e tentar vender: bloqueado. Reconectar mantém favorito. Desfavoritar permite venda perto do mercado.
- [ ] C04 · Venda exige confirmação; cancelar preserva tudo. Confirmar remove apenas o escolhido e credita uma vez.
- [ ] C05 · Afastar-se do mercado, tentar outra base ou agir durante treino/disputa não contorna restrições.
- [ ] C06 · Index registra captura Normal/Gold corretamente; filtros/contagem/silhueta/ficha coerentes. Vender não apaga descoberta.

## Loja, ferramentas e progressão

- [ ] L01 · Shop só acessível nas condições de proximidade; Tools/Lassos corretos, preço/quantidade/owned e motivos de bloqueio claros.
- [ ] L02 · Compra decrementa cota individual e ouro uma vez; saldo insuficiente/cota zero/limite não consome. Reabrir/reconectar na mesma rotação preserva cota.
- [ ] L03 · Duas contas veem a mesma oferta na rotação, mas compras não consomem a cota uma da outra.
- [ ] L04 · Backpack contém só ferramentas possuídas; reordenar funciona, consumo zero remove, renda não troca slots. Respawn não duplica.
- [ ] L05 · Isca atrai dentro do raio; trap só consome em posição válida, arma e desacelera; potion atua durante disputa e respeita estoque/cooldown.
- [ ] B01 · Placas mostram texto e botões nas duas faces após entrar. Só a própria base permite comprar; saldo/custo/nível máximo corretos.
- [ ] B02 · Treinar deixa avatar imóvel; sair/morrer restaura movimento. Melhoria de treino e eficiência produz benefício correto.
- [ ] B03 · Ouro/XP sobem por segundo com valor aprovado de 5×; sem som/aviso invasivo por tick. Conferir efeitos de tamanho/mutação.

## Laço, IA e preferências

- [ ] A01 · Mira em pontos próximos/distantes e criatura em movimento: tiro segue a direção sem arco; carga limita distância real. Testar céu/chão/parede e retorno.
- [ ] A02 · Contorno somente quando elegível; obstáculo/fora do alcance não captura. Erro comum não dispara tutorial/notificação.
- [ ] A03 · Disputa exclusiva sem recompensa duplicada; mínimo Lumito 0. Quando outra espécie for adicionada, testar limite abaixo/igual/acima.
- [ ] A04 · Lumito passeia/pausa/foge com visão/cansaço; não atravessa limites nem trava. Avaliar ritmo de captura, sensação de combate e celebração.
- [ ] S01 · Sound desliga efeitos locais; preferência persiste. Base creatures oculta visuais atuais e novos, preservando renda; ligar restaura.
- [ ] S02 · Cliques rápidos, resposta atrasada e fechar/reabrir Settings não deixam estado visual diferente do confirmado pelo servidor.

## Registrar resultado

Para cada falha: ID, build, dispositivo/resolução, passos, esperado, observado, print/vídeo/Output e frequência. Marcar aprovado/falhou/não testado/não aplicável com data. Continuar apenas blocos independentes se houver falha impeditiva.

Começar por P01–P02, M01, B01–B02, C01/C03/C04. Não é necessário executar tudo numa sessão. Aparência e diversão exigem parecer explícito do desenvolvedor.
