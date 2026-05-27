import json
import math

with open('data.json', 'r') as file:
    data = json.load(file)

def calculate_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

agent_report = {
    agent : {
        'packages_delivered' : 0,
        'total_distance' : 0
    } for agent in data['agents']
}


for package in data['packages']:
    distances = {}
    for agent in data['agents']:
        distances[agent] = calculate_distance(data['warehouses'][package['warehouse']], data['agents'][agent])
    nearest_agent = min(distances,key = lambda i : distances[i])

    agent_report[nearest_agent]['packages_delivered'] += 1
    agent_report[nearest_agent]['total_distance'] += distances[nearest_agent] + calculate_distance(data['warehouses'][package['warehouse']],package['destination'])
    

for agent in agent_report:
    agent_report[agent]['total_distance'] = round(
        agent_report[agent]['total_distance'], 2
    )

    agent_report[agent]['efficiency'] = round(
        agent_report[agent]['total_distance'] / agent_report[agent]['packages_delivered'], 2
    )


best_agent = min(
    agent_report,
    key = lambda agent : agent_report[agent]['efficiency']
    if agent_report[agent]['packages_delivered'] > 0
    else float('inf')
)

agent_report['best_agent'] = best_agent


print(agent_report)