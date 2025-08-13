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
    vector<vector<array<ll, 2>>> adj(n);
    for (int i = 0; i < m; i++) {
        ll x, y, z; cin >> x >> y >> z;
        x--; y--;
        adj[x].push_back({y, z});
        adj[y].push_back({x, z});
    }

    int bit = 0;
    vector<array<int, 2>> vis(n);
    vector<int> vals(n);
    vector<int> temp;
    function<bool(int, int, int, int)> dfs =  [&] (int node, int par, int sign, int pp) {
        vis[node][pp] = 1;
        if (sign) temp.push_back(node);

        vals[node] = sign;
        bool res = true;
        
        for (auto [nei, w]: adj[node]) {
            if (vis[nei][pp] == 1) {
                if (nei == par) continue;
                else {
                    if (w & (1 << bit)) {
                        if (sign == vals[nei]) {
                            return false;
                        }
                    } else {
                        if (sign != vals[nei]) {
                            return false;
                        }
                    } 
                }
            } else if (vis[nei][pp] == 0) {
                if (w & (1 << bit)) {
                    if (sign == 1) res = res && dfs(nei, node, 0, pp);
                    else res = res && dfs(nei, node, 1, pp);
                } else {
                    if (sign == 1) res = res && dfs(nei, node, 1, pp);
                    else res = res && dfs(nei, node, 0, pp);
                }

            }
            
        }
        vis[node][pp] = 2;
        return res;
    };

    vector<ll> A(n);

    for (; bit < 32; bit++) {
        vis.assign(n, {0, 0});
        vals.assign(n, 0);

        for (int start = 0; start < n; start++) {
            if (vis[start][0]) continue;

            vector<int> prev;
            bool val1 = false;
            if (vis[start][0] == 0) {
                val1 = dfs(start, -1, 0, 0);
                if (val1) {
                    prev = temp;
                }
                temp.clear();
            }
            bool val2 = false;
            if (vis[start][1] == 0) {
                val2 = dfs(start, -1, 1, 1);
            }

            vector<int> arr;
            if (val1 && val2) {
                if (temp.size() < prev.size()) arr = temp;
                else arr = prev;
            } else if (val1) {
                arr = prev;
            } else if (val2) {
                arr = temp;
            }else {
                cout << -1 << endl;
                return;
            }

            temp.clear();
            for (auto idx: arr) {
                A[idx] |= 1 << bit;
            }

        }
    }
        
    for (int val: A) {
        cout << val << ' ';
    }
    cout << endl;
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