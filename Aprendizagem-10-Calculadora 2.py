class Calculadora:
    
    def soma(self, valor_a, valor_b): 
        return valor_a + valor_b 

    def subtracao(self, valor_a, valor_b): 
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b): 
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b): 
        return valor_a / valor_b

    def resto(self, valor_a, valor_b): 
        return valor_a % valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 20))
print(calculadora.multiplicacao(30, 20))
print(calculadora.divisao(30, 5))
print(calculadora.resto(400, 20))