from class_app import Question

liste_de_question =["Qui est le president du cameroun: \n \
                    (a) Paul Biya\n \
                    (b) Borel Goudjou \n \
                    (c) Autre ",
                    
                    "Quel est le platt favorie de l'ouest \n \
                    (a) Koki\n \
                    (b) Taro\n \
                    (c) Ndole",
                    
                    "Quel est le fuit le plus consommé au cameroun: \n \
                    (a)Mangue\n \
                    (b) Avocat\n \
                    (c) Orange\n"
                    ]

liste_des_question_avec_reponse = [
    Question(liste_de_question[0], 'a'),
    Question(liste_de_question[1], 'a'),
    Question(liste_de_question[2], 'c'),
]

def test(questions):
    score=0
    name = input("Entrer vootre nom: ")
    for question in questions:
        print(question.question)
        reponse = input("entrer votre reponse: ")
        if reponse == question.reponse:
            score +=1
            
    print(f"salut {name }votre score est egale {score}/{len(questions)}")
    
    rejouer = input("voulez vous rejouer (oui/non)")
    if(rejouer == 'oui'):
        test(liste_des_question_avec_reponse)
    else:
        exit
        
test(liste_des_question_avec_reponse)