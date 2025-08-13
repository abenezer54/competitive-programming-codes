#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    int diff = 0;

    for (int i = 0; i < n; i++){
        cin >> a[i];
        diff += (a[i] & 1 ? 1: -1);
    }

    if (abs(diff) > 1) {
        cout << "-1\n";
        return;
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