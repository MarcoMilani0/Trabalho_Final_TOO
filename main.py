from model.carreta import Carreta
from model.cavalo_mecanico import CavaloMecanico
from model.carga_factory import CargaFactory
from model.motorista import Motorista
from model.entrega import Entrega
from model.transportadora import Transportadora


def main():
    carreta = Carreta("Randon 3 eixos", 30000, 14.5, 3)
    cavalo = CavaloMecanico("Scania R450", 450, "ABC1D23", 2020, carreta)
    motorista = Motorista("Carlos Silva", "12345678900", "E")

    print(motorista)
    print("Pode dirigir o conjunto:", motorista.pode_dirigir_conjunto())
    print(cavalo)

    carga = CargaFactory.criar("casca", nome="Arroz em casca", peso_kg=18000, percentual_sujeira=4)
    cavalo.carregar(carga)
    print("\nDepois de carregar:")
    print(cavalo)
    print(cavalo.carga)

    print("\n--- Erros de propósito ---")
    try:
        cavalo.carregar(CargaFactory.criar("ensacado", nome="Arroz tipo 1", quantidade_sacos=100))
    except ValueError as erro:
        print("Erro:", erro)

    cavalo.descarregar()
    print("\nDepois de descarregar:")
    print(cavalo)

    try:
        cavalo.carregar(CargaFactory.criar("palete", nome="Piso", quantidade_paletes=40, peso_palete_kg=1200))
    except ValueError as erro:
        print("Erro:", erro)

    try:
        cavalo.carregar("string")
    except TypeError as erro:
        print("Erro:", erro)

    try:
        CargaFactory.criar("soja", nome="Soja")
    except ValueError as erro:
        print("Erro:", erro)

    print("\n=== Entrega (State) ===")
    cavalo.carregar(CargaFactory.criar("ensacado", nome="Arroz tipo 1", quantidade_sacos=100))
    entrega = Entrega(motorista, cavalo, "Porto Alegre")
    print(entrega)

    entrega.iniciar()
    print(entrega)

    try:
        entrega.cancelar()
    except ValueError as erro:
        print("Erro:", erro)

    entrega.concluir()
    print(entrega)

    try:
        entrega.iniciar()
    except ValueError as erro:
        print("Erro:", erro)
        print("\n=== Transportadora (Singleton) ===")
    transportadora = Transportadora("Transportadora Exemplo")
    print("É a mesma instância:", transportadora is Transportadora())

    transportadora.cadastrar_cavalo(cavalo)
    transportadora.cadastrar_motorista(motorista)

    cavalo.descarregar()
    cavalo.carregar(CargaFactory.criar("palete", nome="Piso", quantidade_paletes=20, peso_palete_kg=1000))

    entrega2 = transportadora.abrir_entrega(motorista, cavalo, "Curitiba")
    entrega2.iniciar()
    entrega2.concluir()
    print(entrega2)

    print("Total de entregas:", len(transportadora.entregas))
    print(f"Frete das entregas concluídas: R$ {transportadora.total_frete_entregue():.2f}")

    try:
        transportadora.cadastrar_cavalo(cavalo)
    except ValueError as erro:
        print("Erro:", erro)


main()