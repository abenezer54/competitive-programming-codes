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
    vector<vector<int>> vis(n, vector<int>(m));

    vector<vector<int>> dir = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    auto inbound = [&](int i, int j) {
        return (i >= 0 && i < n && j >= 0 && j < m);
    };


    function<int(int, int)> dfs = [&](int i, int j){
        vis[i][j] = 1;
        int res = 0;
        for (int k = 0; k < 4; k++){
            int ni = i + dir[k][0], nj = j + dir[k][1];
            if (inbound(ni, nj) && vis[ni][nj] == 0 && a[i][j] == a[ni][nj]){
                res += dfs(ni, nj);
            }
        }
        return res + 1;

    };

    map<int, int> mx;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (vis[i][j] == 0){
                mx[a[i][j]] = max(mx[a[i][j]], min(2, dfs(i, j)));
            }
        }
    }
    vector<int> arr;
    
    for (auto&[key, val]: mx) {
        arr.push_back(val);
    }

    sort(arr.begin(), arr.end());
    int ans = 0;
    for (int i = 0; i < arr.size() - 1; i++){
        ans += arr[i];
    }
    
    cout << ans << '\n';

   
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