from model.cavalo_mecanico import CavaloMecanico
from model.motorista import Motorista
from model.entrega import Entrega


class Transportadora:
    __instancia = None

    def __new__(cls, nome="Transportadora"):
        if cls.__instancia is None:
            instancia = super().__new__(cls)
            instancia.__nome = nome
            instancia.__cavalos = []
            instancia.__motoristas = []
            instancia.__entregas = []
            cls.__instancia = instancia
        return cls.__instancia

    @property
    def nome(self):
        return self.__nome

    @property
    def cavalos(self):
        return tuple(self.__cavalos)

    @property
    def motoristas(self):
        return tuple(self.__motoristas)

    @property
    def entregas(self):
        return tuple(self.__entregas)

    def cadastrar_cavalo(self, cavalo):
        if not isinstance(cavalo, CavaloMecanico):
            raise TypeError("O cavalo precisa ser um objeto CavaloMecanico")
        if any(c.placa == cavalo.placa for c in self.__cavalos):
            raise ValueError(f"Já existe um cavalo com a placa {cavalo.placa}")
        self.__cavalos.append(cavalo)

    def cadastrar_motorista(self, motorista):
        if not isinstance(motorista, Motorista):
            raise TypeError("O motorista precisa ser um objeto Motorista")
        if any(m.cnh == motorista.cnh for m in self.__motoristas):
            raise ValueError(f"Já existe um motorista com a CNH {motorista.cnh}")
        self.__motoristas.append(motorista)

    def abrir_entrega(self, motorista, cavalo, destino):
        if motorista not in self.__motoristas:
            raise ValueError("O motorista não está cadastrado na transportadora")
        if cavalo not in self.__cavalos:
            raise ValueError("O cavalo não está cadastrado na transportadora")
        entrega = Entrega(motorista, cavalo, destino)
        self.__entregas.append(entrega)
        return entrega

    def entregas_por_status(self, status):
        return [e for e in self.__entregas if e.status == status]

    def total_frete_entregue(self):
        return sum(e.carga.calcular_frete() for e in self.entregas_por_status("Entregue"))