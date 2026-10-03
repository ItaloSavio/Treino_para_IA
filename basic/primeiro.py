clientes = [
    {
        "nome": "Italo",
        "area": "Dados",
        "idade": 18,
        "ativo": True
    },
    {
        "nome": "Marilia",
        "area": "Marketing",
        "idade": 21,
        "ativo": False
    },
    {
        "nome": "João",
        "area": "Financeiro",
        "idade": 24,
        "ativo": True
    },
    {
        "nome": "Ana",
        "area": "TI",
        "idade": 27,
        "ativo": False
    },
    {
        "nome": "Pedro",
        "area": "Rh",
        "idade": 30,
        "ativo": True
    },
    {
        "nome": "Lucas",
        "area": "Vendas",
        "idade": 33,
        "ativo": False
    },
    {
        "nome": "Maria",
        "area": "Operações",
        "idade": 36,
        "ativo": True
    },
    {
        "nome": "Carlos",
        "area": "Atendimento",
        "idade": 19,
        "ativo": False
    },
    {
        "nome": "Beatriz",
        "area": "Dados",
        "idade": 22,
        "ativo": True
    },
    {
        "nome": "Rafael",
        "area": "Marketing",
        "idade": 25,
        "ativo": False
    },
    {
        "nome": "Fernanda",
        "area": "Financeiro",
        "idade": 28,
        "ativo": True
    },
    {
        "nome": "Gabriel",
        "area": "TI",
        "idade": 31,
        "ativo": False
    },
    {
        "nome": "Julia",
        "area": "Rh",
        "idade": 34,
        "ativo": True
    },
    {
        "nome": "Mateus",
        "area": "Vendas",
        "idade": 37,
        "ativo": False
    },
    {
        "nome": "Lívia",
        "area": "Operações",
        "idade": 20,
        "ativo": True
    },
    {
        "nome": "Thiago",
        "area": "Atendimento",
        "idade": 23,
        "ativo": False
    },
    {
        "nome": "Camila",
        "area": "Dados",
        "idade": 26,
        "ativo": True
    },
    {
        "nome": "Daniel",
        "area": "Marketing",
        "idade": 29,
        "ativo": False
    },
    {
        "nome": "Sofia",
        "area": "Financeiro",
        "idade": 32,
        "ativo": True
    },
    {
        "nome": "Eduardo",
        "area": "TI",
        "idade": 35,
        "ativo": False
    },
    {
        "nome": "Patrícia",
        "area": "Rh",
        "idade": 18,
        "ativo": True
    },
    {
        "nome": "Leonardo",
        "area": "Vendas",
        "idade": 21,
        "ativo": False
    },
    {
        "nome": "Isabela",
        "area": "Operações",
        "idade": 24,
        "ativo": True
    },
    {
        "nome": "Vinícius",
        "area": "Atendimento",
        "idade": 27,
        "ativo": False
    },
    {
        "nome": "Renata",
        "area": "Dados",
        "idade": 30,
        "ativo": True
    },
    {
        "nome": "Felipe",
        "area": "Marketing",
        "idade": 33,
        "ativo": False
    },
    {
        "nome": "Clara",
        "area": "Financeiro",
        "idade": 36,
        "ativo": True
    },
    {
        "nome": "Henrique",
        "area": "TI",
        "idade": 19,
        "ativo": False
    },
    {
        "nome": "Larissa",
        "area": "Rh",
        "idade": 22,
        "ativo": True
    },
    {
        "nome": "Rodrigo",
        "area": "Vendas",
        "idade": 25,
        "ativo": False
    }
]

clientes_ativos = 0
clientes_inativos = 0
total_de_dados = 0
total_de_ti = 0
total_de_marketing = 0

for cliente in clientes:
    for chave, valor in cliente.items():
        print(f"{chave}: {valor}")

for cliente in clientes:
    if cliente["ativo"] == True:
        clientes_ativos += 1
    else:
        clientes_inativos += 1
    if cliente["area"] == "Dados":
        total_de_dados += 1
    elif cliente["area"] == "TI":
        total_de_ti += 1
    elif cliente["area"] == "Marketing":
        total_de_marketing += 1

print(f"Clientes ativos: {clientes_ativos}")
print(f"Clientes inativos: {clientes_inativos}")
print(f"Total de dados: {total_de_dados}")
print(f"Total de TI: {total_de_ti}")
print(f"Total de marketing: {total_de_marketing}")