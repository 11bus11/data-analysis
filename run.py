# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#import gspread
#from google.oauth2.service_account import Credentials
#SCOPE = [
#    "https://www.googleapis.com/auth/spreadsheets",
#    "https://www.googleapis.com/auth/drive.file",
#    "https://www.googleapis.com/auth/drive"
#    ]
#CREDS = Credentials.from_service_account_file("creds.json")
#SCOPED_CREDS = CREDS.with_scopes(SCOPE)
#GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#SHEET = GSPREAD_CLIENT.open("Info-stats")

#no1 = SHEET.worksheet("no1")
#data = no1.get_all_values()
#print(data)

polldata = ""
percentage = []

datalist = []

elements = []
temp = 0
i = 0
name = ""

class Userdata:
    def __init__(self, value, percent, title):
        self.value = value
        self.percent = percent
        self.title = title


def validation_universal(tocheck):
    print("not done")

#Preparations for analysis. Creating the objects
def prepare():
    datatitle = input("What kind of data is this?\n")
    totalanswer = Userdata(input("Write the total number of answers\n"), 1, datatitle)
    yesanswer = Userdata(input("Write the number of positive answers:\n"), 0, datatitle)
    noanswer = Userdata(input("Write the number of negative answers:\n"), 0, datatitle)
    noneanswer = Userdata(input("Write the number of declined answers:\n"), 0, datatitle)

#Convert the data to intager
def convert_to_int():
    prepare()
    i = 0
    while i < len(datalist):
        temp = datalist[i]
        datalist[i] = int(temp)
        i = i + 1
    print(datalist)

    return datalist

#Info about how you want to analyse
def analyse_info():
    tempelements = []
    tempelements = input("Write the elements you want to compare to the number of answers\n").split(",")
    return tempelements

#Adds analysation results to list
def calculate_percent(answer):
    answer.percent = answer.value/totalanswer.value

def calculate_result():
    return yesanswer.percent

#Performs analysis
def analyse():
    intlist = convert_to_int()
    percent = 0
    elements = []
    elements = analyse_info()
    x = 0
    print(Userdata)
    while x < len(elements):
        if elements[x] == "yes":
            calculate_percent(yesanswer)
            print(yesanswer.value)
        elif elements[x] == "no":
            calculate_percent(noanswer)
        elif elements[x] == "none":
            calculate_percent(noneanswer)
        else:
            print("something went wrong")
        x = x + 1
    result = calculate_result
    return result

#How the program runs
def main():
    print(analyse())

main()
