# Initial Examples

import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = range(1, 11)

for rando in my_randoms:
    the_numbers_match = True

print(f'{rando} is in the random list')

# Practice: Planet List

planet_list = ["Mercury", "Mars"]

x = ["Jupiter", "Saturn"]

planet_list.append(x)
# planet_list.append("Saturn")
planet_list.extend(x)

planet_list.insert(3, "Venus")
planet_list.insert(5, "Earth")

planet_list.append("pluto")

# WTF is a SLICE?!
# planet_list
rocky_planets = slice(0,2)

# print(f'Planet List:::{planet_list}, Rocky Planets{rocky_planets}')

print(planet_list[rocky_planets])

print(f'Rocky Planets {planet_list[rocky_planets]} and Planet List {planet_list}')

del planet_list[7]

print(planet_list)