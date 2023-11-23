import PySimpleGUI as sg
from scraper import create_player_list
from time import sleep

school = 'oklahoma'

player_list = create_player_list(school)

sorted_list = []
players = []

schools = sorted(['ALL', 'georgia-tech', 'louisville', 'miami', 'north-carolina', 'nc-state', 'pittsburgh', 'syracuse', 'virginia', 'virginia', 'wake-forest', 'notre-dame', 'illinois', 'indiana', 'iowa',
            'maryland', 'michigan', 'michigan-state', 'minnesota', 'nebraska', 'northwestern', 'ohio-state', 'penn-state', 'purdue', 'rutgers', 'wisconsin', 
            'baylor', 'iowa-state', 'kansas', 'kansas-state', 'oklahoma-state', 'tcu', 'texas-tech', 'west-virginia', 'texas', 'oklahoma', 'cincinatti', 'byu', 'houston', 'ucf',
            'arizona', 'arizona-state', 'california', 'ucla', 'colorado', 'oregon', 'oregon-state', 'usc', 'stanford', 'utah', 'washingston', 'washington-state',
            'alabama', 'arkansas', 'auburn', 'florida', 'georgia', 'kentucky', 'lsu', 'ole-miss', 'mississippi-state', 'missouri', 'south-carolina', 'tennessee', 'texas-am', 'vanderbilt'])

positions = [ 'ALL', 'PRO', 'DUAL', 'QB', 'RB', 'FB', 'APB', 'WR', 'TE', 'OT', 'OG', 'OC', 'IOL', 'DT', 'Edge',
              'WDE', 'SDE', 'DL', 'ILB', 'OLB', 'LB', 'CB', 'S', 'ATH', 'K', 'P', 'LS', 'RET', ]

years = [ 'ALL', 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
          2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, ]

states = [ 'ALL', 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

ratings = ['Ascending', 'Descending', 'Class Ascending', 'Class Descending']

def create_col(player_list):
        col = [
                [sg.Text(f'{player_list[i][0]}', size=(18,1), key='-START_CREATECOL-'), sg.Text(f'{player_list[i][1]}', size=(4,1)), sg.Text(f'{player_list[i][2]}'), sg.Push(), sg.Text(f'{player_list[i][3]}'), sg.Text(f'{player_list[i][4]}')] for i in range(len(player_list))
        ]
        return col
        


        # SortPlayers Function
def sortPlayers(key):
        global sorted_list
        global players
        var = str(values[key])
        if len(sorted_list) < 1:
                print('less than 1')
                players = player_list 
                for player in player_list:
                        if var in player:
                                sorted_list.append(player) #(41-47) adds players in player_list to sorted_list if they match the sort criteria (position, class, etc.)             
        elif var == 'ALL':
                z = []
                print('all sort')
                sorted_list = players
                for item in values.items(): # obtains sort criteria after ALL selection for one category
                        if item[1] != var:
                                z.append(item)
                
                x = 0
                index = len(players)
                z = z[1:-1]
                print(players)
                for player in player_list:
                        if len(z) > 1: # something in here doesnt work with ALL sort

                                if z[0][1] in player and z[1][1] in player:
                                        players.append(player)
                        elif len(z) < 1:
                                
                                players = player_list
                                index = 0
                                break
                                
                        else:
                                if str(z[0][1]) in player:
                                        print(player)
                                        print(z[0][1])
                                        players.append(player)
                                
                                
                players = players[index:]
                sorted_list = players

        else:
                print('ADDED LIST')
                players = sorted_list.copy()
                count = len(sorted_list)
                for player in sorted_list[0:count]:
                        if var not in player and var != 'Ascending' and var != 'Descending':
                                sorted_list.remove(player)

        return sorted_list, players


def createWindow(key, window, sorted_list, players):
        var = str(values[key])
        if key == '-SCHOOLS-':
                x = make_school_window(var)
        elif key == '-POSITIONS-' or key == '-CLASS-' or key == '-STATES-':
                x = make_sorted_window(var, sorted_list)
        elif key == '-RATINGS-':
                
                sort = -1
                if var[0:5] == 'Class':
                        sort = -3
                if 'Ascending' in var:
                        players.sort(key = lambda players: players[sort])
                        x = make_sorted_window(var, players)
                if 'Descending' in var:
                        players.sort(reverse=True, key = lambda players: players[sort])
                        x = make_sorted_window(var, players)
        
        window.close()
        window = x
        return window

def make_school_window(school):
        global player_list 
        player_list = create_player_list(school)
        col = create_col(player_list)

        col1 = [
                [sg.Combo(schools, default_value=school, enable_events=True, key='-SCHOOLS-'),  sg.Combo(positions, default_value='ALL', enable_events=True, key='-POSITIONS-'), sg.Combo(years, size=(6), default_value='ALL', enable_events=True, key='-CLASS-'), sg.Combo(states, size=(6), default_value='ALL', enable_events=True, key='-STATES-'), sg.Combo(ratings, default_value='Descending', enable_events=True, key='-RATINGS-')]
                ]

        layout = [
                [sg.Column(col1, key='-COL1-')],
                  [sg.Column(col, size=(460,600), scrollable=True, vertical_scroll_only=True, visible=True, key=f'-COL{school}-')]
                  ]
        return sg.Window('Recruit Search', layout, size=(500, 600))

def make_sorted_window(pos, sort_list):
        col = create_col(sort_list)

        col1 = [
                [sg.Combo(schools, default_value=values['-SCHOOLS-'], enable_events=True, key='-SCHOOLS-'),  sg.Combo(positions, default_value=values['-POSITIONS-'], enable_events=True, key='-POSITIONS-'), sg.Combo(years, size=(6), default_value=values['-CLASS-'], enable_events=True, key='-CLASS-'), sg.Combo(states, size=(6), default_value=values['-STATES-'], enable_events=True, key='-STATES-'), sg.Combo(ratings, default_value=values['-RATINGS-'], enable_events=True, key='-RATINGS-')]
                ]

        layout = [
                [sg.Column(col1, key='-COL1-')],
                  [sg.Column(col, size=(460,600), scrollable=True, vertical_scroll_only=True, visible=True, key=f'-COL{school}-')]
                  ]
        return sg.Window('Recruit Search', layout, size=(500, 600))

win_closed = False
while not win_closed:

        window = make_school_window(school)
        while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                                win_closed = True
                                break
                if event == '-SCHOOLS-' or event == '-POSITIONS-' or event == '-CLASS-' or event == '-STATES-' or event == '-RATINGS-':
                        sortPlayers(event)
                        window = createWindow(event, window, sorted_list, players)
        



                

              

#STOP. Works generally ok. Might want to re structure to make every iteration run through the ALL checks, and make it less hairy. 
# have each list input into one function and come out with a defined action from that function, until going through all of them and being
# sorted correctly. 
