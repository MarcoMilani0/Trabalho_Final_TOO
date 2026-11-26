# Sistema de Controle de Carga de Transportadora

## Descrição e objetivo

Trabalho prático da disciplina de Tecnologia Orientada a Objetos (TOO).

Sistema em Python, orientado a objetos, para controlar o transporte de cargas de arroz de uma transportadora. O sistema cadastra cavalos mecânicos, carretas e motoristas, forma o conjunto (cavalo mecânico + carreta), carrega o conjunto com uma carga, calcula o frete e acompanha o andamento de cada entrega.

## Estrutura do projeto

```text
Trabalho_Final_TOO/
├── main.py
├── menu.py
├── testes.py
└── model/
    ├── carga.py
    ├── carga_factory.py
    ├── carreta.py
    ├── cavalo_mecanico.py
    ├── motorista.py
    ├── estados.py
    ├── entrega.py
    └── transportadora.py
```

## Classes

| Classe | Função |
|---|---|
| `Carga` | Classe abstrata base para os tipos de carga, exigindo o cálculo de peso e frete |
| `ArrozEmCasca` | Carga a granel que aplica desconto no frete conforme o percentual de sujeira |
| `ArrozEnsacado` | Carga calculada pela quantidade de sacos |
| `PaletePiso` | Carga calculada pela quantidade e peso dos paletes |
| `Carreta` | Representa o reboque com modelo, capacidade máxima, extensão e eixos |
| `CavaloMecanico` | Representa o caminhão (modelo, potência, placa e ano); recebe uma carreta acoplada, formando o conjunto, e transporta uma carga por vez |
| `Motorista` | Representa o condutor com nome, CNH e categoria; só a categoria E pode dirigir o conjunto |
| `Entrega` | Vincula motorista, conjunto, carga e destino, controlando o andamento do transporte |
| `EstadoEntrega` | Classe abstrata base dos estados da entrega, que recusa qualquer transição por padrão |
| `EstadoPendente` | Entrega criada; aceita iniciar e cancelar |
| `EstadoEmTransito` | Entrega a caminho; aceita apenas concluir |
| `EstadoEntregue` | Estado final; não aceita transições |
| `EstadoCancelada` | Estado final; não aceita transições |
| `CargaFactory` | Instancia automaticamente o tipo de carga correto a partir do tipo informado |
| `Transportadora` | Gerencia o cadastro único de cavalos, carretas, motoristas e entregas do sistema, e forma os conjuntos |
| `Menu` | Interface de terminal para cadastrar os dados e operar o sistema |

## Pilares da POO

- **Abstração:** `Carga` e `EstadoEntrega` são classes abstratas e não podem ser instanciadas.
- **Encapsulamento:** todos os atributos são privados, com `@property` de leitura. As listas internas só mudam por métodos que validam o que entra, e as properties de lista devolvem uma tupla.
- **Herança:** `ArrozEmCasca`, `ArrozEnsacado` e `PaletePiso` herdam de `Carga`; os estados herdam de `EstadoEntrega`.
- **Polimorfismo:** cada carga calcula peso e frete de um jeito, e o restante do sistema as trata todas como `Carga`.

## Padrões de projeto

- **Factory (`CargaFactory`):** centraliza a criação das cargas. Quem chama informa o tipo (`"casca"`, `"ensacado"`, `"palete"`) e os dados, sem conhecer as classes concretas.
- **State (`estados.py`):** o status da entrega é um objeto de estado. Cada estado decide quais transições aceita (Pendente → Em trânsito → Entregue, ou Pendente → Cancelada); as demais levantam erro.
- **Singleton (`Transportadora`):** existe uma única transportadora no sistema; qualquer chamada a `Transportadora()` devolve a mesma instância.

## Como executar e testar

Requisito: Python 3.11 ou superior.

```bash
git clone https://github.com/MarcoMilani0/Trabalho_Final_TOO
cd Trabalho_Final_TOO
python main.py
```

Execute sempre a partir da raiz do projeto, para os imports `from model...` funcionarem.

O programa abre um menu para cadastrar cavalos, carretas e motoristas, formar o conjunto, carregar a carga, abrir entregas e acompanhar o status. A opção **Executar testes** do menu roda a demonstração completa, que também pode ser executada sozinha com:

```bash
python testes.py
```

Os testes cobrem: carga e descarga do conjunto; recusa de carga acima da capacidade, de tipo inválido e de segunda carga; criação pela Factory, inclusive tipo desconhecido; ciclo de uma entrega pelo State, com transições proibidas; e o Singleton com cadastro duplicado. Cada erro proposital tem um comentário no código explicando o motivo.

## Funcionalidades

- Cadastro de cavalos mecânicos, carretas e motoristas, cada um separadamente
- Formação do conjunto, acoplando uma carreta livre a um cavalo sem carreta
- Carga e descarga do conjunto, validando a capacidade da carreta
- Cálculo de peso e de frete por tipo de carga
- Abertura de entregas e controle do status (iniciar, concluir, cancelar)
- Listagem dos cadastros, resumo das entregas por status e total de frete das entregas concluídas

## Detalhamento de Aprendizado

- **Dificuldades encontradas:** Conseguir impedir erros causados pelos usuários.
- **Como resolvi:** Com ajuda do Claude, pedi para ele imaginar o que um usuário padrão faria no sistema e pensar nos possíveis erros que isso causaria, assim conseguindo prever e fazer a correção dessas exceções.
- **Principal aprendizado:** Uso de padrões de projeto de forma efetiva no código, quando e por que criar classes somente abstratas e tratamento de erros.

## Declaração de Uso de IA

- **Ferramenta e modelo:** Claude, Sonnet 5.5
- **Partes em que foi usada:** Usado para tirar dúvidas sobre a estrutura do projeto, correção de bugs e criação do README.
- **Aprendizado com o uso:** Podendo consultar minhas dúvidas, consegui estender meu entendimento e preencher as lacunas em certos assuntos de TOO.