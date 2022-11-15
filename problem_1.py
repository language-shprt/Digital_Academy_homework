import json

# a) otevře soubor alice.txt.
with open('alice.txt', encoding='utf=8') as text_object:
    text_in_file = text_object.readlines()
print(text_in_file)

# b) spočítá četnost všech znaků (velká písmena považuje za malá, ignoruje mezery a znaky nového řádku).
text_in_file_no_blanks = [sentence.replace('\n', '').replace(' ', '') for sentence in text_in_file]
# print(text_in_file_no_blanks)

count_of_symbols = {}

for sentence in text_in_file_no_blanks:
    for s in sentence:
        if s.lower() in count_of_symbols.keys():
            count_of_symbols[s.lower()] += 1
        else:
            count_of_symbols[s.lower()] = 1


# d) volitelně: slovník je seřazen podle klíčů.
def sort_list_of_keys(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        pivot = list_to_sort[0]
        lesser_symbols = [symbol for symbol in list_to_sort[1:] if symbol < pivot]
        greater_symbols = [symbol for symbol in list_to_sort[1:] if symbol > pivot]
        return sort_list_of_keys(lesser_symbols) + [pivot] + sort_list_of_keys(greater_symbols)

list_of_keys_to_sort = [symbol for symbol in count_of_symbols.keys()]
count_of_symbols_sorted = {}
for key in sort_list_of_keys(list_of_keys_to_sort):
    count_of_symbols_sorted[key] = count_of_symbols[key]


# c) vytvoří soubor ukol1_output.json, který obsahuje slovník, kde klíče jsou znaky a hodnoty jejich četnost.
with open('ukol1_output.json', mode='w',encoding='utf-8') as jason_file:
    json.dump(count_of_symbols_sorted, jason_file, indent=2, ensure_ascii=False)