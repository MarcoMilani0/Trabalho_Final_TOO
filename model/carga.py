from abc import ABC, abstractmethod


class Carga(ABC):
    #classe abstrata
    #o nome é fixo depois de criada a carga.

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    def calcular_peso_kg(self):
        pass

    @abstractmethod
    def calcular_frete(self):
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}: {self.nome} | "
                f"{self.calcular_peso_kg():.0f} kg | "
                f"frete R$ {self.calcular_frete():.2f}")


class ArrozEmCasca(Carga):
    # A sujeira é peso que não é arroz, então reduz o valor do frete.
    VALOR_TONELADA = 120.0

    def __init__(self, nome, peso_kg, percentual_sujeira):
        super().__init__(nome)
        if peso_kg <= 0:
            raise ValueError("O peso precisa ser maior que 0")
        if not 0 <= percentual_sujeira <= 100:
            raise ValueError("A sujeira precisa estar entre 0 e 100%")
        self.__peso_kg = peso_kg
        self.__percentual_sujeira = percentual_sujeira

    @property
    def peso_kg(self):
        return self.__peso_kg

    @property
    def percentual_sujeira(self):
        return self.__percentual_sujeira

    def calcular_peso_kg(self):
        return self.__peso_kg

    def calcular_frete(self):
        toneladas = self.__peso_kg / 1000
        desconto = 1 - self.__percentual_sujeira / 100
        return toneladas * self.VALOR_TONELADA * desconto


class ArrozEnsacado(Carga):
    PESO_SACO_KG = 50
    VALOR_SACO = 2.5

    def __init__(self, nome, quantidade_sacos):
        super().__init__(nome)
        if quantidade_sacos <= 0:
            raise ValueError("A quantidade de sacos precisa ser maior que 0")
        self.__quantidade_sacos = quantidade_sacos

    @property
    def quantidade_sacos(self):
        return self.__quantidade_sacos

    def calcular_peso_kg(self):
        return self.__quantidade_sacos * self.PESO_SACO_KG

    def calcular_frete(self):
        return self.__quantidade_sacos * self.VALOR_SACO


class PaletePiso(Carga):
    VALOR_PALETE = 80.0
    ADICIONAL_PESADO = 20.0  

    def __init__(self, nome, quantidade_paletes, peso_palete_kg):
        super().__init__(nome)
        if quantidade_paletes <= 0:
            raise ValueError("A quantidade de paletes precisa ser maior que 0")
        if peso_palete_kg <= 0:
            raise ValueError("O peso do palete precisa ser maior que 0")
        self.__quantidade_paletes = quantidade_paletes
        self.__peso_palete_kg = peso_palete_kg

    @property
    def quantidade_paletes(self):
        return self.__quantidade_paletes

    @property
    def peso_palete_kg(self):
        return self.__peso_palete_kg

    def calcular_peso_kg(self):
        return self.__quantidade_paletes * self.__peso_palete_kg

    def calcular_frete(self):
        return self.__quantidade_paletes * (self.VALOR_PALETE + self.ADICIONAL_PESADO)