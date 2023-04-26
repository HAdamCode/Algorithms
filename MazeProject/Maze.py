lines = []

# def BFS(town, line, path, desired):
#     if line[0] == desired  or line[1] == desired:
#         return desired
#     else:
#         for l in lines:
#             if (l[0] == town)
#         return path + BFS(lines[i], path, desired)

def add_edge(adj, src, dest):
    if (src not in adj.keys()):
        adj[src] = [dest]
    else:
        t = adj[src]
        t.append(dest)
        adj.update({src: t})
    if (dest not in adj.keys()):
        adj[dest] = [src]
    else:
        t = adj[dest]
        t.append(src)
        adj.update({dest: t})
    # adj[src].append(dest)
    # adj[dest].append(src)
  
# a modified version of BFS that stores predecessor
# of each vertex in array p
# and its distance from source in array d
def BFS(adj, src, dest, v, pred, dist):
 
    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []
  
    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for i in range(v)]
  
    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1
     
    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True
    dist[src] = 0
    queue.append(src)
  
    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
  
                # We stop BFS when we find
                # destination.
                if (adj[u][i] == dest):
                    return True
  
    return False
  
# utility function to print the shortest distance
# between source vertex and destination vertex
def printShortestDistance(adj, s, dest, v):
     
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
  
    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")
  
    # vector path stores the shortest path
    path = []
    crawl = dest
    path.append(crawl)
     
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]
     
  
    # distance from source is in distance array
    print("Shortest path length is : " + str(dist[dest]), end = '')
  
    # printing path from source to destination
    print("\nPath is : : ")
     
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=' ')



firstLine = ''
listOfLines = []
i = 0
with open ('input.txt', 'r') as file:
    for line in file:
        if i == 0:
            firstLine = line
            i += 1
        else:
            listOfLines.append(line)


for line in listOfLines:
    lines.append(line.split())
# print(lines)

# no. of vertices
v = int(firstLine[1])

# array of vectors is used to store the graph
# in the form of an adjacency list
# adj = [[] for i in range(v)]
adj = {}

# Creating graph given in the above diagram.
# add_edge function takes adjacency list, source
# and destination vertex as argument and forms
# an edge between them.

for line in lines:
    add_edge(adj, line[0], line[1])
# add_edge(adj, 0, 1)
# add_edge(adj, 0, 3)
# add_edge(adj, 1, 2)
# add_edge(adj, 3, 4)
# add_edge(adj, 3, 7)
# add_edge(adj, 4, 5)
# add_edge(adj, 4, 6)
# add_edge(adj, 4, 7)
# add_edge(adj, 5, 6)
# add_edge(adj, 6, 7)
source = firstLine[2]
dest = firstLine[3]
printShortestDistance(adj, source, dest, v)