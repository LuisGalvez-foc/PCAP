def mal_asunto(n):
    try:
        return n / 0
    except:
        print("lo hize")    
        raise ValueError
    
try:
    mal_asunto(0)
except ValueError:
    print("error de valor")
except ArithmeticError:
    print("ya veo")
    exit(0)

print("fin")