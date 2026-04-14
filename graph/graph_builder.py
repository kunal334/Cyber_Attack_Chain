import networkx as nx

def build_graph(alerts):
    G = nx.DiGraph()

    for alert in alerts:
        ip = alert["ip"]
        action = alert["type"]

        G.add_node(ip)
        G.add_node(action)
        G.add_edge(ip, action)

    data = nx.node_link_data(G)

    # 🔥 FIX: edges → links
    if "edges" in data:
        data["links"] = data.pop("edges")

    return data