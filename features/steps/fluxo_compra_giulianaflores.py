import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(2)
    context.driver.maximize_window()
    context.driver.get("https://www.giulianaflores.com.br/")
    

@when(u'aciono o botão comprar')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("bernar_otavio_ribeiro@hersa.com.br")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("123456789ABcd")
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    context.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .product-item img").click()
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    context.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZip").click()
    context.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZip").send_keys("01320")
    context.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZipComplement").send_keys("000")
    context.driver.find_element(By.CSS_SELECTOR, ".jSelectZip").click()
    context.driver.execute_script("window.scrollTo(0,282)")
    context.driver.execute_script("window.scrollTo(0,289)")
    context.driver.find_element(By.ID, "btConfirmShippingData").click()
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()
    context.driver.find_element(By.ID, "btnContinue").click()
    context.driver.execute_script("window.scrollTo(0,1502)")
    context.driver.find_element(By.ID, "txtDsDestinationName").click()
    context.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Johnny")
    context.driver.find_element(By.ID, "txtDsNumber").click()
    context.driver.find_element(By.ID, "txtDsNumber").send_keys("355")
    context.driver.find_element(By.ID, "ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0").click()
    context.driver.find_element(By.ID, "btnContinue").click()

@then(u'compra realizada com sucesso')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".chamadaPagamento").text == "Selecione a forma de pagamento de sua preferência"
    context.driver.close()
  