class DBSCAN:
    def __init__(self, eps=0.3, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
    def fit(self, x):
        # Distance matrix D calculation omitted
        #Q1. Identify neighbors within the radius
        neighbors = [np.where(D[i] <= self.eps)[0] for i in range(n)]

        #Q2. A point is a Core Point if it has at least __ neighbors
        self.core_samples_mask_ = np.array([
            len(neighbors[i] >= self.min_samples for i in range(n))
        ])