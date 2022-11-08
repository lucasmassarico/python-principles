def online_count(dicionario):
    cont = 0
    for status in dicionario.values():
        if status.lower() == "online":
            cont += 1
    return cont


if __name__ == '__main__':
    dct = {
        'Alice': 'Online',
        'Bob': 'offline',
        'Niih': 'online',
        'Rafa': 'online',
        'Denis': 'offline',
        'Eve': 'OnlinE',
    }
    print("Resultado: ", online_count(dct))
