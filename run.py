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
    datalist = []
    datatitle = input("What kind of data is this?\n")
    totalanswer = Userdata(int(input("Write the total number of answers\n")), 1, datatitle)
    yesanswer = Userdata(int(input("Write the number of positive answers:\n")), 0, datatitle)
    noanswer = Userdata(int(input("Write the number of negative answers:\n")), 0, datatitle)
    noneanswer = Userdata(int(input("Write the number of declined answers:\n")), 0, datatitle)

        

#Convert the data to intager
def convert_to_int():
    prepare()
    i = 0
    while i < len(datalist):
        temp = datalist[i].value
        datalist[i].value = int(temp)
        i = i + 1
    print(datalist)

    return datalist

#Info about how you want to analyse
def analyse_info():
    tempelements = []
    tempelements = input("Write the elements you want to compare to the number of answers\n").split(",")
    return tempelements

#Calculates the percentage 
def calculate_percent(answer):
    answer.percent = answer.value/totalanswer.value

#Make sure the results are correct and result in 100%
def calculate_result():
    if yesanswer.percent + noanswer.percent + noneanswer.percent == 1:
        print("correct")
    else:
        print("incorrect")

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
