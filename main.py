import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
import bdd
from newcards import *
from setComboBox import *

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

        self.cmb_course.currentIndexChanged.connect(self.nbHoles)
        self.btn_valid.clicked.connect(saveCard18)
        self.btn_valid_9.clicked.connect(saveCard9)

        # Insert data in ComboBox
        lstCourses(self)
        lstWeather(self)
        lstSpeed(self)
        lstStarter(self)
        lstParty(self)
        lstBalls(self)

    def nbHoles(self):
        print("passe par là")
        bddConnect = bdd.Bdd()
        hole_number = bddConnect.read("SELECT coursesholes FROM courses WHERE courses.idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()))

        if hole_number.fetchone()[0] == 9:
            self.stackedWidget.setCurrentIndex(1)
            addCardPage9(self)
        else:
            self.stackedWidget.setCurrentIndex(0)
            addCardPage18(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    form = Main()
    form.show()

    sys.exit(app.exec_())