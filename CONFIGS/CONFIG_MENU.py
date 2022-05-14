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
    agenda = agenda.fillna('DISPONÍVEL')
    agenda.loc[agenda['CLIENTE'] == 'DISPONÍVEL']
    dias_disponiveis = list(agenda['DATA'].drop_duplicates())
    return(dias_disponiveis)

def agenda_dia_mais_proximo_do_solicitado(dias_disponiveis=agenda_dias_disponiveis(),data=str): #ver se assim já se subentende que dias_disponiveis que sera utilizado
    if data not in dias_disponiveis:
        data = pd.to_datetime(data,dayfirst=True).strftime('%d/%m/%Y')
        dias_proximos = abs(pd.to_datetime(data, dayfirst=True)-pd.to_datetime(dias_disponiveis, dayfirst=True))
        selecao = pd.DataFrame(dias_proximos,index=dias_disponiveis)
        data_mais_proxima = selecao.sort_values(by=0,ascending=True).iloc[0].name
    else:
        data_mais_proxima = data
    return(data_mais_proxima)
    