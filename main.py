def capital_indexes(text):
    # exemplo HeLlO
    lista = []
    for pos, char in enumerate(text):
        if char.isupper():
            lista.append(pos)
    return lista


if __name__ == '__main__':
    text = input("Digite o texto: ")
    print("Letras maiúsculas na posição: ", capital_indexes(text))
