#Program to calculate net run rate for a tournament
#NRR = (total runs/total overs faced) - (total runs conceded/total overs bowled)
#Asks input for the team and the relevant data
team_name = input("Enter name of team: ")
team_runs = 0
team_oversf = 0
team_runsc = 0
team_oversb = 0
#We will now ask how many matches were played and gather data by using for loop.
n = int(input("How many matches were played? "))
for i in range(1, n+1):
    team_runs += int(input("Runs in match {}: ".format(i)))
    team_oversf += int(input("Overs faced in match {}: ".format(i)))
    team_runsc += int(input("Runs conceded in match {}: ".format(i)))
    team_oversb += int(input("Overs bowled in match {}: ".format(i)))
#calculating Net Run Rate
netrr = team_runs/team_oversf - team_runsc/team_oversb
print("Net Run Rate for team {} is {}.".format(team_name, netrr))
