import sys
from PyQt5 import uic
from setComboBox import *
from scoreCard import *
from PyQt5.QtWidgets import QMessageBox

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

    def paramHoles(self):
        if self.nbHole == 9:
            endObject = "_9"
            j = 9
        elif self.nbHole == 18:
            endObject = ""
            j = 18
        else:
            print("Save error")
            return "error"

        return endObject, j

    def deleteScoreCard(self, item):
        msg = QMessageBox()
        msg.setWindowTitle("Supprimer carte")
        msg.setText("Souhaitez-vous supprimer votre carte de score n°" + self.tab_result.item(item, 0).text() + " ?")
        msg.setStandardButtons(QMessageBox.Ok |QMessageBox.Cancel)
        result_delete = msg.exec_()

        if result_delete == QMessageBox.Ok:
            id_scorecard = self.tab_result.item(item, 0).text()
            sql = f"""DELETE FROM scorecards WHERE idscorecards = {id_scorecard}"""
            bddConnect = bdd.Bdd()
            delete_scorecards = bddConnect.delete(sql)
            sql = f"""DELETE FROM results WHERE idscorecards = {id_scorecard}"""
            delete_scorecards = bddConnect.delete(sql)
            self.tab_result.removeRow(item)

    def clearCard(self):
        endObject, j = self.paramHoles()

        for i in range(j):
            score = "cmb_hole_" + str(i + 1) + str(endObject)
            club = "cmb_club_" + str(i + 1) + str(endObject)
            fairway = "chk_fairway_" + str(i + 1) + str(endObject)
            green = "chk_green_" + str(i + 1) + str(endObject)

            getattr(self, score).clear()
            getattr(self, club).clear()
            getattr(self, fairway).setChecked(False)
            getattr(self, green).setChecked(False)

            # Enable saved button
            self.btn_valid.setEnabled(True)
            self.btn_valid_9.setEnabled(True)

    def addCardPages(self):
        self.clearCard()
        endObject, j = self.paramHoles()

        bddConnect = bdd.Bdd()
        list_clubs = bddConnect.read("SELECT * FROM clubs ORDER BY idclubs")

        for row in list_clubs:
            for i in range(j):
                club = "cmb_club_" + str(i + 1) + str(endObject)
                getattr(self, club).addItem(str(row[2]), str(row[0]))

        list_score = bddConnect.read(
            "SELECT holesnumber, holespar FROM holes WHERE idcourses = " + self.cmb_course.itemData(
                self.cmb_course.currentIndex()) + " ORDER BY holesnumber")

        for row in list_score:
            maxScore = row[1] + 6
            hole = "lbl_hole_" + str(row[0]) + str(endObject)

            getattr(self, hole).setText(str(row[1]))

            for i in range(maxScore):
                score = "cmb_hole_" + str(row[0]) + str(endObject)
                getattr(self, score).addItem(str(i))

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
        endObject, j = self.paramHoles()

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
        self.tab_result.cellDoubleClicked.connect(lambda item: self.deleteScoreCard(item=item))

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
            self.nbHole = 9
            self.addCardPages()

        else:
            self.stackedWidget.setCurrentIndex(0)
            self.nbHole = 18
            self.addCardPages()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    form = Main()
    form.show()

    sys.exit(app.exec_())