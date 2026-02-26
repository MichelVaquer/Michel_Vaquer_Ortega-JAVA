# Constants per evitar "Magic Numbers"
DESCOMPTE_ROBA = 0.90
RECARREC_ELECTRONICA = 1.15
XEC_JOVE_VALOR = 5
EDAT_MINIMA_ADULT = 18

def aplicar_ajust_categoria(preu, categoria):
    """
    Calcula el preu ajustat segons el tipus de producte.
    """
    if categoria == "ROBA":
        return preu * DESCOMPTE_ROBA
    elif categoria == "ELECTRONICA":
        return preu * RECARREC_ELECTRONICA
    return preu

def calcular_preu_final(preu_original, categoria, edat_client):
    """
    Calcula el preu total aplicant descomptes per categoria i edat.
    """
    # 1. Aplicar ajust per categoria
    preu_total = aplicar_ajust_categoria(preu_original, categoria)
    
    # 2. Aplicar xec jove si s'escau
    if edat_client < EDAT_MINIMA_ADULT:
        preu_total -= XEC_JOVE_VALOR
        
    # 3. Validar que el preu no sigui negatiu
    if preu_total < 0:
        preu_total = 0
        
    print(f"El total per a {categoria} (Edat: {edat_client}) és:")
    print(preu_total)
    return preu_total

# Proves del codi
calcular_preu_final(100, "ROBA", 15)
calcular_preu_final(200, "ELECTRONICA", 40)

