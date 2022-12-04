import csv
from re import I

file_import = "conso-annuelles_v1.csv"
file_output = "clean.csv"

#Lecture du csv
with open(file_import, 'r', newline='') as file:
    tableau=[]
    lire = csv.reader(file)
    print('',end='\n')
    print("Affichage des lignes du tableau",end="\n")
    for ligne in lire:
        print(ligne, end="\n")
        tableau.append(ligne)
       
#écriture dans un csv
with open(file_output, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=",")
    
    for k in tableau:
        spamwriter.writerow(k)