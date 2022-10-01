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
    status = False
    while status == False:
        try:
            tocheck = input()
            tocheck = int(tocheck)
        except ValueError:
            print("The input can not be made numeric. Try again:")
        else:
            status = True
    return tocheck
        

#Preparations for analysis. Creating the objects
def create_object():
    datatitle = input("What kind of data is this?\n")

    totalanswer = Userdata(0, 1, datatitle)
    print("Write the total number of answers:")
    totalanswer.value = validation_universal()

    yesanswer = Userdata(0, 0, datatitle)
    print("Write the number of positive answers:")
    yesanswer.value = validation_universal()

    noanswer = Userdata(0, 0, datatitle)
    print("Write the number of negative answers:")
    noanswer.value = validation_universal()

    noneanswer = Userdata(0, 0, datatitle)
    print("Write the number of avoided answers:")
    noneanswer.value = validation_universal()
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
        raise Exception("Doublecheck your numbers and try again.")

def convert_to_str(elements):


#Performs analysis
def analyse():
    datalist = create_object()
    totalanswer, yesanswer, noanswer, noneanswer = datalist
    print(yesanswer.value)
    result = calculate_result(datalist)
    elements = []
    elements = analyse_info()
    for item in elements:
        if item == "yes":
            yesanswer.percent = calculate_percent(yesanswer, totalanswer)
            print(yesanswer.percent)
        elif item == "no":
            noanswer.percent = calculate_percent(noanswer, totalanswer)
            print(noanswer.percent)
        elif item == "none":
            noneanswer.percent = calculate_percent(noneanswer, totalanswer)
            print(noneanswer.percent)
        else:
            print("something went wrong")
    convert_to_str(elements)
    endresult = "Positive: "
    return endresult

#How the program runs
def main():
    print(analyse())

main()
