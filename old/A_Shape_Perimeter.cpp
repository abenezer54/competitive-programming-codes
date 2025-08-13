#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, m; cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(2));
    for (int i = 0; i < n; i++){
        cin >> a[i][0] >> a[i][1];
    }
    
    set<pair<int, int>> vis;
    int x = 0, y = 0;

    for (int i = 0; i < n; i++){
        x +=  a[i][0];
        y += a[i][1];
        cout << x << 

        for (int k = x; k < x + m; k ++) {
            for (int l = y; l < y + m; l ++){
                vis.insert(pair(k, l));
            }
        }
    } 

    set<pair<int, int>> ans;
    array<pair<int, int>, 4> dir = {{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}};
    for (auto& val: vis){
        int i = val.first, j = val.second;
        for (auto [x, y] : dir) {
            int ni = i + x, nj = j + y;
            if (!vis.count({ni, nj}))
                ans.insert({ni, nj});
        }
    }
    cout << ans.size() << '\n';
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