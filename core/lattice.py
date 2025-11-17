class LatticeNode:
    def __init__(self, nid, goal, constraints=None, resonance=1.0):
        self.nid = nid
        self.goal = goal
        self.constraints = constraints or []
        self.resonance = resonance
        self.edges = {}  # target_nid: weight

    def add_edge(self, target_nid, weight=1.0):
        self.edges[target_nid] = weight

    def propagate(self, signal):
        return {nid: signal * weight * self.resonance
                for nid, weight in self.edges.items()}

class Lattice:
    def __init__(self):
        self.nodes = {}
        self.active_goal = None

    def add_node(self, node):
        self.nodes[node.nid] = node
        if not self.active_goal:
            self.active_goal = node.goal

    def route_signal(self, start_nid, signal):
        if start_nid not in self.nodes:
            return {}
        return self.nodes[start_nid].propagate(signal)
