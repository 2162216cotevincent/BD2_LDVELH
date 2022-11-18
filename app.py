import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier MainWindow.py
from MainWindow import Ui_MainWindow



#QUESTIONS:
#Comment régler le bug de l'appel de la fonction self.pushbutton3
#Comment récupérer l'information du chapitre actuel?



#Informations de connection à la base de données. Changer les infos dépendament de la bd à laquelle on essait de se connecter.
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ldvelh"
    )
    print("Connexion à la base de données réussi")
except ValueError:
    print("Erreur lors de la connexion à la base de données")

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    chapitreActuel = 0

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit
        # self.editIdCitoyen.returnPressed.connect(self.test)

        #Il ne fallait pas mettre prochain_chapitre avec les parenthèses, car cela l'exécute tout de suite, c'est n'est pas ce que l'on veut.
        self.pushButton_3.clicked.connect(self.prochain_chapitre)
        self.pushButton_nouvellePartie.clicked.connect(self.nouvellePartie)
        self.label_erreurCreationPartie.clear()
        self.label_partieSauvegarde.clear()
        self.label_supression.clear()
        self.afficher_charger_partie()
        self.boutonSauvegarde.clicked.connect(self.sauvegarder)
        self.pushButton_2.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(self.charger)
        self.afficher_livre()

    def afficher_livre(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT nom FROM livre")
        myresult = mycursor.fetchall()
        self.comboBox.addItem(myresult[0][0])
    
    def afficher_discipline(self):
        mycursor = mydb.cursor()
        texteIdFiche = "SELECT id FROM fiche_personnage WHERE nom_personnage = (%s)"
        valueIdFiche = (str(self.label_nomPerso.text()),)
        try:
            mycursor.execute(texteIdFiche,valueIdFiche)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idFiche = myresult[0][0]


        texte = "SELECT nom_discipline FROM discipline_kai INNER JOIN personnage_discipline ON discipline_kai.id = personnage_discipline.id_discipline WHERE personnage_discipline.id_fiche = (%s)"
        value = (str(idFiche),)

        try:
            mycursor.execute(texte,value)
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")
        
        myresult = mycursor.fetchall()
        self.comboBox_4.addItem(myresult[0][0])
        self.comboBox_5.addItem(myresult[1][0])
        self.comboBox_6.addItem(myresult[2][0])
        self.comboBox_7.addItem(myresult[3][0])
        self.comboBox_8.addItem(myresult[4][0])
        self.comboBox_9.addItem(myresult[5][0])

    def afficher_arme(self):
        mycursor = mydb.cursor()

        mycursor = mydb.cursor()
        texteIdFiche = "SELECT id FROM fiche_personnage WHERE nom_personnage = (%s)"
        valueIdFiche = (str(self.label_nomPerso.text()),)
        try:
            mycursor.execute(texteIdFiche,valueIdFiche)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idFiche = myresult[0][0]


        texte = "SELECT nom_arme FROM arme INNER JOIN personnage_arme ON arme.id = personnage_arme.id_arme WHERE personnage_arme.id_fiche = (%s)"
        value = (str(idFiche),)

        try:
            mycursor.execute(texte,value)
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")
        
        myresult = mycursor.fetchall()
        self.comboBox_10.addItem(myresult[0][0])
        self.comboBox_11.addItem(myresult[1][0])
 
        

    
    def sauvergarder_discipline(self,comboBox):
        print("hi")
        

    def afficher_chapitre(self):
        mycursor = mydb.cursor()
        self.textBrowser.clear
        texte = ("SELECT texte FROM chapitre WHERE no_chapitre = '%s'")
        #Il faut mettre une virgule après parce que ce doit être un TUPLE, et non un int.
        valeur = (self.chapitreActuel,)


        try:
            mycursor.execute(texte,valeur)
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")

        #On va chercher les résultats.
        myresult = mycursor.fetchall()
        self.textBrowser.setText(myresult[0][0])

    def charger(self):
        partieChoisie = str(self.comboBox_3.currentText())
        mycursor = mydb.cursor()
        texteIdFiche = "SELECT id FROM fiche_personnage WHERE nom_personnage = (%s)"
        valueIdFiche = (str(partieChoisie),)
        try:
            mycursor.execute(texteIdFiche,valueIdFiche)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idFiche = myresult[0][0]

        texte = "SELECT id_chapitre FROM sauvegarde WHERE id_fiche = (%s)"
        value = (str(idFiche),)
        try:
            mycursor.execute(texte,value)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        self.chapitreActuel = myresult[0][0]

        self.afficher_no_chapitre()
        self.afficher_nom_perso(self.comboBox_3.currentText())
        self.afficher_chapitre()
        self.afficher_choix_chapitre(self.chapitreActuel)
        self.afficher_discipline()
        self.afficher_arme()


   

    def supprimer(self):
        mycursor = mydb.cursor()
        texteIdFiche = "SELECT id FROM fiche_personnage WHERE nom_personnage = (%s)"
        valueIdFiche = (str(self.label_nomPerso.text()),)
        try:
            mycursor.execute(texteIdFiche,valueIdFiche)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idFiche = myresult[0][0]
        texte = "DELETE FROM sauvegarde WHERE id_fiche = (%s)"
        value = (str(idFiche),)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            self.label_supression.setText("Partie supprimée.")
        except ValueError:
            print("Erreur lors de la requête.")
        

    def sauvegarder(self):
        mycursor = mydb.cursor()
        texteIdFiche = "SELECT id FROM fiche_personnage WHERE nom_personnage = (%s)"
        valueIdFiche = (str(self.label_nomPerso.text()),)
        try:
            mycursor.execute(texteIdFiche,valueIdFiche)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idFiche = myresult[0][0]

        idChapitre = self.chapitreActuel

        texte = "INSERT INTO sauvegarde(id_fiche,id_chapitre) VALUES (%s,%s)"
        value = (idFiche,idChapitre)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion réussi!")
        except ValueError:
            print("Erreur lors de la sauvegarde")
        self.label_partieSauvegarde.setText("Partie Sauvegardée.")




        #SECTION SAUVEGARDER DISCIPLINES

        textekai = "SELECT id FROM discipline_kai WHERE nom_discipline = (%s)"
        valuekai = (self.comboBox_4.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête")
        #---------
        valuekai = (self.comboBox_5.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête")
        #---------
        valuekai = (self.comboBox_6.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête")
        #---------
        valuekai = (self.comboBox_6.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête")
        #---------
        valuekai = (self.comboBox_7.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête")
        
        self.afficher_charger_partie()
        #---------
        valuekai = (self.comboBox_8.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête")
            #---------
        valuekai = (self.comboBox_9.currentText(),)
        try:
            mycursor.execute(textekai,valuekai)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idDiscipline = myresult[0][0]

        texte = "INSERT INTO personnage_discipline(id_fiche,id_discipline) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion discipline réussi!")
        except ValueError:
            print("Erreur lors de la requête") 




        #SECTION SAUVEGARDE ARMES
        textearme = "SELECT id FROM arme WHERE nom_arme = (%s)"
        valuearme = (self.comboBox_10.currentText(),)
        try:
            mycursor.execute(textearme,valuearme)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idarme = myresult[0][0]

        texte = "INSERT INTO personnage_arme(id_fiche,id_arme) VALUES (%s,%s)"
        value = (idFiche,idarme)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion arme réussi!")
        except ValueError:
            print("Erreur lors de la requête")
        #---------
        valuearme = (self.comboBox_11.currentText(),)
        try:
            mycursor.execute(textearme,valuearme)
        except ValueError:
            print("Erreur lors de la requête.")
        myresult = mycursor.fetchall()

        idarme = myresult[0][0]

        texte = "INSERT INTO personnage_arme(id_fiche,id_arme) VALUES (%s,%s)"
        value = (idFiche,idDiscipline)
        try:
            mycursor.execute(texte,value)
            mydb.commit()
            print("insertion arme réussi!")
        except ValueError:
            print("Erreur lors de la requête")

    def afficher_charger_partie(self):
        mycursor = mydb.cursor()

        texte = "SELECT sauvegarde.id, nom_personnage FROM sauvegarde INNER JOIN fiche_personnage ON sauvegarde.id_fiche = fiche_personnage.id ORDER BY id"
        try:
            mycursor.execute(texte)
            print("Requête réussi!")
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")
        
        myresult = mycursor.fetchall()
        
        #À COMPLÉTER
        for(nom_personnage) in myresult:
            self.comboBox_3.addItem(str(nom_personnage[1]))

        

    def nouvellePartie(self):
        
        #À CORRIGER
        if self.lineEdit_nomPersonnage.text == "":
            label_erreurCreationPartie.setText("Veuillez choisir un nom.")
        else:
            mycursor = mydb.cursor()
            texte = "INSERT INTO fiche_personnage(nom_personnage) VALUES (%s)"
            value = (str(self.lineEdit_nomPersonnage.text()),)
            try:
                mycursor.execute(texte,value)
            except ValueError:
                print("Erreur lors de la création du personnage.")



            self.afficher_no_chapitre()
            self.afficher_chapitre_defaut()
            self.afficher_choix_chapitre_defaut()
            self.afficher_disciplines_kai_defaut()
            self.afficher_nom_perso(value[0])
            self.afficher_armes_defaut()



    def afficher_nom_perso(self, nom):
        
        self.label_nomPerso.setText(nom)

        #self.comboBox_4.currentIndexChanged.connect(self.sauvergarder_discipline(self.comboBox_4))
        #self.comboBox_5.currentIndexChanged.connect(self.sauvergarder_discipline(self.comboBox_5))
        #self.comboBox_6.currentIndexChanged.connect(self.sauvergarder_discipline(self.comboBox_6))
        #self.comboBox_7.currentIndexChanged.connect(self.sauvergarder_discipline(self.comboBox_7))
        #self.comboBox_8.currentIndexChanged.connect(self.sauvergarder_discipline(self.comboBox_8))
        #self.comboBox_9.currentIndexChanged.connect(self.sauvergarder_discipline(self.comboBox_9))

    def afficher_disciplines_kai_defaut(self):
        mycursor = mydb.cursor()

        texte = "SELECT nom_discipline FROM discipline_kai ORDER BY nom_discipline"
        try:
            mycursor.execute(texte)
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")
        
        myresult = mycursor.fetchall()
        
        #À COMPLÉTER
        for(nom_discipline) in myresult:
            self.comboBox_4.addItem(nom_discipline[0])
            self.comboBox_5.addItem(nom_discipline[0])
            self.comboBox_6.addItem(nom_discipline[0])
            self.comboBox_7.addItem(nom_discipline[0])
            self.comboBox_8.addItem(nom_discipline[0])
            self.comboBox_9.addItem(nom_discipline[0])
    
    def afficher_armes_defaut(self):
        mycursor = mydb.cursor()

        texte = "SELECT nom_arme FROM arme ORDER BY nom_arme"
        try:
            mycursor.execute(texte)
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")
        
        myresult = mycursor.fetchall()
        

        for(nom_arme) in myresult:
            self.comboBox_10.addItem(nom_arme[0])
            self.comboBox_11.addItem(nom_arme[0])





        
            


    def afficher_no_chapitre(self):
        self.label_numero_chapitre.setText(str(self.chapitreActuel))
        

    def afficher_chapitre_defaut(self):
        #On clear le texte avant. Pour pas avoir plein de trucs en même temps.
        self.textBrowser.clear
        
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()

        texte = ("SELECT texte FROM chapitre WHERE no_chapitre = '%s'")
        #Il faut mettre une virgule après parce que ce doit être un TUPLE, et non un int.
        valeur = (self.chapitreActuel,)


        try:
            mycursor.execute(texte,valeur)
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")

        #On va chercher les résultats.
        myresult = mycursor.fetchall()

        if myresult == None:
            print("La table est là, mais elle semble vide??? hello???")
            self.textBrowser.setText("Oh non! Il y a eu une erreur!")
        else:
            #On l'insère dans l'endroit prévu dans la fenêtre
            #Pourquoi [0][0]? Parce que fetchall ramène un tableau. dans ce tableau, il y a des entrés contenant d'autre tableaux. Un autre moyen est de faire une boucle.
            self.textBrowser.setText(myresult[0][0])
        self.chapitreActuel = 0
        self.afficher_no_chapitre()


    #Affichage des choix de chapitres par défaut.
    def afficher_choix_chapitre_defaut(self):
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()
        self.comboBox_2.addItem("1")

        



    #Fonction pour afficher le choix des prochains chapitres dans le selectmenu.    
    def prochain_chapitre(self):
        #On clear le texte avant. Pour pas avoir plein de trucs en même temps.
        self.textBrowser.clear

        #La requête à éxécuter
        if(self.chapitreActuel == 0):
            #RAISON: dans ma base de donnée, le premier chapitre est à 1. C'est pour pas tout décaler.
            numeroChapitre = 1
        else:
            numeroChapitre = self.comboBox_2.currentText()

        

        
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()


        texte = ("SELECT texte,no_chapitre FROM chapitre WHERE no_chapitre = %s")
        valeur = (numeroChapitre,)
        #Avant, j'avais écrit int(input(numeroChapitre)). Ça faisait planter mon code SOLIDE.

        #La requête à éxécuter
        try:
            mycursor.execute(texte,valeur)

        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")

        #On va chercher les résultats.
        myresult = mycursor.fetchall()

        if myresult == None:
            print("La table est là, mais elle semble vide??? hello???")
            self.textBrowser.setText("Oh non! Il y a eu une erreur!")
        else:
            #On l'insère dans l'endroit prévu dans la fenêtre
            #Pourquoi [0][0]? Parce que fetchall ramène un tableau. dans ce tableau, il y a des entrés contenant d'autre tableaux. Un autre moyen est de faire une boucle.
            self.textBrowser.setText(myresult[0][0])

        self.chapitreActuel = numeroChapitre
        self.afficher_no_chapitre()
        self.afficher_choix_chapitre(numeroChapitre)








    #Fonction pour afficher le nouveau chapitre choisi.
    def afficher_choix_chapitre(self,numeroChapitre):
        self.comboBox_2.clear()
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()


        #La requête à éxécuter
        if(self.chapitreActuel == 0):
            #RAISON: dans ma base de donnée, le premier chapitre est à 1. C'est pour pas tout décaler.
            self.chapitreActuel = 1

    

        texte = "SELECT no_chapitre_destination FROM lien_chapitre WHERE no_chapitre_origine = %s"
        valeur = (self.chapitreActuel,)
        try:
            mycursor.execute(texte,valeur)

        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")

        #On va chercher les résultats.
        myresult = mycursor.fetchall()
        

        #comboBox_2 = combobox pour le choix des chapitres.
        for(no_chapitre_destination) in myresult:
            self.comboBox_2.addItem(str(no_chapitre_destination[0]))

        self.chapitreActuel = numeroChapitre

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
