# como posso melhorar essa função? Pensar em um jeito
def double_letters(text):
    for pos, letter in enumerate(text):
        if not pos == (len(text) - 1):
            if letter == text[pos + 1]:
                return True
    return False


if __name__ == '__main__':
    word = input("Digite a frase: ")
    print(double_letters(word))
