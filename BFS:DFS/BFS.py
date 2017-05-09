__author__ = 'vijaychandra'

file = 'input.txt'
lines = [line.rstrip('\n') for line in open(file)]
NumberOfLines = int(lines[0])
adjacencyMatrix = []
for x in range(1, NumberOfLines+1):
    input_list = [int(a) for a in lines[x]]
    adjacencyMatrix.append(input_list)
startingVertex = int(lines[len(lines)-1])
vertices = []

def BFS(adjmatrix, start):
    for i in range(0,len(adjmatrix)):
        for j in range(0, len(adjmatrix)):
            if(adjmatrix[start-1][j] == 1):
                if(adjmatrix[i][j] == 1):
                    vertices.append(str(i+1))
                    break
                else:
                    continue

BFS(adjacencyMatrix,startingVertex)
vertices = set(vertices)
vertices = list(vertices)
vertices.sort()

myString = ",".join(vertices)
target = open("output.txt",'w')
target.write("%s" %myString);
print(myString)