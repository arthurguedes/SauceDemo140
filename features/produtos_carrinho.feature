Feature: Produtos Carrinho 

    Scenario: Selecionar Produto 
        Given que entro no site Sauce Demo
        When escrevo nos campos de login com usuario standard_user and senha secret_sauce
        Then sou direcionado para pagina Home and um produto entra no carrinho 