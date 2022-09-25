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

print("Input your data in this fashion:")
print("answer amount,yes answers,no answers,none\n")
polldata = input()
print(polldata)
datalist = polldata.split(",")
print(datalist)
result = 0
elements = ""
temp = 0

def convert_to_int():
    i = 0
    while i < len(datalist):
        temp = datalist[i]
        datalist[i] = int(temp)
        i = i + 1

def analyse():
    convert_to_int()
    percentage = []
    if elements == "yes":
        result = datalist[1]/datalist[0]
    elif elements == "no":
        result = datalist[2]/datalist[0]
    elif elements == "none":
        result = datalist[3]/datalist[0]
    else:
        print("not done")
    print(datalist)
    print(result)

print("what do you want?")
print("Write the elements you want to compare to the number of answers")
#elements = str(input().split(","))
elements = input()
print(elements)

analyse()
