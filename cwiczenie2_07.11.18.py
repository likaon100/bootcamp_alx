def splaszcz(lista):
    out =[]
    for element in lista:
        if isinstance(element, list):
            out.extend(splaszcz(element))
        else:
            out.append(element)
    return out




    return lista


lista = [1,2,3, [4,5 ,[6],7], 7]

assert isinstance (lista[0], int)
assert isinstance (lista[3], int)

assert splaszcz (lista)=[1,2,3,4,5,6,7]
