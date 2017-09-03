from bs4 import BeautifulSoup
import requests
import os
import json
import time

class scrape():
    def __init__(self):
        pass

    def start(self):
        file = open(os.path.expanduser('nba.csv'), 'ab+')
        headers = 'game,weekday,month_day,year,opponent,game_results,,teamscore,opponentscore,w,l,streak,team' + '\n'
        file.write(bytes(headers, encoding='utf-8', errors='ignore'))
        with open('/Users/chasebrooks/PycharmProjects/nba/resources/nba_ref_teams.json', 'r') as datafile:
            data = json.loads(datafile.read())
            teams = []
            for item in data:
                teams.append(item['abbreviation'])
            for i in teams:
                self.teamdata(i)
                time.sleep(3)

    def teamdata(self, abv):
        file = open(os.path.expanduser('nba.csv'), 'ab')
        url = 'www.basketball-reference.com/teams/'+abv+'/2017_games.html'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                  'Accept-Language': 'en-US,en;q=0.8'}
        r = requests.get("https://" + url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        datacolumns = ['g','date_game', 'opp_name', 'game_result', 'overtimes', 'pts', 'opp_pts', 'wins', 'losses', 'game_streak']
        gamedata = ''
        for record in soup.findAll('tr'):
            for data in record.findAll('td', {'data-stat': datacolumns}):
                gamedata += data.text + ','
            gamedata = gamedata + abv + '\n'
        if gamedata.split(',')[1] != '':
            file.write(bytes(gamedata, encoding='utf-8', errors='ignore'))

run = scrape()
run.start()



