#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
const ll INF = LLONG_MAX;

void solve() {
    ll n; cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    vector<ll> p(n + 1);
    for (int i = 0; i < n; i++) {
        p[i + 1] = a[i] + p[i];
    }
    a.insert(a.begin(), INF);
    

    auto monotonic = [&] () {   
        vector<array<ll, 2>> stk = {{0, INF}};
        for (int i = 1; i <= n; i++) {
            ll mn = INF;
            bool found = false;
            while (a[stk.back()[0]] <= a[i]) {
                mn = min(mn, stk.back()[1]);
                if (a[stk.back()[0] < i - 1]) {
                    mn = min(mn, p[stk.back()[0]]);
                    found = true;
                }
                stk.pop_back();
            }
            if (found && p[i - 1] > min(mn, p[stk.back()[0]])) {
                return true;
            } 
            stk.push_back({i, mn});
        
        }

        return false;
    };  

    if (monotonic()) {
        cout << "NO" << endl;
        return;
    }

    reverse(a.begin(), a.end());
    a.pop_back();
    for (int i = 0; i < n; i++) {
        p[i + 1] = a[i] + p[i];
    }
    a.insert(a.begin(), INF);

    
    if (monotonic()) {
        cout << "NO" << endl;
        return;
    }

    cout << "YES" << endl;
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