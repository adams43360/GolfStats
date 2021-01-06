import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
import bdd

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        uic.loadUi("main.ui", self)
        self.setupUi()

    def setupUi(self):
        # Actions
        self.actionCards.triggered.connect(self.scoreCardsPage)
        self.actionAddCard.triggered.connect(self.addCardPage)
        self.btn_valid.clicked.connect(self.saveCard18)
        self.btn_valid_9.clicked.connect(self.saveCard9)
        self.scoreCardsPage()
        self.cmb_course.currentIndexChanged.connect(self.nbHoles)

        # Insert data in ComboBox
        self.lstCourses()
        self.lstWeather()
        self.lstSpeed()
        self.lstStarter()
        self.lstParty()
        self.lstBalls()
        #self.lstClubs()

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
        #list_card = self.bddConnect(sql)

        bddConnect = bdd.Bdd()
        list_card = bddConnect.read(sql)

        self.tab_result.setRowCount(0)

        for row_number, row_data in enumerate(list_card):
            self.tab_result.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tab_result.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def saveCard18(self):
        print("Save 18")

    def saveCard9(self):
        print("Save 9")

    def clearCard18(self):
        print("Clear 18")
        self.cmb_club_1.clear()
        self.cmb_club_2.clear()
        self.cmb_club_3.clear()
        self.cmb_club_4.clear()
        self.cmb_club_5.clear()
        self.cmb_club_6.clear()
        self.cmb_club_7.clear()
        self.cmb_club_8.clear()
        self.cmb_club_9.clear()
        self.cmb_club_10.clear()
        self.cmb_club_11.clear()
        self.cmb_club_12.clear()
        self.cmb_club_13.clear()
        self.cmb_club_14.clear()
        self.cmb_club_15.clear()
        self.cmb_club_16.clear()
        self.cmb_club_17.clear()
        self.cmb_club_18.clear()

        self.cmb_hole_1.clear()
        self.cmb_hole_2.clear()
        self.cmb_hole_3.clear()
        self.cmb_hole_4.clear()
        self.cmb_hole_5.clear()
        self.cmb_hole_6.clear()
        self.cmb_hole_7.clear()
        self.cmb_hole_8.clear()
        self.cmb_hole_9.clear()
        self.cmb_hole_10.clear()
        self.cmb_hole_11.clear()
        self.cmb_hole_12.clear()
        self.cmb_hole_13.clear()
        self.cmb_hole_14.clear()
        self.cmb_hole_15.clear()
        self.cmb_hole_16.clear()
        self.cmb_hole_17.clear()
        self.cmb_hole_18.clear()

    def clearCard9(self):
        print(("Clear 9"))
        self.cmb_club_1_9.clear()
        self.cmb_club_2_9.clear()
        self.cmb_club_3_9.clear()
        self.cmb_club_4_9.clear()
        self.cmb_club_5_9.clear()
        self.cmb_club_6_9.clear()
        self.cmb_club_7_9.clear()
        self.cmb_club_8_9.clear()
        self.cmb_club_9_9.clear()

        self.cmb_hole_1_9.clear()
        self.cmb_hole_2_9.clear()
        self.cmb_hole_3_9.clear()
        self.cmb_hole_4_9.clear()
        self.cmb_hole_5_9.clear()
        self.cmb_hole_6_9.clear()
        self.cmb_hole_7_9.clear()
        self.cmb_hole_8_9.clear()
        self.cmb_hole_9_9.clear()

    def addCardPage9(self):
        self.clearCard9()
        bddConnect = bdd.Bdd()
        list_clubs = bddConnect.read("SELECT * FROM clubs ORDER BY idclubs")

        for row in list_clubs:
            self.cmb_club_1_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_2_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_3_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_4_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_5_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_6_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_7_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_8_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_9_9.addItem(str(row[2]), str(row[0]))

        list_score = bddConnect.read(
            "SELECT holesnumber, holespar FROM holes WHERE idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()) + " ORDER BY holesnumber")

        for row in list_score:
            maxScore = row[1] + 6

            if row[0] == 1:
                self.lbl_hole_1_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_1_9.addItem(str(i))
            elif row[0] == 2:
                self.lbl_hole_2_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_2_9.addItem(str(i))
            elif row[0] == 3:
                self.lbl_hole_3_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_3_9.addItem(str(i))
            elif row[0] == 4:
                self.lbl_hole_4_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_4_9.addItem(str(i))
            elif row[0] == 5:
                self.lbl_hole_5_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_5_9.addItem(str(i))
            elif row[0] == 6:
                self.lbl_hole_6_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_6_9.addItem(str(i))
            elif row[0] == 7:
                self.lbl_hole_7_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_7_9.addItem(str(i))
            elif row[0] == 8:
                self.lbl_hole_8_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_8_9.addItem(str(i))
            elif row[0] == 9:
                self.lbl_hole_9_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_9_9.addItem(str(i))

    def addCardPage18(self):
        self.clearCard18()
        bddConnect = bdd.Bdd()
        list_clubs = bddConnect.read("SELECT * FROM clubs ORDER BY idclubs")

        for row in list_clubs:
            self.cmb_club_1.addItem(str(row[2]), str(row[0]))
            self.cmb_club_2.addItem(str(row[2]), str(row[0]))
            self.cmb_club_3.addItem(str(row[2]), str(row[0]))
            self.cmb_club_4.addItem(str(row[2]), str(row[0]))
            self.cmb_club_5.addItem(str(row[2]), str(row[0]))
            self.cmb_club_6.addItem(str(row[2]), str(row[0]))
            self.cmb_club_7.addItem(str(row[2]), str(row[0]))
            self.cmb_club_8.addItem(str(row[2]), str(row[0]))
            self.cmb_club_9.addItem(str(row[2]), str(row[0]))
            self.cmb_club_10.addItem(str(row[2]), str(row[0]))
            self.cmb_club_11.addItem(str(row[2]), str(row[0]))
            self.cmb_club_12.addItem(str(row[2]), str(row[0]))
            self.cmb_club_13.addItem(str(row[2]), str(row[0]))
            self.cmb_club_14.addItem(str(row[2]), str(row[0]))
            self.cmb_club_15.addItem(str(row[2]), str(row[0]))
            self.cmb_club_16.addItem(str(row[2]), str(row[0]))
            self.cmb_club_17.addItem(str(row[2]), str(row[0]))
            self.cmb_club_18.addItem(str(row[2]), str(row[0]))

        list_score = bddConnect.read(
            "SELECT holesnumber, holespar FROM holes WHERE idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()) + " ORDER BY holesnumber")

        for row in list_score:
            maxScore = row[1] + 6

            if row[0] == 1:
                self.lbl_hole_1.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_1.addItem(str(i))
            elif row[0] == 2:
                self.lbl_hole_2.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_2.addItem(str(i))
            elif row[0] == 3:
                self.lbl_hole_3.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_3.addItem(str(i))
            elif row[0] == 4:
                self.lbl_hole_4.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_4.addItem(str(i))
            elif row[0] == 5:
                self.lbl_hole_5.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_5.addItem(str(i))
            elif row[0] == 6:
                self.lbl_hole_6.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_6.addItem(str(i))
            elif row[0] == 7:
                self.lbl_hole_7.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_7.addItem(str(i))
            elif row[0] == 8:
                self.lbl_hole_8.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_8.addItem(str(i))
            elif row[0] == 9:
                self.lbl_hole_9.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_9.addItem(str(i))
            elif row[0] == 10:
                self.lbl_hole_10.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_10.addItem(str(i))
            elif row[0] == 11:
                self.lbl_hole_11.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_11.addItem(str(i))
            elif row[0] == 12:
                self.lbl_hole_12.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_12.addItem(str(i))
            elif row[0] == 13:
                self.lbl_hole_13.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_13.addItem(str(i))
            elif row[0] == 14:
                self.lbl_hole_14.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_14.addItem(str(i))
            elif row[0] == 15:
                self.lbl_hole_15.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_15.addItem(str(i))
            elif row[0] == 16:
                self.lbl_hole_16.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_16.addItem(str(i))
            elif row[0] == 17:
                self.lbl_hole_17.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_17.addItem(str(i))
            elif row[0] == 18:
                self.lbl_hole_18.setText(str(row[1]))

                for i in range(maxScore):
                    self.cmb_hole_18.addItem(str(i))

    def addCardPage(self):
        self.date_score.setDate(QDate.currentDate())
        self.stacked.setCurrentIndex(1)
        self.setWindowTitle("Ajouter une carte de score")

    def lstCourses(self):
        bddConnect = bdd.Bdd()
        liste_courses = bddConnect.read("SELECT courses.coursesname, courses.idcourses, golfs.golfsname FROM golfs, courses WHERE courses.idgolfs = golfs.idgolfs ORDER BY golfs.golfsname")

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

    def nbHoles(self):
        bddConnect = bdd.Bdd()
        hole_number = bddConnect.read("SELECT coursesholes FROM courses WHERE courses.idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()))

        if hole_number.fetchone()[0] == 9:
            self.stackedWidget.setCurrentIndex(1)
            self.addCardPage9()
        else:
            self.stackedWidget.setCurrentIndex(0)
            self.addCardPage18()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    form = Main()
    form.show()

    sys.exit(app.exec_())