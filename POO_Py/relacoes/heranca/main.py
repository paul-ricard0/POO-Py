from classes.classes import Cliente, Aluno

c1 = Cliente("Paulo", 21)
print(c1.nome)
c1.falar()
c1.comprar()

print()

a1 = Aluno("Lucas", 15)
print(a1.nome)
a1.falar()
a1.estudar()