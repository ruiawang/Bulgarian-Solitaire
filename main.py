import matplotlib.pyplot as plt
import networkx as nx
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'


# change this for the graphs of different sizes
N = 15

def partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

def next_state(state):
    state = list(filter(lambda x: x != 0, [*map(lambda y: y - 1, state)])) + [len(state)]
    return sorted(state)

def main():
    
    G = nx.DiGraph()
    
    G.add_nodes_from([tuple(partition) for partition in partitions(N)])
    for node in G.nodes:
        G.add_edge(node, tuple(next_state(list(node))))
    
    plt.figure(figsize=(48,36))
    pos = nx.nx_pydot.graphviz_layout(G,prog='dot')
    nx.draw_networkx(G, pos=pos, node_color = '#ff00ff',font_size = 6, with_labels=True, verticalalignment='baseline')
    plt.savefig('size_.png')

if __name__ == "__main__":
    main()