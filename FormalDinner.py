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

#convert list of strings to a list of objects
listOfObjects = list()
for i in alphabeticalList:
    listOfObjects.append(Student(i))

#shuffle any given list using a shallow copy to keep the objects the same
def shuffleObjects(copiedList):
    shuffledObjects = copiedList.copy()
    random.shuffle(shuffledObjects)
    return shuffledObjects

firstShuffle = shuffleObjects(listOfObjects)
secondShuffle = shuffleObjects(listOfObjects)
thirdShuffle = shuffleObjects(listOfObjects)

#function to check if table mates have been repeated
def checkTableMates(seatsPerTable, importedList):
    #repeat for every student at the table
    for student in range(seatsPerTable):
        #for every student in a restrictedStudents list
        for restrictedStudent in importedList[student].restrictedStudents:
            #repeat for every student at the table
            for tableMate in range(seatsPerTable):
                if f'{restrictedStudent}' == f'{importedList[tableMate].name}':
                    print('found overlap')
                    return False
    return True

def designate(shuffledNames):
    
    print('\nKitchen staff:')
    #first 7 people are kitchen staff
    for i in range(7):
        print(shuffledNames.pop(0).name)
    
    #next 31 people are waiting
    print('\nWaiters:')
    for waitingTable in range(31):
        print(shuffledNames.pop(0).name + f' waiting at table {waitingTable + 1}')
    
    #rest are sitting at tables
    print('\nTable seatings:')
    #variable to keep track of table number
    tableNumber = 1
    #list to temporarily store names to add to Student classes
    tableList = list()
    
    #make tables of 9 for the first 5 tables
    for i in range (4):
        #check if the next 9 students have sat next to each other before
        #do this 15 times or until all table mates are new
        #if it still doesn't work, then just move on to prevent the program from crashing
        for i in range(15):
            #if table mates are new, move on
            if checkTableMates(9, shuffledNames) == True:
                break
            #if table mates are repeated, shuffle the existing list of Student objects
            shuffledNames = shuffleObjects(shuffledNames)
        for sittingTable in range(9):
            print(shuffledNames[sittingTable].name + f' sitting at table {tableNumber}')
            #add student name to the temporary tableList
            tableList.append(shuffledNames[sittingTable].name)
        for studentObject in range(9):
            #append names of table mates to the students restrictedStudents list
            for name in tableList:
                shuffledNames[studentObject].appendName(name)
            #remove the student's own name from their restrictedStudents List
            del shuffledNames[studentObject].restrictedStudents[studentObject]
        #clear the temporary tableList for reuse
        tableList.clear()
        #delete the most recent 9 students in the list of student objects
        del shuffledNames[:9]
        #move onto next table
        tableNumber += 1
    
    #SAME AS ABOVE BUT WITH 8 STUDENTS PER TABLE
    #for the rest 26 tables (from 6-31)
    for i in range (27):
        #check if the next 8 students have sat next to each other before
        #do this 15 times or until all table mates are new
        #if it still doesn't work, then just move on to prevent the program from crashing
        for i in range(15):
            #if table mates are new, move on
            if checkTableMates(8, shuffledNames) == True:
                break
            #if table mates are repeated, shuffle the existing list of Student objects
            shuffledNames = shuffleObjects(shuffledNames)
        for sittingTable in range(8):
            print(shuffledNames[sittingTable].name + f' sitting at table {tableNumber}')
            #add student name to the temporary tableList
            tableList.append(shuffledNames[sittingTable].name)
        for studentObject in range(8):
            #append names of table mates to the students restrictedStudents list
            for name in tableList:
                shuffledNames[studentObject].appendName(name)
            #remove the student's own name from their restrictedStudents List
            del shuffledNames[studentObject].restrictedStudents[studentObject]
        #clear the temporary tableList for reuse
        tableList.clear()
        #delete the most recent 8 students in the list of student objects
        del shuffledNames[:8]
        #move onto next table
        tableNumber += 1

#print the following onto the terminal
print('First seating assignment:')
designate(firstShuffle)

print('\nSecond seating assignment:')
designate(secondShuffle)

print('\nThird seating assignment:')
designate(thirdShuffle)
