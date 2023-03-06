def enterLesDonnees():
    """Gère l'enregistrement des données de l'élève

    Returns:
        [dictionary]: [paramètre de elève]
    """
    D = {}
    
    while True:
        matricule = input("Entrer matricule de elève: ")
        notes = input("Entrer les differente notes de l'élève separer par une vigurle: ")
        ajoutEleve = input ("Entrer non pour arreter si non entrer n'importe quoi: ")
        
        if matricule in D:
            print(matricule, "existe deja")
        else:
            D[matricule] = notes.split(",")
        if ajoutEleve.lower() == 'non' :
            return D
        
        
def calculMoyenne(data_eleve):
    moy = {}
    
    for matricule in data_eleve:
        sum = 0
        listNote = data_eleve[matricule]
        for note in listNote:
            sum = int(note) + sum

        moy[matricule] = sum/len(listNote)
        
    return moy
    

def afficherMoyenne(moy):
    for matricule in moy:
        print("La moyenne du matricule: ", matricule, "est:", moy[matricule])