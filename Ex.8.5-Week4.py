# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:19:26 2019

@author: USUARIO
"""

filename = input("Enter file name: ")
filehandle = open(filename)
counter = 0

#Ciclo para encontrar correos exclusivamente
#despues de la palabra From

for X in filehandle:
    if "From" in X:
        especificword = X.split()
        if especificword[0] == "From":
            counter = counter + 1
            email = especificword[1]
            print(email)
    else:
        continue
print("There were", counter, "lines in the file with From as the first word")