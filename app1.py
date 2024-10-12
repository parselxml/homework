import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')

cook_book = {}

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    dish_name = lines[i].strip()
    i += 1
    ingredients_count = int(lines[i].strip())
    i += 1
    ingredients = []

    for j in range(ingredients_count):
        ingredients_data = lines[i].strip().split(' | ')
        ingredients_name, quantity, measure = ingredients_data
        ingredients.append({
            'ingredients_name': ingredients_name,
            'quantity': int(quantity),
            'measure': measure
        })
        i += 1

    cook_book[dish_name] = ingredients

    if i < len(lines):
        i += 1

pprint(cook_book)