import jsonpickle


class Medicament:
    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "", p_nom_commercial: str = "",
                 prix: int = 5.1, categorie: bool = False ):
        self._code_medicament = p_code_medicament
        self._nom_chimique = p_nom_chimique
        self._nom_commercial = p_nom_commercial
        self._prix = prix
        self._category = categorie
        self.nb_medicaments = 0
        self.ls_medicaments = []

    # Validation de la valeur de code médicament
    def _get_code_medicament(self):
        return self._code_medicament
    def _set_code_medicament(self, code_medicament: str):

        if self._code_medicament == "ABC123":
            self._code_medicament = code_medicament
        else:
            print("Le code du médicament est invalide")
    Code_Medicament = property(_get_code_medicament, _set_code_medicament)

    def _get_nom_chimique(self):
        return self._nom_chimique
    def _set_nom_chimique(self, nom_chimique: str):
        if len(self._nom_chimique)<=50:
            self._nom_chimique = nom_chimique
        else:
            print("Le nom chimique est trop long")
    Nom_Chimique = property(_get_nom_chimique, _set_nom_chimique)

    def _get_nom_commercial(self):
        return self._nom_commercial
    def _set_nom_commercial(self, nom_commercial: str):
        if len(self._nom_commercial)<=50:
            self._nom_commercial = nom_commercial
        else:
            print("Le nom commercial est trop long")
    Nom_Commercial = property(_get_nom_commercial, _set_nom_commercial)

    def _get_prix(self):
        return self._prix

    def _set_prix(self, prix: float):
        if self._prix>=5 and self._prix<=100:
            self._prix = prix

        else:
            print("Le prix doit être compris entre 5 et 100 dollars")
    Prix = property(_get_prix, _set_prix)

    def _get_categorie(self):
        return self._category
    def _set_categorie(self, categorie: bool):
        if categorie == "Analgesique":
            self._category = True
        elif categorie == "Antibiotique":
            self._category = False
    Categorie = property(_get_categorie, _set_categorie)

    def serialiser_medicament(self):
        with open(self._code_medicament + ".json", "w") as F:
            donnee_medicament = jsonpickle.encode(self)
            F.write(donnee_medicament)

