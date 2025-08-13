#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    vector<vector<int>> vis(n, vector<int>(m, 0));
    
    vector<int> dx = {-1, 0, 1, 0};
    vector<int> dy = {0, 1, 0, -1};

    auto inbound = [&](int i, int j){
        return i >= 0 and i < n and j >= 0 and j < m;
    };


    function<int(int, int)> dfs = [&](int i, int j){
        vis[i][j] = 1;
        vector<int> check;
        for (int bit = 3; bit >= 0; bit--){
            if ((1 << bit) <= a[i][j]){
                check.push_back(1);
                a[i][j] -= (1 << bit);
            } else {
                check.push_back(0);
            }
        }


        int res = 0;
        for (int k = 0; k < 4; k++){
            if (check[k] == 0){
                int ni = i + dx[k], nj = j + dy[k];
                if (inbound(ni, nj) && vis[ni][nj] == 0){
                    res += dfs(ni, nj);
                }
            }
        }

        return res + 1;
    };

    vector<int> ans;
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (vis[i][j] == 0){        
                ans.push_back(dfs(i, j));
            }
        }
    }
    
    sort(ans.begin(), ans.end(), greater<>());
   
    for (auto x: ans){
        cout << x << ' ';
    }
    cout << '\n';
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