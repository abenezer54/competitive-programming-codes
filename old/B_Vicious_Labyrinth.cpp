#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, k; cin >> n >> k;
    vector<int> a(n);

    a[n - 1] = n - 1;
    a[n - 2] = n;
    for (int i = 0; i < n - 2; i++) {
        if (k & 1) {
            a[i] = n;
        } else {
            a[i] = n - 1;
        }
    }
    for (auto val: a) {
        cout << val << ' ';
    }
    cout << endl;
   
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