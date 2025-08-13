#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; int d;
    cin >> n >> d;
    int dd = d;
    for (int x = 2; x <= n && x <= 9; x++) {
        d *= x;
    }

    vector<int> ans = {1};
    for (int x = 3; x <= 9; x += 2) {
        if (x == 0) {
            if (d % 3 == 0) {
                ans.push_back(x);
            }
        } else if (x == 5) {
            if (dd % 3 == 0) {
                ans.push_back(x);
            }
        } else if (x == 7) {
            if (dd % 7 == 0) {
                ans.push_back(x);
            }
        } else {
            if (d % 9 == 0) {
                ans.push_back(x);
            }
        }
    }
    for (auto val: ans) {
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