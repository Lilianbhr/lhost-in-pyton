import sqlite3

def initialiser_bdd():
    # Connexion (crée le fichier s'il n'existe pas)
    conn = sqlite3.connect('ma_base_de_donnees.db3')
    cursor = conn.cursor()

    # Activation des clés étrangères pour SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    print("Création des tables...")

    # 1. Création de la table UTILISATEUR
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UTILISATEUR (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pseudo TEXT NOT NULL UNIQUE,
            mdp TEXT NOT NULL,
            pos_x REAL DEFAULT 0.0,
            pos_y REAL DEFAULT 0.0,
            nom_joueur TEXT
        )
    ''')

    # 2. Création de la table STATISTIQUES
    # id_joueur fait référence à UTILISATEUR(id)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STATISTIQUES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_joueur INTEGER NOT NULL,
            nb_cnx INTEGER DEFAULT 0,
            plus_fort TEXT,
            temps_cnx REAL DEFAULT 0.0,
            nb_combats INTEGER DEFAULT 0,
            FOREIGN KEY (id_joueur) REFERENCES UTILISATEUR(id) ON DELETE CASCADE
        )
    ''')

    print("Insertion des données d'exemple...")

    # Données pour UTILISATEUR
    # Format : (pseudo, mdp, pos_x, pos_y, nom_joueur)
    utilisateurs = [
        ('Lumina', 'p@ssword123', 120.5, 450.2, 'Arthur'),
        ('ShadowK', 'shadow_66', -15.0, 88.4, 'Kylian')
    ]
    
    for u in utilisateurs:
        cursor.execute('''
            INSERT INTO UTILISATEUR (pseudo, mdp, pos_x, pos_y, nom_joueur) 
            VALUES (?, ?, ?, ?, ?)
        ''', u)
        
        # Récupération de l'ID qui vient d'être généré pour lier les stats
        id_genere = cursor.lastrowid
        
        # Données pour STATISTIQUES liées au joueur actuel
        # On crée des stats bidon pour l'exemple
        if u[0] == 'Lumina':
            stats = (id_genere, 12, 'Magiemou', 3600.5, 45)
        else:
            stats = (id_genere, 5, 'Dracodur', 1200.0, 12)
            
        cursor.execute('''
            INSERT INTO STATISTIQUES (id_joueur, nb_cnx, plus_fort, temps_cnx, nb_combats) 
            VALUES (?, ?, ?, ?, ?)
        ''', stats)

    # Sauvegarde des modifications
    conn.commit()
    conn.close()
    print("Base de données 'ma_base_de_donnees.db3' créée et remplie avec succès.")

if __name__ == "__main__":
    initialiser_bdd()