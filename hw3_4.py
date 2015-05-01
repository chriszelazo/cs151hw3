################################
#    Homework 3 - Problem 4    #
################################
# Chet Lemon (A10895241)       #
# Kesav Mulakaluri (A10616114) #
# Chris Zelazo (A10863450)     #
################################
import math
import pdb

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
	labelCounts = [0,0,0]
	for flower in flowers:
		labelCounts[int(flower.label-1)] += 1
		
	p1 = labelCounts[0] / float(len(flowers)) if len(flowers) != 0 else 0.0	# P(X=1)
	p2 = labelCounts[1] / float(len(flowers)) if len(flowers) != 0 else 0.0	# P(X=2)
	p3 = labelCounts[2] / float(len(flowers)) if len(flowers) != 0 else 0.0	# P(X=3)
	
	p1log = -(p1*math.log(p1)) if p1 != 0.0 else 0.0
	p2log = -(p2*math.log(p2)) if p2 != 0.0 else 0.0
	p3log = -(p3*math.log(p3)) if p3 != 0.0 else 0.0
	
	return p1log + p2log + p3log

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
# input: sum dahta [biglist], rule (feature, threshold)
# out: (feature, thresh, entropy, list1, list2)
def splitData(data, rule):
	pdb.set_trace()
	flists = [[],[],[],[]]
	# loop through the features
	feature = rule[0]
	
	flists[feature] = sorted(data, key=lambda x: x.vector[feature], reverse=True)	# sort data by feature

	threshold = rule[1]
	# split list
	list1 = []
	list2 = []
	for thingy in flists[feature]:
		if thingy.vector[feature] < threshold:
			list1.append(thingy)
		else:
			list2.append(thingy)
	
	return [list1, list2]		
	
	
def generateRules(data):
	flists = [[],[],[],[]]
	optimalSplits = [[],[],[],[]] # [[feature, thresh, entropy],[],[],[]]
	for feature in range(4):
		flists[feature] = sorted(data, key=lambda x: x.vector[feature], reverse=True)
		prevPoint = None
		for point in flists[feature]:
			if prevPoint != None:
				threshold = (flists[feature][0].vector[feature] + flists[feature][len(flists[feature])-1].vector[feature]) / 2.0#(point.vector[feature] + prevPoint.vector[feature]) / 2.0
				list1 = []
				list2 = []
				for thingy in flists[feature]:
					if thingy.vector[feature] < threshold:
						list1.append(thingy)
					else:
						list2.append(thingy)
				entropy = calcEntropy(list1) + calcEntropy(list2)
				if optimalSplits[feature] == [] or entropy < optimalSplits[feature][2]:
					optimalSplits[feature] = [feature, threshold, entropy]
			prevPoint = point
	
	optimalSplits.sort(key=lambda x: x[2], reverse=False)
	return optimalSplits


def buildTree(data, rules):
	if isPure(data) or len(rules) == 0:
		return Node(data, data[0].label, None, None, None)
	else:
		dopeSlicings = splitData(data, rules[0])
		zruke = rules.pop(0)
		pdb.set_trace()
		leftNode = None
		# recurse left
		if len(dopeSlicings[0]) > 0:
			leftNode = buildTree(dopeSlicings[0], rules)
			
		rightNode = None
		# recurse right
		if len(dopeSlicings[1]) > 0:
			rightNode = buildTree(dopeSlicings[1], rules)
			
		return Node(None, None, zruke, leftNode, rightNode)
		
rulez = generateRules(train)
print rulez
xXx420treeBlazeit420xXx = buildTree(train, rulez)


