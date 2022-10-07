import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('data_analysis')

answers = SHEET.worksheet("answers")
output = SHEET.worksheet("output")

data = answers.get_all_values()

polldata = ""
percentage = []

alldata = []

elements = []
temp = 0
i = 0
name = ""

class Userdata:
    def __init__(self, value, percent, title):
        self.value = int(value)
        self.percent = percent
        self.title = title


def validation_universal():
    valueyes = 0
    valueno = 0
    valuenone = 0
    amount = 0
    status = False
    while status == False:
        try:
            question = input("Which question do you want to analyse? Write a number\n")
            row = int(question) + 1
        except ValueError:
            print("The input is not a number. Try again:")
        else:
            status = True

    columnlist = answers.col_values(row)
    if len(columnlist) == 0:
        quit()
    for column in columnlist:
        if column == "yes":
            valueyes += 1
        elif column == "no":
            valueno += 1
        elif column == "none":
            valuenone += 1
        elif column == str("question " + question):
            continue
        else:
            print("The inputs has to be either yes, no or none.")
            print("See the imported values below:")
            print(columnlist)
            print("Check the spreadsheet.")
            quit()
    valuetotal = len(columnlist) -1
    return valuetotal, valueyes, valueno, valuenone
        

#Preparations for analysis. Creating the objects
def create_object():
    datatitle = input("What kind of data is this?\n")
    valuelist = validation_universal()

    totalanswer = Userdata(0, 1, datatitle)
    totalanswer.value = valuelist[0]

    yesanswer = Userdata(0, 0, datatitle)
    yesanswer.value = valuelist[1]

    noanswer = Userdata(0, 0, datatitle)
    noanswer.value = valuelist[2]

    noneanswer = Userdata(0, 0, datatitle)
    noneanswer.value = valuelist[3]
    return totalanswer, yesanswer, noanswer, noneanswer

#Calculates the percentage 
def calculate_percent(answer1, answer2):
    answer = answer1.value/answer2.value
    return answer

#Make sure the results are correct and combined is 100%. 
def double_validate_result(l):
    totalanswer, yesanswer, noanswer, noneanswer = l
    if yesanswer.value + noanswer.value + noneanswer.value == totalanswer.value:
        pass
    else:
        print("The number of answers are not correct.")
        print("Check the values in your spreadsheet")
        quit()

def list_result_create(question, resultdata):
    qnum = "question" + question
    listresult = [qnum, resultdata[1], resultdata[2], resultdata[3], resultdata[0]]
    return listresult

def export_result(listresult):
    for item in listresult:
        column = 2
        current = "B" + str(column)
        output.update(current, item)

#Performs analysis
def analyse():
    datalist = create_object()
    print(datalist)
    totalanswer, yesanswer, noanswer, noneanswer = datalist
    print(yesanswer.value)
    result = double_validate_result(datalist)
    for item in datalist:
        item.percent = calculate_percent(item, totalanswer)
    
    print("Spreadsheet now updated")

analyse()