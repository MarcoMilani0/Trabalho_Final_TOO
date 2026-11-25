from abc import ABC, abstractmethod


class EstadoEntrega(ABC):

    @property
    @abstractmethod
    def nome(self):
        pass

    def iniciar(self, entrega):
        raise ValueError(f"Não é possível iniciar uma entrega {self.nome}")

    def concluir(self, entrega):
        raise ValueError(f"Não é possível concluir uma entrega {self.nome}")

    def cancelar(self, entrega):
        raise ValueError(f"Não é possível cancelar uma entrega {self.nome}")


class EstadoPendente(EstadoEntrega):
    @property
    def nome(self):
        return "Pendente"

    def iniciar(self, entrega):
        entrega._mudar_estado(EstadoEmTransito())

    def cancelar(self, entrega):
        entrega._mudar_estado(EstadoCancelada())


class EstadoEmTransito(EstadoEntrega):
    @property
    def nome(self):
        return "Em trânsito"

    def concluir(self, entrega):
        entrega._mudar_estado(EstadoEntregue())

class EstadoEntregue(EstadoEntrega):
    @property
    def nome(self):
        return "Entregue"


class EstadoCancelada(EstadoEntrega):
    @property
    def nome(self):
        return "Cancelada"