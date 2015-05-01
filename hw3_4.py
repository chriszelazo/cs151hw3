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
		labelCounts[int(flower.label-1)]
		
	p1 = labelCounts[0] / float(len(flowers))  	# P(X=1)
	p2 = labelCounts[1] / float(len(flowers))	# P(X=2)
	p3 = labelCounts[2] / float(len(flowers))	# P(X=3)
	
	# entropy eqn
	return -(p1*math.log(p1)) - (p2*math.log(p2)) - (p2*math.log(p3))