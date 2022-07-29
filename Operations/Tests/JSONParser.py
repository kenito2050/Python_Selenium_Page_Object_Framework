import json

# Opening JSON file
f = open('basefile.json', )
g = open('.report.json', )
# returns JSON object as
# a dictionary
data = json.load(f)
#pruebarray = {'line': 2, 'elements': [{'line': 5, 'name': 'QTML-T1', 'description': '', 'id': 'feature-file-to-update-the-status-in-jira;title-of-your-scenario1', 'status': 'Pass', 'type': 'scenario', 'keyword': 'Scenario', 'steps': [{'result': {'duration': 70570701, 'status': 'passed'}}]}], 'name': 'CRD Smoke Test', 'description': '', 'id': 'feature-file-to-update-the-status-in-jira', 'status': 'Pass', 'keyword': 'Feature', 'uri': 'Demo.feature', 'tags': [{'line': 1, 'name': '@demo'}]}
temporal = data
data2 = json.load(g)
#print(data2)
# Iterating through the json
# list
#temporal['line'] = "25"
print("Length DATAOr = ", len(temporal["elements"]))

x = temporal['elements']
x[0]['name'] = "test"
xvar = x
totalTest = len(data2["tests"])
totalBase = len(temporal["elements"])
total = totalBase - totalTest

for i in range(total):
    temporal['elements'].pop()

print("Length DATAloop = ", len(temporal["elements"]))

i = 0
for i in range(totalTest):
    tcname = data2["tests"][i]['nodeid']
    tcname1= tcname.split('::test_')
    temporal["elements"][i]['name'] = tcname1[1]
    temporal["elements"][i]['status'] = data2["tests"][i]['outcome']
    temporal["elements"][i]['steps'][0]['result']['status'] = data2["tests"][i]['outcome']

json.dumps(temporal, indent=4, separators=(". ", " = "))

with open('SmokeTest.json', 'w') as outfile:
    json.dump(temporal, outfile, indent=4)

with open('SmokeTest.json', 'a') as outfile:
    outfile.write("\n]")

with open("SmokeTest.json") as outfile:
    lines = outfile.readlines()  # read
# modify
lines[0] = "[\n{\n"  # you can replace zero with any line number.
with open("SmokeTest.json", "w") as outfile:
    outfile.writelines(lines)  # write back

# Closing file
f.close()
g.close()