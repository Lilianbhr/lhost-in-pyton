import socketserver
import json
import sqlite3
import threading

class SQLGestion(socketserver.BaseRequestHandler):
    """
    Traite les requêtes SQL entrantes et interroge le fichier .db3
    """
    DB_FILE = "ma_base_de_donnees.db3"

    def handle(self):
        try:
            raw_data = self.request.recv(8192).strip()
            if not raw_data:
                return

            # On reçoit le dictionnaire : {"query": "SELECT...", "params": (...)}
            request_data = json.loads(raw_data.decode('utf-8'))
            query = request_data.get("query")
            params = request_data.get("params", ())

            # Exécution sur la base SQLite
            result = self.execute_sql(query, params)
            
            # Renvoi du résultat au client
            self.request.sendall(json.dumps(result).encode('utf-8'))
            
        except Exception as e:
            error_resp = {"status": "error", "message": str(e)}
            self.request.sendall(json.dumps(error_resp).encode('utf-8'))

    def execute_sql(self, query, params):
        try:
            # Connexion au fichier db3
            # check_same_thread=False est important car le serveur est multithreadé
            conn = sqlite3.connect(self.DB_FILE)
            cursor = conn.cursor()
            
            cursor.execute(query, params)
            
            # Si c'est une lecture (SELECT)
            if query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                column_names = [description[0] for description in cursor.description]
                # On transforme en liste de dictionnaires pour le JSON
                data = [dict(zip(column_names, row)) for row in rows]
                return {"status": "success", "data": data}
            
            # Si c'est une écriture (INSERT, UPDATE, DELETE)
            else:
                conn.commit()
                return {"status": "success", "affected_rows": cursor.rowcount}
                
        except sqlite3.Error as e:
            return {"status": "error", "message": f"Erreur SQL: {e}"}
        finally:
            conn.close()

class ThreadedSQLServer(socketserver.ThreadingTCPServer):
    # Permet de réutiliser l'adresse du port immédiatement après l'arrêt du serveur
    allow_reuse_address = True

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    server = ThreadedSQLServer((HOST, PORT), SQLGestion)
    print(f"Serveur SQL (SQLite) actif sur le port {PORT}...")
    server.serve_forever()