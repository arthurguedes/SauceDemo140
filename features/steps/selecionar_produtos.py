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

#Preencher com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} and senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

#Preencher com usuario branco e senha
@when(u'preencho os campos de login com usuario and senha {senha}')
def step_impl(context, senha):
    #context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

#Preencher com usuario mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} and senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    #context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

#Clica no botão de login sem ter preenchido o usuario e senha
@when(u'preencho os campos de login com usuario and senha ')
def step_impl(context):
    #context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    #context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()


#Preencher com usuario e senha através da decisão (IF)
@when(u'digito os campos de login com usuario {usuario} and senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    
    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)

    context.driver.find_element(By.ID, "login-button").click()



    
#Verifica para mensagem outline 
@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2)

    #teardown / encerramento 
    context.driver.quit()



@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"
    context.driver.quit()

#verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem
    context.driver.quit()   
