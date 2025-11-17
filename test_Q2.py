import pytest
from Q2 import afficher_jours_examens


@pytest.mark.parametrize("horaire_examen, resultat_attendu ", [
    ([" 10/12/2015", " 12/12/2025", " 15/12/2025"], ("jeudi, vendredi, lundi"))
])
def test_Q2(horaire_examen, resultat_attendu):
    #act
    resultat = afficher_jours_examens(horaire_examen)
    #assert
    assert resultat == resultat_attendu


@pytest.mark.parametrize("horaire_examen, resultat_attendu ", [
    ([" 10/12/2015", " 12/12/2025", " 15/12/2025"], ("mardi, mercredi, jeudi"))
])
def test_Q2(horaire_examen, resultat_attendu):
    #act
    resultat = afficher_jours_examens(horaire_examen)
    #assert
    assert resultat == resultat_attendu


@pytest.mark.parametrize("horaire_examen, resultat_attendu ", [
    ([" 10/12/2015", " 12/12/2025", " 15/12/2025"], ("lundi, mardi, mercredi"))
])
def test_Q2(horaire_examen, resultat_attendu):
    #act
    resultat = afficher_jours_examens(horaire_examen)
    #assert
    assert resultat == resultat_attendu