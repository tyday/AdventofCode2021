# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day12/input.txt
#
# Created: 12-12-2021 07:41:24
# Creator: Ty Day
class Graph:
    def __init__(self, data):
        self.Vertices = set()
        self.Edges = set()
        self.Neighbors = {}
        for edge in data:
            a,b = edge.split('-')
            self.Vertices.add(a)
            self.Vertices.add(b)
            self.Edges.add(frozenset({a,b}))
            if a in self.Neighbors:
                self.Neighbors[a].append(b)
            else:
                self.Neighbors[a] = [b]
            if b in self.Neighbors:
                self.Neighbors[b].append(a)
            else:
                self.Neighbors[b] = [a]
class Queueing_structure:
    def __init__(self, type):
        self.type = type
        self.data = []
    def __len__(self):
        return(len(self.data))
    def push(self, item):
        self.data.append(item)
    def pop(self):
        if self.type.lower() == 'dfs':  # Stack
            return self.data.pop()
        elif self.type.lower() == 'bfs':    #Queue
            return self.data.pop(0)
        else:
            raise Exception("Unknown queueing structure")
def traversal(start_vertex, graph, structure):
    queueing_structure = Queueing_structure(structure)
    queueing_structure.push((start_vertex, None))
    explored_vertices = []
    routing_table = {}
    while len(queueing_structure) > 0:
        current_vertex, parent = queueing_structure.pop()
        if not current_vertex in explored_vertices:
            explored_vertices.append(current_vertex)
            routing_table[current_vertex] = parent
            for neighbor in graph.Neighbors[current_vertex]: # TODO implement this
                if neighbor not in explored_vertices:
                    queueing_structure.push((neighbor, current_vertex))
    return explored_vertices, routing_table
    


if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day12/test.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    
    print(data)
    graph = Graph(data)
    ev,rt = traversal('start',graph,'bfs')
    print(ev)
    # print(rt)
    for k,v in rt.items():
        print(k,v)