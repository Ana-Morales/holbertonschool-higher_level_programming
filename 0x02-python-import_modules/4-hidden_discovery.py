#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import re
    lista = dir(hidden_4)
    for i in range(len(lista)):
        if re.search("^__", lista[i]) is None:
            print(lista[i])
