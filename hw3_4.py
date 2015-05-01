################################
#    Homework 3 - Problem 4    #
################################
# Chet Lemon (A10895241)       #
# Kesav Mulakaluri (A10616114) #
# Chris Zelazo (A10863450)     #
################################

class Flower:
	def __init__(self, vector, label):
		self.vector = vector
		self.label = label

with open("hw3test.txt") as f:
	test = [map(float, line.rstrip().split(' ')) for line in f]
	test = [Flower(l[:3], l[4]) for l in test]

with open("hw3train.txt") as f:
	train = [map(float, line.rstrip().split(' ')) for line in f]
	train = [Flower(l[:3], l[4]) for l in train]


print train[4].vector
print train[4].label
