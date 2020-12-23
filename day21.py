#https://adventofcode.com/2020/day/21

import re
from collections import defaultdict

def countAppearances(allingredients, allcandidates):
    candidates = {}
    for allergenname, ingredientlist in allcandidates.items():
        candidates[allergenname] = set.intersection(*ingredientlist)

    return sum(allingredients.count(iteringredient) for iteringredient in set(allingredients).difference(set.union(*candidates.values())))

if __name__ == '__main__':    
    rule = re.compile("^((?:\w+ )+)\(contains (.*?)\)$")
    data = open("inputDay21.txt").read().splitlines()
    allcandidates = defaultdict(list)
    allingredients = []
    for line in data:
        ingredient, iterallingredient = rule.match(line).groups()

        ingredients = ingredient.strip().split(" ")
        allergens = iterallingredient.split(", ")

        for allergen in allergens:
            allcandidates[allergen].append(set(ingredients))

        allingredients.extend(ingredients)
        
    print(countAppearances(allingredients,allcandidates))
