import math

def find(object, list):
    for i in list:
        if object(i): 
            return True
        else:
            return False

#return most common value for an attribute
def maximum(attributes, data, target):
    
    frequency = {}
    #find target in data
    index = attributes.index(target)
    #calculate frequency of values in target attributes
    for tuple in data:
        if (frequency.has_key(tuple[index])):
            frequency[tuple[index]] += 1 
        else:
            frequency[tuple[index]] = 1
    max = 0
    major = ""
    for key in frequency.keys():
        if frequency[key]>max:
            max = frequency[key]
            major = key
    return major

#Calculates the entropy
def entropy(attributes, data, targetAttr):

    frequency = {}
    dataEntropy = 0.0
   
    i = 0
    for entry in attributes:
        if (targetAttr == entry):
            break
        ++i
    
    # Calculate the frequency of each of the values in the target attribute
    for entry in data:
        if (frequency.has_key(entry[i])):
            frequency[entry[i]] += 1.0
        else:
            frequency[entry[i]]  = 1.0

    # Calculate the entropy of the data for the target attribute
    for freq in frequency.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
    return dataEntropy

def gain(attributes, data, attr, targetAttr):

    frequency = {}
    subsetEntropy = 0.0
    
    #find index of the attribute
    i = attributes.index(attr)

    # Calculate the frequency of each of the values in the target attribute
    for entry in data:
        if (frequency.has_key(entry[i])):
            frequency[entry[i]] += 1.0
        else:
            frequency[entry[i]]  = 1.0
    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occurance in the training set.
    for val in frequency.keys():
        valProb        = frequency[val] / sum(frequency.values())
        dataSubset     = [entry for entry in data if entry[i] == val]
        subsetEntropy += valProb * entropy(attributes, dataSubset, targetAttr)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy(attributes, data, targetAttr) - subsetEntropy)

#choose best attibute 
def returnbestattr(data, attributes, target):
    best = attributes[0]
    maxGain = 0;
    for attr in attributes:
        newGain = gain(attributes, data, attr, target) 
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    return best

#get values in the column of the given attribute 
def getValues(data, attributes, attr):
    index = attributes.index(attr)
    values = []
    for entry in data:
        if entry[index] not in values:
            values.append(entry[index])
    return values

def getExamples(data, attributes, best, val):
    examples = [[]]
    index = attributes.index(best)
    for entry in data:
        #find entries with the give value
        if (entry[index] == val):
            newEntry = []
            #add value if it is not in best column
            for i in range(0,len(entry)):
                if(i != index):
                    newEntry.append(entry[i])
            examples.append(newEntry)
    examples.remove([])
    return examples

def buildtree(data, attributes, target, recursion):
    recursion += 1
    
    data = data[:]
    vals = [rows[attributes.index(target)] for rows in data]
    default = maximum(attributes, data, target)

    if not data or (len(attributes) - 1) <= 0:
        return default

    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        best = returnbestattr(data, attributes, target)
        tree = {best:{}}

        for val in getValues(data, attributes, best):
            
            examples = getExamples(data, attributes, best, val)
            newAttr = attributes[:]
            newAttr.remove(best)
            subtree = buildtree(examples, newAttr, target, recursion)

            tree[best][val] = subtree
    
    return tree

