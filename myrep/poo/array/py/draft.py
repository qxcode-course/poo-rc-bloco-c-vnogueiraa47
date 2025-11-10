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



