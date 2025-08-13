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
    if (n == 1) {
        cout << k << endl;
        return;
    }

    vector<vector<ll>> a(36);
    a[0] = {1};
    for (int i = 1; i < 36; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) {
                a[i].push_back(a[i - 1][j]);
            } else if (j == i) {
                a[i].push_back(a[i - 1][j - 1]);
            }else {
                a[i].push_back(a[i - 1][j - 1] ^ a[i - 1][j]);
            }
        }
    }

    for (int i = 0; i < 36; i++) {
        cout << i + 1<< ' ' << a[i] << endl;
    }
    
   
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