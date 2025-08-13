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
    vector<int> ind(n + 1), temp(n + 1), par(n + 1);

    int tot = 0;
    for (int node = 1; node <= n; node++) {
        int parent, t; cin >> parent >> t;
        temp[node] = t;
        tot += t;
        ind[parent]++;
        par[node] = parent;
    }

    if (tot % 3 != 0) {
        cout << -1 << endl;
        return;
    }


    queue<int> que;
    for (int node = 1; node <= n; node++) {
        if (ind[node] == 0) {
            que.push(node);
        }
    }
    
    
    vector<int> ans; 
    
    while (!que.empty()) {
        int sz = que.size();

        for (int i = 0; i < sz; i++) {
            int node = que.front(); que.pop();
            if (temp[node] == tot / 3) {
                ans.push_back(node);
                temp[node] = 0;
            }
            ind[par[node]] -= 1;
            temp[par[node]] += temp[node];
            if (ind[par[node]] == 0 && par[node] != 0) {
                que.push(par[node]);
            }
        }
    }

    if (ans.size() != 3) {
        cout << -1 << endl;
        return;
    }
    
    cout << ans[0] << ' ' << ans[1] << endl;
   
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