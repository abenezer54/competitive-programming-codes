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
    vector<ll> a(n);

    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a.rbegin(), a.rend());
    
    ll red = 0;
    ll blue = a[n - 1];
    int l = 0;
    int r = n - 2;
    while (l < r) {
        red += a[l];
        blue += a[r];
        if (red > blue) {
            cout << "YES" << endl;
            return;
        }
        l += 1;
        r -= 1;
    }
    cout << "NO" << endl;
   
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