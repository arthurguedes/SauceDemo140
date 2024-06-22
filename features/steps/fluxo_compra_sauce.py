import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get("https://www.saucedemo.com")


@when(u'digito os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

@then(u'entro na pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs"
    assert context.driver.find_element(By.CLASS_NAME, "title").text == "Products"


@when(u'insiro o produto Sauce Labs Backpack no carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()    


@then(u'verifico os campos titulo, preco e quantidade do produto Sauce Labs Backpack')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == 1
    context.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    assert context.driver.find_element(By.CLASS_NAME,"inventory_item_name").text == "Sauce Labs Bike Light"
    assert context.driver.find_element(By.CLASS_NAME,"inventory_item_price").text == "$ 9.99"

@then(u'removo o produto')
def step_impl(context):
    context.driver.find_element(By.ID,"remove-sauce-labs-bike-light").click()


@then(u'verifico que o carrinho esta vazio')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "0"


@then(u'faz logout')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()
    context.driver.quit()