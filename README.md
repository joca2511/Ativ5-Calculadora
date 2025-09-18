# Ativ5-Calculadora
## Membros
Alan Daiki,
Lucas Rezende,     
Rodrigo Simões Ruy, 
Romulo Canavesso    


# Executar todos os testes
python -m unittest testes.test_unidade
python -m unittest testes.test_integracao

# Executar com cobertura
coverage run -m unittest discover tests
coverage report
coverage html
# Executar teste especifico
python -m unittest testes.test_unidade.TestCalculadora.test_entrada_saida_soma -v