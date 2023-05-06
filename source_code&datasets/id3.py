import decisiontree

def main():
   
    file = open('tennistrainset.csv')

    target = "play"
    data = [[]]
    for row in file:
        row = row.strip("\r\n")
        data.append(row.split(','))
    data.remove([])
    attributes = data[0]
    data.remove(attributes)
    #Generate decision tree using ID3 algorithm
    tree = decisiontree.buildtree(data, attributes, target, 0)
   
    #start writing into output file(output.py)
    file = open('output.py', 'w')
    file.write("import Node\n\n")
    file.write("data = [[]]\n")
    file.write("f = open('tennistestset.csv')\n")
    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tdata.append(line.split(','))\n")
    file.write("data.remove([])\n")
    file.write("tree = %s\n" % str(tree))
    file.write("attributes = %s\n" % str(attributes))
    file.write("count = 0\n")
    file.write("for row in data:\n")
    file.write("\tcount += 1\n")
    file.write("\ttempDict = tree.copy()\n")
    file.write("\tresult = \"\"\n")
    file.write("\twhile(isinstance(tempDict, dict)):\n")
    file.write("\t\troot = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
    file.write("\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
    file.write("\t\tindex = attributes.index(root.value)\n")
    file.write("\t\tvalue = row[index]\n")
    file.write("\t\tif(value in tempDict.keys()):\n")
    file.write("\t\t\tchild = Node.Node(value, tempDict[value])\n")
    file.write("\t\t\tresult = tempDict[value]\n")
    file.write("\t\t\ttempDict = tempDict[value]\n")
    file.write("\t\telse:\n")
    file.write("\t\t\tprint \"Error in input %s\" % count\n")
    file.write("\t\t\tresult = \"?\"\n")
    file.write("\t\t\tbreak\n")
    file.write("\tprint (\"Test case %s = %s\" % (count, result))\n")
   
    
if __name__ == '__main__':
    main()
