class Motorista:

    CATEGORIAS_VALIDAS = ("A", "B", "C", "D", "E")

    def __init__(self, nome, cnh, categoria):
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoria inválida: '{categoria}'")
        self.__nome = nome
        self.__cnh = cnh
        self.__categoria = categoria

    @property
    def nome(self):
        return self.__nome

    @property
    def cnh(self):
        return self.__cnh

    @property
    def categoria(self):
        return self.__categoria

    def pode_dirigir_conjunto(self):
        # cavalo mecânico com carreta exige categoria E
        return self.__categoria == "E"

    def __str__(self):
        return f"Motorista {self.nome} | CNH {self.cnh} | categoria {self.categoria}" 