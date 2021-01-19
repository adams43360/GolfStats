import sqlite3

class Bdd():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('golfstats.db')
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)

    def insert(self, request):
        cur = self.conn.cursor()
        cur.execute(request)
        self.conn.commit()
        return cur.lastrowid

    def read(self, request):
        cur = self.conn.cursor()
        return cur.execute(request)

    def update(self, sql):
        pass

    def delete(self, request):
        cur = self.conn.cursor()
        cur.execute(request)
        self.conn.commit()
        return "deleted"

def main():
    connection = Bdd()

if __name__ == "__main__": main()
