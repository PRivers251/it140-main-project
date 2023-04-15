# Patrick Rivers

import time
import sys

# defines Region class
class Region:
    def __init__(self, name, north, south, east, west, item, villain):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.item = item
        self.villain = villain


# declares each Region object with parameters
plains_of_avondale = Region(
    'Plains of Avondale',
    'The Northern Wasteland',
    'The Gozani Desert',
    'The Forgotten Forest',
    'Hero\'s Graveyard',
    None,
    False
)

northern_wasteland = Region(
    'The Northern Wasteland',
    'Dragon Back Mountains',
    'Plains of Avondale',
    'Drakken Castle',
    None,
    None,
    False
)

dragon_back_mountains = Region(
    'Dragon Back Mountains',
    None,
    'The Northern Wasteland',
    None,
    None,
    'The Dragon Scale Key',
    False
)

drakken_castle = Region(
    'Drakken Castle',
    None,
    'Crystal River Marshes',
    None,
    'The Northern Wasteland',
    None,
    True
)

forgotten_forest = Region(
    'The Forgotten Forest',
    None,
    None,
    'Crystal River Marshes',
    'Plains of Avondale',
    'The Wooden Key',
    False
)

crystal_river_marshes = Region(
    'Crystal River Marshes',
    'Drakken Castle',
    None,
    None,
    'The Forgotten Forest',
    'The Crystal Key',
    False
)

heros_graveyard = Region(
    'Hero\'s Graveyard',
    'Sitrel\'s Tomb',
    None,
    'Plains of Avondale',
    None,
    'The Hero Key',
    False
)

sitrels_tomb = Region(
    'Sitrel\'s Tomb',
    None,
    'Hero\'s Graveyard',
    None,
    None,
    None,
    False
)

gozani_desert = Region(
    'The Gozani Desert',
    'Plains of Avondale',
    None,
    'Shores of the Endless Sea',
    None,
    'The Bone Key',
    False
)

shores_of_the_endless_sea = Region(
    'Shores of the Endless Sea',
    None,
    None,
    'Isles of Burgay',
    'The Gozani Desert',
    None,
    False
)

isles_of_burgay = Region(
    'Isles of Burgay',
    None,
    None,
    None,
    'Shores of the Endless Sea',
    'The Golden Key',
    False
)

# maps each Region.name with it's corresponding Region object
regions = {
    'Plains of Avondale': plains_of_avondale,
    'The Northern Wasteland': northern_wasteland,
    'Dragon Back Mountains': dragon_back_mountains,
    'The Forgotten Forest': forgotten_forest,
    'Crystal River Marshes': crystal_river_marshes,
    'Hero\'s Graveyard': heros_graveyard,
    'Sitrel\'s Tomb': sitrels_tomb,
    'The Gozani Desert': gozani_desert,
    'Shores of the Endless Sea': shores_of_the_endless_sea,
    'Isles of Burgay': isles_of_burgay,
    'Drakken Castle': drakken_castle
}

# Creates user dictionary to keep track of user location & collected items
user = {
    'location': plains_of_avondale.name,
    'items': []
}

# Opening game message to player.
open_message = '''
Hello hero! You are all that stands between the realm being ruled forever
by the vicious Wizard King Slargon.

You are the last descendant of a powerful race of heroes who have protected
the realm for millennia.

The most powerful of your race was Sitrel who lived over 1000 years ago. He
fought against hordes and defeated the most powerful enemies of his day.
Upon his death, he transferred all of his power, might, and wisdom into his
sword, creating a powerful weapon for future generations of heroes to use to
vanquish evil. That sword is the only hope we have of defeating Slargon!

Sitrel's sword can only be wielded by one of the Hero's bloodline. It is held
in a magical chest in his tomb. The chest is locked with 6 locks that have to 
be opened by the 6 keys: The Dragon Scale Key, The Golden Key, The Bone Key,
The Crystal Key, The Wooden Key, and The Hero Key.

You must explore the realm of Cyrenia, collect the 6 keys to retrieve the
Sword of Sitrel and defeat Slargon. But, beware do not enter the region of
Drakken Casle to face Slargon before you have retrieved the keys to the
sword chest! You will be defeated and all hope will be lost!

Good luck brave hero!
'''

for letter in open_message:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)

input('Press ENTER/RETURN to begin your journey...')
print()
print()
print('You are currently in {}'.format(user['location']))


# defines the logic for the player movement
def player_movement(direction):
    current_location = regions[user['location']]
    if direction in ['north', 'south', 'east', 'west']:
        get_direction = getattr(current_location, direction)
        if get_direction is None:
            print('Sorry we cannot go that way! Let\'s try a different direction.')
            print()
        new_location = get_direction if get_direction is not None else user['location']
        print(new_location)
        inventory = [i for i in user['items'] if len(user['items']) > 0]
        print('Inventory: {}'.format(inventory))
        if regions[new_location].item:
            print('This region contains {}.'.format(regions[new_location].item))
        if regions[new_location].villain == True and len(user['items']) < 6:
            print('You have faced Slargon without the Sword of Citrel and have been defeatd!\n'
                  'GAME OVER')
            exit()
        return new_location


# parses user input to get various user commands
def get_player_command():
    get_command = True
    valid_commands = ['go north', 'go south', 'go east', 'go west', 'get key', 'exit']
    while get_command is True:
        player_command = input().strip().lower()
        parse_player_command = player_command.split()

        if player_command not in valid_commands:
            print('Invalid Command!')
            continue

        elif player_command == 'exit':
            exit()

        elif parse_player_command[0] == 'go':
            direction = parse_player_command[1]
            return direction

        elif player_command == 'get key':
            user['items'].append(regions[user['location']].item)
            print('{} is now in your travel sack.\nWhich way would you like to go from here?'.format(regions[user['location']].item))
            regions[user['location']].item = None
            if len(user['items']) == 6:
                print('CONGRATULATIONS!\n'
                      'You have collected all the keys, obtained the sword or Citrel,\n'
                      'and defeated Slargon!')
                exit()


while user['location']:
    user['location'] = player_movement(get_player_command())
