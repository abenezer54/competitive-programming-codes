#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;

    vector<string> s(n), t(m);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> t[i];
    }


    for (int i = 0; i + m - 1 < n; i++) {
        for (int j = 0; j + m - 1 < n; j++) {
            bool ok = true;
            for (int ii = i; ii < i + m; ii++){
                for (int jj = j; jj < j + m; jj++) {
                    if (s[ii][jj] != t[ii - i][jj - j]) {
                        ok = false;
                    }
                }
            }
            if (ok) {
                cout << i + 1 << ' ' << j + 1 << endl;
                return;
            }
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