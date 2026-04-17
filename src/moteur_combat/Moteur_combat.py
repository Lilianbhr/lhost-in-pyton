
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
        verouille une carte plus utilisable
        """
        self.est_verouille = True
        return self.est_verouille


class Combat:
    def __init__(self, phaeton1: str,
                 phaeton2: str,
                 slot: list, # Correspond aux trois emplacements pour placer les attaques et ou parade ou ulti
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
        self.nb_attaque = 0 # Le nombre d'attaque placées
        self.nb_parade = nb_parade
        self.nb_parade = 0
        self.nb_spe = nb_spe
        self.nb_spe = 0
        self.est_valide = False #Bouton pour valider le slot


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

    def valider_slot(self):
        """
        Bouton qui permet de valider le slot. Il faut que les deux joueurs valide pour lancer la phase de combat
        """
        self.est_valide = True
        return self.est_valide

    def attaquer(self, Joueur1, Joueur2):
        """
        Effectue toutes les actions des cartes dasn les slots (attaques, parades et ulti)
        """

        for i in self.slot:

            if Joueur1.slot[i].est_attaque and Joueur2.slot[i].est_attaque or\
                    Joueur1.slot[i].est_ulti and Joueur2.slot[i].est_ulti or\
                    Joueur1.slot[i].est_ulti and Joueur2.slot[i].est_attaque or\
                    Joueur1.slot[i].est_attaque and Joueur2.slot[i].est_ulti:

                Joueur1.sante -= Joueur1.slot[0].degats
                Joueur2.sante -= Joueur2.slot[0].degats

            elif Joueur1.slot[i].est_attaque and Joueur2.slot[i].est_parade :
                if Joueur2.slot[i].parade < Joueur1.slot[i].attaque:
                    Joueur1.sante -= Joueur1.slot[i].degats - Joueur2.slot[0].parade

            elif Joueur2.slot[i].est_attaque and Joueur1.slot[i].est_parade :
                if Joueur1.slot[i].parade < Joueur2.slot[i].attaque:
                    Joueur2.sante -= Joueur2.slot[i].degats - Joueur1.slot[0].parade

            elif Joueur1.slot[i].est_ulti and Joueur2.slot[i].est_parade :
                Joueur2.sante -= Joueur1.slot[i].degats_ulti

            elif Joueur2.slot[i].est_ulti and Joueur1.slot[i].est_parade :
                Joueur1.sante -= Joueur2.slot[i].degats_ulti


    def lancer_combat(self, Joueur1, Joueur2):
        """
        vérifie si les slots sont validé et lance le combat
        """
        if Joueur1.valider_solt() and Joueur2.valider_solt():
            self.attaquer(self, Joueur1, Joueur2)




zoizo_blanc = Phaetons("zoizo_blanc", "feu", 1, 50,
                       "coup de bec", "coup de griffe brulante", "regard perçant",
                       "bouclier de feu", "plumes de métal", "coque imbrisable",
                       "Mega boum", False)

zoiso_de_vierge = Phaetons("zoiso_de_vierge", "feu", 1, 50, "saint kroassement",
                           "Paax", "Chog", "saint croisement", "saint croissant",
                           "Hectarr", "Lars", False)

coup_de_bec = Carte("coup_de_bec", False, True, False,
                    8, 0, 0,)
coup_de_griffe_brulante = Carte("coup_de_griffe_brulante", False, True,False,
                                12, 0, 0,)