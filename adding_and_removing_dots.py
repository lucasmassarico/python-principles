import re


# poderia ter usado .join(string)
def add_dots(texto):
    pos = 1
    aux = texto[0]
    while pos < len(texto):
        aux += '.' + texto[pos]
        pos += 1
    return aux


# poderia ter usado .replace(string)
def remove_dots(texto):
    return re.sub('[.]', '', texto)


if __name__ == '__main__':
    # exemplo de frase: test
    text = input("Insira a frase: ")

    print("Transformando: ", add_dots(text))
    print("Removendo pontos: ", remove_dots(text))
