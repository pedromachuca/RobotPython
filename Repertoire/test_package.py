#Deux manière d'importer un package bien fais avec les dossiers

#manière 1 on importe la fonction table depuis le fonctions dans package 
from package.fonctions import table
table(5)#appel de la fonction

#Ou ...

import package.fonctions
package.fonctions.table(5)#appel de la fonction table
