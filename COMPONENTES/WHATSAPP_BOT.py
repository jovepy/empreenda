# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:18:42 2022

@author: rodrigo.jove
"""

from CONFIG_GERAL import *

contatos= []
grupos = []

EM_ATENDIMENTO = {0:[],1:[],2:[],3:[]}

#0 utilizado para clientes que ainda não enviaram a opcao
PROPRIETARIO_WPP = 'Rodrigo Jovê'

def GERENCIADOR_ATENDIMENTO(contato=str):
    


with open ('../CONFIGS/MSG_SAUDACAO.txt','r',encoding='utf8') as f:
    MSG_SAUDACAO = f.read()
    
def navegar_chrome():
    global driver    
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    prefs = {"download.default_directory" : '.\empreenda\ARQUIVOS\DOWNLOADS'} #LOCAL ONDE SEMPRE SERÁ BAIXADO OS ARQUIVOS, SEMPRE SERÃO APAGADOS APÓS O USO, SÓ É PARA TER UM ARQUIVO NESSA PASTA
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.set_window_position(0,0)
    driver.set_window_size(1600, 800)
    return(driver)

def retorna_back(driver):
    page_content= driver.page_source 
    back = bs(page_content, 'html.parser')
    return(back)


def inicio_contatos():
    contact_list = driver.find_element(by=By.XPATH, value='//*[@id="side"]/div[1]/div/label/div/div[2]')
    contact_list.click()
    contact_list.send_keys(Keys.TAB)
    
def muda_de_contato():    
    selected_contact = driver.find_element(by=By.XPATH, value='//div[@aria-selected="true" and @role="row"]')
    sleep(1)
    selected_contact.send_keys(Keys.ARROW_DOWN) 
    

def busca_tipo_contato():
    """
    Buscará se o contato é uma único ou um grupo.
    Essa aplicação não funciona o atendimento em grupos
    
    return(str)
    """
    nome = driver.find_element(by=By.XPATH, value='//*[@id="main"]/header/div[2]/div[1]/div/span') #encontra o nome 
    nome.click() #  
    site = retorna_back(driver)
    sleep(1)
    busca_tel = site.text.lower().split('sappdados do')[1] #se grupo sem imagem, acontece algo aqui
    tipo_contato = busca_tel[1:len('contato')+1]
    if str(tipo_contato) == 'contato':
        telefone = busca_tel.split('+')[1][:len('XX XX XXXX-XXXX')]    
        contatos.append(telefone)
    else:
        telefone = busca_tel.split('grupo')[1] 
        grupos.append(telefone)
    sair = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button')
    sleep(1)
    sair.click()
    return(telefone)


def enviar_mensagem(texto = str):
    digitar_mensagem = driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    digitar_mensagem.click()
    digitar_mensagem.send_keys(texto)
    enviar = driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    enviar.click()

def cria_dado_estruturado():
    
    """
    Retorna o histórico do contato na seguinte estrutura:
        quem enviou
        a hora e data q foi enviado
        conteúdo da mensagem
        
        return(dict(key:df))
    """
    site = retorna_back(driver)
    sleep(3)
    dados_estruturados = {}
    data_hora_dia_emissor = []
    auxiliar = str(site.find_all('div',class_="copyable-text")).split('data-pre-plain-text="')[1:] #lugar para buscar conversas, talvez seja a melhor tag q puxa tudo
    for tag in auxiliar:
        try:
            data_hora_dia_emissor.append(tag.split(': ">')[0])
        except:
            pass    
    data_hora_dia_emissor = pd.DataFrame(data_hora_dia_emissor)
    data_hora_dia_emissor = (data_hora_dia_emissor[0].str.replace('[','',regex=True).str.replace(', ','&',regex=True).str.replace('] ','&',regex=True)).str.split('&',expand=True)
    data_hora_dia_emissor.columns = ['Hora','Data','Emissor']
    conversa = []
    for i in list(range(len(auxiliar))):
        aux = ((auxiliar[i]).split('<span>')[-1].split('</span>')[0])
        if '<img alt="' in aux:
            conversa.append((aux.split('<img alt="')[1].split('" class'))[0])
        else:
            conversa.append(aux)
    historico = pd.DataFrame(conversa)
    historico.columns = ['Conversa']
    historico = pd.concat([historico,data_hora_dia_emissor],axis=1)
    dados_estruturados = {'Historico':historico}
    return(dados_estruturados)


def ROTINA_ATENDIMENTO():
    """
    Script principal onde a lógica principal está. O produto final se encontra aqui
    """
    driver = navegar_chrome()
    driver.get('https://web.whatsapp.com/')
    pyautogui.alert('Clique aqui após escanear','Aviso')
    inicio_contatos()
    sleep( 1 )
    hoje = date.today().strftime('%d/%m/%Y')
    atendendo = True
    agiliza_cont = 0
    while atendendo == True:
        telefone = busca_tipo_contato()
        dados_estruturados = cria_dado_estruturado()
        if dados_estruturados['Historico']['Data'].iloc[-1] == hoje:
            if telefone in contatos: #deixamos grupos de fora
            
                if dados_estruturados['Historico']['Emissor'].iloc[-1] != PROPRIETARIO_WPP: #apenas pessoas que ainda nao foram respondidas devem ser respondidas
                    #enviar_mensagem(MSG_SAUDACAO)
                    atendimento = True
                    n=0
                    
                    while atendimento == True: #momento que a pessoa fica em atendimento
                        dados_estruturados = cria_dado_estruturado() 
                        sleep(10) #tempo para a primeira resposta
                        if dados_estruturados['Historico']['Emissor'].iloc[-1] == PROPRIETARIO_WPP: #se agora a última mensagem é a minha, vamos esperar a resposta, mas não muito
                            if n <=2: #40 seg para cada resposta
                                sleep(10)
                                n+=1
                            
                            else: #quando o número de tentativas for atingido, coloque o telefone em espera e muda para o próximo
                                atendimento = False
                                EM_ATENDIMENTO[0].append(telefone)
                                muda_de_contato()
                                sleep(1)

                        else: #cliente respondeu e agora devemos entender a opção que ele busca
                            opcao = dados_estruturados['Historico']['Conversa'].iloc[-1]
                            if '1' in opcao:
                                enviar_mensagem(texto='Qual o serviço que você deseja saber o preço?')
                                print('funcao que busca o preco correspondente')
                                INFORMA_PRODUTO(txt=str)
                                #EM_ATENDIMENTO[1]
                            elif '2' in opcao:
                                enviar_mensagem(texto='Qual o serviço que você deseja agendar?')
                                print('funcao agendamento')
                                #EM_ATENDIMENTO[2]
                            elif '3' in opcao:
                                enviar_mensagem(texto='Que pena eu não conseguir te ajudar. Farei seu encaminhamento agora.')
                                print('encaminha para o atendimento humano')
                                #EM_ATENDIMENTO[3]
                            else:
                                print('Mantenha-se apenas às opções disponíveis, digite um número possível')
                                #enviar_mensagem(MSG_SAUDACAO)
                                
                            n=0 #zera a contagem do atendimento, pois respondeu e pode querer continuar
                
                else: #se eu dei a última mensagem, o atendimento foi encerrado ou a pessoa ainda não me respondeu
                    agiliza_cont +=1
                    if agiliza_cont <=10:
                        muda_de_contato() 
                        sleep(1)
                        telefone = busca_tipo_contato()
                        dados_estruturados = cria_dado_estruturado()
                    else:
                        inicio_contatos()
                        telefone = busca_tipo_contato()
                        dados_estruturados = cria_dado_estruturado()
            
            else: #se for um grupo muda para o próximo contato
                muda_de_contato()
                sleep(1)
            
        else: #se a última msg foi enviada ontem, ele retorna ao início
            for c in EM_ATENDIMENTO:
                #criar função para ir diretamente até o contato
                pass
            #após percorrer todos, retornará aos em atendimento para suprir a necessidade e só voltará a atender novos clientes quando os antigos estiverem ok
            #talvez criar um contator para q a cada 10 contatos seguidos ja respondidos voltar para o início dos contatos
            inicio_contatos()
            telefone = busca_tipo_contato()
            dados_estruturados = cria_dado_estruturado()

        
        driver.delete_all_cookies()
    