"""
Collects specified data about all films form the database, changes format, saves the result as a json file.
"""

# Načte soubor.

import json

with open('netflix_titles.tsv', encoding='utf-8') as text_object:
    input_data = text_object.readlines()

full_info_about_films = [film_description.split('\t') for film_description in input_data]
column_names = full_info_about_films[0]
info_about_films = full_info_about_films[1:]


# Vezme z něj údaje, které zadáme.

what_we_want = ['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR'] # just in case we want some other info later
what_we_want_with_index = {}
for title in column_names:
    if title in what_we_want:
        what_we_want_with_index[title] = column_names.index(title)

info_about_films_to_json = []

def item_with_one_detail(name_from_table):
    index = what_we_want_with_index[name_from_table]
    return movie_description[index]
    
def item_with_several_details(name_from_table):
    index = what_we_want_with_index[name_from_table]
    if len(movie_description[index]) > 0:
        return movie_description[index].split(',')
    else: return []

def year_to_decade(name_from_table):
    index = what_we_want_with_index[name_from_table]
    year = int(movie_description[index])
    decade = (year // 10) * 10
    return  decade

for movie_description in info_about_films:
    description_dictionary = {}
    
    description_dictionary['title'] = item_with_one_detail('PRIMARYTITLE')
    description_dictionary['directors'] = item_with_several_details('DIRECTOR')
    description_dictionary['cast'] = item_with_several_details('CAST')
    description_dictionary['genres'] = item_with_several_details('GENRES')
    description_dictionary['decade'] = year_to_decade('STARTYEAR')

    info_about_films_to_json.append(description_dictionary)


# Vytvořený seznam slovníků uloží do souboru movies.json.

with open('movies.json', mode='w', encoding='utf-8') as json_file:
    json.dump(info_about_films_to_json, json_file, indent=4, ensure_ascii=False)