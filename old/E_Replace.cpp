#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    string s, t; cin >> s >> t;

    vector<set<int>> adj(26);
    for (int i = 0; i < n; i++) {
        int u = s[i] - '0'; u -= 49;
        int v = t[i] - '0'; v -= 49;
        adj[u].insert(v);
        if (adj[u].size() > 1) {
            cout << -1 << endl;
            return;
        } 
    }

    int cycle = 0;
    bool check = false;
    int ans = 0;
    vector<int> vis(26);
    for (int start = 0; start < 26; start++) {
        auto cur = start;
        if (adj[start].size() == 0) continue;
        bool normal = true;
        int sz = 0;
        while (vis[cur] == 0) {
            vis[cur] = 1;
            sz++;
            if (adj[cur].size() > 0) {
                int val = *adj[cur].begin();
                if (vis[val]) {
                    cout << "wuu " << cur << ' ' << val <   < endl;
                    cycle++;
                    normal = false;
                    break;
                }
                cur = val;
            }
        }
        if (start == 0) {
            cout << sz << endl;
        }
        ans += sz;
        if (normal) {
            check = true;
        }
    }
    cout << "cycle: " << cycle << endl;

    if (cycle && !check) {
        cout << -1 << endl;
        return;
    }
    ans += cycle;
    cout << ans << endl;
   
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