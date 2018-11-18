# petla while, for

# lista = ["a", "b", "d", "e", "f", "g", "h", "i", "j"]
#
# for litera in lista:
#     print(litera)
#     if litera == "e":
#         print("to jest e!")

#range genereuje liste na podstawie liczby podanej

# for i in range(0, 51,2):
#     print(i)
# ____________________________________________________________________9
fruits = ['apple', 'orange', 'pear', 'banana', 'apple']


i = 0
print ("start pętli {} {}".format("yollo", "elo"))
for i, fruit in enumerate(fruits):
    if i==3:
        break
    print(i)
    print("{} jest git".format(fruit))
print("koniec")