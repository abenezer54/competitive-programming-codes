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
    if (n == 1) {
        cout << a[0] << endl;
        return;
    }

    sort(a.begin(), a.end());
    auto prev = a[0] + a[1] - 1;
    for (int i = 2; i < n; i++) {
        int cur = prev + a[i] - 1;
        prev = cur;

    } 
    cout << prev << endl;
   
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