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

result = 0
elements = []
temp = 0
i = 0

def convert_to_int():
    i = 0
    while i < len(datalist):
        temp = datalist[i]
        datalist[i] = int(temp)
        i = i + 1
    print(datalist)
    return datalist

def analyse(intdata):
    print(intdata)
    percentage = []
    result = []
    print("what do you want?")
    print("Write the elements you want to compare to the number of answers")
    elements = input().split(",")
    x = 0
    while x < len(elements):
        if elements[x] == "yes":
            result = result.append(intdata[1]/intdata[0])
        elif elements[x] == "no":
            result = result.append(intdata[2]/intdata[0])
        elif elements[x] == "none":
            result = result.append(intdata[3]/intdata[0])
        else:
            print("not done")
        x = x + 1
    print(datalist)
    print(result)

def main():
    print("Input your data in this fashion:")
    print("answer amount,yes answers,no answers,none\n")
    polldata = input()
    print(polldata)
    datalist = polldata.split(",")
    print(datalist)
    print(analyse(convert_to_int()))

main()
