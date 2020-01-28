import csv
import random

alphabeticalList = ['Ahmad, Daanish']

class Student:
    def __init__(self, name):
        self.name = name
        self.restrictedStudents = list()
    def appendName(self, appendedName):
        self.restrictedStudents.append(appendedName)

# read the namelist.csv
with open('/Users/Kenny/Desktop/Python/namelist.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
            #add alphabeticalList entries
            alphabeticalList.append(f'{row["Ahmad"]}, {row["Daanish"]}')


listOfObjects = list()
for i in alphabeticalList:
    listOfObjects.append(Student(i))

def shuffleObjects(copiedList):
    shuffledObjects = copiedList.copy()
    random.shuffle(shuffledObjects)
    return shuffledObjects

shuffledObjects = shuffleObjects(listOfObjects)

def designate():
    print('\nKitchen staff:')
    #first 7 people are kitchen staff
    for i in range(7):
        print(shuffledObjects[i].name)
    #next 31 people are waiting
    print('\nWaiters:')
    for waitingTable in range(7,38):
        print(shuffledObjects[waitingTable].name + f' waiting at table {waitingTable - 6}')
    #rest are sitting at tables
    print('\nTable seatings:')
    tableNumber = 1
    #first 5 tables have 9 people
    nineTableCounter = 1
    for sittingTable in range(38,84):
        print(shuffledObjects[sittingTable].name + f' sitting at table {tableNumber}')
        if nineTableCounter % 9 == 0:
            tableNumber += 1
        nineTableCounter +=1
    eightTableCounter = 1
    #rest of the tables have 8 people
    for sittingTable in range(84,290):
        print(shuffledObjects[sittingTable].name + f' sitting at table {tableNumber}')
        eightTableCounter +=1
        if eightTableCounter % 8 == 0:
            tableNumber += 1

designate()
