#Spawns at xx:52:18. The latlong is 49.2876934728628, -123.11289583358442. SpawnId is 54867182cf1. top
#Spawns at xx:21:6. The latlong is 49.28763112411022, -123.11281358494877. SpawnId is 54867182cf3. rightmost
#Spawns at xx:1:39. The latlong is 49.28749777228661, -123.11295152830226. SpawnId is 54867182c61. lowest
from collections import Counter
from datetime import datetime
import sqlite3
import pdb
import operator

class PokeSpawn(object):
	def __init__(self, name, expiry_time):
		self.name = name
		self.expiry_time = expiry_time
poke_dict = { 1: 'Bulbasaur', 2: 'Ivysaur', 3: 'Venusaur', 4: 'Charmander', 5: 'Charmeleon', 6: 'Charizard', 7: 'Squirtle', 8: 'Wartortle', 9: 'Blastoise', 10: 'Caterpie', 11: 'Metapod', 12: 'Butterfree', 13: 'Weedle', 14: 'Kakuna', 15: 'Beedrill', 16: 'Pidgey', 17: 'Pidgeotto', 18: 'Pidgeot', 19: 'Rattata', 20: 'Raticate', 21: 'Spearow', 22: 'Fearow', 23: 'Ekans', 24: 'Arbok', 25: 'Pikachu', 26: 'Raichu', 27: 'Sandshrew', 28: 'Sandslash', 29: 'Nidoran(F)', 30: 'Nidorina', 31: 'Nidoqueen', 32: 'Nidoran(M)', 33: 'Nidorino', 34: 'Nidoking', 35: 'Clefairy', 36: 'Clefable', 37: 'Vulpix', 38: 'Ninetales', 39: 'Jigglypuff', 40: 'Wigglytuff', 41: 'Zubat', 42: 'Golbat', 43: 'Oddish', 44: 'Gloom', 45: 'Vileplume', 46: 'Paras', 47: 'Parasect', 48: 'Venonat', 49: 'Venomoth', 50: 'Diglett', 51: 'Dugtrio', 52: 'Meowth', 53: 'Persian', 54: 'Psyduck', 55: 'Golduck', 56: 'Mankey', 57: 'Primeape', 58: 'Growlithe', 59: 'Arcanine', 60: 'Poliwag', 61: 'Poliwhirl', 62: 'Poliwrath', 63: 'Abra', 64: 'Kadabra', 65: 'Alakazam', 66: 'Machop', 67: 'Machoke', 68: 'Machamp', 69: 'Bellsprout', 70: 'Weepinbell', 71: 'Victreebel', 72: 'Tentacool', 73: 'Tentacruel', 74: 'Geodude', 75: 'Graveler', 76: 'Golem', 77: 'Ponyta', 78: 'Rapidash', 79: 'Slowpoke', 80: 'Slowbro', 81: 'Magnemite', 82: 'Magneton', 83: 'Farfetch\'d', 84: 'Doduo', 85: 'Dodrio', 86: 'Seel', 87: 'Dewgong', 88: 'Grimer', 89: 'Muk', 90: 'Shellder', 91: 'Cloyster', 92: 'Gastly', 93: 'Haunter', 94: 'Gengar', 95: 'Onix', 96: 'Drowzee', 97: 'Hypno', 98: 'Krabby', 99: 'Kingler', 100: 'Voltorb', 101: 'Electrode', 102: 'Exeggcute', 103: 'Exeggutor', 104: 'Cubone', 105: 'Marowak', 106: 'Hitmonlee', 107: 'Hitmonchan', 108: 'Lickitung', 109: 'Koffing', 110: 'Weezing', 111: 'Rhyhorn', 112: 'Rhydon', 113: 'Chansey', 114: 'Tangela', 115: 'Kangaskhan', 116: 'Horsea', 117: 'Seadra', 118: 'Goldeen', 119: 'Seaking', 120: 'Staryu', 121: 'Starmie', 122: 'Mr. Mime', 123: 'Scyther', 124: 'Jynx', 125: 'Electabuzz', 126: 'Magmar', 127: 'Pinsir', 128: 'Tauros', 129: 'Magikarp', 130: 'Gyarados', 131: 'Lapras', 132: 'Ditto', 133: 'Eevee', 134: 'Vaporeon', 135: 'Jolteon', 136: 'Flareon', 137: 'Porygon', 138: 'Omanyte', 139: 'Omastar', 140: 'Kabuto', 141: 'Kabutops', 142: 'Aerodactyl', 143: 'Snorlax', 144: 'Articuno', 145: 'Zapdos', 146: 'Moltres', 147: 'Dratini', 148: 'Dragonair', 149: 'Dragonite', 150: 'Mewtwo', 151: 'Mew', }
def get_pokes(conn):
	"This function retrieves pokemon from your db file"
	c = conn.cursor()
	sql = 'SELECT pokemon_id, datetime(strftime("%s", disappear_time) - 7 * 60 * 60, "unixepoch") from pokemon where spawnpoint_id = "54867182cf1" OR spawnpoint_id = "54867182cf3" OR spawnpoint_id = "54867182c61" order by disappear_time desc'
	c.execute(sql)
	result = c.fetchall()
	#pdb.set_trace()
	names = [poke_dict[poke_data[0]] for poke_data in result]
	occurrences = Counter(names)
	occurDict = sorted(dict(occurrences).items(), key=lambda x: x[1], reverse=True)
	pokespawns = []
	i = 0
	while (i < 5):
		pokemon = result[i]
		name = poke_dict[pokemon[0]]
		time = datetime.strptime(pokemon[1], '%Y-%m-%d %H:%M:%S')
		pokespawns.append(PokeSpawn(name, time))
		print "{} {}".format(name, time)
		i = i+1
	return pokespawns

def get_occur_dict(conn):
	"something"
	c = conn.cursor()
	sql = 'SELECT pokemon_id, datetime(strftime("%s", disappear_time) - 7 * 60 * 60, "unixepoch") from pokemon where spawnpoint_id = "54867182cf1" OR spawnpoint_id = "54867182cf3" OR spawnpoint_id = "54867182c61" order by disappear_time desc'
	c.execute(sql)
	result = c.fetchall()
	#pdb.set_trace()
	names = [poke_dict[poke_data[0]] for poke_data in result]
	occurrences = Counter(names)
	occurDict = sorted(dict(occurrences).items(), key=lambda x: x[1], reverse=True)
	return occurDict

# c = conn.cursor()
# sql = 'SELECT pokemon_id, datetime(strftime("%s", disappear_time) - 7 * 60 * 60, "unixepoch") from pokemon where spawnpoint_id = "54867182cf1" OR spawnpoint_id = "54867182cf3" OR spawnpoint_id = "54867182c61" order by disappear_time desc'
# c.execute(sql)
# result = c.fetchall()
# pdb.set_trace()
# names = [poke_dict[poke_data[0]] for poke_data in result]
# occurrences = Counter(names)
# occurDict = sorted(dict(occurrences).items(), key=lambda x: x[1], reverse=True)
# #pdb.set_trace()
# pokespawns = []
# i = 0
# while (i < 5):
# 	#pdb.set_trace()
# 	pokemon = result[i]
# 	name = poke_dict[pokemon[0]]
# 	time = pokemon[1]
# 	pokespawns.append(PokeSpawn(name, time))
# 	print "{} {}".format(name, time)
# 	i = i+1
# #pdb.set_trace()
	