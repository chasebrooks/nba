import pandas as pd

players = pd.read_json('resources/players.json')
ratings = pd.read_csv('resources/ratings.csv')
teams = pd.read_json('resources/teams.json')

for i in players:
    players['fullName'] = players['firstName'] + ' ' + players['lastName']

result = pd.merge(players, ratings, left_on= 'fullName', right_on='Player')
result = pd.merge(result,teams, left_on='teamId', right_on='teamId')
print(result.head())
result = result[['Player', 'playerId', 'teamId', '2K17', '2K16', 'abbreviation']]

result['2K16'].fillna(result['2K17'], inplace=True)

result.to_csv('resources/players.csv')








