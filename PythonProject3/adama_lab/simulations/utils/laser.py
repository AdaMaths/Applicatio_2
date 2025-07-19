import numpy as np

def profil_gaussien(x, w0=1.0):
    return np.exp(-2 * (x / w0) ** 2)

def pertes_cavite(longueur, pertes_reflexion=0.1):
    return np.exp(-pertes_reflexion * longueur)

def simulation_laser(xmin, xmax, pas, w0, longueur, pertes_reflexion):
    x = np.arange(xmin, xmax, pas)
    profil = profil_gaussien(x, w0)
    pertes = pertes_cavite(longueur, pertes_reflexion)
    intensité_finale = profil * pertes
    return x.tolist(), intensité_finale.tolist()