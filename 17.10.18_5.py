ilosc = 0
for x in range(1, 100):

 if x%3==0 or x%5==0:
    ilosc+=1
    print(x)
print(f"ilosc {ilosc}")