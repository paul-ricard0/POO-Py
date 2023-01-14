

class CarirnhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []

    def inserir_produto(self, produto) -> None:
        self.produtos.append(produto)
        
    def listar_produtos(self) -> None:
        for produto in self.produtos:
            print(produto.name, produto.valor)
    
    def soma_total(self) -> float:
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
    
    
  
class Produto:
    def __init__(self, name: str, valor: float) -> None:
        self.name = name
        self.valor = valor