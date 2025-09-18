# Ativ5-Calculadora
## Membros
Alan Daiki,
Lucas Rezende,     
Rodrigo Simões Ruy, 
Romulo Canavesso    

# Instalar dependencias
pip install -r requirements.txt

# Executar todos os testes
python -m unittest discover testes -v

# Gerar e ler relatorio

## Roda testes com cobertura
coverage run -m unittest discover testes

## Mostra relatório no terminal
coverage report

## (Opcional) Gera relatório visual em HTML
coverage html
start htmlcov/index.html  # No Windows

# Executar teste especifico
python -m unittest testes.test_unidade.TestCalculadora.test_entrada_saida_soma -v