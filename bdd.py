import sqlite3

class Bdd():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('golfstats.db')
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)

    def create(self, sql):
        pass

    def read(self, request):
        cur = self.conn.cursor()

        return cur.execute(request)

        cur.close()
        conn.close()

    def update(self, sql):
        pass

    def delete(self, sql):
        pass

def main():
    connection = Bdd()

if __name__ == "__main__": main()
