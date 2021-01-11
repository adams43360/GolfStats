import bdd

def saveCard18(self):
    print("Save 18")

'''def saveCard9(self):
    print("Save 9")

    for i in range(8):
        i += 1
        value = "cmb_hole_" + str(i) + "_9"
        
        print(getattr(self, value).currentText())
        
        # Insert scorecards
    dateScore = str(self.date_score.text())
    sql = f"""INSERT INTO scorecards (scorecardsdate, idcourses, idpartytype, idstreterballs, idballs, idweather, idtermes) VALUES ('{dateScore}')"""

    bddConnect = bdd.Bdd()
    bddinsert = bddConnect.insert(sql)
    print(bddinsert)

    # Insert results data
    for i in range(8):
        resultClub = 
        sql = "INSERT INTO results (idholes, resultscore, resultfairway, resultgreen, idclubs, resultcomment, idscorecards) VALUES ()"'''


def clearCard9(self):
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

def clearCard18(self):
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

def addCardPage9(self):
    clearCard9(self)
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

    list_score = bddConnect.read("SELECT holesnumber, holespar FROM holes WHERE idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()) + " ORDER BY holesnumber")

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
    clearCard18(self)
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

    list_score = bddConnect.read("SELECT holesnumber, holespar FROM holes WHERE idcourses = " + self.cmb_course.itemData(self.cmb_course.currentIndex()) + " ORDER BY holesnumber")

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