import time
from behave import given, when , then 
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que tem acesso ao site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(2)
    context.driver.maximize_window()
    context.driver.get("https://www.giulianaflores.com.br/")


@when(u'faço login com usuario and senha')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Entre ou cadastre-se").click()
    context.driver.find_element(By.ID, "btnIntentNewCustomer").click()
    context.driver.find_element(By.ID, "btnNewCustomer").click()
    context.driver.find_element(By.ID, "dsName").send_keys("Bernardo Otavio Iago Ribeiro ")
    context.driver.find_element(By.ID, "dsCPF").send_keys("693.032.710-76")
    context.driver.find_element(By.ID, "dsEmail").send_keys("bernardo_otavio_ribeiro@hersa.com.br")
    context.driver.find_element(By.ID, "dsPassword").send_keys("123456789abcd")
    context.driver.find_element(By.ID, "dsPhone").send_keys("(27) 98343-9176")
    context.driver.find_element(By.ID, "dsZip").send_keys("29940-766")
    context.driver.find_element(By.ID, "dsNumber").send_keys("11")
    context.driver.find_element(By.ID, "dsComplement").send_keys("11")
    context.driver.find_element(By.ID, "btnCreateCustomer").click()
    assert context.driver.find_element(By.LINK_TEXT, "Olá, Bernardo!").text == "Olá, Bernardo!" 
    context.driver.find_element(By.LINK_TEXT, "Olá, Bernardo!").click()
    context.driver.find_element(By.LINK_TEXT, "Sair").click()
    context.driver.find_element(By.LINK_TEXT, "Entre ou cadastre-se").click()
    context.driver.find_element(By.ID, "User").send_keys("bernardo_otavio_ribeiro@hersa.com.br")
    context.driver.find_element(By.ID, "dsPassword").send_keys("123456789abcd")
    context.driver.find_element(By.ID, "User").click()
    context.driver.find_element(By.ID, "dsPassword").click()
    context.driver.find_element(By.ID, "dsPassword").click()
    context.driver.find_element(By.ID, "dsPassword").send_keys("12345678abcd")
    context.driver.find_element(By.ID, "btnContinue").click()
    context.driver.find_element(By.ID, "dsPassword").send_keys("123456789abcd")


@then(u'usuario logado')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "li").text == "E-mail ou senha inválidos!"
    context.driver.find_element(By.ID, "btnContinue").click()
    context.driver.find_element(By.ID, "dsPassword").send_keys("12345678abcde")
    context.driver.find_element(By.ID, "btnContinue").click()
    assert context.driver.find_element(By.LINK_TEXT, "Olá, Bernardo!").text == "Olá, Bernardo!"
    context.driver.find_element(By.CSS_SELECTOR, ".header__menulogo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-next .back").click() 
    context.driver.find_element(By.CSS_SELECTOR, ".modal-header > .btn-close").click()
    context.driver.find_element(By.XPATH, "//img[@alt=\'Vaso na Primeira Entrega\']").click()
    context.driver.find_element(By.LINK_TEXT, "Olá, Bernardo!").click()
    context.driver.find_element(By.LINK_TEXT, "Sair").click() 
    context.driver.quit()
