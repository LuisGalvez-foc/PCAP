def imprimir_funcion(args,fun):
    for x in args:
        print('f(',x,')=',fun(x),sep='')


def funcion_grado2(x):
    return 2*x**2-4*x+2

imprimir_funcion([x for x in range(-2,3)],funcion_grado2)
imprimir_funcion([x for x in range(-2,3)],lambda x:2*x**2-4*x+2)