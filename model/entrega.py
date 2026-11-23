from model.motorista import Motorista
from model.cavalo_mecanico import CavaloMecanico
from model.estados import EstadoPendente


class Entrega:
    # Todos os atributos são fixos, exceto o estado, que muda pelo
    # padrão State. O estado só é alterado pelos métodos iniciar(),
    # concluir() e cancelar(), nunca direto de fora.

    def __init__(self, motorista, cavalo, destino):
        if not isinstance(motorista, Motorista):
            raise TypeError("O motorista precisa ser um objeto Motorista")
        if not isinstance(cavalo, CavaloMecanico):
            raise TypeError("O cavalo precisa ser um objeto CavaloMecanico")
        if not motorista.pode_dirigir_conjunto():
            raise ValueError("O motorista precisa ter CNH categoria E para dirigir o conjunto")
        if not cavalo.esta_carregado():
            raise ValueError("O conjunto precisa estar carregado para criar a entrega")
        if not destino:
            raise ValueError("O destino não pode ser vazio")
        self.__motorista = motorista
        self.__cavalo = cavalo
        self.__carga = cavalo.carga
        self.__destino = destino
        self.__estado = EstadoPendente()

    @property
    def motorista(self):
        return self.__motorista

    @property
    def cavalo(self):
        return self.__cavalo

    @property
    def carga(self):
        return self.__carga

    @property
    def destino(self):
        return self.__destino

    @property
    def status(self):
        return self.__estado.nome

    def iniciar(self):
        self.__estado.iniciar(self)

    def concluir(self):
        self.__estado.concluir(self)

    def cancelar(self):
        self.__estado.cancelar(self)

    def _mudar_estado(self, novo_estado):
        # uso interno: chamado pelas classes de estado
        self.__estado = novo_estado

    def __str__(self):
        return (f"Entrega para {self.destino} | {self.carga.nome} | "
                f"motorista {self.motorista.nome} | status: {self.status}")