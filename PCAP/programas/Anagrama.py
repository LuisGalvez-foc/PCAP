
text1=''
text2=''
while True:
    text1=input(" intoduce una palabra : ").upper()
    if not text1.isalpha():
        print("no es una palabra")
        break
    else:
        text2=input("introduce la segunda palabra : ").upper()
        if not text2.isalpha():
            print("no es una palabra")
            break
        if sorted(text1)==sorted(text2):
            print("son anagramas")  
        else:
            print("no son anagramas")



 