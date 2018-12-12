

import re

kod = re.compile("\d{2}-\d{3}")
mail = re.compile("[\w]+\@[-\w]+(?:\.[(a-z)+]+)+$")
data=re.compile("[0-3]*[0-9]\s[A-Z][a-z]{2}\s[1-9][0-9]{2,3}")


wynik=kod.findall("łeło12223l00kkk;;;12-200;;22kk@o2.pl")
wynik1=mail.findall("łeło12223l00kkk;;;12-200;;22kk@o2.pl;;;23 maj 2000")
wynik2=data.findall("łeło12223l00kkk;;;12-200;;22kk@o2.pl;;;23 maj 2000")

print(wynik)
print(wynik1)
print(wynik2)