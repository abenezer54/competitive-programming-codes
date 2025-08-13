#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, k; cin >> n >> k;
    unordered_map<int, int> mp;
    for(int i = 0; i < k; i++){
        int x, y; cin >> x >> y;
        mp[x] += y;

    }
    vector<int> a;
    
    for (auto &pair: mp){
        a.push_back(pair.second);
    }
    
    sort(a.begin(), a.end(), greater<>());
    // cout << a << endl;
    int ans = 0;
    for (int i = 0; i < min(n, int(a.size())); i++){
        ans += a[i];
    }
    cout << ans << '\n';

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