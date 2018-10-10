x = int(input("podaj pozycje gracza x: "))
y = int(input("podaj pozycje gracza y: "))

if  x > 100 or x< 0 or y > 100 or y < 0:
    pozycja = "poza planszą"
elif x >=90 and y >=90:
    pozycja = "prawy górny róg"
elif x <=10 and y >90:
    pozycja = "lewy górny róg"
elif x <=10 and y<=90:
    pozycja = "lewy dolny róg"
elif x > 90 and y<=10:
    pozycja = "prawy dolny róg"
elif x < 0 and y < 0:
    pozycja = "poza plansza"
else:
    pozycja = "centrum"


print(f"Twoja pozycja to: {pozycja}")
