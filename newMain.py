import sys
from PyQt5 import QtWidgets, uic
import datetime
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QApplication, QDesktopWidget
from PyQt5.QtCore import QDate
from Connectdb import connections


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Timetable\\Signin.ui', self)
        self.Signin.clicked.connect(self.signin)
        self.signUp0.clicked.connect(self.signUp)

    def signin(self):
        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Account")
                values = cur.fetchall()
                for i in values:
                    if self.lineUsername.text() == i[1] and self.linePassword.text() == i[2]:
                        win.setCurrentIndex(win.currentIndex() + 1)
                        return
                QMessageBox.information(self, 'title', 'Invalid username or password')
        except:
            QMessageBox.information(self, 'title', 'Invalid username or password')

    def signUp(self):
        create = SignupScreen()
        win.addWidget(create)
        win.setCurrentIndex(win.currentIndex() + 1)

class SignupScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignupScreen, self).__init__()
        uic.loadUi('Timetable\\Signup.ui', self)
        self.signUp1.clicked.connect(self.signUp)

    def signUp(self):
        # try:
        user = self.userSignup.text()
        password = self.passwordSignup.text()
        confirm = self.confirmpassword.text()

        if len(user) == 0 or len(password) == 0 or len(confirm) == 0:
            QMessageBox.information(self, 'Sign up', 'Please fill in the blank')
        elif password != confirm:
            QMessageBox.information(self, 'Sign up', 'Passwords do not match!')
        else:
            self.execute_query("INSERT INTO Account (adminUsername, adminPass)VALUES (?, ?)", user, password, confirm)
            QMessageBox.information(self, "Sign up ", "Successfull")
            # win.setCurrentIndex(win.currentIndex(0))
        # except:
        # QMessageBox.information(self,'Sign up', 'Passwords do not match!')
        login = Login()
        win.addWidget(login)
        win.setCurrentIndex(win.currentIndex() + 1)

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Timetable\\mainnewMenu.ui', self)

        # set Button to change tab
        self.Account_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Class_pushBotton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.Room_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.Subject_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.Timetable_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.Student_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.insert_pushButton_4.clicked.connect(self.checkStudent)
        self.add_Button_timetable.clicked.connect(self.checkTimetable)
        self.insert_pushButton_2.clicked.connect(self.checkSubject)

        self.deleteButton_Room.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(11))

        self.insertClassButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.deleteClassButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(10))

        self.delete_Button_student.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(12))
        self.delete_Button_timetable.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(13))
        self.addButton_Room.clicked.connect(self.checkRoom)
        self.delete_Button_Subject.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(14))
        self.add_button_acc.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(18))
        self.delete_button_acc.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(19))
        self.update_butto_acc.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(20))
        
        self.update_Button_student.clicked.connect(self.checkUpdate_student)
        self.update_subject_button.clicked.connect(self.checkUpdate_subject)

        # set Button to add data
        self.pushButton_4.clicked.connect(self.addStudent)
        self.pushButton_6.clicked.connect(self.addSubject)
        self.pushButton_5.clicked.connect(self.addTimetable)
        self.pushButton_10.clicked.connect(self.addClass)
        self.pushButton_11.clicked.connect(self.addRoom)
        self.save_button_acc.clicked.connect(self.addAcc)

        #set Button to delete data
        self.delete_save_Button_student.clicked.connect(self.deleteStudent)
        self.delete_saveButton_timetable.clicked.connect(self.deleteTimetable)
        self.delete_saveButton_subject.clicked.connect(self.deleteSubject)
        self.delete_saveClass_Button.clicked.connect(self.deleteClass)
        self.delete_saveButton_Room.clicked.connect(self.deleteRoom)
        self.save_delete_Acc.clicked.connect(self.deleteAcc)
        
        # setButton to display data
        self.Account_pushButton.clicked.connect(self.display_Acc)
        self.Class_pushBotton.clicked.connect(self.display_Class)
        self.Room_pushButton.clicked.connect(self.display_Room)
        self.Subject_pushButton.clicked.connect(self.display_Subject)
        self.Timetable_pushButton.clicked.connect(self.display_Timetable)
        self.Student_pushButton.clicked.connect(self.display_Student)
        self.Logout_pushButton.clicked.connect(self.logOut)

        # set Button to search data
        self.search_accButton.clicked.connect(self.search_Acc)
        self.search_classButton.clicked.connect(self.search_Class)
        self.search_roomButton.clicked.connect(self.search_Room)
        self.search_subjectButton.clicked.connect(self.search_Subject)
        self.search_timetableButton.clicked.connect(self.search_Timetable)
        self.search_studentButton.clicked.connect(self.search_Student)

        # set Button to update data
        self.search_update_student.clicked.connect(self.search_edit_Student)
        self.save_update_student.clicked.connect(self.updateStudent)
        
        self.search_update_Subject.clicked.connect(self.search_edit_subject)
        self.save_update_Subject.clicked.connect(self.updateSubject)

        self.search_button_acc.clicked.connect(self.search_edit_acc)
        self.save_update_acc.clicked.connect(self.updateAcc)



    def checkRoom(self):
        self.comboBox_7.clear()

        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Class WHERE Deleted = 0 ")
            values = cur.fetchall()
            for i in values:
                self.comboBox_7.addItem(i[1])

        self.stackedWidget.setCurrentIndex(15)

    def checkStudent(self):
        self.comboBox.clear()

        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Class WHERE Deleted = 0 ")
            values = cur.fetchall()
            for i in values:
                self.comboBox.addItem(i[1])

        self.stackedWidget.setCurrentIndex(6)

    def checkTimetable(self):
        self.comboBox_4.clear()
        self.comboBox_8.clear()
        self.comboBox_2.clear()
        
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Class WHERE Deleted = 0 ")
            class_values = [row[1] for row in cur.fetchall()]
            self.comboBox_4.addItems(class_values)

            cur.execute("SELECT * FROM Subject WHERE Deleted = 0 ")
            subject_values = [row[1] for row in cur.fetchall()]
            self.comboBox_8.addItems(subject_values)

            cur.execute("SELECT * FROM Room WHERE Deleted = 0 ")
            subject_values = [row[1] for row in cur.fetchall()]
            self.comboBox_2.addItems(subject_values)

        self.stackedWidget.setCurrentIndex(7)

    def checkSubject(self):
        self.comboBox_6.clear()

        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Room WHERE Deleted = 0 ")
            values = cur.fetchall()
            for i in values:
                self.comboBox_6.addItem(i[1])

        self.stackedWidget.setCurrentIndex(8)

    def display_table(self, table_name, table_widget):
        values = self.execute_query(f"SELECT * FROM {table_name} WHERE Deleted = 0")
        table_widget.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                table_widget.setItem(row, col, QTableWidgetItem(str(field)))

    def execute_query(self, query):
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute(query)
            values = cur.fetchall()
        return values

    def display_Acc(self):
        self.display_table("Account", self.tableWidget)

    def display_Class(self):
        self.display_table("Class", self.tableWidget_0)

    def display_Room(self):
        self.display_table("Room", self.tableWidget_1)

    def display_Subject(self):
        self.display_table("Subject", self.tableWidget_2)

    def display_Timetable(self):
        self.display_table("Time_Table", self.tableWidget_3)

    def display_Student(self):
        self.display_table("Student", self.tableWidget_4)

    def search_Student(self):
        searchLine = self.search_lineEdit_4.text()
        self.search_lineEdit_4.setText("")
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Student WHERE Full_Name = ?", searchLine)
            values = cur.fetchall()
        self.tableWidget_4.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(field)))

    def search_Acc(self):
        a = self.lineEdit.text()
        self.lineEdit.setText("")
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Account WHERE adminUsername = ?", a)
            values = cur.fetchall()
        self.tableWidget.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(field)))

    def search_Class(self):
        a = self.search_lineEdit_0.text()
        self.search_lineEdit_0.setText("")
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Class WHERE Class_Name = ?", a)
            values = cur.fetchall()
        self.tableWidget_0.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                self.tableWidget_0.setItem(row, col, QTableWidgetItem(str(field)))

    def search_Room(self):
        a = self.search_lineEdit_1.text()
        self.search_lineEdit_1.setText("")
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Room WHERE Room_Name = ?", a)
            values = cur.fetchall()
        self.tableWidget_1.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                self.tableWidget_1.setItem(row, col, QTableWidgetItem(str(field)))

    def search_Subject(self):
        a = self.search_lineEdit_2.text()
        self.search_lineEdit_2.setText("")

        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Subject WHERE Subject_Name = ?", a)
            values = cur.fetchall()
        self.tableWidget_2.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(field)))

    def search_Timetable(self):
        a = self.search_lineEdit_3.text()
        self.search_lineEdit_3.setText("")
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Time_Table WHERE Class_ID = ?", a)
            values = cur.fetchall()
        self.tableWidget_3.setRowCount(len(values))
        for row, record in enumerate(values):
            for col, field in enumerate(record):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(field)))

    def addStudent(self):
        try:
            studentId = self.lineEdit_2.text()
            studentName = self.lineEdit_3.text()
            dob = self.dateEdit.dateTime().toString("dd-MM-yyyy")
            classID = self.comboBox.currentText()
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Student (Student_ID, Full_Name, DoB, Class_ID)VALUES (?, ?, ?, ?)",
                            int(studentId), studentName, dob, classID)
            QMessageBox.information(self, "Student", "Success")
            studentId = self.lineEdit_2.setText("")
            studentName = self.lineEdit_3.setText("")
        except:
            QMessageBox.information(self, "Student", "Add falies")

    def addSubject(self):
        subjectId = self.lineEdit_4.text()
        subjectName = self.lineEdit_6.text()
        lecturer = self.lineEdit_7.text()
        credit = self.comboBox_5.currentText()
        roomName = self.comboBox_6.currentText()

        if not all([subjectId, subjectName, lecturer, credit, roomName]):
            QMessageBox.information(self, "Subject", "Please fill in the blank to add info")
            return
        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO Subject (Subject_ID, Subject_Name, Lecturer, Credit, Room_Name) VALUES (?, ?, ?, ?, ?)",
                    (subjectId, subjectName, lecturer, int(credit), roomName))
            QMessageBox.information(self, "Student", "Success")
            self.lineEdit_4.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
        except:
            QMessageBox.information(self, "Subject", "Please fill in the blank to add information")

    def addTimetable(self):
        day = self.dateEdit_2.dateTime().toString("dd-MM-yyyy")
        classID = self.comboBox_4.currentText()
        subjectId1 = self.comboBox_8.currentText()
        roomName1 = self.comboBox_2.currentText()
        workShift = self.comboBox_3.currentText()

        if not all([day, classID, subjectId1, roomName1, workShift]):
            QMessageBox.information(self, "Timetable", "Please fill in the blank to add info")
            return

        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO Time_Table (Day, Class_ID, Subject_ID, Room_Name, Work_Shift)VALUES (?, ?, ?, ?, ?)",
                    day, classID, subjectId1, roomName1, int(workShift))
            QMessageBox.information(self, "Timetable", "Success")

        except Exception as e:
            print(e)
            QMessageBox.information(self, "Timetable", "Error: Failed to add timetable")

    def addClass(self):
        try:
            classId = self.lineEdit_11.text()
            className = self.lineEdit_12.text()

            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Class (Class_ID, Class_Name) VALUES (?, ?)", (classId, className))
            QMessageBox.information(self, "Class", "Successfull")

            classId = self.lineEdit_11.setText("")
            className = self.lineEdit_12.setText("")

        except:
            QMessageBox.information(self, "Class", "Add class fail")

    def addRoom(self):
        try:
            roomName = self.lineEdit_13.text()
            classID = self.comboBox_7.currentText()

            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Room (Room_Name, Class_ID)VALUES (?, ?)", (roomName, classID))
            QMessageBox.information(self, "Room", "Successfull")

            roomName = self.lineEdit_13.setText("")
        except:
            QMessageBox.information(self, "Room", "Please fill in the blank to add info")

    def addAcc(self):
        try:
            userAcc = self.lineEdit_22.text()
            passAcc = self.lineEdit_23.text()

            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Account (adminUsername, adminPass) VALUES (?, ?)", (userAcc, passAcc))
            QMessageBox.information(self, "Account", "Successfull")

            userAcc = self.lineEdit_22.setText("")
            passAcc = self.lineEdit_23.setText("")

        except:
            QMessageBox.information(self, "Account", "Add Account fail")

        pass

    def deleteAcc(self):
        userInput = self.lineEdit_24.text()
        self.lineEdit_24.setText("")

        try:
            time = datetime.datetime.now()
            print(time)
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE Account SET Deleted = 1, Time_Delete = ? WHERE adminUsername = ?", 
                            (str(time), str(userInput)))
            QMessageBox.information(self, "Delete Account", "Successfully deleted Account")
        except:
            QMessageBox.information(self, "Delete Account", "Enter adminUsername to delete Account")

    def deleteStudent(self):
        studentidInput = self.lineEdit_9.text()
        self.lineEdit_9.setText("")

        try:
            time = datetime.datetime.now()
            print(time)
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE Student SET Deleted = 1, Time_Delete = ? WHERE Student_ID = ?", 
                            (str(time), int(studentidInput)))
            QMessageBox.information(self, "Delete student", "Successfully deleted student")
        except:
            QMessageBox.information(self, "Delete student", "Enter Student_ID to delete student")

    def deleteTimetable(self):
        classID = self.lineEdit_10.text()

        if not classID:
            QMessageBox.warning(self, "Delete Timetable", "Enter Class_ID to delete timetable")
            return

        try:
            time = datetime.datetime.now()
            print(time)
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE Time_Table SET Deleted = 1, Time_Delete = ? WHERE Class_ID = ?", 
                            (str(time), str(classID)))
            QMessageBox.information(self, "Delete TimeTable", "Successfully deleted TimeTable")
            self.lineEdit_10.clear()
            
        except Exception as e:
            error_message = "Failed to delete Timetable: " + str(e)
            QMessageBox.warning(self, "Delete Timetable", error_message)
   
    def deleteSubject(self):
        subjectID = self.lineEdit_14.text()

        if not subjectID:
            QMessageBox.warning(self, "Delete Subject", "Enter Subject_ID to delete Subject")
            return
        try:
            time = datetime.datetime.now()
            print(time)
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE Subject SET Deleted = 1, Time_Delete = ? WHERE Subject_ID = ?", 
                            (str(time), subjectID))
            QMessageBox.information(self, "Delete Subject", "Successfully deleted Subject")
            self.lineEdit_14.clear()

        except Exception as e:
            error_message = "Failed to delete Subject: " + str(e)
            QMessageBox.warning(self, "Delete Subject", error_message)

    def deleteClass(self):
        classID = self.lineEdit_15.text()
        
        if not classID:
            QMessageBox.warning(self, "Delete Class", "Enter Class_ID to delete Class")
            return
        
        try:
            time = datetime.datetime.now()
            conn = connections()
            
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE Class SET Deleted = 1, Time_Delete = ? WHERE Class_ID = ?", (str(time), str(classID)))
            
            QMessageBox.information(self, "Delete Class", "Successfully deleted Class")
            self.lineEdit_15.clear()

        except Exception as e:
            error_message = "Failed to delete Class: " + str(e)
            QMessageBox.warning(self, "Delete Class", error_message)
  
    def deleteRoom(self):
        roomName = self.lineEdit_8.text()

        if not roomName:
            QMessageBox.warning(self, "Delete Room", "Enter Room_Name to delete Room")
            return

        try:
            time = datetime.datetime.now()
            print(time)
            conn = connections()
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE Room SET Deleted = 1, Time_Delete = ? WHERE Room_Name = ?", 
                            (str(time), str(roomName)))
            QMessageBox.information(self, "Delete Room", "Successfully deleted Room")
            self.lineEdit_8.clear()

        except Exception as e:
            error_message = "Failed to delete Room: " + str(e)
            QMessageBox.warning(self, "Delete Room", error_message)

    def logOut(self):
        win.setCurrentIndex(0)
    
    def search_edit_Student(self):
        searchLine = self.lineEdit_17.text()
        studentID = self.lineEdit_5.text()
        fullName = self.lineEdit_16.text()
        doB = self.dateEdit_3.dateTime().toString("dd-MM-yyyy")
        classID = self.comboBox_9.currentText()

        check = 0
        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                query = "SELECT * FROM Student WHERE Student_ID = ? AND Deleted = ?"
                cur.execute(query, (searchLine, check))
                values = cur.fetchone()

                if values:
                    self.lineEdit_5.setText(str(values[1]))
                    self.lineEdit_16.setText(str(values[2]))
                    
                    # Convert the date string to QDate object
                    date_str = values[3]
                    date_obj = QDate.fromString(date_str, "dd-MM-yyyy")
                    self.dateEdit_3.setDate(date_obj)
                    self.comboBox_9.setCurrentText(str(values[4]))

                    QMessageBox.information(self, "Student", "Successful")
                else:
                    QMessageBox.information(self, "Student", "Not found!")
        except Exception as e:
            print("Error:", e)
            QMessageBox.information(self, "Student", "An error occurred!")

    def checkUpdate_student(self):
        self.comboBox_9.clear()
        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Class WHERE Deleted = 0 ")
            values = cur.fetchall()
            for i in values:
                self.comboBox_9.addItem(i[1])

        self.stackedWidget.setCurrentIndex(16)

    def updateStudent(self):
        studentID = self.lineEdit_5.text()
        fullName = self.lineEdit_16.text()
        doB = self.dateEdit_3.date().toString("dd-MM-yyyy")  # Use .date() instead of .dateTime()
        classID = self.comboBox_9.currentText()
        searchStudent = self.lineEdit_17.text()

        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                update_query = "UPDATE Student SET Student_ID=?, Full_Name=?, DoB=?, Class_ID=? WHERE Student_ID=?"
                cur.execute(update_query, (int(studentID), fullName, doB, classID, int(searchStudent)))


                QMessageBox.information(self, 'Student', 'Update success')

                self.lineEdit_5.setText("")  # Clear the text field
                self.lineEdit_16.setText("")  # Clear the text field
                print("fgg")
        except Exception as e:
            print("Error:", e)
            QMessageBox.warning(self, "Student", "Update failed")

    def search_edit_subject(self):
        searchLine_subject = self.lineEdit_18.text()

        check = 0
        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                query = "SELECT * FROM Subject WHERE Subject_ID = ? AND Deleted = ?"
                cur.execute(query, (searchLine_subject, check))
                values = cur.fetchone()

                if values:
                    subjectID = self.lineEdit_19.setText(str(values[1]))
                    subjectName = self.lineEdit_20.setText(str(values[2]))
                    lecturer = self.lineEdit_21.setText(str(values[3]))
                    credit = self.comboBox_10.setCurrentText(str(values[4]))
                    roomName = self.comboBox_11.setCurrentText(str(values[5]))

                    QMessageBox.information(self, "Subject", "Successful")
                else:
                    QMessageBox.information(self, "Subject", "Not found!")
        except Exception as e:
            print("Error:", e)
            QMessageBox.information(self, "Subject", "An error occurred!")

    def checkUpdate_subject(self):
        self.comboBox_11.clear()

        conn = connections()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Room WHERE Deleted = 0 ")
            values = cur.fetchall()
            for i in values:
                self.comboBox_11.addItem(i[1])

        self.stackedWidget.setCurrentIndex(17)

    def updateSubject(self):
        subjectID = self.lineEdit_19.text()
        subjectName = self.lineEdit_20.text()
        lecturer = self.lineEdit_21.text()
        credit = self.comboBox_10.currentText()
        roomName = self.comboBox_11.currentText()
        subjectID1=self.lineEdit_18.text()

        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                update_query = "UPDATE Subject SET Subject_ID=?, Subject_Name=?, Lecturer=?, Credit=?, Room_Name=? WHERE Subject_ID=?"
                cur.execute(update_query, (subjectID, subjectName, lecturer, int(credit), roomName ,subjectID1))

                QMessageBox.information(self, 'Subject', 'Update success')

                self.lineEdit_19.setText("")  # Clear the text field
                self.lineEdit_20.setText("")  # Clear the text field
                self.lineEdit_21.setText("")
        except Exception as e:
            print("Error:", e)
            QMessageBox.warning(self, "Subject", "Update failed")

    def search_edit_acc(self):
        searchLine_Acc = self.lineEdit_25.text()

        check = 0
        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                query = "SELECT * FROM Account WHERE adminUsername = ? AND Deleted = ?"
                cur.execute(query, (searchLine_Acc, check))
                values = cur.fetchone()

                if values:
                    userAcc = self.lineEdit_26.setText(str(values[1]))
                    passAcc = self.lineEdit_27.setText(str(values[2]))

                    QMessageBox.information(self, "Account", "Successful")
                else:
                    QMessageBox.information(self, "Account", "Not found!")
        except Exception as e:
            print("Error:", e)
            QMessageBox.information(self, "Account", "An error occurred!")
        pass

    def updateAcc(self):

        usernameAcc = self.lineEdit_26.text()
        passwordAcc = self.lineEdit_27.text()
        usernameAcc_linesearch = self.lineEdit_25.text()

        try:
            conn = connections()
            with conn:
                cur = conn.cursor()
                update_query = "UPDATE Account SET adminUsername=?, adminPass=? WHERE adminUsername=?"
                cur.execute(update_query, (usernameAcc,passwordAcc, usernameAcc_linesearch))

                QMessageBox.information(self, 'Account', 'Update success')

                self.lineEdit_25.setText("")
                self.lineEdit_26.setText("")
                self.lineEdit_27.setText("")

        except Exception as e:
            print("Error:", e)
            QMessageBox.warning(self, "Account", "Update failed")

        pass

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    win = QtWidgets.QStackedWidget()
    win.addWidget(Login())  # 0
    win.addWidget(MainMenu())  # 1
    win.setCurrentIndex(1)
    desktop = QDesktopWidget().screenGeometry()     
    win.move(int(desktop.width()/2 - win.width()/2), int(desktop.height()/2 - win.height()/2))
    win.show()

    sys.exit(app.exec_())
