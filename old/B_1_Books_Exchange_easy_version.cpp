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
    vector<int> parent, size;
    DSU(int n) {
        parent.resize(n);
        size.assign(n, 1);
        for (int i = 0; i < n; ++i) {
            parent[i] = i; // Each element is its own parent initially
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
        }
    }

    bool is_connected(int x, int y) {
        return find(x) == find(y);
    }
};

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (auto &x: a) {
        cin >> x; x--;
    }
    DSU dsu = DSU(n);
    for (int i = 0; i < n; i++) {
        dsu.union_sets(i, a[i]);
    }

    for (int i = 0; i < n; i++) {
        cout << dsu.size[dsu.find(i)] << ' ';
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