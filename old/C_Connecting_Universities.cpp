#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, k; cin >> n >> k;
    vector<bool> uni(n + 1, false);

    for (int i = 0; i < k * 2; i++){
        int x; cin >> x;
        uni[x] = true;
    }

    vector<int> ind(n + 1, 0);

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++){
        int x, y; cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
        ind[x]++; 
        ind[y]++;
    }
    auto merge = [](auto arr){
        vector<int> merged;
        for(int i = 0; i < arr.size(); i++){
            for (int j = 0; j < arr[i].size(); j++){
                merged.push_back(arr[i][j]);
            }
        }
        return merged;
    };

    queue<int> que;
    for (int node = 1; node <= n; node++){
        if (ind[node] == 1) que.push(node);
    }

    cout << ind << endl;

    vector<unordered_map<int, vector<int>>> arr(n + 1);
    vector<int> lvl(n + 1, 0);
    int level = 0;
    int last = 0;
    while (!que.empty()) {
        int sz = que.size();
        for (int _; _ < sz; _++){
            int node = que.front(); que.pop();
            lvl[node] = level;
            auto cur = merge(arr[node]);
            last = node;
            if (uni[node]){
                cur.push_back(level);
            }
            for (int nei : adj[node]){
                arr[nei][node] = cur;
                ind[nei]--;
                if (ind[nei] == 1){
                    que.push(nei);
                }
            }
        }
        level++;
    }

    cout << last << endl;
    


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