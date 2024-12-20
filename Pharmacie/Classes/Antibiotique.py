from Pharmacie.Classes.Medicament import Medicament


class Antibiotique(Medicament):
    def __init__(self, p_duree_prise_max: int = 0, p_code_medicament: str ="",
                 p_nom_chimique: str = "", p_nom_commercial: str = "",
                 prix: int = 5, categorie: bool = False):
        self._duree_prise_max = p_duree_prise_max
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, prix, categorie)



    # Propriétés
    def _get_duree_prise_max(self):
        return self._duree_prise_max
    def _set_duree_prise_max(self, v_duree_prise_max):
        if v_duree_prise_max > 0 and v_duree_prise_max < 45:
            self._duree_prise_max = v_duree_prise_max

    def __str__(self):
        """
            Méthode spéciale d'affichage

        """
        chaine = " "*60+"\n"+"*"*60+"\n\n"+"   La durée de prise maximale du médicament:"+self._duree_prise_max