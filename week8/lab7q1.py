import sys
noOfNodes = int(sys.argv[1])
initiatorNode = int(sys.argv[2])
def bully_algorithm():
    print(initiatorNode," sends message to coordinator ",noOfNodes)
    print('Node: ' + str(initiatorNode) +' notices the coordinator: ' + str(noOfNodes)+' has failed')
    biggerNodes = []
    if initiatorNode+1 == noOfNodes:
        newCoordinatorNode = initiatorNode
    for i in range(initiatorNode+1, noOfNodes):
        biggerNodes.append(i-1)
        for j in range(i, noOfNodes+1):
            print(i-1,'sent ELECTION message to: ' + str(j))
            biggerNodes.append(j)
        biggerNodes.remove(i-1)
        biggerNodes.remove(noOfNodes)
        for j in biggerNodes:
            print(str(j)+' sent OK message to ' + str(i-1))
        newCoordinatorNode = biggerNodes[len(biggerNodes)-1]
        print()
        biggerNodes = []
    print(newCoordinatorNode,'sent ELECTION message to: ',newCoordinatorNode+1)
    print("No OK message received")
    print("New coordinator : ",newCoordinatorNode)
    print()
    for i in range(0, newCoordinatorNode):
        print(str(newCoordinatorNode)+' sends COORDINATOR message to '+str(i))
if __name__ == '__main__':
 bully_algorithm()