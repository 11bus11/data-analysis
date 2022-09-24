# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Info-stats")

no1 = SHEET.worksheet("no1")
data = no1.get_all_values()
print(data)

polldata = ""

print("Input your data in this fashion:")
print("question nr,answer amount,yes answers,no answers,none,check total\n")
polldata = input()
print(polldata)
datalist = str(polldata.split(","))
print(datalist)

print("what do you want?")
print("Write the elements you want to compare to the number of answers")
elements = str(input().split(","))
print(elements)
percentage = []