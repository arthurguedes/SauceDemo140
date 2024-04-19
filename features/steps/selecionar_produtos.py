# 1 - Bibliotecas / Imports 
import time
from behave import given, when , then 
from selenium import webdriver
from selenium.webdriver.common.by import By




@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome() #instanciar o objeto do Selenium Webdriver especializado para o Chrome
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.saucedemo.com")

@when(u'preencho os campos de login com usuario {usuario} and senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

    

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2)

    #teardown / encerramento 
    context.driver.quit()
    
