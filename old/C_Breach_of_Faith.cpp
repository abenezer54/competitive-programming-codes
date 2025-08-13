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
    n *= 2;
    vector<int> b(n);
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    sort(b.begin(), b.end());
    ll tot = 0;
    for (int i = 0; i < n - 2; i += 2) {
        tot += b[i + 1] - b[i];
    }

    ll r = b[n - 1] - tot;
    cout << b[n - 1] << ' ' << b[n - 2] + r << ' ';
    
    reverse(b.begin(), b.end());
    for (int i = 1; i < n; i++) {
        cout << b[i] << ' ';
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