import random

capitals = {"France": "Paris", "Germany": "Berlin", "Spain": "Madrid"}

country, correct_capital = random.choice(list(capitals.items()))

print(country)
user_input = input("The Capital: ")

if user_input == correct_capital:
    print("Correct")
    exit()
else:
    print("False")
    exit()