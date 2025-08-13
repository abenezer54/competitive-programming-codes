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
    ll last = n;
    for (int i = 0; i < 32; i++) {
        if (x & (1 << i)) continue;

        last = min(last, (ll) 1 << i);
        break;
    }
    vector<ll> ans;
    ll check = 0LL;
    for (ll i = 0; i < last; i++) {
        ans.push_back(i);
        check |= i;
    }
    if (check != x) {
        if (ans.size() == n){
            ans.pop_back();
        }
        ans.push_back(x);
    }

    while (ans.size() != n) {
        ans.push_back(0);
    }
    
    for (auto val: ans) {
        cout << val << " ";
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