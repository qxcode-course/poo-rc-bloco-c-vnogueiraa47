import random
class Foo:
    def __init__(self, x: int):
        self.x = x
    def __str__(self):
        return f'Foo({self.x})'

lista_vazia_int: list[int] = []
lista_vazia_obj: list[Foo] = []

lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preencida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3)]

tamanhoVazia = len(lista_vazia_int)
tamanhoPre = len(lista_preenchida)
print(tamanhoVazia)
print(tamanhoPre)

lista_preenchida.append(7)
print(lista_preenchida)
lista_preenchida.pop()
print(lista_preenchida)

lista_preenchida.insert(0, 7)
print(lista_preenchida)
lista_preenchida.pop(0)
print(lista_preenchida)

lista_preenchida.insert(2, 8998)
print(lista_preenchida)
lista_preenchida.pop(2)
print(lista_preenchida)

listaString = [str(x) for x in lista_preenchida]
listaForm = " ".join(listaString)
print(listaForm)

lista_vazia_int = list(range(8))
print(lista_vazia_int)

lista_alearorios = [random.randint(1,100) for i in range(5)]
print(lista_alearorios)

print(lista_preenchida[0])
print(lista_preenchida[2])

for i in lista_preenchida:
    print(i)

for i in range(len(lista_preenchida)):
    print(lista_preenchida[i])

for x in lista_preenchida:
    if x == 3:
        print("Numero 3 encotrado")
    else:
        print("Numero 3 não encontrado")

if 3 in lista_preenchida:
    print("Numero encontrado")

newList = [x for x in lista_preenchida if x % 2 == 0]
print(newList)

newList1 = [ x ** 2 for x in lista_preenchida]
print(newList1)

lista_preenchida.remove(3)
print(lista_preenchida)

newLista3 = [1,2,3,3,3,4,4,5,5,6,1,2,9,10,3,3,3]
while 3 in newLista3:
    newLista3.remove(3)
print(newLista3)

newList4 = [5, 3, 2, 7, 1, 4, 6]
newList4.sort()
print(newList4)

newList7 = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(newList7)
print(newList7)



