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

def analyse_info():
    

def concatenate_result_list(num1, list):
    temp = ["temp"]
    tempresult = []
    temp[0] = list[num1]/list[0]
    tempresult = tempresult + temp
    return tempresult

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
    result = [name]
    x = 0
    while x < len(elements):
        if elements[x] == "yes":
            result = result + concatenate_result_list(1, intlist)
        elif elements[x] == "no":
            result = result + concatenate_result_list(2, intlist)
        elif elements[x] == "none":
            result = result + concatenate_result_list(3, intlist)
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
