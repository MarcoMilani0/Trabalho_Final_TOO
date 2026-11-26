import os
import subprocess
import sys

from model.carreta import Carreta
from model.cavalo_mecanico import CavaloMecanico
from model.carga_factory import CargaFactory
from model.motorista import Motorista
from model.transportadora import Transportadora


class Menu:
    CAMPOS_CARGA = {
        "casca": [
            ("peso_kg", "Peso (kg): ", float),
            ("percentual_sujeira", "Sujeira (%): ", float),
        ],
        "ensacado": [
            ("quantidade_sacos", "Quantidade de sacos: ", int),
        ],
        "palete": [
            ("quantidade_paletes", "Quantidade de paletes: ", int),
            ("peso_palete_kg", "Peso de cada palete (kg): ", float),
        ],
    }

    def __init__(self):
        self.__transportadora = Transportadora("Transportadora")

    def _ler_texto(self, mensagem):
        while True:
            texto = input(mensagem).strip()
            if texto:
                return texto
            print("O valor não pode ser vazio.")

    def _ler_numero(self, mensagem, tipo=float):
        while True:
            try:
                return tipo(input(mensagem))
            except ValueError:
                print("Valor inválido, digite um número.")

    def _escolher(self, itens, titulo):
        if not itens:
            print(f"Não há registros em '{titulo}'.")
            return None
        print(f"\n{titulo}:")
        for i, item in enumerate(itens, start=1):
            print(f"{i} - {item}")
        indice = self._ler_numero("Escolha o número: ", int)
        if not 1 <= indice <= len(itens):
            print("Opção inexistente.")
            return None
        return itens[indice - 1]

    def _conjuntos(self):
        return [c for c in self.__transportadora.cavalos if c.tem_carreta()]

    def cadastrar_cavalo(self):
        cavalo = CavaloMecanico(
            self._ler_texto("Modelo: "),
            self._ler_numero("Potência (cv): "),
            self._ler_texto("Placa: ").upper(),
            self._ler_numero("Ano: ", int),
        )
        self.__transportadora.cadastrar_cavalo(cavalo)
        print("Cavalo cadastrado com sucesso (ainda sem carreta).")

    def cadastrar_carreta(self):
        carreta = Carreta(
            self._ler_texto("Modelo da carreta: "),
            self._ler_numero("Capacidade (kg): "),
            self._ler_numero("Extensão (m): "),
            self._ler_numero("Quantidade de eixos: ", int),
        )
        self.__transportadora.cadastrar_carreta(carreta)
        print("Carreta cadastrada com sucesso.")

    def formar_conjunto(self):
        cavalos_sem_carreta = [c for c in self.__transportadora.cavalos if not c.tem_carreta()]
        cavalo = self._escolher(cavalos_sem_carreta, "Cavalos sem carreta")
        if cavalo is None:
            return
        carreta = self._escolher(list(self.__transportadora.carretas_livres), "Carretas livres")
        if carreta is None:
            return
        self.__transportadora.formar_conjunto(cavalo, carreta)
        print(f"Conjunto formado: {cavalo}")

    def cadastrar_motorista(self):
        motorista = Motorista(
            self._ler_texto("Nome: "),
            self._ler_texto("CNH: "),
            self._ler_texto("Categoria (A, B, C, D ou E): ").upper(),
        )
        self.__transportadora.cadastrar_motorista(motorista)
        print("Motorista cadastrado com sucesso.")

    def carregar_conjunto(self):
        cavalo = self._escolher(self._conjuntos(), "Conjuntos")
        if cavalo is None:
            return
        print("Tipos de carga: casca, ensacado, palete")
        tipo = self._ler_texto("Tipo: ").lower()
        campos = self.CAMPOS_CARGA.get(tipo)
        if campos is None:
            raise ValueError(f"Tipo de carga desconhecido: '{tipo}'")
        nome = self._ler_texto("Nome da carga: ")
        dados = {param: self._ler_numero(texto, tipo_valor)
                 for param, texto, tipo_valor in campos}
        carga = CargaFactory.criar(tipo, nome=nome, **dados)
        cavalo.carregar(carga)
        print(f"Carga carregada: {carga}")

    def descarregar_conjunto(self):
        cavalo = self._escolher(self._conjuntos(), "Conjuntos")
        if cavalo is None:
            return
        carga = cavalo.descarregar()
        print(f"Carga '{carga.nome}' descarregada.")

    def abrir_entrega(self):
        motorista = self._escolher(self.__transportadora.motoristas, "Motoristas")
        if motorista is None:
            return
        cavalo = self._escolher(self._conjuntos(), "Conjuntos")
        if cavalo is None:
            return
        destino = self._ler_texto("Destino: ")
        entrega = self.__transportadora.abrir_entrega(motorista, cavalo, destino)
        print(f"Entrega aberta: {entrega}")

    def atualizar_entrega(self):
        entrega = self._escolher(self.__transportadora.entregas, "Entregas")
        if entrega is None:
            return
        print("1 - Iniciar\n2 - Concluir\n3 - Cancelar")
        opcao = self._ler_texto("Ação: ")
        if opcao == "1":
            entrega.iniciar()
        elif opcao == "2":
            entrega.concluir()
        elif opcao == "3":
            entrega.cancelar()
        else:
            print("Opção inválida.")
            return
        print(f"Atualizada: {entrega}")

    def listar_tudo(self):
        print("\n--- Cavalos mecânicos ---")
        if not self.__transportadora.cavalos:
            print("(nenhum)")
        for cavalo in self.__transportadora.cavalos:
            print(cavalo)

        print("\n--- Carretas ---")
        if not self.__transportadora.carretas:
            print("(nenhuma)")
        livres = self.__transportadora.carretas_livres
        for carreta in self.__transportadora.carretas:
            situacao = "livre" if carreta in livres else "acoplada"
            print(f"{carreta} [{situacao}]")

        print("\n--- Motoristas ---")
        if not self.__transportadora.motoristas:
            print("(nenhum)")
        for motorista in self.__transportadora.motoristas:
            print(motorista)

        print("\n--- Entregas ---")
        if not self.__transportadora.entregas:
            print("(nenhuma)")
        for entrega in self.__transportadora.entregas:
            print(entrega)

    def resumo(self):
        entregas = self.__transportadora.entregas
        print(f"\nTotal de entregas: {len(entregas)}")
        for status in ("Pendente", "Em trânsito", "Entregue", "Cancelada"):
            quantidade = len(self.__transportadora.entregas_por_status(status))
            print(f"  {status}: {quantidade}")
        print(f"Frete das entregas concluídas: R$ {self.__transportadora.total_frete_entregue():.2f}")

    def executar_testes(self):
        caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testes.py")
        print("\nTESTES")
        subprocess.run([sys.executable, caminho])
        print("FIM DOS TESTES")

    # ---------- laço principal ----------
    def _mostrar_menu(self):
        print(f"""
{self.__transportadora.nome}
1  - Cadastrar cavalo mecânico
2  - Cadastrar carreta
3  - Formar conjunto (acoplar carreta ao cavalo)
4  - Cadastrar motorista
5  - Carregar conjunto
6  - Descarregar conjunto
7  - Abrir entrega
8  - Atualizar status da entrega
9  - Listar cadastros
10 - Resumo das entregas
11 - Executar testes
0  - Sair""")

    def executar(self):
        acoes = {
            "1": self.cadastrar_cavalo,
            "2": self.cadastrar_carreta,
            "3": self.formar_conjunto,
            "4": self.cadastrar_motorista,
            "5": self.carregar_conjunto,
            "6": self.descarregar_conjunto,
            "7": self.abrir_entrega,
            "8": self.atualizar_entrega,
            "9": self.listar_tudo,
            "10": self.resumo,
            "11": self.executar_testes,
        }
        while True:
            self._mostrar_menu()
            opcao = input("Opção: ").strip()
            if opcao == "0":
                print("Encerrando.")
                break
            acao = acoes.get(opcao)
            if acao is None:
                print("Opção inválida.")
                continue
            try:
                acao()
            except (ValueError, TypeError) as erro:
                print("Erro:", erro)