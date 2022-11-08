def mid(texto):
    if len(texto) % 2 != 0:
        return texto[int(len(texto) / 2)]
    else:
        return ""


if __name__ == '__main__':
    text = input("Digita a mensagem: ")
    print("Resultado: ", mid(text))
