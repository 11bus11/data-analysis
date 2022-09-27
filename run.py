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

def prepare():
    polldata = input()
    print(polldata)
    datalist = polldata.split(",")
    print(datalist)
    return datalist

def convert_to_int():
    datalist = prepare()
    i = 0
    while i < len(datalist):
        temp = datalist[i]
        datalist[i] = int(temp)
        i = i + 1
    print(datalist)
    return datalist

def analyse():
    intlist = convert_to_int()
    elements = []
    percent = 0
    name = input("what kind of data is it?\n")
    print("what do you want?")
    print("Write the elements you want to compare to the number of answers")
    elements = input().split(",")
    print(elements, "elements")
    print(intlist, "int")
    x = 0
    while x < len(elements):
        result = [name]
        temp = ["temp"]
        if elements[x] == "yes":
            percent = intlist[1]/intlist[0]
            temp[0] = percent
            result = result.extend(temp)
            print(percent)
            print(result)
        elif elements[x] == "no":
            percent = intlist[2]/intlist[0]
            temp[0] = percent
            result = result.extend(temp)
            print(percent)
            print(result)
        elif elements[x] == "none":
            percent = intlist[3]/intlist[0]
            temp[0] = percent
            result = result + temp
            print(percent)
        else:
            print("not done")
        x = x + 1
    
    print(intlist)
    print(result, "RES")
    return result

def main():
    print("Input your data in this fashion:")
    print("answer amount,yes answers,no answers,none\n")
    print(analyse())

main()
