from bs4 import BeautifulSoup
import requests
import lxml

school = 'oklahoma'
def create_player_list(school):

    url = f'https://247sports.com/college/{school}/Sport/Football/AllTimeRecruits/'

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
    }


    player_list = []
    states = []

    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    players = soup('a', class_ ='ri-page__name-link')
    ratings = soup('span', class_ = 'score')
    positions = soup('div', class_ = 'position')
    years = soup('span', class_ = 'meta')

    def string_cleaner(string):
        string = string.replace(' ', '')
        string = string.replace('\n', '')
        return string


    for year in years:
        years.remove(year)
        states.append(string_cleaner(year.text)[-3:-1])


    for i, player in enumerate(players):
        player = player.text
        rating = ratings[i].text
        position = string_cleaner(positions[i].text)
        year = string_cleaner(years[i].text)[-4:]
        state = states[i]
        player_list.append([player, position, year, state, rating])

    for index, player in enumerate(player_list):
        if len(player_list[index][0]) > 22:
            num = player_list[index][0].find(' ')
            player_list[index][0] = player_list[index][0][:num+2] + '.'

    
    return player_list
