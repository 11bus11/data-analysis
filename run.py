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
            tocheck = input("Which question do you want to analyse?\n")
            row = int(tocheck) + 1
        except ValueError:
            print("The input can not be made numeric. Try again:")
        else:
            status = True

    columnlist = answers.col_values(row)
    for column in columnlist:
        try:
            if column == "yes":
                valueyes += 1
            elif column == "no":
                valueno += 1
            elif column == "none":
                valuenone += 1
        except ValueError:
            print("The input can not be made numeric. Check your spreadsheet.")
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


#Info about how you want to analyse
def analyse_info():
    tempelements = []
    tempelements = input("Write the elements you want to compare to the number of answers\n").split(",")
    return tempelements

#Calculates the percentage 
def calculate_percent(answer1, answer2):
    answer = answer1.value/answer2.value
    return answer

#Make sure the results are correct and result in 100%
def calculate_result(l):
    totalanswer, yesanswer, noanswer, noneanswer = l
    if yesanswer.value + noanswer.value + noneanswer.value == totalanswer.value:
        print("correct")
    else:
        print("The number of answers are not the same as you stated.")
        print("Check the values in your spreadsheet")
        quit()

#def convert_to_str(elements):


#Performs analysis
def analyse():
    datalist = create_object()
    print(datalist)
    totalanswer, yesanswer, noanswer, noneanswer = datalist
    print(yesanswer.value)
    result = calculate_result(datalist)
    for item in datalist:
        item.percent = calculate_percent(item, totalanswer)
    return datalist

#How the program runs
def main():
    print(analyse())

main()