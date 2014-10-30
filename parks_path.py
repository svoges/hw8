def algorithm(G, l, k):
    dist = [m][m]
    seen = {m}
    for each vertex v in V:
        dist[v][v] = 0 #distance from v to v is 0
    for each edge (u, v) in l:
        dist[u][v] = l[u][v]
    for a = 1...|V|:
        for b = 1...|V|:
            for c = 1...|V|:
                if dist[b][c] > dist[b][a] + dist[a][c]:
                    dist[b][c] = dist[b][a] + dist[a][c]
    shortest_path = [m - k][k]
    for i = 0...m:
        for all j = 0...i:
            shortest_path[i][j] = 0
        for j = i + 1...k:
            shortest_path[i][j] = l[i - 1][i] + min(shortest_path[i - 1][j -1] + shortest_path[i - 1][j])
    return minimum != 0 at column k in shortest_path
