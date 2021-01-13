import sys
from PyQt5 import uic
from newcards import *
from setComboBox import *
from scoreCard import *

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        uic.loadUi("main.ui", self)
        self.setupUi()

    def setupUi(self):
        # Actions
        self.actionCards.triggered.connect(self.scoreCardsPage)
        self.actionAddCard.triggered.connect(self.addCardPage)
        self.scoreCardsPage()
        self.nbHole = 0
        lstCourses(self)

    def saveCard(self):
        # Disable saved button
        self.btn_valid.setEnabled(False)
        self.btn_valid_9.setEnabled(False)

        # Save the head of the card into scorecads
        id_course = self.cmb_course.itemData(self.cmb_course.currentIndex())
        id_speed = self.cmb_speed.itemData(self.cmb_speed.currentIndex())
        id_weather = self.cmb_weather.itemData(self.cmb_weather.currentIndex())
        id_balls = self.cmb_balls.itemData(self.cmb_balls.currentIndex())
        id_starter = self.cmb_starter.itemData(self.cmb_starter.currentIndex())
        id_party = self.cmb_party.itemData(self.cmb_party.currentIndex())
        date_sc = str(self.date_score.text())

        sql = f"""INSERT INTO scorecards (scorecardsdate, idcourses, idpartytype, idstarterballs, idballs, idweather, idtermes) 
                                 VALUES ("{date_sc}", {id_course}, {id_party}, {id_starter}, {id_balls}, {id_weather}, {id_speed})"""

        bddConnect = bdd.Bdd()
        id_card = bddConnect.insert(sql)

        # Save all the line into results
        if self.nbHole == 9:
            print("Save 9")
            endObject = "_9"
            j = 9
        elif self.nbHole == 18:
            print("Save 18")
            endObject = ""
            j = 18
        else:
            print("Save error")
            return "error"

        for i in range(j):
            score = "cmb_hole_" + str(i + 1) + str(endObject)
            club = "cmb_club_" + str(i + 1) + str(endObject)
            fairway = "chk_fairway_" + str(i + 1) + str(endObject)
            green = "chk_green_" + str(i + 1) + str(endObject)

            id_score = getattr(self, score).currentText()
            id_club = getattr(self, club).itemData(getattr(self, club).currentIndex())

            if getattr(self, fairway).isChecked() == True:
                id_fairway = 1
            else:
                id_fairway = 0

            if getattr(self, green).isChecked() == True:
                id_green = 1
            else:
                id_green = 0

            sql = f"""INSERT INTO results (idholes, resultscore, resultfairway, resultgreen, idclubs, resultcomment, idscorecards) 
                                             VALUES ({i + 1}, {id_score}, {id_fairway}, {id_green}, {id_club}, "", {id_card})"""
            id_score = bddConnect.insert(sql)
            print("card inserted n° : " + str(id_score))

    def scoreCardsPage(self):
        # Hide ToolBar
        self.toolBarCards.hide()
        self.toolBarParameters.hide()
        self.toolBarStats.hide()

        # Show ToolBar
        self.toolBarCards.show()

        self.stacked.setCurrentIndex(0)
        self.tab_result.setColumnCount(9)
        self.tab_result.setHorizontalHeaderLabels(["Id carte", "Date", "Parcours", "Score", "Nb Fairway", "Greens en régulation", "Météo", "Fluidité de jeu", "Mode de jeu"])
        #self.tab_result.cellDoubleClicked.connect(lambda item: self.addCardPage(item=item))
        self.setWindowTitle("Mes cartes de score")

        sql = "SELECT scorecards.idscorecards, " \
              "scorecards.scorecardsdate, " \
              "courses.coursesname, " \
              "sum(results.resultscore) as resultat, " \
              "sum(results.resultfairway) as fairway, " \
              "sum(results.resultgreen) as green, " \
              "weather.weathername, " \
              "partytype.partytypename, " \
              "termes.termesname " \
              "FROM scorecards, courses, results, weather, partytype, termes " \
              "WHERE scorecards.idcourses = courses.idcourses AND " \
              "scorecards.idweather = weather.idweather AND " \
              "scorecards.idtermes = termes.idtermes AND " \
              "scorecards.idpartytype = partytype.idpartytype AND " \
              "scorecards.idscorecards = results.idscorecards " \
              "GROUP BY scorecards.idscorecards;"

        bddConnect = bdd.Bdd()
        list_card = bddConnect.read(sql)

        self.tab_result.setRowCount(0)

        for row_number, row_data in enumerate(list_card):
            self.tab_result.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tab_result.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def addCardPage(self):
        self.date_score.setDate(QDate.currentDate())
        self.stacked.setCurrentIndex(1)
        self.setWindowTitle("Ajouter une carte de score")
        self.nbHoles()

        self.cmb_course.currentIndexChanged.connect(self.nbHoles)
        self.btn_valid.clicked.connect(self.saveCard)
        self.btn_valid_9.clicked.connect(self.saveCard)

        # Clear data in ComboBox
        self.cmb_speed.clear()
        self.cmb_weather.clear()
        self.cmb_balls.clear()
        self.cmb_starter.clear()
        self.cmb_party.clear()

        # Insert data in ComboBox
        lstWeather(self)
        lstSpeed(self)
        lstStarter(self)
        lstParty(self)
        lstBalls(self)


    def nbHoles(self):
        bddConnect = bdd.Bdd()
        hole_number = bddConnect.read("SELECT coursesholes FROM courses WHERE courses.idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()))

        if hole_number.fetchone()[0] == 9:
            self.stackedWidget.setCurrentIndex(1)
            addCardPage9(self)
            self.nbHole = 9
        else:
            self.stackedWidget.setCurrentIndex(0)
            addCardPage18(self)
            self.nbHole = 18

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    form = Main()
    form.show()

    sys.exit(app.exec_())