import numpy as np
import pandas as pd
import requests
import json
import time

def getPokemonInfo(dex_no):
    r = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(dex_no))
    mon_dict = r.json()
    name = mon_dict['name']
    moves = []
    abilities = []
    types = []
    stat_arr = np.zeros(6, dtype=int)
    for move in mon_dict['moves']:
        moves.append(move['move']['name'])
    for i, stat in enumerate(mon_dict['stats']):
        stat_arr[i] = stat['base_stat']
    for abil in mon_dict['abilities']:
        abilities.append(abil['ability']['name'])
    for t in mon_dict['types']:
        types.append(t['type']['name'])
    
    return name, moves, stat_arr, abilities, types


pokedex = pd.DataFrame({
    'name': pd.Series(),
    'type': pd.Series(),
    'abilities': pd.Series(),
    'moves':pd.Series(),
    'stats':pd.Series()
})

# There are 1025 pokemon at time of writing.

for dex_no in range(1,1026):
    time.sleep(1/10) # polite for the API
    print("Fetching mon",dex_no,"/",1025,end='\r')
    name, move_list, stats, abils, types = getPokemonInfo(dex_no)
    mon = {
        'name':name,
        'type':types,
        'abilities':abils,
        'moves':move_list,
        'stats':stats,
    }
    pokedex = pokedex._append(mon, ignore_index=True)

pokedex.to_feather("pokedex.feather")
pokedex.head()
