import pygame
import sys
from client import DBClient  # On importe votre classe client

class ConnexionInterface:
    def __init__(self, host='localhost', port=9999):
        # Initialisation de Pygame
        pygame.init()
        self.ecran = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Testeur de Connexion SQL")
        
        # Polices et Couleurs
        self.font = pygame.font.SysFont("Arial", 20)
        self.small_font = pygame.font.SysFont("Arial", 16)
        self.COLOR_BG = (30, 30, 35)
        self.COLOR_BTN = (50, 150, 50)
        self.COLOR_TEXT = (255, 255, 255)
        self.COLOR_ERR = (200, 50, 50)

        # Instance du client
        self.client = DBClient(host, port)
        
        # État de l'interface
        self.status_msg = "Prêt"
        self.derniere_reponse = "Aucune donnée"
        self.serveur_en_ligne = False

    def dessiner_texte(self, text, x, y, couleur=None, font=None):
        if couleur is None: couleur = self.COLOR_TEXT
        if font is None: font = self.font
        img = font.render(text, True, couleur)
        self.ecran.blit(img, (x, y))

    def run(self):
        # Définition des boutons (Rectangles)
        btn_test = pygame.Rect(50, 100, 200, 50)
        btn_requete = pygame.Rect(50, 170, 200, 50)

        running = True
        while running:
            self.ecran.fill(self.COLOR_BG)
            
            # 1. Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_test.collidepoint(event.pos):
                        self.test_connexion()
                    if btn_requete.collidepoint(event.pos):
                        self.test_requete()

            # 2. Dessin de l'interface
            self.dessiner_texte("Tableau de bord de test réseau", 50, 30)
            
            # Dessin des boutons
            pygame.draw.rect(self.ecran, self.COLOR_BTN, btn_test, border_radius=5)
            self.dessiner_texte("Tester Connexion", 65, 112)
            
            pygame.draw.rect(self.ecran, (70, 70, 200), btn_requete, border_radius=5)
            self.dessiner_texte("Envoyer SELECT", 75, 182)

            # 3. Affichage du statut et des réponses
            # État du serveur (Pastille)
            voyant = (0, 255, 0) if self.serveur_en_ligne else (255, 0, 0)
            pygame.draw.circle(self.ecran, voyant, (50, 270), 8)
            self.dessiner_texte(f"Statut : {self.status_msg}", 70, 260)

            # Zone de réponse (Logs)
            pygame.draw.rect(self.ecran, (20, 20, 20), (50, 310, 700, 150))
            self.dessiner_texte("Dernière réponse du serveur :", 50, 290, font=self.small_font)
            
            # Affichage multiligne simplifié pour la réponse
            self.dessiner_texte(str(self.derniere_reponse)[:150], 60, 320, couleur=(150, 255, 150), font=self.small_font)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def test_connexion(self):
        """ Vérifie simplement si le serveur répond """
        res = self.client.query("SELECT 1") # Requête SQL minimale
        if "error" not in res.get("status", ""):
            self.status_msg = "Serveur en ligne"
            self.serveur_en_ligne = True
            self.derniere_reponse = "Ping réussi !"
        else:
            self.status_msg = "Serveur hors ligne"
            self.serveur_en_ligne = False
            self.derniere_reponse = res.get("message")

    def test_requete(self):
        """ Envoie une vraie requête de test """
        self.status_msg = "Envoi de la requête..."
        res = self.client.query("SELECT * FROM UTILISATEUR LIMIT 1", ())
        self.derniere_reponse = str(res)
        if res.get("status") == "success":
            self.status_msg = "Données reçues"
        else:
            self.status_msg = "Erreur SQL"

if __name__ == "__main__":
    # Assurez-vous que le serveur (server.py) tourne avant de lancer l'interface
    app = ConnexionInterface(host='localhost', port=9999)
    app.run()