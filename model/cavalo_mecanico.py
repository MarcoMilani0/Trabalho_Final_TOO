from model.carreta import Carreta
from model.carga import Carga


class CavaloMecanico:


    def __init__(self, modelo, potencia_cv, placa, ano, carreta):
        if potencia_cv <= 0:
            raise ValueError("A potência precisa ser maior que 0")
        if not isinstance(carreta, Carreta):
            raise TypeError("A carreta precisa ser um objeto Carreta")
        self.__modelo = modelo
        self.__potencia_cv = potencia_cv
        self.__placa = placa
        self.__ano = ano
        self.__carreta = carreta
        self.__carga = None

    @property
    def modelo(self):
        return self.__modelo

    @property
    def potencia_cv(self):
        return self.__potencia_cv

    @property
    def placa(self):
        return self.__placa

    @property
    def ano(self):
        return self.__ano

    @property
    def carreta(self):
        return self.__carreta

    @property
    def carga(self):
        return self.__carga

    def esta_carregado(self):
        return self.__carga is not None

    def carregar(self, carga):
        if not isinstance(carga, Carga):
            raise TypeError("Só é possível carregar objetos do tipo Carga")
        if self.esta_carregado():
            raise ValueError(f"O conjunto já está carregado com '{self.__carga.nome}'")
        if carga.calcular_peso_kg() > self.__carreta.capacidade_kg:
            raise ValueError(
                f"Carga de {carga.calcular_peso_kg():.0f} kg excede a capacidade "
                f"da carreta de {self.__carreta.capacidade_kg:.0f} kg"
            )
        self.__carga = carga

    def descarregar(self):
        if not self.esta_carregado():
            raise ValueError("O conjunto não está carregado")
        carga = self.__carga
        self.__carga = None
        return carga

    def __str__(self):
        situacao = self.__carga.nome if self.esta_carregado() else "vazio"
        return (f"Cavalo {self.modelo} | placa {self.placa} | {self.ano} | "
                f"{self.potencia_cv} cv | {self.carreta} | carga: {situacao}")