

# try:
#     print(lista[3])
#     list.add(6)
# # except Exception as e:
# #     print("wystąpił jakiś błąd")
# #     print(e)
# except ImportError as e:
#     # print("coś nie tak")
#     raise IndexError("")
# except AttributeError as e:
#     print("raczej coś nie tak")
# #expect wykonuje sie tlko wtedy kiedy powstał wyjątek
#
# print("aAA")

# kasa = [10,50,20,50,100,200]
#     try:

def main():
    operacja = input("podaj typ operacji w - wpłata  y - wypłata")
    if operacja == "w":
        banknoty = input("Podaj jakie banknoty wpłacasz - wpisz rozdzielając space")
        banknoty = banknoty.split()
        banknoty = [int(x) for x in banknoty]

    print(banknoty)


    #wpłata
    #wypłata


# x = input ("Podaj typ operacji")
# if x == ("wypłata"):
#     input("Podaj kwotę do wypłaty")
#     input.int ()
# print("Brak operacji")


