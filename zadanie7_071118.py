
#lista =(1,2,3,4,5,6)

out = [false, false, false, true, true, true]

def bigger_than_3(lista):
    out=[]
    for element in lista:
        if element>3:
            out.append(true)
        else:
            out.append(false)
    return out


assert sprawdzam_czy_wieksze_niz_3(lista)== out