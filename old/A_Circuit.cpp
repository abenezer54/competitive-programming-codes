#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    vector<int> a(n * 2);
    for (auto &x: a) cin >> x;
    int cnt = 0;
    for (auto x: a) {
        if (x) 
        cnt++;
    }
    // cout << cnt << endl;
    int mn = (cnt / 2) + ((2 * n - cnt) / 2);
    int mx = min(cnt, 2 * n - cnt);
    cout <<n -  mn << ' ' << mx<< '\n';


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