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

def DFS(adjmatrix, start):
    for i in range(0, len(adjmatrix[start-1])):
        if(adjmatrix[start-1][i] == 1):
            for j in range(0,len(adjmatrix)):
                if(adjmatrix[j][i] == 1):
                    vertices.append(str(j+1))


DFS(adjacencyMatrix,startingVertex)
vertices = set(vertices)
vertices = list(vertices)
vertices.sort()
myString = ",".join(vertices)
target = open("output.txt",'w')
target.write("%s" %myString);
print(myString)