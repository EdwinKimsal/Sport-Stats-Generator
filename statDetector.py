# Imports
import ast

# Asking for the type of stat
stat = input("Please type the number corresponding to the stat of your choice: \n 1 = Points Scored \n 2 = Points Allowed \n 3 = Touchdowns \n")

# Asking for the connotations
connotation = input("Please type the number corresponding to the connotation of your choice: \n 1 = Positive \n 2 = Negative \n 3 = Neutral \n")

# Asking for the team
team = input("Please type the number corresponding to the team of your choice: \n 1 = 49ers \n 2 = Bears \n 3 = Bengals \n")

# List of possibilities
statList = ["points", "pointsAllowed", "TDs"]
connotationList = ["positive", "negative", "neutral"]
teamList = ["49ers", "Bears", "Bengals"]

# Input numbers to words
stat = statList[int(stat) - 1]
connotation = connotationList[int(connotation) - 1]
team = teamList[int(team) - 1]

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
    for week in range(int(programFile["Games Per Week"])):
        currentStat = statsFile[team][str(season + 1) + ", " + str(week + 1) + " | " + stat]
        statsList.append(currentStat)

# Set total, statNumber, and statNumberList
total = 0
statNumber = 0
statNumberList = []

# Take the avg for each week
# Run this loop for the length of statsList
for week in range(len(statsList)):

    # Run this loop for the number of the current week
    for element in range(week + 1):
        total = total + int(statsList[element])
    
    # Find the avg for each week and append it to statNumberList
    statNumber = total / (week + 1)
    statNumberList.append(statNumber)

    # Reset the total to zero
    total = 0

# Positive Function

# Neutral Function

# Negative Function

# Detecting the connotaiton and running the appropriate function

# ++++++++++++++ TEST ++++++++++++++ TEST ++++++++++++++ TEST ++++++++++++++
print(statNumberList)