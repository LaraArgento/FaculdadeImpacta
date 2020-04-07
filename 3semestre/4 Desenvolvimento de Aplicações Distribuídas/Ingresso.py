
'''
Crie uma classe chamada Ingresso que possua um atributo valor e um 
método __str__() que retorne à informação do valor do ingresso. 

Crie uma classe IngressoVIP, que herda de Ingresso e possui um atributo
valor Adicional. O método __str__() da classe IngressoVIP deve considerar
que o valor do ingresso é o valor da superclasse somado ao valor Adicional do IngressoVIP. 
Crie uma classe para testar os objetos das classes Ingresso e IngressoVIP
Crie uma classe ColetorDeIngresso que recebe os ingressos e devolve o valor total.

'''

class Ingresso():
	def __init__(self, valor): 
		super(Ingresso, self).__init__()
		self.valor = valor

	def __str__(self):
		return str(self.valor)


class IngressoVIP():
	adicional = -2.00

	def __init__(self):
		super(self)

	def __str__(self):
		return str(self.valor + self.adicional)


