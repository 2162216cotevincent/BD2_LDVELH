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
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit
        # self.editIdCitoyen.returnPressed.connect(self.test)



        #On affiche les affaires par défauts.
        self.afficher_chapitre_defaut()
        self.afficher_choix_chapitre_defaut()
        #self.pushButton_3.clicked.connect(self.prochain_chapitre(self.comboBox_2.currentText()))  #à tester
        self.afficher_choix_chapitre()


    def afficher_chapitre_defaut(self):
        #On clear le texte avant. Pour pas avoir plein de trucs en même temps.
        self.textBrowser.clear
        
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()

        #La requête à éxécuter
        try:
            texte = mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre = '0'")
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
        

    def afficher_choix_chapitre_defaut(self):
        #comboBox_2 = combobox pour le choix des chapitres.
        self.comboBox_2.addItem("1")
    def prochain_chapitre(self, numeroChapitre):
        

        #On clear le texte avant. Pour pas avoir plein de trucs en même temps.
        self.textBrowser.clear
        
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()

        texte = ("SELECT texte FROM chapitre WHERE no_chapitre = %s")
        valeur = int(input(numeroChapitre))

        #La requête à éxécuter
        try:
            mycursor.execute(texte,valeur)
            mydb.commit

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

    def afficher_choix_chapitre(self,numeroChapitre):
        #On se créer un curseur pour parcourir la base de données
        mycursor = mydb.cursor()
        #La requête à éxécuter
        try:
            texte = mycursor.execute("SELECT no_chapitre_destination FROM lien_chapitre WHERE no_chapitre_origine = %s")
        except ValueError:
            print("Damn! Il y a eu une erreur lors de l'exécution de la requête.")



    # On défini la fonction qu'on avait déclaré pour le clique sur le bouton
    def recherche_citoyen(self):
        # On récupère la valeur du line edit
        citoyen_id = self.editIdCitoyen.text()
        # Ensuite on pourrait lancer une fonction qui interroge la BD
        # Pour l'exemple on va simplement afficher la valeur dans le label 
        # lblResultat
        self.lblResultat.setText(citoyen_id)
        # editIdCitoyen et lblResultat sont les noms qu'on a donné au widget
        # dans l'éditeur Qt Designer

    def test(self):
        self.lblResultat.setText('Tu as appuyé sur Enter')

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
