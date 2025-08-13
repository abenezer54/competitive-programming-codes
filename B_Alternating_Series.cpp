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

    int off = 0;
    if (n % 2 == 0) {
        off = 1;
    }
    vector<int> ans;
    for (int i = 0; i < n - off; i++) {
        if (i & 1) {
            ans.push_back(3);
        } else {
            ans.push_back(-1);
        }
    }
    if (off) {
        ans.push_back(2);
    }


    for (auto val : ans) {
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