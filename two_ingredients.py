from recipe import Recipe
import pickle
import inflect 

with open('ScrapedRecipes/all_recipes.pickle', 'rb') as f:
    recipes = pickle.load(f)

temp_recipes = recipes
recipes = []

for item in temp_recipes:
    if item is not None:
        recipes.append(item)

foods = set(x.strip().lower() for x in open('raw_data/backend_food_names.txt', 'r+').readlines())


## Convert all plural nouns to singular, reduces ingredients that need to be entered into food names
def plural_to_singular(ingredients):
    p = inflect.engine()
    new_ingredients = []
    for ingredient in ingredients:
        ingredient = ingredient.strip().replace(',', '').replace('*', '').replace('\xa0', ' ').replace(';', '').replace('"', '').replace('/', ' ').replace('.', '')
        ## Handle parentheses later
        singular_phrase = []
        for word in ingredient.split(' '):
            word = word.strip()
            if word:
                singular = p.singular_noun(word)

            if singular is not False:
                singular_phrase.append(singular)
            else:
                singular_phrase.append(word)
        new_ingredients.append(" ".join(singular_phrase).lower())
    return new_ingredients


def get_ingredients(recipe):
    matches = []
    for ingredient in recipe.ingredients:
        temp = []
        duplicates = []
        for food in foods:
            if food in ingredient and len(set(food.split(' ')).intersection(set(ingredient.split(' ')))) == len(food.split(' ')):
                    duplicate = False
                    for previous in temp:
                        if food in previous:
                            duplicate = True
                        if previous in food:
                            duplicates.append(previous)
                    if not duplicate:
                        temp.append(food)

        for item in duplicates:
            if item in temp:
                temp.remove(item)
        
        ## Edge case with garlic
        
        if 'garlic' in temp:
            if 'clove' in temp:
                temp.remove('clove')
            if 'cloves' in temp:
                temp.remove('cloves')

        if len(temp) == 0:
            if 'water' in set(ingredient.split(' ')) or 'ice' in set(ingredient.split(' ')) or 'cooking spray' in ingredient:
                continue
            elif 'recipe follow' in ingredient:
                continue
            else:
                with open('raw_data/unknown_ingredients.txt', 'a') as f:
                    f.write('no ingredient ' + ingredient + '\n')
        ##if len(temp) == 1 and ('and' in ingredient or 'or' in ingredient):
            ##with open('raw_data/unknown_ingredients.txt', 'a') as f:
                ##f.write('and or ingredient ' + ingredient + ' ' + ' '.join(temp) + '\n')
        ##if len(temp) > 1:
            ##with open('raw_data/unknown_ingredients.txt', 'a') as f:
                ##f.write('multiple ingredient ' + ingredient + ' ' + ' '.join(temp) + '\n')
        for x in temp:
            matches.append(x)
    return matches

# recipe.ingredients = plural_to_singular(recipe.ingredients)
# print(get_ingredients(recipe))

print(len(recipes))

for x in range(10000):
    recipe = recipes[x]
    recipe.ingredients = plural_to_singular(recipe.ingredients)
    get_ingredients(recipe)