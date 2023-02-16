# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import os
import shutil
import threading
from datetime import time

import selenium as selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)

qdb = [15786,22059,24148,24149,15787,22061,15788,22068,22073,15790,1792,26086,31026,31024,38489]
makeB= [2202,148,1897,22060,1898,149,215,22066,22071,384,179,1899]
intense= [2184,138,24966,1854,151,210,22065,22070,1283,791,1855]

estrMakes = [makeB, intense]

lista = []

cds = [1100,994,649,1329,1317,1283]

ciclos = ['01/2022','02/2022','03/2022','04/2022','05/2022','06/2022','07/2022','08/2022','09/2022','10/2022','11/2022','12/2022','13/2022','14/2022','15/2022','16/2022','17/2022','01/2023']

raizDir = "C:\\Users\\estevao.silva\\Desktop\\"

def login_sgi(email, password):
    print("entrando com usuário e senha")
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html/body/form/main"))
    )
    driver.find_element(By.XPATH, '/html/body/form/main/div[2]/div/div[2]/div[1]/input').send_keys(email)
    driver.find_element(By.XPATH, '/html/body/form/main/div[2]/div/div[2]/div[3]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/form/main/div[3]/button/span[1]').click()


def close_notice():
    print("fechando a noticia")
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "pnlAvisoImportante"))
        )
        driver.find_element(By.XPATH, '/html/body/form/div[4]/div/div/a').click()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


def first_acess(url):
    print("realizando o primeiro acesso ao Gera")
    driver.get(url)
    login_sgi("estevao.silva@gruponatureza.adm.br", "E$tv2022")
  #  close_notice()


def relatorio_vendas_corte_em_pedidos():
    print("navegando até o relatório de 'Vendas/Cortes em Pedidos'.")
    driver.execute_script("__acao('navegar', '1028')")
    selector_element_by_id("ContentPlaceHolder1_situacaoDropDown_d1","Entregue").click()
    selector_element_by_id("ContentPlaceHolder1_seletorBuscaDropDown_d1","Por Produto").click()
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_produtoPanel')))
    codModComercial = driver.find_element(By.ID, 'ContentPlaceHolder1_txtCodigoModeloComercial_T2')
    codModComercial.send_keys(3)
    driver.find_element(By.ID,'ContentPlaceHolder1_modeloComercial_T2').click()
    WebDriverWait(driver, 3).until_not(EC.text_to_be_present_in_element_value((By.ID,"ContentPlaceHolder1_modeloComercial_T2"), "aguarde..."))
    selector_element_by_id("ContentPlaceHolder1_tipoItemPedidoDropDown_d1", "Venda").click()
    selector_element_by_id('ContentPlaceHolder1_tipoBuscaItemDropDown_d1', 'Item Pedido').click()
    selector_element_by_id('ContentPlaceHolder1_tipoRelatProdutoDropDown_d1', 'Analítico').click()
    for ciclo in ciclos:
        selector_element_by_id('ContentPlaceHolder1_campanhaInicioDropDown_d1', ciclo).click()
        selector_element_by_id('ContentPlaceHolder1_campanhaTerminoDropDown_d1', ciclo).click()
        for cd in cds:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_cenCanalDistribuicao_T2")))
            driver.find_element(By.ID, "ContentPlaceHolder1_cenCanalDistribuicao_T2").send_keys(cd)
            driver.find_element(By.ID,"ContentPlaceHolder1_descricaoCDTextbox_T2").click()
            WebDriverWait(driver, 30).until_not(EC.text_to_be_present_in_element_value((By.ID,"ContentPlaceHolder1_descricaoCDTextbox_T2"), "aguarde..."))
            for codEstrProd in lista:
                selector_element_by_xpath("ContentPlaceHolder1_seletorBuscaDropDown_d1", '//*[@id="ContentPlaceHolder1_seletorBuscaDropDown_d1"]/option[1]').click()
                selector_element_by_id("ContentPlaceHolder1_seletorBuscaDropDown_d1", "Por Produto").click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_listaEstruturaProduto_T2")))
                selector_element_by_id('ContentPlaceHolder1_ddlTipoEstruturaProduto_d1', 'Buscar 1').click()
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlTipoEstruturaProduto_d1")))
                selector_element_by_id('ContentPlaceHolder1_ddlTipoEstruturaProduto_d1', 'Preencher manualmente').click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_listaEstruturaProduto_T2")))
                driver.find_element(By.ID,'ContentPlaceHolder1_listaEstruturaProduto_T2').clear()
                driver.find_element(By.ID,'ContentPlaceHolder1_listaEstruturaProduto_T2').send_keys(codEstrProd)
                driver.find_element(By.ID, 'ContentPlaceHolder1_txtProdutoDescricao_T2').click()
                WebDriverWait(driver, 60).until_not(EC.text_to_be_present_in_element_value((By.ID, "ContentPlaceHolder1_txtEstruturaProdutoDescricao_T2"),"aguarde..."))
                driver.find_element(By.ID,'ContentPlaceHolder1_buscarButton_btn').click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UpdateProgress1" and @style="display: block;"]')))
                WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="UpdateProgress1" and @style="display: none;"]')))
                if EC._element_if_visible(driver.find_element(By.ID, 'mensagemPanel'), True):
                    if driver.find_element(By.ID, 'msgAlert').text == 'Ocorreu um problema ao acessar o sistema. Verifique as ações realizadas e tente novamente. (663)':
                        driver.find_element(By.ID, 'popupOkButton').click()
                        lista.remove(codEstrProd)
                        lista.append(codEstrProd)
                        pass
                    elif driver.find_element(By.ID, 'mensagemLabel').text == 'Nenhum item de pedido encontrado':
                        estrMakes.remove(codEstrProd)
                        lista.find_element(By.ID, 'popupOkButton').click()
                        lista.find_element(By.ID, 'ContentPlaceHolder1_Img1').click()
                        pass
                else:
                    WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID,'ContentPlaceHolder1_exportarButton2_btn')))
                    driver.find_element(By.ID, 'ContentPlaceHolder1_exportarButton2_btn').click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='agendamentoExportacao_exportarPanel']/div/div/div[2]/div[1]/div/div/div[2]/ul/li[2]"))).click()
                    driver.find_element(By.XPATH, "//*[@id='agendamentoExportacao_colunasTab']/div[1]/div/div/label[@class='h2-title col-md-2 text-uppercase']").click()
                    driver.find_element(By.ID, 'agendamentoExportacao_okButton_B1').click()
                    main_page = driver.current_window_handle
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="UpdateProgress1" and @style="display: block;"]')))
                    WebDriverWait(driver, 300).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="UpdateProgress1" and @style="display: none;"]')))
                    driver.execute_script("window.open('');")
                    han = driver.window_handles
                    print("handles:", han)
                    driver.switch_to.window(driver.window_handles[2])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
                    get_file_and_store(driver, cd, ciclo, codEstrProd)
                    driver.switch_to.window(main_page)

def get_file_and_store(driver, cd, ciclo, codEstrProd):
    driver.get("chrome://downloads/")
     # return the file name once the download is completed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/downloads-manager//div[2]/iron-list/downloads-item[1]//div[2]/div[2]/div[4]/span[1]/a')))
    filePath = driver.find_element(By.XPATH, '/html/body/downloads-manager//div[2]/iron-list/downloads-item[1]//div[2]/div[2]/div[4]/span[1]/a').get_attribute("attribute name")
    print(filePath)


def move_file(fromPath, toPath, fileName):
    oldFileName = fromPath.stem
    newFileName = fromPath.replace(oldFileName, fileName)
    os.rename(fromPath, newFileName)
    shutil.move(newFileName, toPath)

def selector_element_by_id(id, optionText):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id)))
        driver.find_element(By.ID, id).click()
        xpath=f'//*[@id="{id}"]/option[text()="{optionText}"]'
        return driver.find_element(By.XPATH,xpath)
    except ElementNotInteractableException as error:
        print(error)

def selector_element_by_xpath(id, optionText):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, optionText)))
        driver.find_element(By.ID, id).click()
        return driver.find_element(By.XPATH,optionText)
    except ElementNotInteractableException as error:
        print(error)

def abrir_listas(lista, n):
    buckts = [[],[]]
    for buckt in buckts:
        while len(buckt) < n:
            buckt.append(lista.pop())
    return  buckts

def join_listas(listas):
    result = []
    for lista in listas:
        text = str()
        for l in lista:
            if text == str():
                text = str(l)
            else:
                text = text + ";"
                text = text + str(l)
        result.append(text)
    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for l in estrMakes:
        for i in l:
            lista.append(i)
    lista = abrir_listas(lista, 5)
    lista = join_listas(lista)
    url = "https://sgi.e-boticario.com.br/Paginas/Acesso/Entrar.aspx?ReturnUrl=%2fDefault.aspx"
    first_acess(url)
    relatorio_vendas_corte_em_pedidos()
    driver.close()
    driver.quit()
    exit()










