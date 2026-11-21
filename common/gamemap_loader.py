import json
import sys
import os

from common.gamemap import *

def get_gamemap_names() :
    names = []
    for file_name in os.listdir('maps') :
        if file_name.endswith('.json') :
            names.append(file_name[:-5])
    names.sort()
    return names

def load_gamemap(gamemap_name) :
    path = _complete_path(gamemap_name)
    try :
        f = open(path)
        map_data = json.load(f)
        f.close()
    except FileNotFoundError :
        print('map not found :', path)
        sys.exit()

    tiles = list(map(list, map_data['tiles']))

    return map_data['name'], map_data['start_gold'], map_data['lives'], tiles

def _complete_path(gamemap_name) :
    return 'maps/' + gamemap_name + '.json'