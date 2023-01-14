"""
Outras linguagens usam: public, protected, private

Python:
_ privado fraco 
(Pode ser modificado, mas é unma convenção que quando se tem não é para se mudar)

__ privado forte
(Para ser acessado tem qeu usar _NOMECLASSE__nomeAtributo. 
Mas também é um convenção de que não se deve alterar nesse atributo)
"""

class BaseDeDados:
    
    def __init__(self) -> None:
        self.__dados = {} # Declarando uma lista com o privado forte 

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados: # Conferindo se não existe 'clientes' em dados 
            self.__dados['clientes'] = {id: nome} 
        else:
            self.__dados['clientes'].update({id: nome})
    
    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clintes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1,'Paulo')
bd.inserir_cliente(2, 'Ricardo')
bd.inserir_cliente(3, 'Lima')

#bd.__dados = 'OASDBNSNSAF' # vai da erro, PORQUE EU COLOQUEI __
#print(bd.__dados) ISSO DARIA ERRO NO CÓDIGO, PORQUE NÃO POSSO ACESSAR

bd.dados = 'daleee'
print(bd.dados) # VAI MOSTRAR O VALOR QUE CRIEI NA LINHA 36


print(bd._BaseDeDados__dados) # Aqui realmente vou acessar a variavel que protegida




