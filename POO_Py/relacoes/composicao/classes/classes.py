

class Cliente:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.idade = idade
        self.enderecos = []
    
    
    @property
    def nome(self)-> str:
        return self.__nome
    
    def insere_endereco(self, cidade: str, estado: str) -> None:
        self.enderecos.append(Endereco(cidade, estado))
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')
        
class Endereco:
    
    def __init__(self, cidade: str, estado: str) -> None:
        self.cidade = cidade
        self.estado = estado
        
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')
    
    
     