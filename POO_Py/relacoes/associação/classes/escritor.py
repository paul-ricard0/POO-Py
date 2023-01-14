

class Escritor:
    
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__ferramenta = None
    
    @property # Getter
    def nome(self) -> str:
        return self.__nome
    
    @property # Getter
    def ferramenta(self) -> str:
        return self.__ferramenta
    
    @ferramenta.setter # Setter
    def ferramenta(self, ferramenta) -> None:
        self.__ferramenta = ferramenta


