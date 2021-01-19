import bdd

def lstCourses(self):
    bddConnect = bdd.Bdd()
    liste_courses = bddConnect.read(
        "SELECT courses.coursesname, courses.idcourses, golfs.golfsname FROM golfs, courses WHERE courses.idgolfs = golfs.idgolfs ORDER BY golfs.golfsname")

    for row in liste_courses:
        self.cmb_course.addItem(str(row[0] + " : " + row[2]), str(row[1]))

def lstWeather(self):
    bddConnect = bdd.Bdd()
    liste_weather = bddConnect.read("SELECT * FROM weather ORDER BY weathername")

    for row in liste_weather:
        self.cmb_weather.addItem(str(row[1]), str(row[0]))

def lstSpeed(self):
    bddConnect = bdd.Bdd()
    liste_speed = bddConnect.read("SELECT * FROM termes ORDER BY termesname")

    for row in liste_speed:
        self.cmb_speed.addItem(str(row[1]), str(row[0]))

def lstStarter(self):
    bddConnect = bdd.Bdd()
    liste_starter = bddConnect.read("SELECT * FROM starterballs ORDER BY starterballsname")

    for row in liste_starter:
        self.cmb_starter.addItem(str(row[1]), str(row[0]))

def lstParty(self):
    bddConnect = bdd.Bdd()
    liste_party = bddConnect.read("SELECT * FROM partytype ORDER BY partytypename")

    for row in liste_party:
        self.cmb_party.addItem(str(row[1]), str(row[0]))

def lstBalls(self):
    bddConnect = bdd.Bdd()
    liste_balls = bddConnect.read("SELECT * FROM balls ORDER BY ballsname")

    for row in liste_balls:
        self.cmb_balls.addItem(str(row[1]), str(row[0]))