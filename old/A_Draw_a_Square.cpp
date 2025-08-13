#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    set<int> val;
    for (int i = 0; i < 4; i++) {
        int x; cin >> x;
        val.insert(x);
    }
    if (val.size() == 1) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
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