#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for(auto &x: a) cin >> x;
    sort(a.begin(), a.end());
    vector<int> b;
    for (int i = 0; i < n - 1; i++){
        b.push_back(a[i + 1] - a[i]);
    }
    
    // cout << a << endl;
    int gcd = b[0];
    for (int i = 1; i < n - 1; i++){
        gcd = __gcd(gcd, b[i]);
    }
    cout << (gcd != 0 ? gcd : -1) << endl;

    
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