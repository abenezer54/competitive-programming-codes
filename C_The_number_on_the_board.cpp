#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int k; cin >> k;
    string s; cin >> s;
    vector<int> a;
    for (auto val: s) {
        a.push_back(val - '0');
    }
    sort(a.begin(), a.end());
    auto tot = accumulate(a.begin(), a.end(), 0);
    int ans = 0;
    for (int i = 0; i < a.size(); i++) {
        if (tot >= k) break;
        tot += 9 - a[i];
        ans++;
    }
    cout << ans << endl;

   
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