#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_values = [recipe.values()]
  ingredient_values = [ingredients.values()]
  #turns the keys and values into a set of tuples
  recipe_tuple = {recipe.items()}
  ingredients_tuple = {ingredients.items()}
  #compare keys
  #return amount of batches able to make after comparing keys 
  if recipe['milk'] < ingredients['milk'] or recipe['butter'] < ingredients['butter'] or recipe['flour'] < ingredients['flour'] :
    if recipe_values.sort() == ingredients_values.sort():
    #math.gcd(recipe.get(recipe.values()),ingredients.get(ingredients.values())) == 0:
      return 0
    else:
      return math.gcd(recipe.get(milk),ingredients.get(milk)) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))