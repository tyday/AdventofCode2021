# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day12/input.txt
#
# Created: 12-12-2021 07:41:24
# Creator: Ty Day

import string

class Vertex:
    def __init__(self, val) -> None:
        self.val = val
        self.revisitable = False if val[0] in string.ascii_lowercase else True
        self.neighbors = set()

class Graph:
    def __init__(self, data):
        self.graph = {}
        for item in data:
            self.add_vertice(item)
        # dict(sorted(d.items()))
        self.graph =dict(sorted(self.graph.items()))
    def add_vertice(self, item):
        a,b = item.split('-')
        a_not_revisitable = True if a[0] in string.ascii_lowercase else False
        b_not_revisitable = True if b[0] in string.ascii_lowercase else False
        if a in self.graph:
            self.graph[a]['neighbors'].add(b)
        else: self.graph[a] = {
            'neighbors':{b},
            'not_revisitable': a_not_revisitable
            }
        if b in self.graph:
            self.graph[b]['neighbors'].add(a)
        else: self.graph[b] = {
            'neighbors':{a},
            'not_revisitable': b_not_revisitable
            }

def find_paths(graph, start_vertex,visited):
    if start_vertex == 'end':
        return 1
    elif len(graph[start_vertex]['neighbors']) < 1:
        return 0
    else:
        local_visited = visited[:]
        if  graph[start_vertex]['not_revisitable']:
            local_visited += [start_vertex]
        neighbors = graph[start_vertex]['neighbors']
        neighbors = [n for n in neighbors if n not in visited]
        results = 0
        for neighbor in neighbors:
            results += find_paths(graph,neighbor,local_visited)
        return results

def find_paths_2(graph, start_vertex, visited, visited_once, visited_twice):
    neighbors = graph[start_vertex]['neighbors']
    neighbors = [n for n in neighbors if n not in visited]
    if start_vertex == 'end':
        return [['end']]
    elif len(neighbors) < 1:
        return [[start_vertex]]
    else:
        local_visited = visited[:]
        local_visited_once = visited_once[:]
        if  graph[start_vertex]['not_revisitable']:
            if start_vertex == 'start' or start_vertex == 'end':
                local_visited += [start_vertex]
            elif visited_twice == True:
                local_visited += [start_vertex]
            elif start_vertex in local_visited_once: # and visited_twice:
                visited_twice = True
                local_visited += [start_vertex]
                local_visited += local_visited_once
                neighbors = [n for n in neighbors if n not in local_visited]
            else:
                local_visited_once.append(start_vertex)

        # neighbors = graph[start_vertex]['neighbors']
        # neighbors = [n for n in neighbors if n not in visited]
        routes = []
        for neighbor in neighbors: #start,A,b,A,c,A,c,A,end
            result = find_paths_2(graph,neighbor,local_visited,local_visited_once,visited_twice)
            for r in result:
                routes.append(r)
        [r.insert(0, start_vertex) for r in routes]
        return routes[:]


if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day12/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    
    print(data)
    graph = Graph(data)
    for vertix in graph.graph:
        graph.graph[vertix]['neighbors']= sorted(graph.graph[vertix]['neighbors'])
    # print(graph.graph)
    # print(find_paths(graph.graph, 'start',[]))
    routes = find_paths_2(graph.graph, 'start',[], [],False)
    print(len(routes))
    # r = [print(",".join(r)) for r in routes if r[-1] == 'end']
    r = [r for r in routes if r[-1] == 'end']
    print(len(r))

    