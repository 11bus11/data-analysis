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


class Userdata:
    """
    Defines the class used for the userdata.
    """
    def __init__(self, value, percent, title):
        self.value = int(value)
        self.percent = percent
        self.title = title


def validation_universal():
    """
    Makes sure all the inputs are the correct type.
    Also checks that the chosen question exist.
    """
    valueyes = 0
    valueno = 0
    valuenone = 0
    status = False
    while status is False:
        try:
            question = input("Which question do you want to analyse? Write a whole number.\n")
            row = int(question) + 1
        except ValueError:
            print("The input is not a whole number. Try again:")
        else:
            status = True

    columnlist = answers.col_values(row)
    if len(columnlist) == 0:
        print("The question you chose does not exist.")
        print("Make sure the data is added correctly to the spreadsheet.")
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
    valuetotal = len(columnlist) - 1
    return valuetotal, valueyes, valueno, valuenone


def create_object():
    """
    Creates the objects used t keep track of all information.
    The objects are for the differrent options and total numbers of answers.
    """
    datatitle = input("What kind of question is this?\n")
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


def calculate_percent(answer1, answer2):
    """
    Calculates how many percent of the answers each option are.
    """
    answer = answer1.value/answer2.value
    return answer


def double_validate_result(list):
    """
    Double-check that the amount of answers are correct.
    """
    totalanswer, yesanswer, noanswer, noneanswer = list
    if yesanswer.value + noanswer.value + noneanswer.value == totalanswer.value:
        pass
    else:
        print("The number of answers are not correct.")
        print("Check the values in your spreadsheet")
        quit()


def list_result_create(title, resultdata):
    """
    Creates a list of the results.
    Will be used in the export_result function.
    """
    qtitle = title
    listresult = [qtitle, resultdata[1], resultdata[2], resultdata[3], resultdata[0]]
    return listresult


def export_result(listresult):
    """
    Updates the outputs spreadsheet.
    """
    rowlist = ["B1", "B2", "B3", "B4", "B5"]
    row = 0
    while row < len(rowlist):
        current = rowlist[row]
        print(current + " is being updated...")
        if current == "B1":
            output.update(current, listresult[row])
        else:
            output.update(current, listresult[row]*100)
        row += 1


def main():
    """
    The function that tells the program how to run.
    """
    print("This program checks the amounts (in percent) of each options.")
    print("Make sure the correct data in the spreadsheet is correct.")
    print("Also make sure the layout of the spreadsheet is correct.")
    print("Check the READ.me to see the layout.")
    datalist = create_object()
    totalanswer, yesanswer, noanswer, noneanswer = datalist
    result = double_validate_result(datalist)
    for item in datalist:
        item.percent = calculate_percent(item, totalanswer)
    finaldata = [totalanswer.percent, yesanswer.percent, noanswer.percent, noneanswer.percent]
    export_result(list_result_create(totalanswer.title, finaldata))
    print("Spreadsheet now updated!")
    print("REMEMBER: All values are in percent.\n")
    print("You can now find the resulting information in the spreadsheet.")
    print("In the outputs sheet.")
    print("Run the program again to analyse a different question.")
    print("Program by: Erik Vodopivec Forsman")


main()
