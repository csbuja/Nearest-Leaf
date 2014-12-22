import math
def leftChild(i):
	return i*2+1
def rightChild(i):
	return i*2+2

def parent(i):
	if i%2==0: 
		return int(math.floor(i-1)/2)
	else:
	 	return int(math.floor(i)/2)

def nodeExists(i,bt):
	return (i<= len(bt)-1 ) and bt[i]!= None
#returns a tuple of value and distance for the nearest root
def findDown(currPos,bt):
	distanceCL = 999999999999999999 #don't remember syntax for max
	closestLeafI = -1
	stack = [(currPos,0)]

	while len(stack) != 0: 
		front = stack[0]
		stack = stack[1:]
		if not nodeExists(leftChild(front[0] ),bt ) and not nodeExists(rightChild(front[0] ),bt ):
			if front[1] < distanceCL:
				distanceCL = front[1]
				closestLeafI = front[0]
		else:
			if front[1] < distanceCL:
				if nodeExists(leftChild(front[0] ),bt ):
					stack.append((leftChild(front[0]),front[1]+1) )
				if nodeExists(rightChild(front[0] ),bt ):
					stack.append((rightChild(front[0]),front[1]+1) )
	return (bt[closestLeafI],distanceCL)

def ClosestLeaf(currPos,bt):
	down = findDown(currPos,bt)
	updistance = 1

	while(down[1] > updistance+1) and parent(currPos)!=currPos: #add the optimization of not going down the same tree again

		currPos = parent(currPos)
		ancestorDown = findDown(currPos,bt)
		ancestorDown = (ancestorDown[0],ancestorDown[1]+updistance)

		if ancestorDown[1] < down[1]:
			down = ancestorDown
		updistance+=1
	print "The closest leaf to " + bt[currPos] + " is " + down[0] + ", and it is " + str(down[1]) + " edges away."
	return



if __name__ == "__main__":

	 #	 	A
	 #     / \
	 #	 Z	  G
	 #  /  \
	 # V    T
	 #       \
	 #       X
	 #       /
	 #      Z
	 #	   /
	 #    P
	 # MAKE AN ENCODING OF THIS
	
	encoding = ["A","Z","G","V","T",None, None,None,None,None,"X"]
	while len(encoding)!= 21:
		encoding.append(None)
	encoding.append("Z")
	while len(encoding)!=43:
		encoding.append(None)
	encoding.append("P")

	ClosestLeaf(4,encoding)
