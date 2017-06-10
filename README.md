# Star Wars
Using a Star Wars API to visualize information of the characters of the Star Wars Universe.

## Example Code
```python
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
```

## Visual of The Graph
![alt text](https://cdn.rawgit.com/ryanc20/star-wars-data/8414289b/star_wars_heights.svg "Star Wars Heights")
__Note:__ the graphic does not show the characters' names, just know that Yoda is the small one. The .svg file does show names, but I did not want to use an x-axis label because, frankly, it looked bad.

## Motivation
I love the Star Wars universe and thought it would be a fantastic starting point for practicing data visualization using python. I plan to get more exposure to extracting information and using the data to create meaningful visualizations and observations.

## API Reference
I used The Star Wars API: [SWAPI](https://swapi.co/), "The Star Wars API is the world's first quantified and programmatically-formatted set of Star Wars data."
