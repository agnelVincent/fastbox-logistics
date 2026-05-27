import json
import math
import csv


file_name = input("Enter JSON file name: ")

with open(file_name, 'r') as file:
    data = json.load(file)


#Euclidean formula
def calculate_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)


#Initializing empty agent report dictionary
agent_report = {
    agent : {
        'packages_delivered' : 0,
        'total_distance' : 0
    } for agent in data['agents']
}


for package in data['packages']:
    distances = {}
    warehouse_location = data['warehouses'][package['warehouse']]
    for agent in data['agents']:
        distances[agent] = calculate_distance(warehouse_location, data['agents'][agent])
    nearest_agent = min(distances,key = lambda i : distances[i]) #Finding the nearest agent to the warehouse

    agent_report[nearest_agent]['packages_delivered'] += 1
    agent_report[nearest_agent]['total_distance'] += distances[nearest_agent] + calculate_distance(warehouse_location, package['destination'])
    #Summed the distance from warehouse to agent location with the distance from warehouse to destination
    

#Calculated the efficiency and rounded the figures
for agent in agent_report:
    agent_report[agent]['total_distance'] = round(
        agent_report[agent]['total_distance'], 2
    )

    if agent_report[agent]['packages_delivered'] > 0:
        agent_report[agent]['efficiency'] = round(
            agent_report[agent]['total_distance'] /
            agent_report[agent]['packages_delivered'],
            2
        )
    else:
        agent_report[agent]['efficiency'] = 0

#Found the best agent
best_agent = min(
    agent_report,
    key = lambda agent : agent_report[agent]['efficiency']
    if agent_report[agent]['packages_delivered'] > 0
    else float('inf')
)

agent_report['best_agent'] = best_agent

#Exporting top performer details to CSV
with open('top_performer.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    #CSV column headings
    writer.writerow([
        'Agent',
        'Packages Delivered',
        'Total Distance',
        'Efficiency'
    ])

    #Top performer data
    writer.writerow([
        best_agent,
        agent_report[best_agent]['packages_delivered'],
        agent_report[best_agent]['total_distance'],
        agent_report[best_agent]['efficiency']
    ])




#Saved the agent report to report.json
with open('report.json', 'w') as file:
    json.dump(agent_report,file, indent=4)