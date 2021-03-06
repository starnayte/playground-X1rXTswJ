# On va simplement réutiliser ce qu'on a fait pour le problème 114

from functools import lru_cache

# La longueur de la bande
n_max=50
# Longueur minimale de la bande rouge
longueur_min=50


# On note u(n) le nombre de façons de remplir n cases.
@lru_cache(maxsize=None)
def u(n):
    if longueur_min>n : return 1
    # La première bande rouge peut être d'une longueur allant de 3 à n suivie d'une case noire précédée de i cases noires. On fait la somme sur toutes ces possibilités des façons de remplir les cases restantes.
    somme = 1 # Tout est noir
    for i in range(n-longueur_min+1): # Le nombre de cases noires avant la bande rouge
        for longueur in range(longueur_min, n-i+1): # On parcourt les longueurs du bloc rouge possibles
            somme += u(n-i-longueur-1)
    return somme
    

# Fonction qui cherche
def chercher():
    n=3
    while u(n)<=1000000:
        n+=1
    return n
    
print(chercher())
