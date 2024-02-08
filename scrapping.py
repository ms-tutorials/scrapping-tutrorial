import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://www.pro-football-reference.com")

soup = BeautifulSoup(req.content, features="html.parser")

teams = []

table =  soup.find('table', {'id': 'AFC'})

for row in table.find('tbody').find_all('tr'):
    try:
        if row.find('a'):
            team = {
                "name": row.find('a').text,
                "wins": row.find('td',{'data-stat':"wins"}).text,
                "losses": row.find('td',{'data-stat':"losses"}).text,
                "percentage": row.find('td',{'data-stat':"win_loss_perc"}).text,
            }
        teams.append(team)
    except:
        pass


print(teams)


football = pd.DataFrame(teams)

print(football)