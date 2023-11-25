# Import
import random
import secrets
import math

# Customizable Variables
gamesPerSeason = 10
seasonsToSim = 1

# Team Dictionary
teams = {
"Panters": {"place": "North"},
"Generals": {"place": "North"},
"Stars": {"place": "North"},
"Maulers": {"place": "North"},
"Stallions": {"place": "South"},
"Gamblers": {"place": "South"},
"Showboats": {"place": "South"},
"Breakers": {"place": "South"}
}

# Team List
teamsList = []
for team in teams:
    teamsList.append(team)

# Season Dictionary
seasons = {}

# Stat Dictionary
stats = {}

# Games per week
gamesPerWeek = len(teamsList) // 2

# Season OVR Generator Function
def ovrGen():
    
    # Thre categories for each team
    categories = ['Offense', 'Defense', 'Special']

    # Giving each team stats for each category
    for team in teams:
        for category in categories:
            teams[team][category] = random.random()    

# Season Scheduler Function
def seasonScheduler():
    # Run this loop for the season being simulated
    for season in range(seasonsToSim):
        seasons[str(season + 1)] = str(season + 1)

        # Run this loop for every week in each season
        for week in range(gamesPerSeason):
            # Run this loop for every game each week
            for game in range(gamesPerWeek):
                team1 = secrets.choice(teamsList)
                teamsList.remove(team1)
                team2 = secrets.choice(teamsList)
                teamsList.remove(team2)
                matchup = team1 + ', ' + team2

            # Run this loop for every team to append the team back into the teamsList
            for team in teams:
                teamsList.append(team)

    seasons['1'] = 'Stars, Stallions'

# Season Simulator Function
def gameSimulator():
    # Teams playing
    playingTeams = seasons['1'].split(', ')
    team1 = playingTeams[0]
    team2 = playingTeams[1]

    # Each team's offense compared to defense
    team1O = teams[team1]['Offense'] - teams[team2]['Defense'] + 1.25
    team2O = teams[team2]['Offense'] - teams[team1]['Defense'] + 1.25

    # Each team's TDs
    team1TD = math.floor(random.randrange(2, 4) * team1O)
    team2TD = math.floor(random.randrange(2, 4) * team2O)

    # Each team's FGs
    team1FG = math.floor(random.randrange(0, 5) * (teams[team1]['Special'] + 1))
    team2FG = math.floor(random.randrange(0, 5) * (teams[team2]['Special'] + 1))

    # Each team's points
    team1Points = (team1TD * 7) + (team1FG * 3)
    team2Points = (team2TD * 7) + (team2FG * 3)

    # Final Score
    finalScore = team1 + ': ' + str(team1Points) + ' | ' + team2 + ': ' + str(team2Points)

    # Who won?
    if (team1Points > team2Points):
        winner = team1

    elif (team2Points > team1Points):
        winner = team2
    
    else:
        winner = ''

    # Print Score/Winner
    print('++++++++++++++++')
    print(finalScore)
    print(winner)
    print('++++++++++++++++')






# TEST!!!!!!!!!!!!!!!!!!!!!!!!!
for season in range(seasonsToSim):
    seasonScheduler()
    ovrGen()
    gameSimulator()