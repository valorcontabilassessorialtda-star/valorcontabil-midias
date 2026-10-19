# Guia de posts do Instagram — Valor Contábil

Este repositório guarda as artes dos posts do Instagram @valorcontabil.assessoria25 e as regras para criá-las.
As imagens ficam públicas aqui para o Metricool conseguir buscá-las pelo link raw do GitHub.

## Rotina

- Publicação no feed: terça, quarta, quinta e sexta, às 06:00 (America/Fortaleza). 4 posts por semana.
- Cada post é criado na véspera (segunda a quinta) como RASCUNHO no Metricool, para os sócios revisarem e confirmarem.
- Plano gratuito do Metricool: limite de 20 publicações por mês. Nunca criar mais de 1 post por dia de publicação.
- Metricool: marca `valorcontabil.assessoria25`, blogId `7522187`, fuso `America/Fortaleza`.

## Público e temas

- Áreas principais: construção civil, imóveis (PF e PJ), holdings (familiar, patrimonial, imobiliária).
- Também: empresas em geral, área trabalhista (CLT, eSocial, folha, férias, 13º, rescisão), tributária (Reforma Tributária: IBS, CBS, Imposto Seletivo, transição; Simples Nacional, Lucro Presumido, IRPF, IRPJ, ITBI, ITCMD), obrigações e prazos.
- Alternar o nível: um post para leigos (linguagem simples, exemplo do dia a dia) e outro para empresários / quem já entende (mais técnico, números, prazos, impacto no caixa).
- Priorizar novidades recentes e prazos próximos. Sempre verificar as informações em fontes oficiais ou confiáveis (Receita Federal, gov.br, Planalto, CFC, portais contábeis sérios) antes de afirmar números, alíquotas, prazos ou datas.
- Nunca repetir um tema já listado em `historico.md` nos últimos 60 dias.
- Conteúdo informativo, sem promessas de resultado, sem sensacionalismo, sem comparação depreciativa com outros escritórios (respeitar o Código de Ética do Contador quanto à publicidade).

## Visual

- Formato: 1080x1350 px (4:5), JPG de alta qualidade.
- Imagem única ou carrossel (2 a 6 telas), conforme o conteúdo pedir. Carrossel quando há passo a passo, lista ou comparação.
- Pouco texto por tela, bem explicado. Títulos grandes, números em destaque.
- Fundo escuro (navy) ou claro (branco/gelo), conforme a leitura. Padrão: capa e fechamento escuros, telas de conteúdo claras.
- Ilustrações modernas, isométricas/3D feitas em SVG no estilo do símbolo da marca (prismas com gradiente verde-água), quando ajudarem.
- Fonte: Poppins (já instalada no ambiente). Pesos 400, 600, 700, 800.
- Cores:
  - Navy: `#0d161d` / `#13222b`
  - Verde-água: `#2bd4bd` (destaque), `#1e9e8c` (médio), `#0e4f47` (escuro)
  - Cinza texto em fundo escuro: `#c4ccd4`; em fundo claro: `#3b4a55`
- Logo: `marca/logo-transparente-texto-claro.png` em fundo escuro; `marca/logo-transparente-texto-escuro.png` em fundo claro. Sempre no rodapé à esquerda.
- Variar layouts entre os posts para o feed não ficar repetitivo (mantendo cores, fonte e logo).
- Modelo de referência: `modelos/carrossel-exemplo.html` (cada tela é um `.slide` com id `s1`, `s2`...). Para gerar as imagens: `python3 scripts/render.py <html> <pasta> <prefixo>`.
- Sempre conferir visualmente cada imagem gerada (texto cortado, sobreposição com o logo, erros de português) antes de enviar.

## Legenda

- Começar com um gancho curto. Explicar em poucas linhas. Usar emojis com moderação (✅ 📌 📲 🏢).
- Fechar com chamada para contato, quando fizer sentido:
  - Elias Carvalho | CRC-PI 014153/O | (89) 99457-4219
  - Maikon Figueiredo | CRC-PI 011923/O | (89) 99404-5050
- SEMPRE mencionar os sócios na legenda: `@eliascarvalho.cont @maikonfigueiredo.cont`
- 8 a 12 hashtags relevantes, incluindo `#ValorContábil #Contabilidade #Picos #Piauí`.
- A tela final do carrossel (ou o rodapé da imagem única) pode trazer os nomes, CRC e telefones dos sócios; não é obrigatório em todo post.

## Áudio / Reels

- Por enquanto, apenas posts de imagem/carrossel no feed (sem áudio).
- Reels só quando os sócios definirem as músicas da biblioteca do Instagram (registrar aqui nome e artista).

## Onde salvar

- Cada post em `posts/AAAA-MM-DD-tema-curto/` com as imagens, o `post.html` usado e `legenda.txt`.
- Link público das imagens: `https://raw.githubusercontent.com/valorcontabilassessorialtda-star/valorcontabil-midias/main/posts/<pasta>/<arquivo>.jpg`
- Após criar o post, registrar uma linha em `historico.md`.
