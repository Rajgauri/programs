import Node

data = [[]]
f = open('tennistestset.csv')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'outlook': {'rainy': {'temperature': {'mild': {'humidity': {'high': {'windy': {'TRUE': 'no', 'FALSE': 'yes'}}, 'normal': 'yes'}}, 'cool': {'humidity': {'normal': {'windy': {'TRUE': 'no', 'FALSE': 'yes'}}}}}}, 'overcast': 'yes', 'sunny': {'temperature': {'hot': 'no', 'mild': {'humidity': {'high': 'no', 'normal': 'yes'}}, 'cool': 'yes'}}}}
attributes = ['outlook', 'temperature', 'humidity', 'windy', 'play']
count = 0
for row in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.value)
		value = row[index]
		if(value in tempDict.keys()):
			child = Node.Node(value, tempDict[value])
			result = tempDict[value]
			tempDict = tempDict[value]
		else:
			print "Error in input %s" % count
			result = "?"
			break
	print ("Test case %s = %s" % (count, result))
