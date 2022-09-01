def online_count(dict):
    cont = 0
    for status in dict.values():
        if status.lower() == "online":
            cont += 1
    return cont


if __name__ == '__main__':
    dict = {
        'Alice': 'Online',
        'Bob': 'offline',
        'Niih': 'online',
        'Rafa': 'online',
        'Denis': 'offline',
        'Eve': 'OnlinE',
    }
    print("Resultado: ", online_count(dict))
