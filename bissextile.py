#!/usr/bin/python3.5
#-*- coding: utf-8 -*-

#Programme testant si une annee est bissextile ou non

annee = input("Saisissez une année : ")

annee = int(annee)

if annee %400 == 0 or (annee % 4 == 0 and annee % 100 !=0):

    print("L'Année est bissextile")

else:
    print("L'Année n'est pas bissextile")
