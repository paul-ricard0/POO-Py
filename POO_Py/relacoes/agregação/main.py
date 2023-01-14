from classes.classes import Produto, CarirnhoDeCompras

carrinho = CarirnhoDeCompras()

p1 = Produto('Camiseta', 250)
p2 = Produto('iPhone', 100000)
p3 = Produto('Caneca', 30)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.listar_produtos()

print(carrinho.soma_total())