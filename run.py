polldata = ""
percentage = []

alldata = []

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
def create_object():
    alldata = []
    datatitle = input("What kind of data is this?\n")
    totalanswer = Userdata(input("Write the total number of answers\n"), 1, datatitle)
    yesanswer = Userdata(input("Write the number of positive answers:\n"), 0, datatitle)
    noanswer = Userdata(input("Write the number of negative answers:\n"), 0, datatitle)
    noneanswer = Userdata(input("Write the number of declined answers:\n"), 0, datatitle)
    return totalanswer, yesanswer, noanswer, noneanswer

        

#Convert the data to intager
def convert_to_int(alldata):
    data = alldata
    i = 0
    while i < len(alldata):
        temp = alldata[i].value
        alldata[i].value = int(temp)
        i = i + 1
    print(alldata)
    return alldata

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
def calculate_result():
    if yesanswer.percent + noanswer.percent + noneanswer.percent == 1:
        print("correct")
    else:
        print("incorrect")

#Performs analysis
def analyse():
    
    datalist = create_object()
    totalanswer, yesanswer, noanswer, noneanswer = datalist
    print(yesanswer.value)
    intlist = convert_to_int(datalist)
    percent = 0
    elements = []
    elements = analyse_info()
    x = 0
    while x < len(elements):
        if elements[x] == "yes":
            yesanswer.percent = calculate_percent(yesanswer, totalanswer)
            print(yesanswer.percent)
        elif elements[x] == "no":
            noanswer.percent = calculate_percent(noanswer, totalanswer)
            print(noanswer.percent)
        elif elements[x] == "none":
            noneanswer.percent = calculate_percent(noneanswer, totalanswer)
            print(noneanswer.percent)
        else:
            print("something went wrong")
        x = x + 1
    result = calculate_result
    return result

#How the program runs
def main():
    print(analyse())

main()
