def scoreCardsPage(self):
    # Hide ToolBar
    self.toolBarCards.hide()
    self.toolBarParameters.hide()
    self.toolBarStats.hide()

    # Show ToolBar
    self.toolBarCards.show()

    self.stacked.setCurrentIndex(0)
    self.tab_result.setColumnCount(9)
    self.tab_result.setHorizontalHeaderLabels(
        ["Id carte", "Date", "Parcours", "Score", "Nb Fairway", "Greens en régulation", "Météo", "Fluidité de jeu",
         "Mode de jeu"])
    # self.tab_result.cellDoubleClicked.connect(lambda item: self.addCardPage(item=item))
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
    list_card = self.bddConnect(sql)
    self.tab_result.setRowCount(0)

    for row_number, row_data in enumerate(list_card):
        self.tab_result.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.tab_result.setItem(row_number, column_number, QTableWidgetItem(str(data)))


def addCardPage(self):
    self.stacked.setCurrentIndex(1)
    self.setWindowTitle("Ajouter une carte de score")