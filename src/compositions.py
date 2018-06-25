class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in braches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
