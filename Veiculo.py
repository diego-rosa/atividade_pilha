class Veiculo:

    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimirInformacoes(self):
        print("Marca: ",self.marca)
        print("Modelo: ",self.modelo)
