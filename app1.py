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


def get_shop_list_by_dishes(dishes: list, person_count: int):
    ingredients_ = {}
    for i in dishes:
        for j in cook_book[i]:
            ingredients_name_ = j['ingredients_name']
            measure_ = j['measure']
            quantity_ = j['quantity']

            if ingredients_name_ not in ingredients_:
                ingredients_[ingredients_name_] = {'measure': measure_, 'quantity': quantity_ * person_count}
            else:
                ingredients_[ingredients_name_]['quantity'] += quantity_ * person_count
    pprint(ingredients_)
    
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
