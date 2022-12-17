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
  vector<vector<vi>> dp(minutes + 1, vector<vi>(N, vi(1 << N, -1)));
  dp[0][0][0] = 0;

  for (int time = 1; time <= minutes; time++) {
    for (int node = 0; node < N; node++) {
      for (int state = 0; state < (1 << N); state++) {
        // cout << "\ntime=" << time << ", node=" << node << ", state=" << state << "\n";

        // Turn turning node on
        // cout << "  trying turning node on\n";
        int a1 = -1;
        if (state & (1 << node)) {
          int prev = dp[time - 1][node][state ^ (1 << node)];
          if (prev == -1) continue;
          a1 = prev + get_pressure[state ^ (1 << node)];
        }
        // cout << "    produced " << a1 << "\n";

        // Move to a neighbor
        // cout << "  trying moving to a neighbor\n";
        int a2 = -1;
        for (int other = 0; other < N; other++) {
          int d = adj[node][other];
          if (d > time) continue;

          int prev = dp[time - d][other][state];
          if (prev == -1) continue;

          a2 = max(a2, prev + get_pressure[state] * d);
          // cout << "    neighbor=" << other << ", " << prev << "\n";
        }
        // cout << "    produced " << a2 << "\n";

        int ans = max({dp[time - 1][node][state], a1, a2});
        dp[time][node][state] = ans;

        // cout << "  FINAL dp value=" << ans << "\n";
      }
    }
  }

  int ans = 0;
  for (int node = 0; node < N; node++) {
    for (int state = 0; state < (1 << N); state++) {
      // cout << setw(4) << dp[minutes][node][state] << " ";

      ans = max(ans, dp[minutes][node][state]);
    }
    cout << "\n";
  }
  cout << ans << "\n";

  return 0;
}
