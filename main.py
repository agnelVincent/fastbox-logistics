import json
import math

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

def calculate_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)


agent_report = {}

for package in data['packages']:
    distances = {}
    for agent in data['agents']:
        distances[agent] = calculate_distance(data['warehouses'][package['warehouse']], data['agents'][agent])
    nearest_agent = min(distances,key = lambda i : distances[i])
    if not agent_report.get(nearest_agent):
        agent_report[nearest_agent] = {'packages_delivered' : 1, 
                                       }
    else:
        agent_report[nearest_agent]['packages_delivered'] += 1
    
print(agent_report)