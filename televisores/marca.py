class Marca:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre: str) -> None:
        self.__nombre = nombre