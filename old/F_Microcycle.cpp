#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

class DSU {
private:
    vector<int> parent, size;

public:
    DSU(int n) {
        parent.resize(n);
        size.assign(n, 1);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]); 
        }
        return parent[node];
    }

    void union_sets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (size[rootX] > size[rootY]) {
                swap(rootX, rootY); 
            }
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        }
    }

    bool is_connected(int x, int y) {
        return find(x) == find(y);
    }
};



void solve() {
    int n, m; cin >> n >> m;
    vector<array<int, 3>> edges;
    for (int j = 0; j < m; j++) {
        int u, v, w; cin >> u >> v >> w;
        u--; v--;
        edges.push_back({w, u, v});
    }

    set<int> wuu;
    sort(edges.begin(), edges.end());
    // cout << edges << endl;
    DSU dsu = DSU(n);
    int bound = 0;
    while (bound < m) {
        if (dsu.is_connected(edges[bound][1], edges[bound][2])) {
            break;
        } else {
            dsu.union_sets(edges[bound][1], edges[bound][2]);
        }
        bound++;
    }

    int res = INT_MAX;
    vector<vector<array<int, 2>>> adj(n);
    for (int j = 0; j <= bound; j++) {
        auto [w, u, v] = edges[j];
        res = min(res, w);
        adj[u].push_back({v, w});
        wuu.insert(u);
        wuu.insert(v);
        adj[v].push_back({u, w});
    }

    vector<int> col(n, 0);
    vector<int> parent(n);
    vector<int> ans;
    vector<int> result;

   
    function<int(int, int)> dfs = [&] (int node, int par) {
        col[node] = 1;
        int x = 0;
        result.push_back(node + 1);
        
        for (auto [nei, w]: adj[node]) {
            if (col[nei] == 1 && nei != par) {
                // cout << "found " << node + 1 << ' ' << nei + 1<< endl;
                vector<int> path;
                int cur = node;
                while (cur != nei) {
                    path.push_back(cur);
                    cur = parent[cur];
                }
                path.push_back(cur);
                ans = path;

            } else if (col[nei] == 0) {
                parent[nei] = node;
                dfs(nei, node);
            }
        }

        col[node] = 2;
        return x;
    };


    for (int node = 0; node < n; node++) {
        if (col[node] == 0 && wuu.count(node)) {
            // cout << "called here: " << node + 1<< endl;
            dfs(node, -1);
        }
    }
    cout << res << ' ' << ans.size()  << endl;
    
    for (auto node: result) {
        cout << node  << ' ';
    }

    cout << endl;
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