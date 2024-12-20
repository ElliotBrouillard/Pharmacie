# Importation des classes nécessaires au bon fonctionnement
from Pharmacie.Classes.Medicament import Medicament
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets
#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################
def cacher_labels_erreur(objet):
    """
    Cacher les labels d'erreur
    """
    objet.label_erreur_code_medicament_existe_pas.setVisible(False)
    objet.label_erreur_code_medicament_existe.setVisible(False)
    objet.label_erreur_code_medicament_invalide.setVisible(False)
    objet.label_erreur_nom_chimique.setVisible(False)
    objet.label_erreur_nom_commercial.setVisible(False)
    objet.label_erreur_prix.setVisible(False)



######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetremedicament(QtWidgets.QDialog, UI_PY.dialog_medicament.Ui_Dialog_Medicament):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetremedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Médicament")

    def on_pushButton_Ajouter_clicked(self):
        # Instancier un objet medicament
        medicament = Medicament()
        # Entrée de donnée pour les attributs de medicament
        medicament._code_medicament = self.lineEdit_code_medicament.text()
        medicament._nom_chimique = self.lineEdit_nom_chimique.text()
        medicament._nom_commercial = self.lineEdit_nom_commercial.text()
        medicament._nom_prix = self.lineEdit_nom_prix.text()
        medicament._categorie = self.comboBox_categorie.currentText()
        if medicament._nom_chimique == "":
            self.lineEdit_nom_chimique.clear()
            self.label_erreur_nom_chimique.setVisible(True)
        if medicament._nom_commercial == "":
            self.label_erreur_nom_commercial.setVisible(True)
        if medicament._code_medicament == "":
            self.lineEdit_code_medicament.clear()
            self.label_erreur_code_medicament_invalide.setVisible(True)

        # Si le choix dans la comboBox est Antibiotique, activé les labels, lineEdits et labels d'erreur d'antibiotique et
        # désactivation des labels, lineEdits et labels d'erreur d'analgesique
        if self.comboBox_categorie.currentText() == "AntiBiotique":
            self.label_antibiotique.setVisible(True)
            self.label_duree_prise_max.setVisible(True)
            self.lineEdit_duree_prise_max.setVisible(True)
            if self.duree_prise_max<0:
                self.label_erreur_duree_prise_max.setVisible(True)


            self.label_analgesique.setVisible(False)
            self.label_dose_quot_max.setVisible(False)
            self.lineEdit_dose_quot_max.setVisible(False)
            self.label_erreur_dose_quot_max.setVisible(False)

        if self.comboBox_categorie.currentText() == "Analgesique":
            self.label_analgesique.setVisible(True)
            self.label_dose_quot_max.setVisible(True)
            self.lineEdit_dose_quot_max.setVisible(True)
            if self.duree_prise_max<0:
                self.label_erreur_dose_quot_max.setVisible(True)
            self.label_antibiotique.setVisible(False)
            self.label_duree_prise_max.setVisible(False)
            self.lineEdit_duree_prise_max.setVisible(False)
            self.label_erreur_duree_prise_max.setVisible(False)

