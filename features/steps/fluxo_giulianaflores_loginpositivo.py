import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.get("https://www.giulianaflores.com.br/")

@when(u'digito o campo de login com usuario bernar_otavio_ribeiro@hersa.com.br e senha 123456789ABcd')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("bernar_otavio_ribeiro@hersa.com.br")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("123456789ABcd")
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()


@then(u'exibe mensagem de login valido')
def step_impl(context):
    assert context.driver.find_element(By.ID, "lblWelcome").text == "Bom Dia, Bernardo!"
    context.driver.find_element(By.CSS_SELECTOR, "li > a:nth-child(2)").click()
    context.driver.close()
  

