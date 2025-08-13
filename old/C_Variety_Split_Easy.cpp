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
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }   

    map<int, int> cnt;
    for (auto val: a) {
        cnt[val] += 1;
    }

    int ans = cnt.size();
    set<int> cur;
    for (int i = 0; i < n; i++) {
        cnt[a[i]]--;
        cur.insert(a[i]);
        if (cnt[a[i]] == 0) {
            cnt.erase(a[i]);
        }
        ans = max(ans, (int)(cur.size() + cnt.size()));

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