# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestegiulianaflores():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(2)
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testegiulianaflores(self):
    self.driver.get("https://www.giulianaflores.com.br/")
    self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("arthurguedes@hotmail.com")
    self.driver.find_element(By.ID, "ContentSite_txtPassword").click()
    self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("12345678")
    self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".font_erro").text == "e-mail ou senha inválidos!"
    self.driver.close()
  
  