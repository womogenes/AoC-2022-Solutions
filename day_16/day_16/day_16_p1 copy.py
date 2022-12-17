from collections import defaultdict
from heapq import heapify, heappop, heappush
from pprint import pprint
from functools import lru_cache
from collections import deque

with open("../day_16.in") as fin:
    lines = fin.read().strip().split("\n")


adj = defaultdict(list)
flow = []
nodes = []
node_to_idx = {}

for i, line in enumerate(lines):
    parts = line.split(" ", 9)
    node = parts[1]
    nodes.append(node)
    node_to_idx[node] = i
    flow.append(int(parts[4][5:-1]))
    adj[node].extend(parts[-1].split(", "))


# Run Floyd-Warshall
N = len(nodes)
dist = [[1 << 60] * N for _ in range(N)]

for node in nodes:
    node_idx = node_to_idx[node]
    for nbr in adj[node]:
        nbr_idx = node_to_idx[nbr]
        dist[node_idx][nbr_idx] = 1

    dist[node_idx][node_idx] = 0


for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


# Only a subset of the nodes actually have flow
good_nodes = []
for i in range(N):
    if flow[i] > 0:
        good_nodes.append(i)


M = len(good_nodes)


# Export adjacency matrix
M = len(good_nodes) + 1

AA = node_to_idx["AA"]
good_nodes.insert(0, AA)

with open("./day_16_parsed.in", "w") as fout:
    fout.write(f"{M}\n")
    fout.write(" ".join(map(str, [flow[i] for i in good_nodes])) + "\n")
    for i in range(M):
        line = ""
        for j in range(M):
            a, b = good_nodes[i], good_nodes[j]
            line += f"{dist[a][b]} "
        fout.write(line[:-1] + "\n")

exit()


@lru_cache(None)
def get_pressure(state):
    total = 0
    i = 0
    while state > 0:
        if state & 1:
            total += flow[good_nodes[i]]
        state >>= 1
        i += 1

    return total


dp = [[[-1] * (1 << M) for _ in range(M)] for _ in range(31)]

# dp[time][good_node][state]
for time in range(1, 31):
    for good_node in range(M):
        for state in range(1 << M):
            # Alternatives!
            a1 = 0

            if not state & (1 << good_node):
                a1 = dp[time - 1][good_node][state ^ (1 << good_node)]

            a2 = 0
            for other in range(M):
                d = dist[good_node][other]

                # Not enough time to get there and do anything
                if d > time:
                    continue

                a2 = max(a2, dp[time - d][other][state])

            # Status quo, a1, or a2
            ans = max(dp[time - 1][good_node][state], a1, a2)

            ans += get_pressure(state)

            dp[time][good_node][state] = ans


# Get from AA to any other node
ans = 0

cost_to_reach = {}

visited = set()
dq = deque([("AA", 0)])

while len(dq) > 0:
    node, cost = dq.popleft()
    if node in visited:
        continue
    visited.add(node)

    if flow[node_to_idx[node]] > 0:
        cost_to_reach[node] = cost

    for nbr in adj[node]:
        dq.append((nbr, cost + 1))

for i, good_node in enumerate(good_nodes):
    t = cost_to_reach[nodes[good_node]]

    if t >= 30:
        continue

    ans = max(ans, dp[30 - t][i][0])


for row in dp[1]:
    print(row[:10])

print(ans)
