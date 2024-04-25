import sqlite3
import mysql.connector

class SQL:
    

    mydb = mysql.connector.connect(
        host = "localhost:3306",
        user="root",
        database="orders"

    )
    cursor = mydb.cursor()
    #TODO: talk about adding ingredients to database -> varying amout talk as group later
    #adds colums, and a sample recipe to database
    sql = "INSERT INTO RecipeDatabase (title, time, servings, difficulty, ingredients, backendIngredients, quantityWhole, quantityMass, quantityVolume, steps, tags) VALUES('Sample Recipe', 10, 5, 'Advanved', 'chopped food1', 'food1', 5, NULL, NULL, 3, NULL);"
    cursor = mydb.cursor(sql) 

    def __init__(self, title = 0, time = 0, servings = 0, difficulty = 0, ingredients = 0, backendIngredients = 0, quantityWhole = 0, quantityMass = 0, quantityVolume = 0, steps = 0, tags = 0) -> None:
        #add in the database
        sql = "USE orders; INSERT INTO RecipeDatabase (title, time, servings, difficulty, ingredients, backendIngredients, quantityWhole, quantityMass, quantityVolume, steps, tags) VALUES(" + title + ", " + time + ", " + servings +", " + difficulty + ", " + ingredients + ", " + backendIngredients + ", " + quantityWhole + ", " + quantityMass + ", " + quantityVolume + ", " + steps + ", " + tags + ");"
        

    def add(self, title = 0, time = 0, servings = 0, difficulty = 0, ingredients = 0, backendIngredients = 0, quantityWhole = 0, quantityMass = 0, quantityVolume = 0, steps = 0, tags = 0) -> None:
        sql = "USE orders; INSERT INTO RecipeDatabase (title, time, servings, difficulty, ingredients, backendIngredients, quantityWhole, quantityMass, quantityVolume, steps, tags) VALUES(" + title + ", " + time + ", " + servings +", " + difficulty + ", " + ingredients + ", " + backendIngredients + ", " + quantityWhole + ", " + quantityMass + ", " + quantityVolume + ", " + steps + ", " + tags + ");"
        
    def insert(self, column, value):
        pass

    def delete(self, row):
        pass

    def update(self, column, value):
        pass

    def select(self, column, value):
        pass
