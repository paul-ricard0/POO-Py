from classes.classes import Cliente

cliente1 = Cliente('Paulo', 21)
cliente1.insere_endereco('Belo Horizonte', 'MG')

print(cliente1.nome)
cliente1.lista_enderecos()
print('############## AGORA VOU DELETAR O CLIENTE1 E POR ISSO VAI DELETAR O ENDEREÇOS ASSOCIADOS A ELE ##############')
del cliente1
print()


cliente2 = Cliente('João', 30)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')

print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Carla', 15)
cliente3.insere_endereco('Salvador', 'BA')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('############## AGORA O COLETOR DE LIXO VAI DELETAR O CLIENTE ######################')