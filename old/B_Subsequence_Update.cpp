#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, l, r; cin >> n >> l >> r;
    vector<int> a(n);

    for (int i = 0; i < n; i++){
        cin >> a[i];
    } 
    
    cout << a << '\n';

   
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