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
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int l, r; cin >> l >> r;
        mp[l]++; mp[r + 1]--;
    }   

    vector<int> a;
    for (auto&[x, y]: mp) {
        a.push_back(x);
    }

    sort(a.begin(), a.end());

    for (int i = 1; i < a.size(); i++) {
        mp[a[i]] += mp[a[i - 1]];
    }

    for (auto &[x, y]: mp) {
        if (y > 2) {
            cout << "NO" << endl;
            return;
        }
    }

    cout << "YES" << endl;
   
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