from collections import defaultdict
from heapq import heapify, heappop, heappush

with open("./day_16.in") as fin:
    lines = fin.read().strip().split("\n")


adj = defaultdict(list)
flow = defaultdict(int)
nodes = []
node_to_idx = {}

for i, line in enumerate(lines):
    parts = line.split(" ", 9)
    node = parts[1]
    nodes.append(node)
    node_to_idx[node] = i
    flow[node] = int(parts[4][5:-1])
    adj[node].extend(parts[-1].split(", "))


# Visit all 15 nonzero valves in some order
# 2^15 isn't horrible
# approx. 30 * 2^15

def get_pressure(state):
    total = 0
    for i in range(len(state)):
        if state[i]:
            total += flow[nodes[i]]
    return total


ans = 0

seen = set()
pq = [(0, "AA", 30, (False,) * 59)]

count = 0

# TIME COMPLEXITY
total_states = 30 * 15 * (1 << 15)


while len(pq) > 0:
    front = heappop(pq)
    pressure, node, time, state = front
    pressure *= -1

    if (pressure, node, time, state) in seen:
        continue
    seen.add((pressure, node, time, state))

    # Done?
    if time == 0:
        ans = max(ans, pressure)
        continue

    idx = node_to_idx[node]

    pressure += get_pressure(state)

    # 1. open the valve
    if flow[node] > 0 and not state[idx]:
        new_state = list(state)
        new_state[idx] = True
        new_state = tuple(new_state)
        heappush(pq, (-pressure, node, time - 1, new_state))

    # 2. move to a neighbor
    for nbr in adj[node]:
        heappush(pq, (-pressure, nbr, time - 1, state))

    heappush(pq, (-pressure, node, time - 1, state))

    count += 1
    if count % 100000 == 0:
        print(f"{str(count).rjust(9)}/{total_states}", end="")
        print("\t", f"{round(count/total_states * 100, 3)}%")


# That's it
print(ans)
