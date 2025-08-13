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
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }   

    int x = a[0] % 2, y = a[1] % 2;
    for (int i = 2; i < n; i++) {
        if (i & 1 && (a[i] % 2 != y)) {
            cout << "NO" << endl;
            return;
        }
        if (!(i & 1) && (a[i] % 2 != x)) {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
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