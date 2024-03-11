import sys
noOfNodes = int(sys.argv[1])
initiatorNode = int(sys.argv[2])
nodes = []
def ring_algo():
    print("Coordinator node "+str(noOfNodes)+" has failed")
    print("Intiating ring algorithm from : "+ str(initiatorNode))
    i = initiatorNode+1
    print("In node "+str(initiatorNode))
    nodes.append(initiatorNode)
    print("Present list containing nodes : ",nodes)
    while(True):
        if i == initiatorNode:
            break
        if i > noOfNodes:
            i = 0
        if i == noOfNodes:
            print("Node "+str(i)+" is dead. So keep moving")
            print("Sending values to process : "+str(0))
            i+=1
            continue
        print("In node "+str(i))
        nodes.append(i)
        print("Present list containing nodes : ",nodes)
        print("Sending values to process : "+str(i+1))
        i+=1
    print("Back to initiator node : ",initiatorNode)
    print("The maximum value shall be the coordinator node - ")
    coordinator = max(nodes)
    print("Coordinator node : ", coordinator)
    i = coordinator+1
    while(True):
        if i == coordinator:
            break
        if i > noOfNodes:
            i = 0
        print("Coordinator ",coordinator," sends election winner message to ",i)
        i+=1
if __name__ == '__main__':
 ring_algo()
