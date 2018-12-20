#-*- coding: utf-8 -*-
#import du module math
import math


#création d'une fonction
def table7():
    nb = 7
    i = 0
    while i < 8:
        print(nb, "x", i, "=", nb*i)
        i += 1

#Appel de la fonction        
table7()

#Crétion d'une fonction lambda retourne le carré de l'argument stocker la focntion dans la variable f
f = lambda x: x*x

#Affiche le résultat de la fonction lambda
print(f(5))

#affiche le résultat de la fonction de l'import math sqrt
print(math.sqrt(5))
