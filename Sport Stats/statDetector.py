# Imports
import ast

# Asking for the type of stat
stat = input("Please type the number corresponding to the stat of your choice: \n 1 = Points Scored \n 2 = Points Allowed \n 3 = Touchdowns \n")

# Asking for the connotations
connotation = input("Please type the number corresponding to the connotation of your choice: \n 1 = Positive \n 2 = Neutral \n 3 = Negative \n")

# Asking for the team
team = input("Please type the number corresponding to the team of your choice: \n 1 = 49ers \n 2 = Bears \n 3 = Bengals \n")

# Print a noticible break
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

# List of possibilities
statList = ["points", "pointsAllowed", "TDs"]
connotationList = ["positive", "neutral", "negative"]
teamList = ["49ers", "Bears", "Bengals"]

# statDict (+0 (pos.) or +2 (neg.) for connotation)
statDict = {
    "points": "0",
    "pointsAllowed": "1",
    "TDs": "0"
}

# Input numbers to words
stat = statList[int(stat) - 1]
connotation = connotationList[int(connotation) - 1]
team = teamList[int(team) - 1]

# connotationWeight (+0. or +2 based on statDict)
connotationWeight = statDict[stat]

# Opening and reading the stats.txt file
f = open("stats.txt")
statsFile = f.read()
statsFile = ast.literal_eval(statsFile)

# Opening and reading the program.txt file
f = open("program.txt")
programFile = f.read()
programFile =  ast.literal_eval(programFile)

# Creating a statsList
statsList = []

# Getting last game
# Run this loop for each season
for season in range(int(programFile["Seasons"])):

    # Run this loop for every week in each season
    for week in range(int(programFile["Games Per Week"]) + 1):
        currentStat = statsFile[team][str(season + 1) + ", " + str(week + 1) + " | " + stat]
        statsList.append(currentStat)

# Set variables
total = 0
statNumber = 0
statNumberList = []
weekTracker = []

# Take the avg for each week
# Run this loop for the length of statsList
for week in range(len(statsList)):

    # Run this loop for the number of the current week
    for element in range(week + 1):
        total = total + int(statsList[element])
    
    # Find the avg for each week and append it to statNumberList
    statNumber = total / (week + 1)
    statNumberList.append(statNumber)

    # Find/Appebd the weekNum
    weekNum = len(statsList) - week
    weekTracker.append(weekNum)

    # Reset the total to zero
    total = 0

# (START) Rank the avg by highest to lowest using heap sort

# Heapify Function
def heapify(statNumberList, n, i):
    largest = i  # Largest is the initial
    l = 2 * i + 1  # left = 2 * i + 1
    r = 2 * i + 2  # right = 2 * i + 2
 
    # If left child of root exists and greater than root...
    if l < n and statNumberList[i] < statNumberList[l]:
        # Largest = Left
        largest = l
 
    # If right child of root exists and greater than root...
    if r < n and statNumberList[largest] < statNumberList[r]:
        # Largest = Right
        largest = r
 
    # Change root, if needed
    if largest != i:
        (statNumberList[i], statNumberList[largest]) = (statNumberList[largest], statNumberList[i])  # swap
        (weekTracker[i], weekTracker[largest]) = (weekTracker[largest], weekTracker[i])  # swap
 
        # Call heapify with the root
        heapify(statNumberList, n, largest)
 
# heapSort Function
def heapSort(statNumberList):
    n = len(statNumberList)
 
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(statNumberList, n, i)
 
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        (statNumberList[i], statNumberList[0]) = (statNumberList[0], statNumberList[i])  # swap
        (weekTracker[i], weekTracker[0]) = (weekTracker[0], weekTracker[i])  # swap
        heapify(statNumberList, i, 0)
 
# Call heapSort
heapSort(statNumberList)

# (END) Rank the avg by highest to lowest using heap sort

# Positive Function
def positiveFun():
    statisticUsed = statNumberList[-1 + int(connotationWeight)]
    weekUsed = weekTracker[-1 + int(connotationWeight)]
    print(statisticUsed)
    print(weekUsed)

# Neutral Function
def neutralFun():
    i = int(len(statNumberList) // 2)
    statisticUsed = statNumberList[i]
    weekUsed = weekTracker[i]
    print(statisticUsed)
    print(weekUsed)

# Negative Function
def negativeFun():
    statisticUsed = statNumberList[0 - int(connotationWeight)]
    weekUsed = weekTracker[0 - int(connotationWeight)]
    print(statisticUsed)
    print(weekUsed)

# Detecting the connotaiton and running the appropriate function
if (connotation == "positive"):
    positiveFun()

if (connotation == "neutral"):
    neutralFun()

if (connotation == "negative"):
    negativeFun()

# ++++++++++++++ TEST ++++++++++++++ TEST ++++++++++++++ TEST ++++++++++++++
print(weekTracker)
print(statNumberList)