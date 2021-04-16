# TODO: 틀린 케이스가 몇개 있는데(25개 케이스에서 5개) 나중에 해결해보기

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


def solution(n, weak, dist):
    g = Graph()
    cnts = []
    for i, w in enumerate(weak):
        next = weak[i + 1 if i + 1 < len(weak) else 0]
        g.add_edge(w, next, next - w if w < next else n - w + next)

    for i in range(len(g.vert_dict)):
        selects = set()
        points = list(g.vert_dict.values())[i:] + list(g.vert_dict.values())[:i]
        for j, d in enumerate(sorted(dist, reverse=True)):
            cur_d = d
            cands = [x for x in points if x not in selects]
            if len(cands) == 0:
                cnts.append(j)
                break
            elif len(cands) == 1:
                cnts.append(j + 1)
                break
            vertex = cands[0]
            selects.add(vertex)
            while len(cands) > 1:
                vertex = cands[0]
                neighbor = cands[1]
                if neighbor not in vertex.get_connections() or vertex.get_weight(neighbor) > cur_d:
                    if cur_d == d:
                        cands = cands[1:]
                        continue
                    else:
                        break
                selects.add(neighbor)
                if len(selects) == len(points):
                    cnts.append(j + 1)
                cur_d -= vertex.get_weight(neighbor)
                if cur_d == 0:
                    break
                cands = cands[1:]

    return min(cnts if cnts else [-1])


if __name__ == '__main__':
    print(solution(100, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))
