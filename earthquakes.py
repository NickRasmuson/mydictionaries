'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''


import json

infile = open('eq_data.json')

# 1
earthquakes = json.load(infile)
count = 0

for i in (earthquakes)['features']:
    count += 1

print('the total number of earthquakes is :', count)

# 2
eq_dict = {}
for i in (earthquakes)['features']:
    if i['properties']['mag'] > 6:
        place = i['properties']['place']
        mag = i['properties']['mag']
        lon = i['geometry']['coordinates'][0]
        lat = i['geometry']['coordinates'][1]
        eq_dict[place] = [mag, lon, lat]

print(eq_dict)

# 3
for place in eq_dict:
    values = eq_dict[place]
    print(f"Location: {place}")
    print(f"Magnitude: {values[0]}")
    print(f"Longitude: {values[1]}")
    print(f"Latitude: {values[2]}")
    print()
    print()
