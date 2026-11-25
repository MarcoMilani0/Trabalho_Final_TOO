class Carreta:
    def __init__(self, modelo, capacidade_kg, extensao_m, eixos):
        if capacidade_kg <= 0:
            raise ValueError("A capacidade precisa ser maior que 0")
        if extensao_m <= 0:
            raise ValueError("A extensão precisa ser maior que 0")
        if eixos < 2:
            raise ValueError("A carreta precisa ter pelo menos 2 eixos")
        self.__modelo = modelo
        self.__capacidade_kg = capacidade_kg
        self.__extensao_m = extensao_m
        self.__eixos = eixos

    @property
    def modelo(self):
        return self.__modelo

    @property
    def capacidade_kg(self):
        return self.__capacidade_kg

    @property
    def extensao_m(self):
        return self.__extensao_m

    @property
    def eixos(self):
        return self.__eixos

    def __str__(self):
        return (f"Carreta {self.modelo} | {self.capacidade_kg} kg | "
                f"{self.extensao_m} m | {self.eixos} eixos")