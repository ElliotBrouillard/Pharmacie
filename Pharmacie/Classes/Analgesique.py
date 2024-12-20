from Medicament import Medicament

class Analgesique(Medicament):
    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "", p_nom_commercial: str = "", prix: int = 5, categorie: bool = True ,  p_dose_quot_max: int = 0):
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, prix, categorie, p_dose_quot_max)
        self._dose_quot_max = p_dose_quot_max

    # Propriétés
    # propriété dose_quot_max
    def _get_dose_quot_max(self):
        return self._dose_quot_max
    def _set_dose_quot_max(self, v_dose_quot_max: int):
        if self.v_dose_quot_max > v_dose_quot_max:
            self._dose_quot_max = v_dose_quot_max

    dose_quot_max = property(_get_dose_quot_max, _set_dose_quot_max)

    # Méthode magique __str__
    def __str__(self):
        """
        Méthode magique str
        """