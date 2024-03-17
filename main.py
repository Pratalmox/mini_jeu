class Gladiateur:
    def __init__(self, nom, pv, force, competence):
        self.nom = nom
        self.pv = pv
        self.force = force
        self.competence = competence


def personnage():
    gladiateur1 = Gladiateur(str(input("Entrée votre pseudo : ")), 8, 4, "")
    print("Bienvenue au joueur :", gladiateur1.nom)

def arene():
    print("1 pour entrer dans l'arène 2 pour attendre")
    number = int(input("Votre choix : "))

    if number == 1:
        combat()

    else:
        print("Choix invalide")
        arene()

def combat():
    ennemi1 = Gladiateur("Deimos", 8, 6, "Rage")
    ennemi2 = Gladiateur("Kassandra", 8, 2, "Resistance")
    print("Ennemi 1 :", ennemi1.nom,"\nEnnemi 2 :", ennemi2.nom)
    number = int(input("Choisisser un adversaire : "))

    if number == 1:
        print(ennemi1.nom)
        #à faire

    elif number == 2:
        print(ennemi2.nom)
        #à faire

    else:
        print("Choix invalide")
        combat()
class Arme:
    def __init__(self, nom, degat):
        self.nom = nom
        self.degat = degat


def glaive():
    arme1 = Arme("Glaive", 8)
    print("Vous avez pris un", arme1.nom, "qui inflige", arme1.degat, "de dégats")


def dague():
    arme2 = Arme("Dague", 4)
    print("Vous avez pris une", arme2.nom, "qui inflige", arme2.degat, "de dégats")


def arc():
    arme3 = Arme("Arc", 6)
    print("Vous avez pris un", arme3.nom, "qui inflige", arme3.degat, "de dégats")


def equipement():
    print("Glaive 8 de dégats, Dague 4 de dégats, Arc 6 de dégats")
    print("1 pour prendre le glaive\n2 pour prendre la dague\n3 pour prendre l'arc")
    number = int(input("Votre choix: "))

    if number == 1:
        glaive()

    elif number == 2:
        dague()

    elif number == 3:
        arc()

    else:
        print("Choix invalide")
        equipement()


class Competence:
    def __init__(self, nom, effet):
        self.nom = nom
        self.effet = effet


def capacite():
    competence1 = Competence("Rage", "augmente la force de 2")
    competence2 = Competence("Résistance", "augmente la vie de 2")

    print("Rage augmente la force de 2, Resistance augmente la vie de 2")
    print("1 pour prendre la Rage\n2 pour prendre la Résistance")
    number = int(input("Votre choix: "))

    if number == 1:
        print(competence1.nom, competence1.effet)
    elif number == 2:
        print(competence2.nom, competence2.effet)
    else:
        print("Choix invalide")
        capacite()


def main():
    personnage()

    equipement()

    capacite()

    arene()

main()
