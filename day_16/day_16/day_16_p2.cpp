#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

void setIO(string s) {
  freopen((s + ".in").c_str(), "r", stdin);
  freopen((s + ".out").c_str(), "w", stdout);
}

const int minutes = 30;

int main() {
  setIO("day_16_parsed");

  int N;
  cin >> N;

  // Read flows
  vi flow(N);
  for (int i = 0; i < N; i++) {
    cin >> flow[i];
  }

  // Grab adjacency matrix
  vector<vi> adj(N, vi(N));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> adj[i][j];
    }
  }

  // Preprocess state-pressure calculation
  // cout << "finished reading input\n";

  vi get_pressure(1 << N);
  for (int state = 0; state < (1 << N); state++) {
    int total = 0;
    int i = 0;
    int temp_state = state;
    while (temp_state > 0) {
      if (temp_state & 1) {
        total += flow[i];
      }
      temp_state >>= 1;
      i++;
    }
    get_pressure[state] = total;
  }

  // cout << "finished get_pressure preprocessing\n";

  // DO THE DP
  // index by time, node, state
  vector<vector<vector<vi>>> dp(minutes + 1, vector<vector<vi>>(N, vector<vi>(N, vi(1 << N, -1))));
  dp[0][0][0][0] = 0;

  for (int time = 1; time <= minutes; time++) {
    for (int node = 0; node < N; node++) {
      for (int node2 = 0; node2 < N; node2++) {
        for (int state = 0; state < (1 << N); state++) {
        }
      }
    }
  }

  return 0;
}
