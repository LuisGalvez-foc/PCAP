
"""esta funcion usa return (inutilmente)"""
def fun_bad(n):
    for i in range(n):
        return i
    
"""esta funcion usa yield (!bien echo!)"""
def fun_good(n):
    for i in range(n):
        yield i


for c in fun_good(5):
    print(c)