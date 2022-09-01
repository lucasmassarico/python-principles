def mid(text):
    if len(text) % 2 != 0:
        return text[int(len(text)/2)]
    else:
        return ""


if __name__ == '__main__':
    text = input("Digita a mensagem: ")
    print("Resultado: ", mid(text))
