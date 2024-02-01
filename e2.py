"""
Helena Herrera Aviles
1/2/24
exercici 2
"""
try:
    files = int(input("Introdueix el nombre de files de la matriu: "))
    columnes = int(input("Introdueix el nombre de columnes de la matriu: "))
    if files == columnes and files % 2 == 0:
        matriu = [['1' if i == 0 or i == files - 1 or j == 0 or j == columnes - 1 else '0' for j in range(columnes)] for i in range(files)]
        for fila in matriu:
            print(" ".join(fila))
    else:
        print("La matriu ha de ser quadrada i tenir una mida parella.")
except:
    print("Així no era")
