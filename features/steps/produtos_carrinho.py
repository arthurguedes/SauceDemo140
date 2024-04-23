import time
from behave import given, when , then 
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'que entro no site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome() #instanciar o objeto do Selenium Webdriver especializado para o Chrome
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    context.driver.get("https://www.saucedemo.com")



@when(u'escrevo nos campos de login com usuario {usuario} and senha {senha}')
def step_impl(context, usuario , senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    


@then(u'sou direcionado para pagina Home and um produto entra no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"
    context.driver.quit()