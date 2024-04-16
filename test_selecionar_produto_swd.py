# 1 - bibliotecas 
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classe (Opcional) 
class Teste_Produtos:
# 2.1 - Atributos 
    url = "https://www.saucedemo.com"                  #endereço do site alvo 

# 2.2 - Funções e métodos 
    def setup_method(self,method):                            # método de inicialização dos testes 
        self.driver = webdriver.Chrome()                 # instanciar o objeto do Selenium Webdriver como Chrome 
        self.driver.implicitly_wait(2)                # define o tempo de espera padrão por elementos em 10 segundos 

    def teardown_method(self,method):                       # finalização dos testes
        self.driver.quit()                           # destroi o objeto do selenium webdriver da memória 
        
    def test_selecionar_produto(self):         # método de teste 
        self.driver.get(self.url)                     # abre o navegador
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")  
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce") 



    
