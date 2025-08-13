#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
class DSU {

public:
    vector<ll> parent, size, total;
    DSU(int n) {
        parent.resize(n);
        size.assign(n, 1);
        total.assign(n, 0);
        for (int i = 0; i < n; ++i) {
            parent[i] = i; 
        }
    }

    int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]); // Path compression
        }
        return parent[node];
    }

    void union_sets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (size[rootX] > size[rootY]) {
                swap(rootX, rootY); // Ensure rootY is the larger root
            }
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
            total[rootY] += total[rootX];
        }
    }

    bool is_connected(int x, int y) {
        return find(x) == find(y);
    }
};

void solve() {
    int n; cin >> n;
    vector<int> a(n), p(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> p[i]; p[i]--;
    }
    reverse(p.begin(), p.end());
    vector<bool> ok(n, false);
    DSU dsu = DSU(n);
    vector<ll> ans;
    ll mx = 0;
    for (int i = 0; i < n; i++) {
        ans.push_back(mx);
        dsu.total[p[i]] = a[p[i]];
        ok[p[i]] = true;
        if (p[i] + 1 < n && ok[p[i] + 1]) {
            dsu.union_sets(p[i], p[i] + 1);
        }

        if (p[i] - 1 >= 0 && ok[p[i] - 1]) {
            dsu.union_sets(p[i], p[i] - 1);
        }
        mx = max(mx, dsu.total[dsu.find(p[i])]);
    }

    for (int i = n - 1; i >= 0; i--) {
        cout << ans[i] << endl;
    }

   
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