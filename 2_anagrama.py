def isAnagrama():
    palabra1 = input("Porfavor indique la primera palabra: ").lower()
    palabra2 = input("Porfavor indique la segunda palabra: ").lower()

    if palabra1 != palabra2:
        palabra1 = sorted(list(palabra1))
        palabra2 = sorted(list(palabra2))
        if palabra1 == palabra2:
            return True
        else:
            return False
    else:
        return False

resultado = isAnagrama()
print(resultado)