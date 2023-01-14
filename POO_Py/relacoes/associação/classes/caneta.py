

class Caneta:
    
    def __init__(self, marca) -> None:
        self.__marca = marca
        
    @property # Getter
    def marca(self) -> str:
        return self.__marca
    
    def escrever(self) -> None:
        print('Caneta está escrevendo...')
    
    