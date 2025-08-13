#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;


void solve() {
    int n; cin >> n;
    vector<int> p(n + 1);
    
    for (int i = 1; i <= n; i++){
        cin >> p[i];
    }

    vector<int> vis(n + 1);
    vector<int> ans;
    for (int i = 1; i <= n; i++){
        int cur = i;
        int sz = 0;
        bool found = false;
        while (vis[cur] == 0){
            sz++;
            vis[cur] = 1;
            cur = p[cur];
            found = true;
        }
        if (found){
            ans.push_back(sz);
        }
    }

    sort(ans.begin(), ans.end());
    ll res = 0;
    if (ans.size() >= 2){
        ll tot = ans[ans.size() - 1] + ans[ans.size() - 2];
        res += tot * tot;
        ans.pop_back(); ans.pop_back();
    }

    for (int i = 0; i < ans.size(); i++){
        res += (ll)ans[i] * ans[i];
    }

    cout << res << endl;
   
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