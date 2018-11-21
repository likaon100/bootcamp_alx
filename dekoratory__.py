

def fun():
    print('yolo')

fun()

def prosty_dekorator(func):
    def wrapper():
        print('przed wywolaniem')
        func()
        print('po wywolaniu')
    return wrapper

@prosty_dekorator
def fun():
    print('czesc')


print('akuku')
