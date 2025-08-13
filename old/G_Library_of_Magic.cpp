#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

ll query(ll l, ll r){
    cout << "xor " << l << ' ' << r << endl;
    ll res; cin >> res;
    if (res == -1)
        exit(0);
    return res;
}

void answer(ll a, ll b, ll c){
    cout << "ans " << a << ' ' << b << ' ' << ' ' << c << endl;
}


void solve() {
    ll n; cin >> n;

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