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

@when(u'digito o campo de login com usuario arthurguedes@hotmail.com e senha 12345678')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("arthurguedes@hotmail.com")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").click()
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("12345678")
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()


@then(u'exibe mensagem de login invalido')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".font_erro").text == "e-mail ou senha inválidos!"
    context.driver.close()
  

