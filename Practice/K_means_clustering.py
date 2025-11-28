class Kmeans:
    def fit(self, x):
        #Randomly select initial centroids
        self.centroid = x[np.random.choice(range(len(x)), slelf.n_clusters, replace = False)]

        for _ in range(self.max_iter):
            #Q1. Calculate Euclidean distance between data points and centoids 
            distances = norm(np.expand_dims(x, axis=1) - np.expand_dims(self.centroids, axis=0), axis=-1) #axis = ???(-1 or 2)
            #Q2. Assign each data point to the slosest centroid(find index of min distance)
            self.labels_ = np.argmin(distances, axis = -1) #axis = ???(-1 or 1)
            #Q3. Update centoids by calculating the__ of oints in each cluster
            new_centroids = np.array([x[self.labels_ == i].mean(axis=0) for i in range(self.n_clusters)]) #.mean(axis=0)
            
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids