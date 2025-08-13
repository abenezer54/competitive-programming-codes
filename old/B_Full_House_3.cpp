#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    vector<int> cnt(15);
    for (int i = 0; i < 7; i++) {
        int x; cin >> x;
        cnt[x] += 1;
    }

    sort(cnt.rbegin(), cnt.rend());

    if (cnt[0] > 2 && cnt[1] > 1) cout << "Yes" << endl;
    else cout << "No" << endl;
   
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