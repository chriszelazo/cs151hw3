################################
#    Homework 3 - Problem 4    #
################################
# Chet Lemon (A10895241)       #
# Kesav Mulakaluri (A10616114) #
# Chris Zelazo (A10863450)     #
################################
import math

class Flower:
	def __init__(self, vector, label):
		self.vector = vector
		self.label = label
		
class Node:
	# ctor input:
		# data: list of Flower objects in the node
		# label: set to None for non-leaf nodes
		# left/right: left/right child (Node obj)
	def __init__(self, data, label, rule, left, right):
		self.data = data
		self.label = label
		self.rule = rule
		self.left = left
		self.right = right
		

with open("hw3test.txt") as f:
	test = [map(float, line.rstrip().split(' ')) for line in f]
	test = [Flower(l[:4], l[4]) for l in test]

with open("hw3train.txt") as f:
	train = [map(float, line.rstrip().split(' ')) for line in f]
	train = [Flower(l[:4], l[4]) for l in train]

# Calculates entropy given a list of flower objects
# jizzes out a float
def calcEntropy(flowers):
	print flowers
	labelCounts = [0,0,0]
	for flower in flowers:
		labelCounts[int(flower.label-1)] += 1
		
	p1 = labelCounts[0] / float(len(flowers))  	# P(X=1)
	p2 = labelCounts[1] / float(len(flowers))	# P(X=2)
	p3 = labelCounts[2] / float(len(flowers))	# P(X=3)
	
	if p1 == 0.0:
		entropy = - (p2*math.log(p2)) - (p3*math.log(p3))
	elif p2 == 0.0:
		entropy = -(p1*math.log(p1)) - (p3*math.log(p3))
	elif p3 == 0.0:
		entropy = -(p1*math.log(p1)) - (p2*math.log(p2))
	else:
		entropy = -(p1*math.log(p1)) - (p2*math.log(p2)) - (p3*math.log(p3))  
		
	return entropy

# isPure
# checks if a node is pure (contains only one label)
def isPure(data):
	labelCounts = [0,0,0]
	for flower in data:
		labelCounts[int(flower.label-1)] += 1
		
	if labelCounts[0] == len(data) or labelCounts[1] == len(data) or labelCounts[2] == len(data):
		return True
	else:
		return False

# splitData
# input: sum dahta [biglist]
# out: (feature, thresh, entropy, list1, list2)
def splitData(data):
	flists = [[],[],[],[]]
	optimalSplit = None		# (feature, thresh, entropy, list1, list2)
	# loop through the features
	for feature in range(4):
		flists[feature] = sorted(data, key=lambda x: x.vector[feature], reverse=True)	# sort data by feature
		# loop through each point
		prevPoint = None
		for point in flists[feature]:
			if prevPoint != None:
				threshold = abs(point.vector[feature] - prevPoint.vector[feature]) / 2.0
				
				# split list
				list1 = []
				list2 = []
				for thingy in flists[feature]:
					if thingy.vector[feature] < threshold:
						list1.append(thingy)
					else:
						list2.append(thingy)
				print list1, list2
				entropy = calcEntropy(list1) + calcEntropy(list2)
				if optimalSplit == None or entropy < optimalSplit[2]:
					optimalSplit = (feature, threshold, entropy, list1, list2)
				
			prevPoint = point
			
	return optimalSplit
	
# buildTree: recursive
# pass the data and a tree shall rise
def buildTree(data):
	if isPure(data): 
		return Node(data, data[0].label, None, None, None)
	else:
		# split data
		dopeSlicings = splitData(data)
		# recurse left
		leftNode = buildTree(dopeSlicings[3])
		# recurse right
		rightNode = buildTree(dopeSlicings[4])
		
		return Node(None, None, dopeSlicings, leftNode, rightNode)

print buildTree(train)