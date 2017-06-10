import requests
import pygal
from pygal.style import Style
from operator import itemgetter

star_wars_characters = []

for page in range(1,88):
	# Error occurs, there is no page 17 on the http://swapi.co/api/people/
	# Skips over page 17 to avoid the error
	if page == 17:
		page += 1
	else:
		URL = ('http://swapi.co/api/people/' + str(page) + '/')
		r = requests.get(URL)
		star_wars_dict = r.json()

		star_wars_character = {
			'name': star_wars_dict['name'],
			'height': star_wars_dict['height'],
			'gender': star_wars_dict['gender'],
			'homeworld': star_wars_dict['homeworld'],
			'films': star_wars_dict['films'],
			'species': star_wars_dict['species']
			}
		star_wars_characters.append(star_wars_character)

star_wars_characters = sorted(star_wars_characters, key=itemgetter('name'))

my_config = pygal.Config(
	show_legend = False,
	title_font_size = 24,
	label_font_size = 14,
	major_label_font_size = 18,
	truncate_label = 15,
	show_y_guides = True)

chart = pygal.Bar(my_config)
chart.title = 'Height of Characters in The Star Wars Franchise'

for star_wars_character in star_wars_characters:
	if star_wars_character['height'] != 'unknown':
		chart.add(star_wars_character['name'], int(star_wars_character['height']))

chart.render_to_file('star_wars_heights.svg')




