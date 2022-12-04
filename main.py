import csv 

#variables
#nom du ficher d'entree
file_import = "conso-annuelles_v1.csv"
#nom du ficher de sorti
file_output = "conso-clean.csv"

#Fonction
def parsing_line(line) -> list:
    
        #Liste contenant toutes les ligens du csv
        list_item_line = line
        #Suppression de la Colonnes ID_Logement
        list_item_line.pop(1)
        #Cellules non vide par défaut
        Cellule_vide = False
        for item in list_item_line:
            #Test si la cellules est vide
            if len(item) == 0:
                Cellule_vide = True 
        
        #Si la ligne n'est pas vide
        if not Cellule_vide:
            #Sommes des consommations des deux années
            annee_total = float(list_item_line[1].replace(',','.').replace('-','0')) + float(list_item_line[2].replace(',','.').replace('-','0'))
            #suppression de la colone la première année de conso
            list_item_line.pop(1)
            #suppression de la colone de la deuxième année de conso
            list_item_line.pop(1)
            #Ajout de la colonne conso total des deux dernières années
            list_item_line.insert(2, annee_total)
            
            return list_item_line

    
    
#Tri de la liste
def sort_order(list_all_data) -> list:
        list_all_item = list_all_data
        #Tri le type par ordre alphabétique
        #Création d'un dictionnaire
        dico_type = {}
        for data_list in list_all_item:
                if data_list[1] in dico_type:
                    #récupération de la liste pour la clé du type du dictionnaire
                    list_value_temp = dico_type[data_list[1]]
                    #Ajout à la liste des items de la clé le nouvel item qui a le type
                    list_value_temp.append(data_list)
                    #Mise a jour de la valeur de la cle avec la nouvelle liste
                    dico_type[data_list[1]] = list_value_temp
                #sinon le type de l'item n'est pas dans le dictionnaire, il faut l'ajouter
                else:
                    #ajout dans le dictionnaire avec comme clé le type du nouvel item
                    dico_type[data_list[1]] = [data_list]
        # Tri des items par ordre decroissant de la consomation annuelle
        #pour chaque clé dans le dictionnaire 
        for key in dico_type:
            #tri du type de la consommation annuelle dans l'ordre decroissent
            list_keys = sorted(dico_type[key], key=lambda inner_list: inner_list[2], reverse=True)
            #Mise a jour de la cle avec la nouvelle liste d'element trier
            dico_type[key] = list_keys
        #creation d'une liste vide
        list_ordered_item = []
        #Pour chaque cle dans l'ordre alaphabetic du dictionnaire
        for i in sorted(dico_type.keys()):
            #Pour chaque liste d'item pour la valeur de la cle i
            for item in dico_type[i]:
                #Ajout de la liste order
                list_ordered_item.append(item)
        #ajout des titre de chaque colonne
        list_ordered_item.insert(0, ['Appareil suivi', 'Type', 'Consommation Total des deux dernieres annees']) 
        return list_ordered_item


# Fonction d'écriture dans le nouveau fichier csv
def write_csv(list_cleaned) -> None:
        #ouverture du fichier à écrire
        with open(file_output, 'w', newline ='', encoding="latin-1") as csv_file:
            writer = csv.writer(csv_file)
            #ecriture de la liste dans le fichier
            writer.writerows(list_cleaned)


#lecture du csv
def read_csv_line() -> None:
        #Création d'une liste vide
        liste_clean = []
        #ouvre le fichier csv en lecture
        with open(file_import, 'r', encoding="latin-1") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            #saut de la premiere ligne du fichier csv pour avoir les nom de la ligne 72
            next(csv_reader)
            #pour chaque ligne du csv executer le code suivant
            for line in csv_reader:
                    #récupération des lignes parsées
                    liste_clean_temp = parsing_line(line)
                    #Test si la variable est bien une liste
                    if type(liste_clean_temp) is list:
                        #ajout de la liste clean dans la liste avec laquelle on va écrire le csv
                        liste_clean.append(liste_clean_temp)
        #écriture des ligne parsé et trié du csv
        write_csv(sort_order(liste_clean))
        


if __name__ == "__main__":
   read_csv_line()