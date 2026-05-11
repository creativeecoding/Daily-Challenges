
"""
Challenge: Oldest Person
Description: Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.
If multiple people share the oldest age, return all of their names in the order they appear in the input.
"""
def get_oldest(people):
    if not people:
        return []
        
    # Start by assuming the first person is the oldest
    oldest_age = people[0]["age"]
    oldest_names = [people[0]["name"]]
    
    # Check everyone else, starting from the second person
    for person in people[1:]:
        current_age = person["age"]
        current_name = person["name"]
        
        if current_age > oldest_age:
            oldest_age = current_age
            oldest_names = [current_name]
            
        elif current_age == oldest_age:
            oldest_names.append(current_name)
            
    return oldest_names
