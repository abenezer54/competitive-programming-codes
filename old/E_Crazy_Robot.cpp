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

    vector<vector<int>> vis(n, vector<int>(m));
    vector<vector<int>> ans(n, vector<int>(m));
    vector<array<int, 2>> direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    queue<array<int, 2>> que;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'L') {
                que.push({i, j});
                ans[i][j] = 1;
                vis[i][j] = 1;
                break;
            }
        }
    }


    auto inbound = [&] (int i, int j) {
        return i >= 0 && i < n && j >= 0 && j < m;
    };


    auto is_valid = [&] (int i, int j) {
        bool found = false;
        int free_count = 0;
        for (auto [dx, dy]: direction) {
            int ni = i + dx, nj = j + dy;
            if (inbound(ni, nj)) {
                if (ans[ni][nj]) {
                    found = true;
                } else if (grid[ni][nj] == '.') {
                    free_count++;
                }
            }
        }
        return found && free_count <= 1;
    };


    while (!que.empty()) {
        auto[i, j] = que.front();
        que.pop();

        if (is_valid(i, j) || grid[i][j] == 'L') {
            ans[i][j] = 1;
            vis[i][j] = 1;
        } else {
            continue;
        }

        for (auto [dx, dy]: direction) {
            int ni = i + dx, nj = j + dy;
            if (inbound(ni, nj) && vis[ni][nj] == 0 && grid[ni][nj] == '.') {
                que.push({ni, nj});
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (ans[i][j] && grid[i][j] != 'L') {
                grid[i][j] = '+';
            }
        }
    }

    for (auto val: grid) {
        cout << val << endl;
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}