import networkx as nx
import sys

G = nx.DiGraph()
listOfLines = {}
firstLine = []
startingNode = ''
endingNode = ''
i = 0
found = False
fastLines = []
with open (sys.argv[1], 'r') as file:
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
                listOfLines[splitLineFlipped[0]] = [newFlippedLine]
                G.add_node(newFlippedLine)
            else:
                temp = listOfLines[splitLineFlipped[0]]
                temp.append(newFlippedLine)
                listOfLines.update({splitLineFlipped[0]: temp})
                G.add_node(newFlippedLine)

            if splitLine[0] == firstLine[2]:
                G.add_edge(startingNode, line)
                G.add_edge(startingNode, newFlippedLine)
            elif splitLineFlipped[0] == firstLine[2]:
                G.add_edge(startingNode, newFlippedLine)
                G.add_edge(startingNode, line)

            if splitLine[0] == firstLine[3]:
                G.add_edge(newFlippedLine, endingNode)
                G.add_edge(line, endingNode)
            elif splitLineFlipped[0] == firstLine[3]:
                G.add_edge(newFlippedLine, endingNode)
                G.add_edge(line, endingNode)

            if splitLine[0] == firstLine[2] and splitLine[1] == firstLine[3]:
                found = True
                fastLines.append(splitLine[0] + ' ' + splitLine[1])
            if splitLine[1] == firstLine[2] and splitLine[0] == firstLine[3]:
                found = True
                fastLines.append(splitLine[1] + ' ' + splitLine[0])

for node in G.nodes:
    useNode = node.split()
    first = useNode[0]
    second = useNode[1]
    color = useNode[2]
    pathType = useNode[3]
    if (color == 'null'):
        continue
    for path in listOfLines[second]:
        usePath = path.split()
        firstPath = usePath[0]
        secondPath = usePath[1]
        colorPath = usePath[2]
        pathTypePath = usePath[3]
        if second == firstPath and first == secondPath:
            continue
        else:
            if first == secondPath:
                if color == colorPath or pathType == pathTypePath:
                    G.add_edge(path, node)
            elif second == firstPath:
                if color == colorPath or pathType == pathTypePath:
                    G.add_edge(node, path)
            
                    
thePaths = nx.all_shortest_paths(G, startingNode, endingNode)
output = ''
listOfPaths = []
i = 0

if not found:
    try:
        for path in thePaths:
            listOfPaths.append(path)
        listOfPaths = sorted(listOfPaths)
        for path in listOfPaths[0]:
            if i == 0:
                i += 1
                continue
            output += path.split()[0] + ' '
            i += 1
        
        print(output)
    except:
        print('NO PATH')
else:
    fastLines = sorted(fastLines)
    print(fastLines[0])