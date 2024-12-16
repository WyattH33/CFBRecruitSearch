import PySimpleGUI as sg
from recruit_gui import make_school_window, createWindow
from player_sorting import sortPlayers
from scraper import create_player_list

def event_loop(school):
        window, player_list = make_school_window(school) # creates base window with 'oklahoma'
        data = player_list
        while True: # event loop for UI
                event, values = window.read() # waits for user input
                if event == sg.WIN_CLOSED:
                                win_closed = True
                                break
                if event == '-POSITIONS-' or event == '-CLASS-' or event == '-STATES-':
                        data = sortPlayers(event, player_list, values) # sorts player list based on sort criteria
                if event == '-RATINGS-':
                        pass
                if event == '-SCHOOLS-': 
                        player_list = create_player_list(values[event]) # gets a new player_list from the selected school
                window = createWindow(event, window, data, values) # loads new window based on sorted data

def main():
        school = 'oklahoma'
        event_loop(school)
main()