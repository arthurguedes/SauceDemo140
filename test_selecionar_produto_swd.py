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
        self.driver.maximize_window()

    def teardown_method(self,method):                       # finalização dos testes
        self.driver.quit()                           # destroi o objeto do selenium webdriver da memória 
        
    def test_selecionar_produto(self):         # método de teste 
        self.driver.get(self.url)                     # abre o navegador
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")  
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR,"input.submit-button.btn_action").click()

        #transição de página 
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(N) .inventory_item_price").text == "$29.99"

        #inclusão no carrinho 
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text == "1"

        #verificação do produto no carrinho 
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        assert self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1"
        assert self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text == "$29.99"

        #remoção de produto 
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        #logout 
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        self.driver.close()







