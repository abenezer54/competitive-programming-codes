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
    vector<array<int, 3>> a, b, arr;
    for (int i = 0; i < n; i++) {
        int l, r; cin >> l >> r;
        a.push_back({l, -r, i});
        b.push_back({-r, l, i});
        arr.push_back({l, r});
    }

    map<array<int, 2>, int> left_val, right_val;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    vector<array<int, 2>> stk;
    for (int i = 0; i < n; i++) {
        int l = a[i][0], r = -a[i][1];
        while (!stk.empty() && stk.back()[1] < r) {
            stk.pop_back();
        }
        if (!stk.empty()) {
            left_val[array<int, 2>{l, r}] = l - stk.back()[0];
        }
        stk.push_back({l, r});
    }

    stk.clear();
    for (int i = 0; i < n; i++) {
        
        int r = -b[i][0], l = b[i][1];

        while (!stk.empty() && stk.back()[0] > l) {
            stk.pop_back();
        }

        if (!stk.empty()) {
            right_val[array<int, 2>{l, r}] = stk.back()[1] - r;
        }
        
        stk.push_back({l, r});
    }

    // vector<int> ans(n);
    for (int i = 0; i < n; i++) {
        ll ans = left_val[{arr[i][0],  arr[i][1]}] + right_val[{arr[i][0],  arr[i][1]}];
        cout << ans << endl;
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