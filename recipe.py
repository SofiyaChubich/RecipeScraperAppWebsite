class Recipe:
    def __init__(self, title, time, servings, diffuculty, ingredients, quantityWhole, quantityMass, quantityVolume, steps, tags):
        self.title = title
        self.time = time
        self.servings = servings
        self.difficulty = diffuculty
        self.ingredients = ingredients
        self.ingredients_backend_side = ingredients #TODO: finish and call method to set backend ingredients
        self.quantityWhole = quantityWhole
        self.quantityMass = quantityMass
        self.quantityVolume = quantityVolume
        self.steps = steps
        self.tags = tags
    
    def set_ingredients_backend_side(self, ingredients):
        self.ingredients_backend_side = ingredients



