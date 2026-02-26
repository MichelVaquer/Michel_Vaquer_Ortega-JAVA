def calcular(p, t, e):
    # p és el preu, t és el tipus de producte, e és l'edat
    res = p
    
    if t == "ROBA":
        res = p * 0.9 # descompte del 10%
    elif t == "ELECTRONICA":
        res = p * 1.15 # recàrrec del 15%
        
    if e < 18:
        res = res - 5 # xec jove de 5 euros
        
    if res < 0:
        res = 0
        
    print("El total es:")
    print(res)

calcular(100, "ROBA", 15)
calcular(200, "ELECTRONICA", 40)



