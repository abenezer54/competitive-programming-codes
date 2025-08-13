#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, x; cin >> n >> x;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
    }

    priority_queue<array<ll, 2>> pq;
    pq.push({1, 0});
    set<ll> vis = {0};
    ll cur_sum = 0;
    ll ans = -1;

    for (ll i = 0; i < n; i++) {
        cur_sum += a[i];
        int r = cur_sum % x;
        auto [idx, num] = pq.top(); pq.pop();
        idx *= -1;
        if (num == r) {
            if (!pq.empty()) {
                auto [idx2, num2] = pq.top(); pq.pop();
                idx2 *= -1;
                ans = max(ans, i - idx2);
                pq.push({-1 * idx2, num2});
            } 
            pq.push({ -1 * idx, num});
        } else {
            ans = max(ans, i - idx);
            pq.push({-1 * idx, num});
        }

        if (!vis.count(cur_sum % x)) {
            pq.push({-1 * i, r});
            vis.insert(cur_sum % x);
        }

    }
    cout << ans << endl;
   
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