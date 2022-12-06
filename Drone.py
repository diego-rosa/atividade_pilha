from Veiculo import Veiculo

class Drone(Veiculo):

    def __init__(self,marcaD, modeloD, qtdHelices):
        super().__init__(marcaD, modeloD)
        self.qtdHelices = qtdHelices
        self.proximo = None

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Número de Hélices: ",self.qtdHelices)

'''
A classe drone é composta dos atributos marca, modelo e quantidade de hélices.
O atributo quantidade de hélices é fracamente privado.
'''
