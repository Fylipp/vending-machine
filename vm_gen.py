from functools import reduce

from graphviz import Digraph


def create_graph(target, steps, initial=0):
    nodes, edges = create_graph_components(initial, steps, target)

    g = Digraph()

    for node in nodes:
        g.node(str(node))

    for edge in edges:
        g.edge(str(edge[0]), str(edge[1]), str(edge[1] - edge[0]))

    return g, nodes, edges


def create_graph_components(initial, increments, target):
    nodes = {initial}
    edges = set()

    while True:
        changed = False

        for node in tuple(nodes):  # Shallow copy of set
            for increment in increments:
                new_nodes, new_edges = progress_step(node, target, increment)

                edge_count = len(edges)

                nodes.update(new_nodes)
                edges.update(new_edges)

                changed = changed or edge_count != len(edges)

        if not changed:
            break

    while trim_graph(nodes, edges, target):  # Trim the graph iteratively until it is finished
        pass

    return nodes, edges


def progress_step(start, stop, step):
    nodes = set()
    edges = set()
    node = start
    old_node = None

    while node <= stop:
        if old_node is not None:
            edges.add((old_node, node))

        nodes.add(node)

        old_node = node
        node += step

    return nodes, edges


def trim_graph(nodes, edges, target):
    def is_not_stub(n):  # Find out whether R(n,_)
        return any(filter(lambda e: e[0] == n, edges))

    stubs = []

    for node in filter(lambda n: not (n == target or is_not_stub(n)), nodes):
        stubs.append(node)

    # Find all edges linked to the stubs, e[0] can be ignored because ~R(n,_) [since that was the stub criteria]
    stub_edges = reduce(list.__add__, map(lambda n: list(filter(lambda e: e[1] == n, edges)), stubs), [])

    for stub in stubs:
        nodes.remove(stub)

    for edge in stub_edges:
        edges.remove(edge)

    return len(stubs) > 0
