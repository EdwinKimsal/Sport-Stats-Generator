# Import
import random
import secrets
import math

# Customizable Variables
gamesPerSeason = 17
seasonsToSim = 1

# Team Dictionary
teams = {
"49ers": {},
"Bears": {},
"Bengals": {},
"Bills": {},
"Broncos": {},
"Browns": {},
"Buccaneers": {},
"Cardinals": {},
"Chargers": {},
"Chiefs": {},
"Colts": {},
"Commanders": {},
"Cowboys": {},
"Dolphins": {},
"Eagles": {},
"Falcons": {},
"Giants": {},
"Jaguars": {},
"Jets": {},
"Lions": {},
"Packers": {},
"Panthers": {},
"Patriots": {},
"Raiders": {},
"Rams": {},
"Ravens": {},
"Saints": {},
"Seahawks": {},
"Steelers": {},
"Texans": {},
"Titans": {},
"Vikings": {}
}

# Stat Dictionary
stats = {
"49ers": {"games": "0"},
"Bears": {"games": "0"},
"Bengals": {"games": "0"},
"Bills": {"games": "0"},
"Broncos": {"games": "0"},
"Browns": {"games": "0"},
"Buccaneers": {"games": "0"},
"Cardinals": {"games": "0"},
"Chargers": {"games": "0"},
"Chiefs": {"games": "0"},
"Colts": {"games": "0"},
"Commanders": {"games": "0"},
"Cowboys": {"games": "0"},
"Dolphins": {"games": "0"},
"Eagles": {"games": "0"},
"Falcons": {"games": "0"},
"Giants": {"games": "0"},
"Jaguars": {"games": "0"},
"Jets": {"games": "0"},
"Lions": {"games": "0"},
"Packers": {"games": "0"},
"Panthers": {"games": "0"},
"Patriots": {"games": "0"},
"Raiders": {"games": "0"},
"Rams": {"games": "0"},
"Ravens": {"games": "0"},
"Saints": {"games": "0"},
"Seahawks": {"games": "0"},
"Steelers": {"games": "0"},
"Texans": {"games": "0"},
"Titans": {"games": "0"},
"Vikings": {"games": "0"}
}

# Team List
teamsList = []
for team in teams:
    teamsList.append(team)

# Games per week
gamesPerWeek = len(teamsList) // 2

# Season OVR Generator Function
def ovrGen():

    # The categories for each team
    categories = ['Offense', 'Defense', 'Special']

    # Giving each team stats for each category
    for team in teams:
        for category in categories:
            teams[team][category] = random.random()

# Program Dictionary
program = {
"Seasons": str(seasonsToSim),
"Games Per Season": str(gamesPerSeason),
"Teams": str(len(teamsList)),
"Games Per Week": str(gamesPerWeek)
}

# Season Dictionary
seasons = {}

# Season Scheduler Function
def seasonScheduler():

    # Run this loop for the season being simulated
    for season in range(seasonsToSim):

        # Run this loop for every week in each season
        for week in range(gamesPerSeason):

            # Run this loop for every game each week
            for game in range(gamesPerWeek):
                team1 = secrets.choice(teamsList)
                teamsList.remove(team1)
                team2 = secrets.choice(teamsList)
                teamsList.remove(team2)
                matchup = team1 + ', ' + team2
                seasons[str(season + 1) +  ", " + str(week + 1) +  ", " + str(game + 1)] = matchup

            # Run this loop for every team to append the team back into the teamsList
            for team in teams:
                teamsList.append(team)

# Season Simulator Function
def gameSimulator():

    # Run this loop for the season being simulated
    for season in range(seasonsToSim):

        # Run this loop for every week in each season
        for week in range(gamesPerSeason):

            # Run this loop for every game each week
            for game in range(gamesPerWeek):

                # Teams playing
                playingTeams = seasons[str(season + 1) +  ", " + str(week + 1) +  ", " + str(game + 1)].split(', ')
                team1 = playingTeams[0]
                team2 = playingTeams[1]

                # Each team's offense compared to defense
                team1O = teams[team1]['Offense'] - (2 * teams[team2]['Defense']) + 2.1
                team2O = teams[team2]['Offense'] - (2 * teams[team1]['Defense']) + 2.1

                # Each team's TDs
                team1TD = math.floor(random.randrange(2, 5) * team1O)
                team2TD = math.floor(random.randrange(2, 5) * team2O)
                stats[team1][str(season + 1) + ", " + str(week + 1) + " | TDs"] = str(team1TD)
                stats[team2][str(season + 1) + ", " + str(week + 1) + " | TDs"] = str(team2TD)

                # Each team's FGs
                team1FG = math.floor(random.randrange(0, 4) * (teams[team1]['Special'] + 1))
                team2FG = math.floor(random.randrange(0, 4) * (teams[team2]['Special'] + 1))
                stats[team1][str(season + 1) + ", " + str(week + 1) + " | FGs"] = str(team1FG)
                stats[team2][str(season + 1) + ", " + str(week + 1) + " | FGs"] = str(team2FG)

                # Each team's safties
                team1Safty = math.floor(random.randrange(0, 10) * teams[team1]['Defense'] / 8.25)
                team2Safty = math.floor(random.randrange(0, 10) * teams[team2]['Defense'] / 8.25)
                stats[team1][str(season + 1) + ", " + str(week + 1) + " | safties"] = str(team1Safty)
                stats[team2][str(season + 1) + ", " + str(week + 1) + " | safties"] = str(team2Safty)

                # Each team's points
                team1Points = (team1TD * 7) + (team1FG * 3) + (team1Safty * 2)
                team2Points = (team2TD * 7) + (team2FG * 3) + (team2Safty * 2)
                stats[team1][str(season + 1) + ", " + str(week + 1) + " | points"] = str(team1Points)
                stats[team2][str(season + 1) + ", " + str(week + 1) + " | points"] = str(team2Points)

                # Each team's pointsAllowed
                stats[team1][str(season + 1) + ", " + str(week + 1) + " | pointsAllowed"] = str(team2Points)
                stats[team2][str(season + 1) + ", " + str(week + 1) + " | pointsAllowed"] = str(team1Points)

                # Final Score
                finalScore = team1 + ': ' + str(team1Points) + ' | ' + team2 + ': ' + str(team2Points)

                # Who won?
                if (team1Points > team2Points):
                    stats[team1][str(season + 1) + ", " + str(week + 1) + " | win"] = "1"
                    stats[team2][str(season + 1) + ", " + str(week + 1) + " | lose"] = "1"

                elif (team2Points > team1Points):
                    stats[team1][str(season + 1) + ", " + str(week + 1) + " | lose"] = "1"
                    stats[team2][str(season + 1) + ", " + str(week + 1) + " | win"] = "1"
                
                else:
                    stats[team1][str(season + 1) + ", " + str(week + 1) + " | tie"] = "1"
                    stats[team2][str(season + 1) + ", " + str(week + 1) + " | tie"] = "1"
                
                # +1 to both team's games
                stats[team1]["games"] = str(int(stats[team1]["games"]) + 1)
                stats[team2]["games"] = str(int(stats[team2]["games"]) + 1)

# Calling functions
seasonScheduler()
ovrGen()
gameSimulator()

# Creating stats.txt
fileStats = open("stats.txt", "w")
fileStats.write(str(stats))
fileStats.close()

# Creating program.txt
fileProgram = open("program.txt", "w")
fileProgram.write(str(program))
fileProgram.close()