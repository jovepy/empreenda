from CONFIG_GERAL import *

def RETORNA_AGENDA():
    AGENDA = pd.read_excel('../TABELAS/AGENDA.xlsx')
    AGENDA = AGENDA.fillna('DISPONIVEL')
    AGENDA['DATA'] = pd.to_datetime(AGENDA['DATA'],dayfirst=True).dt.strftime("%d/%m/%y")
    return(AGENDA)

def RETORNA_PRODUTOS():
    PRODUTOS = pd.read_excel('../TABELAS/SERVIÇOS.xlsx')
    PRODUTOS.index.name = 'OPCAO'
    return(PRODUTOS)


def agenda_dias_disponiveis(agenda=RETORNA_AGENDA()):
    agenda = agenda.fillna('DISPONIVEL')
    agenda = agenda.loc[agenda['CLIENTE'] == 'DISPONIVEL']
    agenda = agenda.loc[agenda['DATA'] >= date.today().strftime('%d/%m/%Y')]
    dias_disponiveis = list(agenda['DATA'].drop_duplicates())
    return(dias_disponiveis)

def agenda_dia_mais_proximo_do_solicitado(dias_disponiveis=agenda_dias_disponiveis(),data=str):
    if data not in dias_disponiveis:
        data = pd.to_datetime(data,dayfirst=True).strftime('%d/%m/%Y')
        dias_proximos = abs(pd.to_datetime(data, dayfirst=True)-pd.to_datetime(dias_disponiveis, dayfirst=True))
        selecao = pd.DataFrame(dias_proximos,index=dias_disponiveis)
        data_mais_proxima = selecao.sort_values(by=0,ascending=True).iloc[0].name
    else:
        data_mais_proxima = data
    return(data_mais_proxima)

def agenda_horarios_dia_selecionado(agenda=RETORNA_AGENDA(),data_mais_proxima=str):
    horarios_disponiveis = agenda.loc[agenda['DATA']== data_mais_proxima]
    horarios_disponiveis = list(horarios_disponiveis[horarios_disponiveis['CLIENTE'] == 'DISPONIVEL']['HORA'])
    return(horarios_disponiveis)

def INFORMA_PRODUTO(txt=str):
    PRODUTOS = RETORNA_PRODUTOS()
    doc = nlp(txt)
    for nn, p in enumerate(PRODUTOS['SERVIÇO']):
        if nn == 0:
            anterior = doc.similarity(nlp(p))
            vencedor = p
        else:
            atual = doc.similarity(nlp(p))
            if atual > anterior:
                vencedor = p
    return(vencedor)

#deve-se criar uma mensagme de confirmacao, um loop de confirmacao, um a um ou geral?
    