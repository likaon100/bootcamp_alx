def nasza_funkcja():
    def wrapper(*args,**kwarqs ):
        wynik=func(*args, **kwarqs)
        '<b>'+wynik+'<\\b>'
    return wrapper

@bold

def nasza_funcja():
    return 'jakas funkcja'

print (nasza_funkcja())

