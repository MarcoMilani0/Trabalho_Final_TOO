from model.carreta import Carreta
from model.carga import Carga


class CavaloMecanico:


    def __init__(self, modelo, potencia_cv, placa, ano, carreta=None):
        if potencia_cv <= 0:
            raise ValueError("A potência precisa ser maior que 0")
        self.__modelo = modelo
        self.__potencia_cv = potencia_cv
        self.__placa = placa
        self.__ano = ano
        self.__carreta = None
        self.__carga = None
        if carreta is not None:
            self.acoplar_carreta(carreta)

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

    def tem_carreta(self):
        return self.__carreta is not None

    def esta_carregado(self):
        return self.__carga is not None

    def acoplar_carreta(self, carreta):
        if not isinstance(carreta, Carreta):
            raise TypeError("A carreta precisa ser um objeto Carreta")
        if self.tem_carreta():
            raise ValueError(f"O cavalo já está acoplado a uma carreta ({self.__carreta.modelo})")
        self.__carreta = carreta

    def carregar(self, carga):
        if not isinstance(carga, Carga):
            raise TypeError("Só é possível carregar objetos do tipo Carga")
        if not self.tem_carreta():
            raise ValueError("O cavalo precisa ter uma carreta acoplada para carregar")
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
        carreta = self.__carreta if self.tem_carreta() else "sem carreta"
        situacao = self.__carga.nome if self.esta_carregado() else "vazio"
        return (f"Cavalo {self.modelo} | placa {self.placa} | {self.ano} | "
                f"{self.potencia_cv} cv | {carreta} | carga: {situacao}")