#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;


// int dfs(int i, int j, int k, auto &grid, int cur, auto &vis) {
//     cout << "called here" << '\n';
    
//     vector<pair<int, int>> direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

//     int res = 0;
//     if (cur == k){
//         return 1;
//     }
//     for (auto p:direction){
//         int ni = i + p.first;
//         int nj = j + p.second;
//         if (0 <= ni < grid.size() && 0 <= nj < grid[0].size() && !vis[ni][nj]){
//             vis[ni][nj] = true;
//             res += dfs(ni, nj, k, grid, cur + 1, vis);
//         }
//     }
//     return res;

// }

void solve() {
    int n, m, k; cin >> n >> m >> k;
    vector<string> grid(n);
    for (int i = 0; i < n; i++){
        cin >> grid[i]; 
    }

    vector<pair<int, int>> direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int tot = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (grid[i][j] == '#')
                continue;
                
            vector<vector<bool>> vis(n, vector<bool>(m, false));
            vis[i][j] = true;

            auto dfs = [&](auto&& self, int i, int j, int s) {
                if (s == k){
                    return 1;
                }
                int res = 0;
                
                for (auto p:direction){
                    int ni = i + p.first;
                    int nj = j + p.second;

                    if (0 <= ni && ni < n && 0 <= nj && nj < m && !vis[ni][nj] &&  grid[ni][nj] != '#' ){
                        vis[ni][nj] = true;
                        res += self(self, ni, nj, s + 1);
                        vis[ni][nj] = false;
                    }
                }
                return res;
                
            };
            int val = dfs(dfs, i, j, 0);
            tot += val;
            }
    }  
    cout << tot << '\n';  
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