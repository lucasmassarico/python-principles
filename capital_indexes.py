def capital_indexes(texto):
    # exemplo HeLlO
    lista = []
    for pos, char in enumerate(texto):
        if char.isupper():
            lista.append(pos)
    return lista


if __name__ == '__main__':
    text = input("Digite o texto: ")
    print("Letras maiúsculas na posição: ", capital_indexes(text))
