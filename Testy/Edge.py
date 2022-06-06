class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self):
        return "( " + str(self.u) + ", " +  str(self.v) + " )"

    def __eq__(self, other):
        return self.w == other.w

    def __lt__(self, other):
        return self.w < other.w

    def __le__(self, other):
        return self.w <= other.w
