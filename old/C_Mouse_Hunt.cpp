#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> c(n);
    vector<int> a(n);

    for (int i = 0; i < n; i++){
        cin >> c[i];
    }
    for (int i = 0; i < n; i++){
        cin >> a[i]; --a[i];
    }

    vector<bool> vis(n);
    vector<int> ind(n);
    ll ans = 0;

    for (int i = 0; i < n; i++){
        if (a[i]== i){
            ans += c[a[i]];
            vis[i] = true;
        } else{
            ind[a[i]]++;
        }
    }

    queue<int> que;
    for (int i = 0; i < n; i++){
        if (vis[i] == false && ind[i] == 0){
            que.push(i);
        }
    }

    while(!que.empty()){
        int node = que.front(); que.pop();
        vis[node] = true;

        ind[a[node]]--;
        if (ind[a[node]] == 0){
            que.push(a[node]);
        }
    }

    for (int i = 0; i < n; i++){
        int mn = 1e5;
        if (vis[i]) continue;
        int cur = i;
        
        while (!vis[cur]) {
            mn = min(mn, c[cur]);
            vis[cur] = true;
            cur = a[cur];
        }
        ans += mn;
    }

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