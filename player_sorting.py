from recruit_gui import *
from scraper import *


sort_criteria = {}

def sort(var, players): 
    sortlist = []
    for index, player in enumerate(players):
        if var in player:
            sortlist.append(player)   
    return sortlist

def sortPlayers(event, players, values): # returns a new list from players that is sorted based on event 
        var = str(values[event])
        new_list = []
        if var == 'ALL': # Sorting if user selects ALL 
            del sort_criteria[event]
        elif event != '-SCHOOLS-': 
            sort_criteria[event] = var
        placeholder = players.copy()
        for key, value in sort_criteria.items():
                event = key
                placeholder = sort(value, placeholder)
        
        new_list = placeholder
        
        return new_list