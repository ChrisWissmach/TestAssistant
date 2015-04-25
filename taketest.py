from graphics import*
from mybutton import MyButton
from createcircle import*
from createrectangle import*
from objects import*
from random import *

#Steve Truong (core), Vishrut (Check what answers the student got right/wrong), Chris (save mark to file)
class TakeTest:
    """TakeTest allows the user to take the test. The Display() method will display the layout of the test
    such as the question numbers, question, and answers. The Randomized() method rearranges all the answers
    to change the order and appends them into a new list called NewRandomList. The Undisplay() method undraws
    the display. The UndrawQuestion() method will undraw the current question. The CheckDisplay() method creates
    the buttons and also creates the points/dots in the buttons. The TrackAnswer() method keeps track of the answer
    chosen and draws/undraws the dot depending on the answer currently selected and allows the user to continue on
    to the next question."""
    def __init__(self,win,AllQuestions,AllAnswers,QuestionNum,StudentAnswers,AnswerCount,CorrectAnswers,Username):
        self.win = win
        self.AllQuestions = AllQuestions
        self.AllAnswerList = AllAnswers
        self.StudentAnswers = StudentAnswers
        self.AnswerCount = AnswerCount
        self.CorrectAnswers = CorrectAnswers
        self.TrackAnswers = []
        self.QuestionNum = QuestionNum
        self.Username= Username
    def Display(self):
        #Display the layout
        #ObjectList contains the rectangles that will have the questions - (Polymorhpic function, calling the draw method by using
        #the CreateCircle and CreateRectangle class
        #QuestionNum is the questionnumber(1,2,3...) and QuestionText will contain the question itself
        #ObjectList contains Rectangles/Circles
        #NewRandomList contains the answers that are rearranged.
        self.QuestionNum = self.QuestionNum + 1
        self.QuestionText = Text(Point(300,50),self.AllQuestions[self.QuestionNum])
        self.QuestionText.draw(self.win)

        self.ObjectList = [CreateRectangle(self.win,75,525,110,160,"",self.NewRandomList[self.QuestionNum][0],""),CreateRectangle(self.win,75,525,165,215,"",self.NewRandomList[self.QuestionNum][1],""),
        CreateRectangle(self.win,75,525,220,270,"",self.NewRandomList[self.QuestionNum][2],""),CreateRectangle(self.win,75,525,275,325,"",self.NewRandomList[self.QuestionNum][3],""),
        CreateCircle(self.win,30,40,10,55,25,self.QuestionNum+1,"")]
        for obj in self.ObjectList:
            obj.Draw()

    def Randomized(self):
        #RandomAllAnswerList has all the answers randomized
        #The first loops through each of the list that are contained inside AllAnswerList
        #Within that loop, each of the answer orders arre switched around and appended to a new list called NewRandomList
        #i will loop through each set of answers
        #Answer will hold the answer within the list
        #TrackAnswer will keep track of the answers  already randomized
        self.NewRandomList = []
        for i in range(len(self.AllAnswerList)):
            MyList = self.AllAnswerList[i]
            for n in range(4):
                while True:
                    Random = randint(0,3)
                    Answer =  (MyList[Random])
                    if self.TrackAnswers.count(Answer) == 0:
                        self.TrackAnswers.append(Answer)
                        break
            self.NewRandomList.append(self.TrackAnswers)
            self.TrackAnswers = []

    def Undisplay(self):
        #Undisplays all the Objects in ObjectList/the display of the test.
        for obj in self.ObjectList:
            obj.Undraw()

    def UndrawQuestion(self):
        #Undraws the question
        self.QuestionText.undraw()

    def CheckDisplay(self):
        #Create Buttons/Dots
        #The MutipleChoiceButtons will contain all the buttons by using  MCBUttonsList (Containing
        #coordinates,colour/text
        #The dotList will contain all the point/dot positions
        self.MutipleChoiceButtons = []
        MCButtonsList = [(495,515,125,145,"","White",""), (495,515,180,200,"","White",""),
        (495,515,235,255,"","White",""), (495,515,290,310,"","White","")]

        for (x1,x2,y1,y2,label,colour,textcolour) in MCButtonsList:
            self.MutipleChoiceButtons.append(MyButton(self.win,x1,x2,y1,y2,label,colour,textcolour))


        #List of Dot points (lets user know what answer is selected)
        self.DotList = [CreateCircle(self.win,495,515,125,145,6,"","black"),CreateCircle(self.win,495,515,180,200,6,"","black"),
        CreateCircle(self.win,495,515,235,255,6,"","black"),CreateCircle(self.win,495,515,290,310,6,"","black")]
        for obj in self.DotList:
            obj.Draw()
            obj.Unshow()


    def TrackAnswer(self):
        #TrackAnswer will keep track of the selected answer out of the four mutiple choice answers.
        #AnswerClick will check if an answer has been selected, if so then the continue button will be enable
        #MutipleChoiceButtons are the answer buttons
        #The DotList contains all the postions where the dot will appear(lets user know what answer is selected)
        #The AnswerNum will see which answer is chosen which stores it into a variable called CurrentValue
        #The NewRandomList contains all the possible answers and the QuestionNum will select those sets of answers for that question
        #Then the CurrentValue will select the answer chosen
        AnswerClick = "False"
        while True:
            pt = self.win.getMouse()
            for AnswerNum in range(4):
                if self.MutipleChoiceButtons[AnswerNum].click(pt):
                    AnswerClick = "True"
                    for EachDot in range(4):
                        self.DotList[EachDot].Unshow()
                    self.DotList[AnswerNum].Show()
                    CurrentValue = AnswerNum
            if self.Continue[0].click(pt) and AnswerClick == "True":
                self.StudentAnswers.append(self.NewRandomList[self.QuestionNum][CurrentValue])
                break
        print(self.StudentAnswers)
    def Continue(self):
        #Draws the Continue button
        self.Continue = []
        Continue = [(480,600,350,400,"Continue","Dodgerblue","White")]
        for (x1,x2,y1,y2,label,colour,textcolour) in Continue:
            self.Continue.append(MyButton(self.win,x1,x2,y1,y2,label,colour,textcolour))
    def CheckAnswers(self):
        for i in range(len(self.StudentAnswers)):
            if self.StudentAnswers[i] == self.CorrectAnswers[i]:
               self.AnswerCount = self.AnswerCount +1
            else:
                 pass
        file = open(self.Username + "Marks.txt","a")
        Percent = int(self.AnswerCount / len(self.AllQuestions) * 100)
        print(Percent,file = file)