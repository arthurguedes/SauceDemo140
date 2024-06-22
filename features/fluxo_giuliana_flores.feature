Feature: Fluxo Giuliana Flores

Scenario: Criação usuário
    Given que acesso o site Giuliana Flores
    When digito os campos de cadastro
    Then cria uma nova conta 

Scenario: Login Negativo
    Given que acesso o site Giuliana Flores 
    When digito o campo de login com usuario arthur@hotmail.com e senha 1234
    Then exibe mensagem de login invalido 

Scenario: Login Positivo
    Given que acesso o site Giuliana Flores 
    When digito o campo de login com usuario bernar_otavio_ribeiro@hersa.com.br e senha 123456789ABcd
    Then exibe mensagem de login valido

Scenario: Fluxo Compra
    Given que acesso o site Giuliana Flores
    And faz login
    And seleciono produto no banner 
    And acesso o carrinho
    When aciono o botão comprar
    Then compra realizada com sucesso
    
