## Seja bem-vindo ao projeto [Empreenda](https://jovepy.github.io/empreenda/)

Nesse projeto você encontrará uma microestrutura de serviços que auxiliará o empreendedor em três esferas:
1. Atendimento ao público
2. Gerenciamento de estoques/Agenda
3. Precificação de produtos/Serviços

A proposta desse projeto é auxiliar qualquer pessoa que busque empreender e que possua baixo capital inicial. Proponho-me e vos convido a criar uma ferramenta que agregue valor à sociedade. Esse é meu [IG](https://instagram.com/jove.py/), nos destaques existem uma série de vídeos feitos por mim explicando o conceito e proposta.

Você poderá contribuir utilizando o [repositório oficial](https://github.com/jovepy/empreenda) do projeto 

OBS: o símbolo *** significa que ainda há a inclusão de novos scripts/componentes à pasta
# [Estrutura do Projeto](https://miro.com/app/board/uXjVO60CGLc=/?share_link_id=474544749315)
## PASTAS
- BASICOS: funções úteis e gerais a todo o projeto.
- COMPONENTES: módulos com utilidades específicas. No caso as três esferas do projeto
    1. Atendimento
    2. Gerenciamento de estoques/agenda
    3. Precificação de produtos/serviços
    4. Dashboard para Busines Inteligence
- CONFIGS: configurações dos módulos e local
- TABELAS: informações do empreendedor, simula um banco de dados, porém com o objetivo de ser simples, por isso tabelas em excel.
- DEPENDÊNCIAS: programas e bibliotecas necessários para o funcionamento

## Composição das PASTAS
### BASICOS
    1. *** 

### COMPONENTES

    1. WHATSAPP_BOT.PY: utilizado para o atendimento via Whatsapp. O único propósito desse script é receber, estrutura e enviar informações
    2. GERENCIADOR.PY: utilizado para gerenciar o resultado oriundo do atendimento, podendo ser uma agenda de horários ou estoque.
    3. PREFICACAO.PY: utiliza microeconomia e os dados obtidos com o atendimento e o estoque para precificar o produto e gerar indicadores úteis.
    4. DASHBOARD.PY: exibe as informações obtidas na precificação.

### CONFIGS

    1. CONFIG_GERAL.PY: configurações gerais do programa e local
    2. CONFIG_MENU.PY: configurações dos menus do atendiemnto no WPP
    3. MSG_SAUDACAO.TXT: mensagem exibida para início do diálogo
    4. ***

### DEPENDÊNCIAS

    1. Bibliotecas.txt: bibliotecas necessárias de serem instaladas

# Em progresso...

