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
-