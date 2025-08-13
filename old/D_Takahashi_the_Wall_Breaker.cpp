#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];
    int A, B, C, D; cin >> A >> B >> C >> D;
    A--; B--;
    C--; D--;

    priority_queue<array<int, 3>> pq;
    pq.push({0, A, B});
    vector<vector<int>> vis (n, vector<int>(m, 1e9));
    vector<int> dx = {1, -1, 0, 0, 2, -2, 0, 0};
    vector<int> dy = {0, 0, 1, -1, 0, 0, 2, -2};

    vis[A][B] = 0;
    auto inbound = [&] (int i, int j) {
        return (i >= 0 && i < n && j >= 0 && j < m);
    };

    while (!pq.empty()) {
        cout << pq << endl;
        auto [w, i, j] = pq.top();
        pq.pop();
        if (vis[i][j] < -1 * w) continue;
        
        vis[i][j] = -1 * w;
        if (i == C && j == D) {
            break;
        }

        for (int k = 0; k < 8; k++) {
            int ni = i + dx[k], nj = j + dy[k];
            int ii = i + dx[k % 4], jj = j + dy[k % 4];
            if (inbound(ni, nj)) {
                int cur_cost = w;
                if (grid[ni][nj] == '#' || (grid[ii][jj] == '#')) cur_cost -= 1;
                if (-1 * cur_cost < vis[ni][nj]) {
                    pq.push({cur_cost, ni, nj});
                    vis[ni][nj] = -1 * cur_cost;
                }

            }
        }

    }
    cout << vis[C][D] << endl;

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    // cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}