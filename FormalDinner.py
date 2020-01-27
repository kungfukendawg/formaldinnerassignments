import csv
import random

alphabeticalDictionary = {'Ahmad, Daanish': 0}

# read the namelist.csv
with open('/Users/Kenny/Desktop/Python/namelist.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #counter for alphabeticalDictionary values
    counter = 1
    for row in csv_reader:
            #add alphabeticalDictionary entries
            alphabeticalDictionary.update({f'{row["Ahmad"]}, {row["Daanish"]}': counter})
            counter += 1

#print(alphabeticalDictionary)

#function to shuffle the dictionary
def shuffleNames():
    shuffledKeys = list(alphabeticalDictionary.keys())
    random.shuffle(shuffledKeys)
    return shuffledKeys

shuffledKeys = shuffleNames()
#print(shuffledKeys)

def attachValues():
    shuffledList = ([(key, alphabeticalDictionary[key]) for key in shuffledKeys])
    return shuffledList
    
shuffledList = attachValues()
#print(shuffledList)

def designate():
    counter = 0
    print('\nKitchen staff:')
    #first 7 people are kitchen staff
    while counter <= 6:
        print(shuffledKeys.pop(0))
        counter += 1
    #next 31 people are waiting
    print('\nWaiters:')
    for waitingTable in range(31):
        print(shuffledKeys.pop(0) + f' waiting at table {counter - 6}')
        counter += 1
    
    print('\nTable seatings:')

    tableNumber = 1
    tableCounter = 1
    while tableNumber <= 31:
        print(shuffledKeys.pop(0) + f' sitting at table {tableNumber}')
        tableCounter += 1
        if tableCounter % 8 == 0:
            tableNumber += 1
    remainderTableCounter = 1
    for name in range(5):
        print(shuffledKeys.pop(0) + f' sitting at table {remainderTableCounter}')
        remainderTableCounter += 1

designate()

#print(shuffledKeys)