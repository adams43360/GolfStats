import bdd

def clearCard9(self):
    for i in range(9):
        score = "cmb_hole_" + str(i + 1) + "_9"
        club = "cmb_club_" + str(i + 1) + "_9"
        fairway = "chk_fairway_" + str(i + 1) + "_9"
        green = "chk_green_" + str(i + 1) + "_9"

        getattr(self, score).clear()
        getattr(self, club).clear()
        getattr(self, fairway).setChecked(False)
        getattr(self, green).setChecked(False)

        # Enable saved button
        self.btn_valid_9.setEnabled(True)

def clearCard18(self):
    # Enable saved button
    self.btn_valid.setEnabled(True)

    for i in range(18):
        score = "cmb_hole_" + str(i + 1)
        club = "cmb_club_" + str(i + 1)
        fairway = "chk_fairway_" + str(i + 1)
        green = "chk_green_" + str(i + 1)

        getattr(self, score).clear()
        getattr(self, club).clear()
        getattr(self, fairway).setChecked(False)
        getattr(self, green).setChecked(False)

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