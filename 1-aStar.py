def aStarAlgo(start_node, stop_node):

    open_set = set(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes
    g[start_node] = 0  # distance of starting node from itself is zero
    # start_node is root node so it has no parent nodes
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in Graph_nodes[n]:
                # nodes 'm' not in first and last set are added to first n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # for each node m,compare its distance from start i.e g(m) to the from start through n node
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight  # update g(m)
                        parents[m] = n  # change parent of m to n
                        if m in closed_set:  # if m in closed set,remove and add to open
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node then we begin reconstructing the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        # remove n from the open_list, and add it to closed_list because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def heuristic(n):
    # for simplicity we'll consider heuristic distances given and this function returns heuristic distance for all nodes
    H_dist = {'S': 6, 'A': 5, 'B': 4, 'C': 5,
              'D': 2, 'E': 2, 'F': 1, 'G': 0, 'H': 4}
    return H_dist[n]


# Describe the graph here
Graph_nodes = {
    'S': [('A', 3), ('B', 2)],
    'A': [('B', 4)],
    'B': [('C', 1), ('E', 4)],
    'C': [('H', 2)],
    'E': [('D', 6), ('F', 1)],
    'D': [('G', 2)],
    'H': None,
    'G': None,
    'F': None
}

aStarAlgo('A', 'G')
