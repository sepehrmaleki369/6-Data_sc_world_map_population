import json
import pygal
from pygal import style
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from country_codes import get_country_code


filename = 'worldpopulation.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}

for pop_dict in pop_data:

    country_name = pop_dict['country']
    population = int(float(pop_dict['population']))

    code = get_country_code(country_name)
    if code:
        # print(code + " " + str(population))
        cc_populations[code] = population

    elif country_name == 'Iran':
        cc_populations['ir'] = population

    elif country_name == 'Russia':
        cc_populations['ru'] = population
    
    else:
        print("ERROR" +" "+  country_name)

# group countries into 3 population levels.

cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    # print(cc,pop)
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = pygal.maps.world.World()

# change color style    with hex format
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style = wm_style)

wm.title = "world populations, country by country"
wm.add( '0-10,',cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_pop.svg')
    
