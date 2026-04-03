import socket
import json

class DBClient:
    """
    Classe utilitaire pour communiquer avec le serveur de base de données.
    Elle gère la connexion, la sérialisation JSON et la récupération des erreurs.
    """
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port

    def query(self, sql_string, params=()):
        """
        Envoie une requête SQL et ses paramètres au serveur.
        
        :param sql_string: La requête SQL (ex: "SELECT * FROM table WHERE id = ?")
        :param params: Un tuple contenant les valeurs à substituer aux '?'
        :return: Un dictionnaire contenant le statut et les données (ou l'erreur)
        """
        
        # 1. Préparation du message
        # On regroupe la requête et les paramètres dans un dictionnaire
        chargement = {
            "query": sql_string,
            "params": params
        }
        
        try:
            # 2. Création du Socket
            # socket.AF_INET : On utilise l'adresse IPv4
            # socket.SOCK_STREAM : On utilise le protocole TCP (fiable, garantit l'ordre)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                
                # 3. Connexion au serveur
                sock.connect((self.host, self.port))
                
                # 4. Envoi des données
                # json.dumps : Transforme le dictionnaire en chaîne de caractères (string)
                # .encode('utf-8') : Transforme la chaîne en octets (bytes) pour le réseau
                message = json.dumps(chargement).encode('utf-8')
                sock.sendall(message)
                
                # 5. Attente et réception de la réponse
                # 16384 (16 Ko) est la taille maximale du tampon de réception
                # Si la réponse est plus grande, il faudra boucler sur recv()
                reponse_brute = sock.recv(16384)
                
                if not reponse_brute:
                    return {"status": "error", "message": "Le serveur a fermé la connexion sans réponse."}

                # 6. Décodage de la réponse
                # .decode('utf-8') : Transforme les octets reçus en chaîne de caractères
                # json.loads : Transforme la chaîne JSON en dictionnaire Python exploitable
                return json.loads(reponse_brute.decode('utf-8'))

        except ConnectionRefusedError:
            return {"status": "error", "message": "Impossible de se connecter : le serveur est-il lancé ?"}
        except Exception as e:
            # Capture toute autre erreur (réseau, timeout, format de données)
            return {"status": "error", "message": f"Erreur client : {str(e)}"}

# --- EXEMPLE DE TEST ---
if __name__ == "__main__":
    # Initialisation du client (pointe vers localhost par défaut)
    db = DBClient(host='127.0.0.1', port=9999)
    
    # Test d'une lecture de données
    # Note : On passe les paramètres dans un tuple (obligatoire pour la sécurité)
    print("--- Test Lecture ---")
    reponse = db.query("SELECT * FROM UTILISATEUR WHERE pseudo = ?", ('Lumina',))
    
    if reponse.get("status") == "success":
        for ligne in reponse["data"]:
            print(f"Utilisateur trouvé : {ligne}")
    else:
        print(f"Erreur : {reponse.get('message')}")

    # Test d'une écriture
    print("\n--- Test sur l'autre table ---")
    reponse_ins = db.query("SELECT * FROM STATISTIQUES")
    print(f"Résultat : {reponse_ins}")