
"""
Challenge: Allergen Friendly Meals
Description: Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.
Each meal is in the format [meal, allergens], where meal is the name of the meal and allergens is an array of the allergens the meal contains.
Return safe meal names in the same order given. If no meal is safe, return an empty array.
"""
def get_allergen_friendly_meals(meals, allergens):
    safe_meals = []
    
    for meal_name, meal_allergens in meals:
        is_safe = True
        
        # Check if any of the meal's allergens are in the avoid list
        for allergen in meal_allergens:
            if allergen in allergens:
                is_safe = False
                break 
                
        if is_safe:
            safe_meals.append(meal_name)
            
    return safe_meals
