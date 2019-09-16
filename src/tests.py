# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import quadratures as q    # nos formules de quadrature
import fonctions_test as f # nos fonctions pour faire des tests

a,b = 0., 1.        # l'intervalle
# On va faire l'approximation en découpant en 2^k morceaux pour k=0,1...k_max
k_max = 10
N = 2**np.arange(k_max) # pour avoir 2^{0,1,2,3,4...k_max}
h = (b-a)/N             # c'est aussi un tableau

Q = np.zeros_like(N,dtype=np.float) # Alloue un tableau de la même
                                    # taille que N, initialisé à 0
E = np.zeros_like(N,dtype=np.float) # pour les erreurs

# monome de degré 0,1,2: f(x) = 1,x,^2
for k in np.arange(3):
    print("test pour le degré {}".format(k))
    f.degre = k # degré des monomes à tester
    I = f.monome_int(b)-f.monome_int(a) # intégrale exacte puisqu'on
                                        # connait une primitive
    # Calcul des quadratures et des erreurs
    for i in np.arange(k_max):
        Q[i] = q.pt_milieu(f.monome,a,b,N[i])
        E[i] = I-Q[i]
        print ("{:5d} {:14.8g} {:14.8g} {:14.8g}".format(N[i],I,Q[i],E[i]))
    # On peut tracer les courbes d'erreur
    plt.loglog(N,E,'+-',label="monome de degré {}".format(k))
    
plt.title("Test de convergence méthode du point milieu sur des monomes")
plt.legend()
plt.xlabel("N")
plt.ylabel("Erreur")
plt.grid()
# Utilisez une des lignes ci-dessous pour voir/enregistrer le graphique
# plt.show() 
plt.savefig("../img/test_1.png")

