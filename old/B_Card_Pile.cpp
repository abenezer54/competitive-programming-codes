#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int q; cin >> q;
    vector<int> stk(100, 0);
    for (int i = 0; i < q; i++) {
        int op; cin >> op;
        if (op == 1) {
            int x; cin >> x;
            stk.push_back(x);
        } else {
            cout << stk.back() << endl;
            stk.pop_back();
        }
    } 
   
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    // cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}