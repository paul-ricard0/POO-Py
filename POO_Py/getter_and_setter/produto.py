
import re

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    
    # Getter
    @property  # é um decorador usado para indicar que isso é um get 
    def preco(self): # o nome da função é usado o mesmo nome da variavel 
        return self._preco #pode usar qualquer novo nome para o preco
    
    # Setter
    @preco.setter # é um decorador usado para indicar que isso é um get 
    def preco(self, valor): # o nome da função é usado o mesmo nome da variavel
        if isinstance(valor, str):
            valor = float(re.sub('[^0-9]', '', valor))
            
        self._preco = valor # tem que passar o mesmo nome que passsou no Getter
    

    # Getter
    @property
    def nome(self):
        return self._nome 
    
    # Setter
    @nome.setter
    def nome(self, valor):
        # Fazendo isso todo nome que eu passar no momento que crio o objeto vai alterar todos os A por @
        self._nome = valor.replace('A', '@')  
        
    
    
    
p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)


