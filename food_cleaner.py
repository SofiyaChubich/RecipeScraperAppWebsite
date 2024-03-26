'''
    method to clean up umbrealla food txt files
'''
def clean_umbrella_foods(filename):
    dirty_food = open(filename, 'r+').readlines()
    clean_food = open('cleaned_' + filename, "a")
    for food in range(len(dirty_food) - 1):
        current_food = dirty_food[food]
        if "[" in current_food:
            current_food = current_food[:current_food.find("[")]
            current_food.strip()
            clean_food.write(current_food + "\n")
        elif ",,,,,," == current_food:
            dirty_food.remove(current_food)
            food -= 1
        else:
            current_food = current_food[:current_food.find(",,,,,,")]
            current_food.strip()
            clean_food.write(current_food + "\n")
    clean_food.close()

'''
    create methods to convert time to minutes to keep constent on backend
    and method to go from minutes to hours for front end
    '''
def time_to_minutes(self):
    for time in self.time:
        if "hr" in time:
            time.lower()
            split_index = time.index("hr")
            hr = time[:split_index - 1].strip()
            min = time[split_index + 2:].strip()
            time = int(hr)*60 + int(min)

def minutes_to_time(self):
    for time in self.time:
        if time > 60:
            hr = int(time/60)
            min = int(time%60)
            time = hr + " hr " + min + " min"

    '''TODO: translate the ingredients to a simplified version for backend calculations
        use this food vocab word list to match with food typee https://www.oxfordlearnersdictionaries.com/us/topic/food 
        return list of tuples (quantity, ingredient)

        currently not time efficient -> look for more efficient way later
    '''
def ingredients_to_backed(self, ingredients):
    foods = open('backend_food_names.txt', "r").readlines()
    backend_ingredients = []
    unkown_foods = open('unkonwn_foods.txt', "a")
    for ingredient in ingredients:
        actual_food = ""
        actual_quantity = 0
        for food in foods:
            if food in ingredient:
                actual_food = food
            else:
                unkown_foods.write(ingredient + "\n")


    #TODO: create method within Recipe to convert 
    #     ingerdients from list to dictionary {amount:ingredient}
def ingredient_to_dict(self, ingredients):
    pass
    
    #TODO: sort backend_food_names in order of size

clean_umbrella_foods('cider_apples.txt')