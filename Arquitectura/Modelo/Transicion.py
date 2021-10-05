graph = {}
array = [['q0', 'x', 'q1'], ['q4', 'x', 'q4'], ['q4', 'y', 'q4'], ['q1', 'x', 'q1'], ['q1', 'y', 'q2'],
         ['q2', 'y', 'q2'], ['q2', 'x', 'q3']]
estado = ['q0', 'q1', 'q2', 'q3', 'q4']
array2 = [['q0', '0', ['q0', 'q1', 'q2']], ['q0', '1', ['q1']], ['q1', '1', ['q1', 'q2']], ['q1', '2', ['q2']],
          ['q0', '2', ['q2']], ['q2', '2', ['q2']]]
estado2 = ['q0', 'q1', 'q2']


def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = {}


# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(a, p, b):
    global graph
    # Check if vertex v1 is a valid vertex
    if a not in graph:
        print("Vertex ", a, " does not exist.")
    # Check if vertex v2 is a valid vertex
    if type(b) == list:
        for i in range(len(b)):
            if b[i] not in graph:
                print("Vertex ", b, " does not exist.")
            else:
                temp = {p: b}
                graph[a].update(temp)
    else:
        if b not in graph:
            print("Vertex ", b, " does not exist.")
        else:
            temp = {p: b}
            graph[a].update(temp)

# stores the number of vertices in the graph
vertices_no = 0

def crearDiccionario(a, e):
    graph.clear()
    for i in range(len(e)):
        add_vertex(e[i])  # añade vertice
    for i in range(len(a)):
        add_edge(a[i][0], a[i][1], a[i][2])  # añade adyacentes'''


def retornarDiccionario():
    print("Diccionario construido: ", graph)
    return graph

