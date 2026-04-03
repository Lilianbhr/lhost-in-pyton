
class Phaetons:
    def __init__(self, nom: str, type: str, niveau: int, sante, attaque1: str, attaque2: str, attaque3: str, parade1: str, parade2: str, parade3: str, ulti = str, evolution = bool):
        self.nom = nom
        self.type = type
        self.niveau = niveau
        self.sante = sante
        self.attaque1 = attaque1
        self.attaque2 = attaque2
        self.attaque3 = attaque3
        self.parade1 = parade1
        self.parade2 = parade2
        self.parade3 = parade3
        self.ulti = ulti
        self.evolution = evolution

    def evoluer(self):
        """
        fait évoluer le paheton
        """
        pass


class Carte:
    def __init__(self,nom, mouvement, degats, parade, degat_ulti):
        self.nom = nom
        self.mouvement = mouvement
        self.degats = degats
        self.parade = parade
        self.degat_ulti = degat_ulti

class Joueur:
    def __init__(self, pseudo: str, sante: float):
        self.pseudo = pseudo


class Combat:
    def __init__(self, phaeton1, phaeton2, slot, attaque, parade, coup_speciaux, boost_attaque):
        self.phaetton1 = phaeton1
        self.phaeton2 = phaeton2
        self.slot = slot
        self.attaque = attaque
        self.parade = parade
        self.coup_speciaux = coup_speciaux

    def lancer_attaque(self):
        """
        Lance une carte attaque dans un slot
        """

    def lancer_parade(self):
        """
        Lance une carte parade dans un slot
        """

    def lancer_coup_speciaux(self):
        """
        Lance une carte parade dans un slot
        """

    def infliger_degats(self):


