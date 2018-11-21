
class vector:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'wektor ({self.x}, {self.y})'

    def __add__(self, other):
        nowy_x = self.x+other.x
        nowy_y = self.y + other.y
        return vector (nowy_x, nowy_y)
    def __lt__(self, other):
        d1=(self.x**2 + self.x**2)**(1/2)
        d2=(self.y**2 + self.y**2)**(1/2)
        return d1<d2

v1=vector(1,3)
v2=vector(2,3)
print(v1)
print(v2)

v3=v1+v2

print(v3)
print (v2>v1)