#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    vector<int> a(4);
    for (auto &x: a) cin >> x;
    unordered_map<int, int> mp;
    for (int i = 0; i < 4; i++){
        mp[a[i]]++;
    }
    int ans = 0;

    for (auto pair: mp){
        ans  += pair.second / 2;
    }
     
    cout << ans << '\n';
    
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