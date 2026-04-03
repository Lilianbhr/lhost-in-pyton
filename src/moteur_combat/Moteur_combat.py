#class Joueur:
    #def __init__(self, pseudo: str):
        #self.pseudo = pseudo

class Phaetons:
    def __init__(self,
                 nom: str,
                 type: str,
                 niveau: int,
                 sante, attaque1: str,
                 attaque2: str,
                 attaque3: str,
                 parade1: str,
                 parade2: str,
                 parade3: str,
                 ulti = str,
                 evolution = bool):
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

    def infliger_degats(self, adversaire):
        adversaire.sante -= self.degats

    def parer(self, adversaire):
        adversaire.degats -= self.parade


class Combat:
    def __init__(self, phaeton1: str,
                 phaeton2: str,
                 slot: list,
                 attaque: list,
                 parade: list,
                 coups_speciaux: list,
                 boost_attaque: float,
                 nb_attaque: int,
                 nb_parade: int,
                 nb_spe: int):
        self.phaetton1 = phaeton1
        self.phaeton2 = phaeton2
        self.slot = slot
        self.attaque = attaque
        self.parade = parade
        self.coups_speciaux = coups_speciaux
        self.boost_attaque = boost_attaque
        self.nb_attaque = nb_attaque
        self.nb_attaque = 0
        self.nb_parade = nb_parade
        self.nb_parade = 0
        self.nb_spe = nb_spe
        self.nb_spe = 0

    def placer_attaque1(self):
        """
        placer une carte attaque dans le slot
        """
        if self.nb_attaque < 2 or self.nb_spe < 1:
            self.slot.append(self.attaque[0])
            self.nb_attaque += 1
        else:
            print("seulement 2 cartes de ce type")

    def placer_attaque2(self):
        """
        placer une carte attaque dans le slot
        """
        if self.nb_attaque < 2  or self.nb_spe < 1:
            self.slot.append(self.attaque[1])
            self.nb_attaque += 1
        else:
            print("seulement 2 cartes de ce type")

    def placer_attaque3(self):
        """
        placer une carte attaque dans le slot
        """
        if self.nb_attaque < 2  or self.nb_spe < 1:
            self.slot.append(self.attaque[2])
            self.nb_attaque += 1
        else:
            print("seulement 2 cartes de ce type")

    def placer_parade1(self):
        """
        placer une carte parade dans le slot
        """
        if self.nb_parade < 2 or self.nb_spe < 1:
            self.slot.append(self.parade[0])
            self.nb_parade += 1

    def placer_parade2(self):
        """
        placer une carte parade dans le slot
        """
        if self.nb_parade < 2 or self.nb_spe < 1:
            self.slot.append(self.parade[1])
            self.nb_parade += 1

    def placer_parade3(self):
        """
        placer une carte parade dans le slot
        """
        if self.nb_parade < 2 or self.nb_spe < 1:
            self.slot.append(self.parade[2])
            self.nb_parade += 1

    def placer_coup_special1(self):
        """
        place une carte coup_speciaux dans le slot
        """
        if self.nb_spe < 1:
            self.slot.append(self.coups_speciaux[0])
            self.nb_spe += 1

    def placer_coup_special2(self):
        """
        place une carte coup_speciaux dans le slot
        """
        if self.nb_spe < 1:
            self.slot.append(self.coups_speciaux[1])
            self.nb_spe += 1

    def placer_coup_speciaux3(self):
        """
        place une carte coup_speciaux dans le slot
        """
        if self.nb_spe < 1:
            self.slot.append(self.coups_speciaux[2])
            self.nb_spe += 1


    def confirmer_slot(self):
        """
        confirme et lance les cartes dans le slot
        """
        pass
