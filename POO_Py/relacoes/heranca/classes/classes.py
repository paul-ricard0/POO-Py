class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} Falando...')
    
    
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} Comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} Estudando...')
    