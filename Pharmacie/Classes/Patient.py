from Medicament import Medicament
from datetime import date
class Patient:
    def __init__(self, p_num_patient: int = 2111111 , p_nom_patient: str = "", p_prenom_patient:str = "", p_courriel: str = "", p_date_naiss_patient: date = date.today(),  p_list_medic = list[Medicament] ):
        self._num_patient = p_num_patient
        self._nom_patient = p_nom_patient
        self._prenom_patient = p_nom_patient
        self._courriel = p_courriel
        self._date_naiss_patient = p_date_naiss_patient
        if p_list_medic is None:
            self._list_medic = []
        else:
            self._list_medic = p_list_medic

    # Propriétés
    def _get_num_patient(self):
        return self._num_patient
    def _set_num_patient(self, num_patient):
        if len(num_patient)==7 and num_patient[0]%2==0:
            self._num_patient = num_patient
        else:
            print("Le numéro de patient doit être composée de sept chiffres dont le premier est pair")

    def _get_nom_patient(self):
        return self._nom_patient
    def _set_nom_patient(self, nom_patient):
        if len(self._nom_patient)<=50:
            self._nom_patient = nom_patient
        else:
            print("Le nom du patient est trop long")
    def _get_prenom_patient(self):
        return self._prenom_patient
    def _set_prenom_patient(self, prenom_patient):
        if len(self._prenom_patient)<=50:
            self.prenom_patient = prenom_patient
        else:
            print("Le prenom du patient est trop long")

    # def _get_courriel(self):
    #     return self._courriel
    # def _set_courriel(self, courriel):
    #     if self.courriel = nom.prenom@gmail.com:
    #         self._courriel = courriel


    # définition de la méthode privée calculer_Age
    @staticmethod
    def calculer_Age(p_date_naiss_patient: date):
        today = date.today()
        if p_date_naiss_patient > today:
            return -1
        else:
            return today.year - p_date_naiss_patient.year() - ((today.month, today.day) < (p_date_naiss_patient.month(), p_date_naiss_patient.day()))

    # définition de la méthode public verif_age
    def estAdulte(self, age):
        calculer_Age()
        if age>=18:
            print("Patient est majeur")
        elif age<18:
            print("Enfant")
    def afficherMedicaments(self):
        print("*"*60)
        print("##### Voici les médicaments du patient ######")
        print(self._list_medic)
        print("*"*60)

    def ajouterMedicaments(self, medicament):
        self._list_medic.append(medicament)

    def supprimerMedicament(self, medicament):
        self._list_medic.remove(medicament)

