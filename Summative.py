#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sutav2573
#
# Created:     21/01/2014
# Copyright:   (c) sutav2573 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
from random import*
from time import*
from delete import *
from mybutton import MyButton
from taketest import *
from diffbuttons import *
from entrybox import *
from studentclass import Student
from edit import Edit
from question import*

#CreateTest made by Jimmy
class CreateTest:
    def __init__(self,win):
        self.win = win

    #Creates the Test Buttons
    def TestButtons(self):
        self.CreateTestList = [(0,175,525,600,"Add a New Question", "dodgerblue","White"),(425,600,525,600,"Done Creating Test","dodgerblue","white")]
        self.CreateTestButts = []
        for (x1,x2,y1,y2,label,colour,textcolour) in self.CreateTestList:
            self.CreateTestButts.append(MyButton(self.win,x1,x2,y1,y2,label,colour,textcolour))
        self.ButtonLabel,self.win = GetKeyPress(self.CreateTestButts,self.win)
        return self.ButtonLabel

    #Gets the Test Title
    def GetTestName(self):
        #Entry Box for Test Name
        self.TestName = EntryBox(self.win,300,50,30,"Test Name")

        #Creates the Done Button (Finish creating Test Name)
        self.DoneButtonList = [(100,500,125,225,"Done Creating Test Name","Dodgerblue","white")]
        self.ButtonList = []
        for (x1,x2,y1,y2,label,colour,textcolour) in self.DoneButtonList:
            self.ButtonList.append(MyButton(self.win,x1,x2,y1,y2,label,colour,textcolour))
        self.ButtonList.append(MyButton(self.win,0,600,550,600,"Cancel","dodgerblue","white"))
        self.ButtonLabel,self.win = GetKeyPress(self.ButtonList,self.win)
        return self.ButtonLabel,self.ButtonList,self.TestName


#Main() made by
def main():
    #Jimmy Chris and Steve
    """Teacher's username: Teacher
       Teacher's password: 12354
    """
    win = GraphWin("Login",500,400)
    win.setBackground("lightgray")
    #Giant text in the middle to let users know that they're in the login page
    LogText = Text(Point(250,100),"Login")
    LogText.setSize(20)
    LogText.draw(win)
    Exit = ExitButton(win,420,500,5,50,"Quit","dodgerblue","white")
    EasterEgg = InvisibleButton(win,0,80,5,50,"Invisible","dodgerblue","white")



    #User and Password Entry boxes
    UserBox = EntryBox(win,246,155,21,"Username")
    PassBox = EntryBox(win,246,205,21,"Password")
    Login = MyButton(win,87,405,260,295,"Login","dodgerblue","White")
    #Checks to see if username is in database
    UsernameCheckFile = open("students.txt")
    UsernameList = []
    for line in UsernameCheckFile:
        info = line.split()
        UsernameList.append(info[2].lower())
    UsernameCheckFile.close()

    #Sign up button that takes you to the Register menu if you don't have an account
    Signup = Text(Point(370,320),"Sign-Up")
    Signup.setTextColor("slategray")
    Signup.setSize(12)
    Signup.draw(win)
    #Underlines the signup button
    Underline = Line(Point(343,327),Point(400,327))
    Underline.setFill('slategray')
    Underline.draw(win)
    #Used so you can see where the sign-up button will be
    #Get rid of this later

    #Chris
    while True:
        pt = win.getMouse()
        if Login.click(pt):
            #checks if the teacher is logging in
           if UserBox.returnText().lower() =="teacher":
              teacherFile = open(UserBox.returnText().lower() + ".txt","r")
              for line in teacherFile:
                    info = line.split()
                    Password = info[0]
              if PassBox.returnText() == Password:
                 win.close()
                 TeacherInterface()
              #Teacher password is wrong
              else:
                NoUsername = Text(Point(250,365),"Invalid username or password")
                NoUsername.setSize(20)
                NoUsername.draw(win)
                sleep(1)
                NoUsername.undraw()
            #Username doesn't exist
           elif UsernameList.count(UserBox.returnText().lower()) == 0:
                NoUsername = Text(Point(250,365),"Invalid username or password")
                NoUsername.setSize(20)
                NoUsername.draw(win)
                sleep(1)
                NoUsername.undraw()

           else:
                #opens the users file and gets their information
                infile = open(UserBox.returnText() + ".txt","r")
                for line in infile:
                    info = line.split()
                    Password = info[3]
                #lets them log in if the username and password are good
                if PassBox.returnText() == Password:
                   win.close()
                   StudentInterface(UserBox.returnText())
                   infile.close()
                else:
                    #Student password is wrong
                    PasswordMismatch = Text(Point(250,365),"Invalid username or password")
                    PasswordMismatch.setSize(20)
                    PasswordMismatch.draw(win)
                    pass
        elif pt.getX() >= 341 and pt.getX() <= 400 and pt.getY() >= 312 and pt.getY() <= 330:
            win.close()
            Register()
        #Jimmy
        elif EasterEgg.click(pt):
            Jimmy = Image(Point(50,50),"jd.gif")
            Jimmy.draw(win)
            sleep(0.1)
            Jimmy.undraw()
            pass
        elif Exit.click(pt):
            Exit.Quit()
        else:
            pass
    win.close()

#Jimmy and Steve (graphics) and Chris (save to file)
def Register():
    RegisterWin = GraphWin("Register",500,400)
    RegisterWin.setBackground("lightgray")
    RegText = Text(Point(250,50),"Register")
    RegText.setSize(20)
    RegText.draw(RegisterWin)
    #Text Boxes for register menu
    CreateAcc = MyButton(RegisterWin,87,405,295,330,"Create Account","dodgerblue","White")
    Cancel = MyButton(RegisterWin,87,405,340,375,"Cancel","dodgerblue","White")
    NameBox = EntryBox(RegisterWin,165,105,10,"First Name")
    LastBox = EntryBox(RegisterWin,330,105,10,"Last Name")
    UserBox = EntryBox(RegisterWin,246,155,21,"Username")
    Pass1Box = EntryBox(RegisterWin,246,205,21,"Password")
    Pass2Box = EntryBox(RegisterWin,246,255,21,"Confirm Password")
    InvalidPass = Text(Point(250,365),"Passwords do not match")
    #Jimmy and Chris
    while True:
        pt = RegisterWin.getMouse()
        #Checks if the Create Account button is clicked
        if CreateAcc.click(pt):
            #Checks to see if username has been used already
            UsernameCheckFile = open("students.txt")
            for line in UsernameCheckFile:
                info = line.split()
                if info[2] == UserBox.returnText():
                    InvalidUser = Text(Point(250,390),"Username already taken")
                    InvalidUser.setSize(20)
                    InvalidUser.draw(RegisterWin)
                    sleep(1)
                    RegisterWin.close()
                    Register()
            #If the passwords do not match then it will give you an error and you won't be able to sign up
            if Pass1Box.returnText() != Pass2Box.returnText():
                InvalidPass = Text(Point(250,390),"Passwords do not match")
                InvalidPass.setSize(20)
                InvalidPass.draw(RegisterWin)
                sleep(1)
                InvalidPass.undraw()
            else:
                #Creates the text file. Username will be the text file name
                #Inside the text file is First Name , Last Name, Username, and Password
                Account = Student(RegisterWin,NameBox.returnText(),LastBox.returnText(),UserBox.returnText().lower(),Pass1Box.returnText(),Pass2Box.returnText())
                outfile = open("students.txt","a")
                print(NameBox.returnText(),LastBox.returnText(),UserBox.returnText().lower(),file= outfile)
                outfile.close()
                outfile =open(UserBox.returnText() + ".txt", "w")
                MarkFile = open(UserBox.returnText() + "Marks.txt","a")
                print(NameBox.returnText(),LastBox.returnText(),UserBox.returnText().lower(),Pass1Box.returnText(),"No_Mark",file=outfile)
                outfile.close()
                break

        elif Cancel.click(pt):
            RegisterWin.close()
            main()
        else:
            pass


    RegisterWin.close()
    main()
#Vishrut
def TeacherInterface():
    """ This function creates the menu window and the buttons like access students,
        create test and logout for the teacher.After that the program calls GetKeyPress
        function to get a click  from the user on one of the buttons above. That function
        returns the name of the button pressed and depending on what the button name
        is the first thing it will do is close the menu window and then call a function
        or start the program again. """
    Menu = GraphWin("Menu Window",500,650)
    Menu.setBackground("lightgray")
    # the following list has the specification of three buttons
    Bcoordandlabels = [(100,400,50,150,"Create Test","dodgerblue","White"),
                      (100,400,200,300,"Access Students","dodgerblue","White"),
                      (100,400,350,450,"Delete Test","dodgerblue","White"),
                      (100,400,500,600,"Logout","dodgerblue","White")]
    Buttons = []
    # the following two lines goes through list of specification for the buttons
    #and append it to Button list but before appending the specification don't have
    # the win and don't call the MyButton Method so that also gets append into the list of buttons
    for (x1,x2,y1,y2,label,colour,textcolour) in Bcoordandlabels:
        Buttons.append(MyButton(Menu,x1,x2,y1,y2,label,colour,textcolour))
    while True:
        ButtonLabel,Menu = GetKeyPress(Buttons,Menu)
        if ButtonLabel =="Create Test":
           Menu.close()
           MakeTest()
        elif ButtonLabel == "Access Students":
             Menu.close()
             AccessStudents()
        #Jimmy and Vishrut
        elif ButtonLabel == "Delete Test":
            Menu.close()
            DeleteTests()
        else:
             if ButtonLabel =="Logout":
                Menu.close()
                main()

#Vishrut
def StudentInterface(Username):
    """Askes the student if they wish to change their password,
             write the test or logout.
    """
    StudentWin = GraphWin("Student Menu",500,500)
    StudentWin.setBackground("lightgray")
    StudentMenuButtons = [(100,400,50,150,"Write Test","dodgerblue","White"),
                         (100,400,200,300,"Change Password","dodgerblue","White"),
                         (100,400,350,450,"Logout","dodgerblue","White")]
    Buttons = []
    # the following two lines goes through list of specification for the buttons
    #and append it to Button list but before appending the specification don't have
    # the win and don't call the MyButton Method so that also gets append into the list of buttons
    for (x1,x2,y1,y2,label,colour,textcolour) in StudentMenuButtons:
        Buttons.append(MyButton(StudentWin,x1,x2,y1,y2,label,colour,textcolour))

    while True:
        ButtonLabel,StudentWin = GetKeyPress(Buttons,StudentWin)
        if ButtonLabel =="Write Test":
           StudentWin.close()
           StudentTakeTest(Username)
        elif ButtonLabel == "Change Password":
             changePass(Username)
        else:
             if ButtonLabel == "Logout":
                StudentWin.close()
                main()

#Chris and Vishrut
def changePass(Username):
    """ This function so far allows a student to change their Password.
        First reads through the students file and then sends the info to
        the edit class. Then asks the student to for new password and confrim
        the password. Then the changed password will print into the file."""
    ChangePassWin = GraphWin("Change Password",250,200)
    ChangePassWin.setBackground("lightgray")
    #Makes the Entry Boxes to enter the new password
    Pass1Box = EntryBox(ChangePassWin,125,50,15,"New Password")
    Pass2Box = EntryBox(ChangePassWin,125,100,15,"Confirm Password")
    #Makes the buttons
    Buttonspecs = [(20,120,135,185,"Done","dodgerblue","White"),
                  (130,230,135,185,"Cancel","dodgerblue","White")]
    Buttons=[]
    for (x1,x2,y1,y2,label,colour,textcolour) in Buttonspecs:
        Buttons.append(MyButton(ChangePassWin,x1,x2,y1,y2,label,colour,textcolour))

    #Opens the file with the users information
    infile =open(Username+".txt","r")
    for line in infile:
        Name,Last,UserName,PassWord,Mark = line.split()
        StudentInfoSave = Edit(ChangePassWin,Name,Last,UserName,PassWord,PassWord)
    infile.close()

    #When the user clicks Done, it checks to see if the passwords match, then writes the users information (with the new password) to their file
    while True:
        ButtonLabel,ChangePassWin = GetKeyPress(Buttons,ChangePassWin)
        if ButtonLabel =="Done":
           Pass1 = Pass1Box.returnText()
           Pass2 = Pass2Box.returnText()
           if Pass1 == Pass2:
               StudentInfoSave.ChangeInfo(Pass1,Pass2)
               StudentInfoSave.ChangePass()
               infile =open(Username+".txt","w")
               print("{0} {1} {2} {3} {4}".format(Name,Last,UserName,Pass1,Mark),file = infile)
               ChangePassWin.close()
               break
           else:
            #Passwords don't match
            NoMatch = Text(Point(125,18),"Passwords do not match")
            NoMatch.draw(ChangePassWin)
            pass


        else:
             if ButtonLabel =="Cancel":
                ChangePassWin.close()
                return

#Jimmy Dong
def MakeTest():
    CreateTestWin = GraphWin("Create a Test", 600,600)
    CreateTestWin.setBackground("lightgray")
    List = []
    while True:
        #Question Number
        QNumber = 1
        TestPage = CreateTest(CreateTestWin)
            #Calls the Question Class
        QuestionPage = Question(CreateTestWin)
        #Calls the ButtonLabel, ButtonList, and TestName
        ButtonLabel,ButtonList,TestName = TestPage.GetTestName()

        #Test Name is equal to the Test name u put in the entry box + .txt
        NameofTests = TestName.returnText() + ".txt"

        #If you are done creating your test name
        if ButtonLabel == "Done Creating Test Name":
            ButtonList[1].UndrawButton()
            infile = open("AllTests.txt","r")
            #Looks inside the txt file and searches for the test name you have created. If there is already a test with that name
            #Then it will not let you create a test
            TestNames = []
            for line in infile:
                FileInfo,n =line.split("\n")
                TestNames.append(FileInfo)

        elif ButtonLabel == "Cancel":

            CreateTestWin.close()
            TeacherInterface()

        #If the TestNames List does not have the txt file with the Test Name then it will undraw the buttons
        #and put the TestName into 2 different txt files.
                #If the TestName is more than 12 characters then it won't work
        #You subtract 4 because NameofTests includes .txt which adds 4 characters
        if TestNames.count(NameofTests) == 0 and (len(NameofTests) - 4) <= 12:
        #If you create a different name that hasn't been created before then it will print the Test Name into the AllTests txt  file
        #Undraw the buttons and move onto the next part
            infile = open("AllTests.txt","a")
            print (NameofTests,file=infile)
            #Undraws the button and Creates a file with that test name
            ButtonList[0].UndrawButton()
            outfile = open(NameofTests,"w")
            TestName.UndrawEntry()
            outfile.close()
            infile.close()
            break
        #If the Test Name is 12 characters or more then it will tell you that you can't create the test
        #You subtract 4 because NameofTests includes .txt which adds 4 characters
        elif (len(NameofTests) - 4) >12:
            TooLong = Text(Point(300,300),"Test Name Must Be Under 12 Characters")
            TooLong.setSize(20)
            TooLong.draw(CreateTestWin)
            sleep(1)
            TooLong.undraw()
            ButtonList[0].UndrawButton()
            TestName.UndrawEntry()
        #If you create a test that is already taken
        else:
            NATest = Text(Point(300,300),"{0} has already been used.".format(TestName.returnText()))
            NATest.setSize(20)
            NATest.draw(CreateTestWin)
            sleep(1)
            NATest.undraw()
            #Since it redraws the button above. If you enter the same Test name that you already have
            #Then it will undraw the button then redraw it to prevent the buttons to not be undrawn in the next part
            ButtonList[0].UndrawButton()
            TestName.UndrawEntry()



    #Question # To let User know how many questions they have created
    QuestionNum = Text(Point(300,30),"Question #{0}".format(QNumber))
    QuestionNum.setSize(20)
    QuestionNum.draw(CreateTestWin)



    while True:
    #Creates the Entry Boxes in Question Class
        QuestionPage.TestBoxes()
        #Checks for when the user is done creating a question / test
        ButtonLabel = TestPage.TestButtons()
        infile = open(TestName.returnText()+".txt","a")
        if ButtonLabel == "Add a New Question":
            QNumber = QNumber + 1
            QuestionNum.setText("Question #{0}".format(QNumber))
            #Gets all of the Inputs
            QuestionBox = QuestionPage.getQuestion()
            CorrectBox = QuestionPage.getCorrectAnswer()
            WrongBox1, WrongBox2,WrongBox3 = QuestionPage.getWrongAnswers()
            print (QuestionBox,'~',CorrectBox,'~',WrongBox1,'~',WrongBox2,'~',WrongBox3,file=infile)

        if ButtonLabel == "Done Creating Test":
            #Gets all of the Inputs
            QuestionBox = QuestionPage.getQuestion()
            CorrectBox = QuestionPage.getCorrectAnswer()
            WrongBox1, WrongBox2,WrongBox3 = QuestionPage.getWrongAnswers()
            print (QuestionBox,'~',CorrectBox,'~',WrongBox1,'~',WrongBox2,'~',WrongBox3,file=infile)

            infile.close()
            CreateTestWin.close()
            TeacherInterface()


#Jimmy and Vishrut
#Displays all the test names onto the window
#If you click on one of the tests it deletes it
def DeleteTests():
    TestNameWin = GraphWin("Delete Test",1000,610)
    TestNameWin.setBackground("lightgray")
    Tests = []
    TestFile = open("AllTests.txt","r")
    for line in TestFile:
        label,n = line.split(".")
        Tests.append(label)
    TestFile.close()
    TestButtonList = []
    Buttonspecs = ButtonSpecs(Tests)

    for (x1,x2,y1,y2,label,colour,textcolour) in Buttonspecs:
        TestButtonList.append(MyButton(TestNameWin,x1,x2,y1,y2,label,colour,textcolour))
    TestButtonList.append(MyButton(TestNameWin,0,1000,560,610,"Cancel","dodgerblue","white"))
    #Loop for the buttons
    while True:
          #Cancel Button
        ButtonLabel,TestNameWin = GetKeyPress(TestButtonList,TestNameWin)
        if ButtonLabel == "Cancel":
            TestNameWin.close()
            TeacherInterface()
        #Deletes The Test
        else:
             filename = DeleteFiles("{0}.txt".format(ButtonLabel))
             filename.DeleteFile()
             for i in Tests:
                 if ButtonLabel== i:
                    Tests.remove(i)
             #the following first deletes the file with all the test name and create a new one
             #with the same name and prints the list with the list of test name
             deletefile = DeleteFiles("AllTests.txt")
             deletefile.DeleteFile()
             outfile = open("AllTests.txt","a")
             for x in range(len(Tests)):
                 print("{0}.txt".format(Tests[x]),file= outfile)
             outfile.close()
             TestNameWin.close()
             TeacherInterface()




#Vishrut
def AccessStudents():
    """This function reads a file with the names of all the students
            that made a account and puts them in a list. Then the last and first name
            is combined becomes the key and username becomes the value. Then calls a
            function to make specification for student buttons and returns them in a
            list. Then then the button is created and gets appended to a list. Then
            wait for a click. If clicked on a students name calls StudentInfo function.
            If cancel is clicked it goes back. """
    AccessStudentsWin= GraphWin("Access Students Window",1000,610)
    AccessStudentsWin.setBackground("lightgray")
    infile = open("students.txt","r")

    FirstNameList =[]
    LastNameList=[]
    UserNameList=[]
    for line in infile:
        Name,Lastname,User= line.split()
        FirstNameList.append(Name)
        LastNameList.append(Lastname)
        UserNameList.append(User)
    infile.close()

    StudentButtonList = {}
    for i in range (len(FirstNameList)):
        Name = FirstNameList[i]+ " " + LastNameList[i]
        StudentButtonList[Name] = UserNameList[i]
    Buttonspecs =ButtonSpecs(StudentButtonList)
    StudentButtons = []
    for (x1,x2,y1,y2,label,colour,textcolour) in Buttonspecs:
        StudentButtons.append(MyButton(AccessStudentsWin,x1,x2,y1,y2,label,colour,textcolour))
    StudentButtons.append(MyButton(AccessStudentsWin,0,1000,560,610,"Cancel","dodgerblue","white"))

    ButtonLabel,AccessStudentsWin = GetKeyPress(StudentButtons,AccessStudentsWin)
    for student in StudentButtonList:
        if student == ButtonLabel:
           infile = open("{0}.txt".format(StudentButtonList[student]),"r")
           AccessStudentsWin.close()
           StudentInfo(infile,ButtonLabel)
           infile.close()
        if ButtonLabel == "Cancel":
            AccessStudentsWin.close()
            TeacherInterface()


#Chris
def CalculateAverage(user):
    #Opens the users mark file
    StudentMarkFile = open(user + "Marks.txt","r")
    Marks = []
    #appends all their test marks to a list
    for line in StudentMarkFile:
        Marks.append(int(line))
    if len(Marks) == 0:
        Average = "No Mark"
    #finds the average of the marks
    else:
        Average = int(sum(Marks)/len(Marks))
    return Average


#Chris
#Displays the students info in a separate window for the teacher to see
def StudentInfo(infile,StudentName):
    Student = GraphWin("{0}".format(StudentName),500,300)
    Student.setBackground("lightgray")
    #gets the students info
    for line in infile:
        first,last,user,password,mark = line.split()
    #displays the students info on the window
    Name = Text(Point(250,50),"Name: {0} {1}".format(first,last))
    Name.setSize(24)
    Name.draw(Student)

    Username = Text(Point(250,100),"Username: {0}".format(user))
    Username.setSize(24)
    Username.draw(Student)

    #calculates the students average to be displayed in the window
    Average = CalculateAverage(user)

    if Average == "No Mark":
        Mark= Text(Point(250,150),"Average: {0}".format(Average))
        Mark.setSize(24)
        Mark.draw(Student)
    else:
        Mark= Text(Point(250,150),"Average: {0}%".format(Average))
        Mark.setSize(24)
        Mark.draw(Student)

    BackButton = [MyButton(Student,50,450,230,280,"Back","dodgerblue","white")]
    ButtonLabel,Student = GetKeyPress(BackButton,Student)
    if ButtonLabel == "Back":
        Student.close()
        AccessStudents()

#Vishrut
def ButtonSpecs(StudentButtonList):
    """This Function a dict as a parameter and goes through it and creates
            a list of button specification for each student in the dict."""

    Buttonspecs=[]
    ycount = 25
    xcount = 25
    for j in StudentButtonList:
        Buttonspecs.append((xcount,xcount + 115,ycount,ycount+50,"{0}".format(j),"dodgerblue","White"))
        if ycount >=425:
            ycount =25
            xcount = xcount +140
        else:
            ycount = ycount+100


    return Buttonspecs


def GetKeyPress(ButtonList,win):
    """This function ask the users for a click and figures out if any of the
    buttons were clicked and if they were the loop will find the name of
    the button and return it"""
    while True:
          pt = win.getMouse()
          for Button in ButtonList:
              if Button.click(pt):
                 ButtonLabel = Button.getLabel()
                 return ButtonLabel,win
              else:
                pass
#Steve
def GetQandA(ButtonLabel):
    #Opening the file with the Questions and Answers and returning the Questions in a list as well with each set
    #of questions in a list in a list
    file = open(ButtonLabel+".txt","r")
    QuestionList = []
    AnswerList = []
    AllAnswerList = []
    CorrectAnswerList = []
    #Get the Questions and Answers from the text file and append them to a list
    #Append the answers from that question to another list - A list with mutiple list containing
    #the answers. Answer 4 contains a New Line Character so that is removed.
    #The QuestionList will be a list containing all the questions.
    #The AnswerList will be a list containing all the answers for that question.
    #The AllAnswerList will containing all the answers.
    for line in file:
        Question,Answer1,Answer2,Answer3,Answer4 = line.split('~')
        QuestionList.append(Question)
        AnswerList.append(Answer1)
        AnswerList.append(Answer2)
        AnswerList.append(Answer3)
        AnswerList.append(Answer4.rstrip())
        AllAnswerList.append(AnswerList)
        AnswerList = []
    return (QuestionList,AllAnswerList)
#Steve
def StudentTakeTest(Username):
    #The main function that allows the user to take the test.

    TestNameWin = GraphWin("Test Name",1000,610)
    TestNameWin.setBackground("lightgray")

    Tests = []

    TestFile = open("AllTests.txt","r")
    for line in TestFile:
        label,n = line.split(".")
        Tests.append(label)


    TestButtonList = []
    Buttonspecs = ButtonSpecs(Tests)

    for (x1,x2,y1,y2,label,colour,textcolour) in Buttonspecs:
        TestButtonList.append(MyButton(TestNameWin,x1,x2,y1,y2,label,colour,textcolour))
    TestButtonList.append(MyButton(TestNameWin,0,1000,560,610,"Cancel","dodgerblue","white"))



    while True:
        ButtonLabel,TestNameWin = GetKeyPress(TestButtonList,TestNameWin)
        if ButtonLabel == "Cancel":
            TestNameWin.close()
            StudentInterface(Username)
            break

        else:
            file = open(ButtonLabel + ".txt", "r")
            TestNameWin.close()
            break



    #GetQandA function is called to get the answers/questions from the text file
    #Window in defined and the background is set to grey
    win = GraphWin("Take Test", 600,400)
    QuestionList,AllAnswerList = GetQandA(ButtonLabel)
    win.setBackground("lightgray")

    #Opening the file with the Questions and answers and defining variables with empty lists.
    QuestionList = []
    AnswerList = []
    AllAnswerList = []
    StudentAnswers = []
    AnswerCount = 0
    CorrectAnswers = []
    #Get the Questions and Answers from the text file and append them to a list
    #Append the answers from that question to another list - A list with mutiple list containing
    #the answers. Answer 4 contains a New Line Character so that is removed.
    #The QuestionList will be a list containing all the questions.
    #The AnswerList will be a list containing all the answers for that question.
    #The AllAnswerList will containing all the answers.
    for line in file:
        Question,Answer1,Answer2,Answer3,Answer4 = line.split('~')
        QuestionList.append(Question)
        CorrectAnswers.append(Answer1)
        AnswerList.append(Answer1)
        AnswerList.append(Answer2)
        AnswerList.append(Answer3)
        AnswerList.append(Answer4.rstrip())
        AllAnswerList.append(AnswerList)
        AnswerList = []

    #Defines Test as a variable and randomized all the questions
    #Questionlist contains all the questions
    #AllAnswerList contains a list with all the possible answers within a list
    #Defines Test as a variable and randomized all the questions
    #Questionlist contains all the questions
    #AllAnswerList contains a list with all the possible answers within a list and the continue button will be drawn
    Test = TakeTest(win,QuestionList,AllAnswerList,-1,StudentAnswers,AnswerCount,CorrectAnswers,Username)
    Test.Randomized()
    Test.Continue()

    #Loops through each question and calls the function Display which draws the display layout of the test
    #The CheckDisplay draws the the button with the dots - when the user clicks on the answer, a little dot will
    #display to let the user know the answer has a "check". The TrackAnswer will force the user to select an answer
    #before undrawing the display/question and then drawing the new one.
    for i in range(len(AllAnswerList)):
        Test.Display()
        Test.CheckDisplay()
        Test.TrackAnswer()
        Test.Undisplay()
        Test.UndrawQuestion()
    Test.CheckAnswers()
    #Closes the window
    win.close()
    StudentInterface(Username)

##try:
main()
##except:
##    sys.exit()