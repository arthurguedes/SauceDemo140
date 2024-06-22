import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.get("https://www.giulianaflores.com.br/")

@when(u'digito os campos de cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    context.driver.find_element(By.NAME, "ctl00$ContentSite$txtName").send_keys("Bernardo Otavio Iago Ribeiro ")
    context.driver.find_element(By.NAME, "ctl00$ContentSite$txtCpf").send_keys("693.032.710-76")
    context.driver.find_element(By.NAME, "ctl00$ContentSite$txtEmail").send_keys("bernar_otavio_ribeiro@hersa.com.br")
    context.driver.find_element(By.NAME, "ctl00$ContentSite$txtPasswordNew").send_keys("123456789ABcd")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("61932-500")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_btnAddressFind").click()
    context.driver.find_element(By.NAME, "ctl00$ContentSite$CustomerAddress$txtAddressNumber").send_keys("250")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11952348954")

@then(u'cria uma nova conta')
def step_impl(context):
    context.driver.find_element(By.ID,"ContentSite_btnCreateCustomer").click()
    context.driver.close()

