
class Phaetons:
    def __init__(self,

                 nom: str,
                 types: str,
                 niveau: int,
                 sante : float,
                 attaque1: str, #carte
                 attaque2: str, #carte
                 attaque3: str, #carte
                 parade1: str, #carte
                 parade2: str, #carte
                 parade3: str, #carte
                 ulti = str, #carte
                 evolution = bool):

        self.nom = nom
        self.types = types
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
        fait évoluer le paheton et applique les modification (à définir)
        """
        pass


class Carte:
    def __init__(self,

                 nom: str,
                 est_parade:bool,
                 est_attaque:bool,
                 est_ulti:bool,
                 degats: float,
                 parade: float,
                 degat_ulti: float,):

        self.nom = nom
        self.degats = degats
        self.parade = parade
        self.degat_ulti = degat_ulti
        self.est_parade = est_parade
        self.est_attaque = est_attaque
        self.est_ulti = est_ulti
        self.est_verouille = False


    def verouiller(self):
        """
        verouille une carte qui n'est plus utilisable
        """
        self.est_verouille = True
        return self.est_verouille


class Combat:
    def __init__(self,

                 phaeton1: str,
                 phaeton2: str,
                 slot: list, # Correspond aux trois emplacements vide pour placer les attaques et ou parade ou ulti
                 attaque: list, # La liste des trois cartes d'attaque que le joueur peut placer dans le slot
                 parade: list, # idem pour les parades
                 coups_speciaux: list, # idem pour les coups speciaux
                 boost_attaque: float):

        self.phaetton1 = phaeton1
        self.phaeton2 = phaeton2
        self.slot = slot
        self.attaque = attaque
        self.parade = parade
        self.coups_speciaux = coups_speciaux
        self.boost_attaque = boost_attaque
        self.nb_attaque = 0 # nombre de cartes d'attaque dans le slot
        self.nb_parade = 0 # nombre de cartes de parade dans le slot
        self.nb_spe = 0 # nombre de cartes de spe dans le slot (=coups speciaux)
        self.est_valide = False # bouton pour valider le slot


    def placer_attaque1(self):
        """
        placer une carte attaque dans le slot
        """
        if self.nb_attaque < 2 or self.nb_spe < 1:
            self.slot.append(self.attaque[0])
            self.nb_attaque += 1
        else:
            print("seulement 2 cartes de ce type sont autorisés au maximum")

    def placer_attaque2(self):
        """
        placer une carte attaque dans le slot
        """
        if self.nb_attaque < 2  or self.nb_spe < 1:
            self.slot.append(self.attaque[1])
            self.nb_attaque += 1
        else:
            print("seulement 2 cartes de ce type sont autorisés au maximum")

    def placer_attaque3(self):
        """
        placer une carte attaque dans le slot
        """
        if self.nb_attaque < 2  or self.nb_spe < 1:
            self.slot.append(self.attaque[2])
            self.nb_attaque += 1
        else:
            print("seulement 2 cartes de ce type sont autorisés au maximum")

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

    def valider_slot(self):
        """
        Bouton qui permet de valider le slot. Il faut que les deux joueurs valide pour lancer la phase de combat
        """
        self.est_valide = True
        return self.est_valide

    @staticmethod
    def attaquer(joueur1, joueur2):
        """
        Effectue toutes les actions des cartes dans les slots (attaques, parades et ulti)
        """

        for i in joueur1.slot:

            if joueur1.slot[i].est_attaque and joueur2.slot[i].est_attaque or\
                    joueur1.slot[i].est_ulti and joueur2.slot[i].est_ulti or\
                    joueur1.slot[i].est_ulti and joueur2.slot[i].est_attaque or\
                    joueur1.slot[i].est_attaque and joueur2.slot[i].est_ulti:

                joueur1.sante -= joueur2.slot[i].degats
                joueur2.sante -= joueur1.slot[i].degats

            elif joueur1.slot[i].est_attaque and joueur2.slot[i].est_parade :
                if joueur2.slot[i].parade < joueur1.slot[i].degats:
                    joueur2.sante -= joueur1.slot[i].degats - joueur2.slot[i].parade

            elif joueur2.slot[i].est_attaque and joueur1.slot[i].est_parade :
                if joueur1.slot[i].parade < joueur2.slot[i].attaque:
                    joueur1.sante -= joueur2.slot[i].degats - joueur1.slot[i].parade

            elif joueur1.slot[i].est_ulti and joueur2.slot[i].est_parade :
                joueur2.sante -= joueur1.slot[i].degats_ulti

            elif joueur2.slot[i].est_ulti and joueur1.slot[i].est_parade :
                joueur1.sante -= joueur2.slot[i].degats_ulti


    def lancer_combat(self, joueur1, joueur2):
        """
        vérifie si les slots sont validé et lance le combat
        """
        if joueur1.valider_solt() and joueur2.valider_solt():
            self.attaquer(joueur1, joueur2)
