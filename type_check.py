def only_ints(a, b):
    if (type(a) == int) & (type(b) == int):
        return True
    else:
        return False


if __name__ == '__main__':
    print(only_ints(1, 1))
