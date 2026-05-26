import json
import math

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

def calculate_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

