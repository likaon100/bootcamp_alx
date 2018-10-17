lista = (1,2,3,4,5,-6,7,8,9,-10)

dodatnie =0
ujemne =0

for x in lista:
    if x>0:
        dodatnie +=1
    elif x<0:
        ujemne -=1
print (f"ilosc ujemne (ujemne), ilosc dodatnie (dodatnie)")