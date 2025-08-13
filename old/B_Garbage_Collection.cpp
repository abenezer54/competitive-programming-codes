#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        int x, y; cin>> x; cin >> y;
        a[i].first = x;
        a[i].second = y;
    }
    // cout << a << '\n';
    int q; cin >> q;
    for (int i = 0; i < q; i ++) {
        int x, y; cin >> x >> y;

        int m = y % a[x - 1].first;
        // cout << "here" << x << ' ' << y  << ' ' << m << ' ' << a[x - 1]  <<'\n';
        if (m <= a[x - 1].second){
            cout << y + (a[x - 1].second - m) << "\n";
        } else {
            int diff = m - a[x - 1].second;
            cout << y  + a[x - 1].first - diff << '\n';
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