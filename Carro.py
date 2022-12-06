'''A classe carro é composta dos atributos marca, modelo e portas.
O atributo portas é fortemente privado.'''
from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self,marcaC, modeloC, portas):
        super().__init__(marcaC, modeloC)
        self.portas = portas
        self.proximo = None
'''
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Número de Portas: ",self.portas)
'''
