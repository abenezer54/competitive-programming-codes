#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;

    vector<string> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
   
    int sz = 0;
    int ans = 0;

    for (int i = 0; i < n; i++){
        if (sz + a[i].size() <= m){
            sz += a[i].size();
            ans++;
        } else {
            break;
        }
    }


    cout << ans << "\n";
   
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