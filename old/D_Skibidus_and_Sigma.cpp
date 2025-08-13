#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, m; cin >> n >> m;
    vector<vector<ll>> a(n, vector<ll>(m));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    auto xx = [m](const vector<ll>& row1, const vector<ll>& row2) {
        ll v1 = 0, v2 = 0;
        ll s1 = 0, s2 = 0;
        for (int j = 0; j < m; j++) {
            v1 += (m - j) * row1[j];
            v2 += (m - j) * row2[j];
            s1 += row1[j];
            s2 += row2[j];
        }
        if (s1 != s2){
            return s1 > s2;
        }
        return v1 > v2; 
    };

    sort(a.begin(), a.end(), xx);

    ll val = n * m;
    ll ans = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            ans += val * a[i][j];
            val--;
        }
    }
    // cout << a << '\n';

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