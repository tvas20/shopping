import gerItens

class Lista():
    def __init__(self):
        self.nomes = []
        self.precos = []

novo = Lista()

parar = True

while parar:
    item = gerItens.searchItem()
    novo.nomes.append(item['nome'])
    novo.precos.append(item['preco'])
    for i in range(len(novo.nomes)):
        print(f"{novo.nomes[i]}..........{novo.precos[i]}")
    print(f"Subtotal: {sum(novo.precos)}")
    if input("terminar?: ") == '0':
        parar = False
print("-------------------------Final------------------------")
for i in range(len(novo.nomes)):
    print(f"{novo.nomes[i]}..........{novo.precos[i]}")
print(f"Total: {sum(novo.precos)}")