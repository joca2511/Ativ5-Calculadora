from ..src.calculadora import Calculadora

# Entrada e saída
def test_entrada_saida_soma(self):
    calc = Calculadora()
    resultado  = calc.somar(5,3)
    self.assertEqual(resultado,8)
def test_entrada_saida_soma2(self):
    calc = Calculadora()
    resultado = calc.somar(10,-3)
    self.assertEqual(resultado,7)
# Tipagem

def test_tipagem(self):
    calc = Calculadora()
    with self.assertRaises (TypeError):
        calc.somar(5,True) # Boolean no lugar de inteiro

def test_tipagem2(self):
    calc = Calculadora()
    res = calc.somer(5,1.2)
    self.assertEqual(res,6.2) # Soma de inteiro e float
    

# Consistência
def test_consistencia_historico(self):
    calc = Calculadora()
    calc.somar(2,3)
    calc.multiplicar(4,5)
    self.assertEqual(len(calc.historico),2)
    self.assertIn("2 + 3 = 5",calc.historico)
    self.assertIn("4 * 5 = 20", calc.historico)
def test_consistencia_historico2(self):
    calc = Calculadora()
    calc.dividir(25,3)
    calc.subtrair(10,-20)
    self.assertEqual(len(calc.historico),2)
    self.assertIn("25 / 3 = 8.333333333333334",calc.historico)
    self.assertIn("10 - -20 = 30",calc.historico)
# Inicialização
def test_inicializacao(self):
    calc = Calculadora()
    self.assertEqual(calc.resultado,0)
    self.assertEqual(len(calc.historico),0)
    
def test_inicializacao2(self):
    calc = Calculadora()
    with self.assertRaises(TypeError):
        calc.dividir()
# Modificação de dados
def test_modificacao_historico(self):
    calc = Calculadora()
    calc.somar(1,1)
    self.assertEqual(len(calc.historico),1)
    calc.limpar_historico()
    self.assertEqual(len(calc.historico),0)
def test_modificacao_historico2(self):
    calc = Calculadora()
    calc.dividir(35,2)
    self.assertEqual(len(calc.historico),1)
    calc.subtrair(25,-2)
    self.assertEqual(len(calc.historico),2)
# Limite Inferior

def test_limiteInferior(self):
    calc = Calculadora()
    
    #Teste com zero
    res = calc.somar(0,0)
    self.assertEqual(res, 0)

def test_limiteInferior2(self):
    calc = Calculadora()

    # Teste com infinito negativo
    res = calc.somar(1,float('-inf'))
    self.assertEqual(res, float('-inf'))
    

# Limite Superior

def test_limiteSuperior(self):
    calc = Calculadora()
    
    #Teste com números muito grandes
    res = calc.somar(823926748464,93282738436783)
    self.assertEqual(res, 94106665185247)

def test_limiteSuperior(self):
    calc = Calculadora()

    # Teste com infinito positivo
    res = calc.somar(1,float('inf'))
    self.assertEqual(res, float('inf'))

# Valores Fora do Intervalo

def test_foraDoIntervalo(self):
    calc = Calculadora()
    with self.assertRaises(ValueError):
        calc.dividir(2,0)

# Fluxos de Controle
def test_fluxos_divisao ( self ) :
    
    calc = Calculadora()
    # Caminho normal
    resultado = calc.dividir (10 , 2)
    self.assertEqual( resultado , 5)
    # Caminho de erro
    with self.assertRaises( ValueError ) :
        calc.dividir (10 , 0)
        
def test_fluxos_divisao2 ( self ) :
    calc = Calculadora()
    resultado = calc.dividir(200,32)
    self.asserEqual(resultado,6.25)
    with self.assertRaises(ValueError):
        calc.dividir(200,0)

# Mensagens de Erro
def test_mensagens_erro(self):
    calc = Calculadora()
    try:
        calc.dividir(5,0)
    except ValueError as e:
        self.assertEqual(str(e)," Divisao por zero nao permitida ")
def test_mensagens_erro2(self):
    calc = Calculadora()
    try:
        calc.multiplicar(20,"vinte")
    except ValueError as e:
        self.assertEqual(str(e)," Argumentos devem ser numeros ")
