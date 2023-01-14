"""
Essa é relação mais fraca
quando deleta o objeto os outros continua existindo 
"""

from classes import escritor, caneta, maquinaDeEscrever


escritor = escritor.Escritor('Paulo')
caneta = caneta.Caneta('Bic')
maquina = maquinaDeEscrever.MaquinaDeEscrever()

# Estou passando o objeto maquina para a variavel ferramenta
escritor.ferramenta = maquina 

# Agora a variável ferramenta tem acesso aos métodos do objeto maquina, 
# já que ela recebeu o objeto como parâmetro 
escritor.ferramenta.escrever()