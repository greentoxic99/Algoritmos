
# Pesquisa binaria em python
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    print ("Valor de 'ALTO'", alto)

    while baixo <= alto:
        meio = (baixo + alto) // 2
        print ("valor de 'MEIO'", meio)
        chute = lista[meio]
        print ("valor de 'CHUTE'", chute)
        if chute == item:
            print("item encontrado")
            return meio
        if chute > item:
            print("chute maior que o item")
            alto = meio - 1
        else:
            print("chute menor que o item")
            baixo = meio + 1
    return None


minha_lista = [3, 9, 10, 11, 12, 13, 14, 17, 18, 19]


print(pesquisa_binaria(minha_lista, 3))
#print(pesquisa_binaria(minha_lista, -1))
