#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const ll MOD = 1e9 + 7;


void solve() {
    ll a, b; cin >> a >> b;
    ll g = gcd(a, b);
    a /= g;
    b /= g;
    ll x = 0;
    while (a != 1) {
        x++;
        if (a % 2 == 0) {
            a /= 2;
        } else if (a % 3 == 0) {
            a /= 3;
        } else if (a % 5 == 0) {
            a /= 5;
        } else {
            break;  
        }
    }

    while (b != 1) {
        x++;        
        if (b % 2 == 0) {
            b /= 2;
        } else if (b % 3 == 0) {
            b /= 3;
        } else if (b % 5 == 0) {
            b /= 5;
        } else {
            break;
        }
    }
    if (a != 1 || b != 1) {
        cout << -1 << endl;
    } else {
        cout << x << endl;
    }
    
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ll t = 1;
    // cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}