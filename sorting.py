from recipe import Recipe
import pickle
import re

## This file cleans up the title, servings, difficulty, and steps component of the recipe object

def cleanup_title(recipe):
    if recipe is not None:
        return recipe.title.strip()

def cleanup_servings(recipe):
    if recipe is not None:
        numbers = re.findall('\d+\.\d+|\d+', recipe.servings)
        if len(numbers) >= 1:
            return float(numbers[0])
        else:
            return None

def cleanup_difficulty(recipe):
    if recipe is not None:
        if re.search("Easy", recipe.difficulty):
            return "Easy"
        elif re.search("Intermediate", recipe.difficulty):
            return "Intermediate"
        elif re.search("Advanced", recipe.difficulty):
            return "Advanced"
        else:
            return "No Difficulty"

def cleanup_steps(recipe):
    if recipe is not None:
        new_steps = []
        for line in recipe.steps:
            new_steps.append(line.strip())
        return new_steps
