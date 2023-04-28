import networkx as nx
import matplotlib as plt
import matplotlib.pyplot as p

G = nx.DiGraph()
listOfLines = {}
firstLine = []

i = 0
with open ('input.txt', 'r') as file:
    for line in file:
        if i == 0:
            firstLine = line.split()
            i += 1
            startingNode = firstLine[2] + ' ' + firstLine[2] + ' ' + 'null' + ' ' + 'null'
            endingNode = firstLine[3] + ' ' + firstLine[3] + ' ' + 'null' + ' ' + 'null'
            listOfLines[firstLine[2]] = [startingNode]
            listOfLines[firstLine[3]] = [endingNode]
            G.add_node(startingNode)
            G.add_node(endingNode)
        else:
            line = line.split('\n')[0]
            splitLine = line.split()
            splitLineFlipped = []
            splitLineFlipped.append(splitLine[1])
            splitLineFlipped.append(splitLine[0])
            splitLineFlipped.append(splitLine[2])
            splitLineFlipped.append(splitLine[3])
            newFlippedLine = splitLineFlipped[0] + ' ' + splitLineFlipped[1] + ' ' + splitLineFlipped[2] + ' ' + splitLineFlipped[3]
            if splitLine[0] not in listOfLines:
                listOfLines[splitLine[0]] = [line]
                G.add_node(line)
            else:
                temp = listOfLines[splitLine[0]]
                temp.append(line)
                listOfLines.update({splitLine[0]: temp})
                G.add_node(line)
            if splitLineFlipped[0] not in listOfLines:
                listOfLines[splitLineFlipped[1]] = [newFlippedLine]
                G.add_node(newFlippedLine)
            else:
                temp = listOfLines[splitLineFlipped[0]]
                temp.append(newFlippedLine)
                listOfLines.update({splitLineFlipped[0]: temp})
                G.add_node(newFlippedLine)
            if splitLine[0] == firstLine[0]:
                G.add_edge(firstLine[0], line)
            if splitLineFlipped[0] == firstLine[0]:
                G.add_edge(firstLine[0], newFlippedLine)
            if splitLine[0] == firstLine[1]:
                G.add_edge(firstLine[1], line)
            if splitLineFlipped[0] == firstLine[1]:
                G.add_edge(firstLine[1], newFlippedLine)
# print(G.nodes)
for node in G.nodes:
    useNode = node.split()
    # print(node)
    first = useNode[0]
    second = useNode[1]
    color = useNode[2]
    pathType = useNode[3]
    # print(listOfLines)
    for path in listOfLines[second]:
        # print(path)
        usePath = path.split()
        firstPath = usePath[0]
        secondPath = usePath[1]
        colorPath = usePath[2]
        pathTypePath = usePath[3]
        if path == node: continue
        if color == colorPath or pathType == pathTypePath:
            print(node)
            print(path)
            G.add_edge(node, path)
        # else:
        #     print(node)
        #     print(path)
        #     G.add_edge(path, node)

nx.draw(G, with_labels = True)
p.savefig('peopleEatDogsSometimes.png')
startingNode = firstLine[2] + ' ' + firstLine[2] + ' ' + 'null' + ' ' + 'null'
endingNode = firstLine[3] + ' ' + firstLine[3] + ' ' + 'null' + ' ' + 'null'
listOfPaths = nx.all_shortest_paths(G, startingNode, endingNode)
for paths in listOfPaths:
    print(paths)