# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

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
    close_notice()

def relatorio_vendas_corte_em_pedidos():
    print("navegando até o relatório de 'Vendas/Cortes em Pedidos'.")
    driver.execute_script("__acao('navegar', '1028')")
    driver.find_element(By.ID, "ContentPlaceHolder1_situacaoDropDown_d1").click()
    driver.find_element(By.XPATH, "/html/body/form/div[4]/div[13]/div/div/div[2]/div/div[1]/span[1]/select/option[5]").click()
    driver.find_element(By.ID, "ContentPlaceHolder1_seletorBuscaDropDown_d1").click()
    driver.find_element(By.XPATH, "/html/body/form/div[4]/div[13]/div/div/div[2]/div/div[1]/span[2]/select/option[2]").click()
    selector_element_by_id("ContentPlaceHolder1_campanhaInicioDropDown_d1","02/2023").click()
    driver.find_element(By.ID, "ContentPlaceHolder1_txtEstruturaComercialCodigo_T2").send_keys(649)
    driver.find_element(By.ID, 'ContentPlaceHolder1_txtCodigoModeloComercial_T2').send_keys(3)
    driver.find_element(By.ID, 'ContentPlaceHolder1_tipoItemPedidoDropDown_d1').click()
    selector_element_by_id("ContentPlaceHolder1_tipoItemPedidoDropDown_d1","Venda").click()
    selector_element_by_id('ContentPlaceHolder1_tipoBuscaItemDropDown_d1','Item Pedido').click()


def selector_element_by_id(id, optionText):
    driver.find_element(By.ID, id).click()
    xpath=f'//*[@id="{id}"]/option[text()="{optionText}"]'
    return driver.find_element(By.XPATH,xpath)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://sgi.e-boticario.com.br/Paginas/Acesso/Entrar.aspx?ReturnUrl=%2fDefault.aspx"
    first_acess(url)
    relatorio_vendas_corte_em_pedidos()










