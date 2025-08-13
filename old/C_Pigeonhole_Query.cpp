#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, q; cin >> n >> q;
    vector<int> nest(n), cnt(n, 1);
    iota(nest.begin(), nest.end(), 0);
    int ans = 0;
    for (int i = 0; i < q; i++) {
        int op; cin >> op;
        if (op  == 2) {
            cout << ans << endl;
            continue;
        }

        int a, b; cin >> a >> b;
        --a; --b;
        int prev = nest[a];
        cnt[prev]--;
        if (cnt[prev] == 1) --ans;
        nest[a] = b;
        cnt[b]++;
        if (cnt[b] == 2) ++ans;
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