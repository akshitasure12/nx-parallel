from .common import (
    backends,
    num_nodes,
    edge_prob,
    get_cached_gnp_random_graph,
    Benchmark,
)
import networkx as nx


class DAG(Benchmark):
    params = [(backends), (num_nodes), (edge_prob)]
    param_names = ["backend", "num_nodes", "edge_prob"]

    def time_colliders(self, backend, num_nodes, edge_prob):
        G = get_cached_gnp_random_graph(num_nodes, edge_prob, is_directed=True)
        _ = nx.dag.colliders(G, backend=backend)

    def time_v_structures(self, backend, num_nodes, edge_prob):
        G = get_cached_gnp_random_graph(num_nodes, edge_prob, is_directed=True)
        _ = nx.dag.v_structures(G, backend=backend)
