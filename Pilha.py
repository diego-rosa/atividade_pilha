from Carro import Carro

class Pilha:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def addCarro(self,marcaC,modeloC,portas):
        carro = Carro(marcaC,modeloC,portas)
        if self.inicio == None:
            self.inicio = carro
            self.fim = carro
        else:
            self.fim.proximo = carro
            self.fim = carro
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia!\n--------------")
        else:
            print("---------------------\n")
            texto = ""
            aux = self.inicio
            while( aux ):
                texto += aux.marca + " - " + aux.modelo + " - "
                aux = aux.proximo
            print(texto)

    def remover(self):
        if self.inicio == None:
                print("Lista Vazia!\n--------------")
        else:
            if self.inicio.proximo == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.fim.proximo
            self.imprimir()
