class Metrics:
    def __init__(self):
        self.metrics = {}
    def increment(self, name):
        if name not in self.metrics:
            self.metrics[name] = 0
        self.metrics[name] += 1
    def get(self, name):
        return self.metrics.get(name, 0)