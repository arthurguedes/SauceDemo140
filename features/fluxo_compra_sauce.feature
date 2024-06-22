Feature: Fluxo de Compra

Scenario: Fluxo de compra "Sauce Labs Backpack"
    Given que acesso o site Sauce Demo
    When digito os campos de login com usuario standard_user e senha secret_sauce
    Then entro na pagina Home
    When insiro o produto Sauce Labs Backpack no carrinho 
    Then verifico os campos titulo, preco e quantidade do produto Sauce Labs Backpack
    And removo o produto 
    Then verifico que o carrinho esta vazio 
    And faz logout 