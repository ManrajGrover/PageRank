import networkx as nx

def pagerank(graph):
    df=0.85
    iterations=100
    mindelta=0.00001
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        return {}
    min_value = (1.0-df)/graph_size 
    pr = dict.fromkeys(nodes, 1.0/graph_size)
    #print pr
    for i in range(iterations):
        diff = 0
        for node in nodes:
            rank = min_value
            for refpage in graph.in_edges(node):
              #  print refpage
              #  print len(graph.neighbors(refpage[0]))
                rank = rank + df*pr[refpage[0]]/len(graph.neighbors(refpage[0]))
              #  print rank
            diff += abs(pr[node] - rank)
            pr[node] = rank
            # print "pr node " + str(node) + " "+ str(pr[node])
        if diff < mindelta:
            break
    return pr

G = nx.DiGraph()
G.add_edge(2,1)
G.add_edge(2,3)
G.add_edge(3,1)
G.add_edge(4,1)
G.add_edge(4,2)
G.add_edge(4,3)
x = pagerank(G)
for i in range(len(x)):
    print x[i+1]
