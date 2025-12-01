def pagerank(edges, n_node, beta=0.85, epoch=100):
    #Initialize all nodes with equal probability 
    r = [1/n_node] * n_node
    
    #Calculate out-degree (number of outgoing links) for each node
    d = [0] * n_node
    for u, _ in edges:
        d[u] += 1

    #Q1. Calculate the bade probability of a Random Jump (Teleport)
    # This is the probability that a surfer jumps to any other random page
    teleport = (1 - beta) / n_node # (1-b) / N formula
    for _ in range(epoch):
        #Initialize next rank with the base teleport probability.
        r_next = [teleport] * n_node
        #Q2. Distribute rank through edges (Link Traversal).
    #  # For every edge u -> v, node u passes a portion of its rank to v.
    # The amount passed is u's current rank divided by its out-degree, scaled by beta.
        for u, v in edges:
            r_next[v] += beta * r[u] / d[u] # beta * r[u]/d[u]

        #Q3. Handle Rank Sinks 
    # Some rank is lost because nodes with no outgoing edges (sinks) effectively "trap" the surfer.
    # We calculate the lost probability (1 - sum of current ranks) and redistribute it equally.
        r_sum = sum(r_next)
        for u in range(n_node):
            r_next[u] += (1 - r_sum) / n_node #(1- r_sum) / n_node

        r = r_next
    return r
#Q1. Damping Factor
#Q2. Voting Mechanism (outgoing link)
#Q3. Rank Sink Problem 
