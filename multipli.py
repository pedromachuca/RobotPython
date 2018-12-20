#-*- coding:utf-8 -*-

"""module multipli contenant la fonction table"""

def table(nb, max=10):

    """Fonction affichant la table de multiplication par nb de 
    1 x nb jusqu'à max x nb"""

    i = 0
    while i < max:
        print(i+1, "x", nb, "=", (i+1)*nb)
        i += 1
if __name__ == "__main__":
    table(4)

