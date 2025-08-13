#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
   ll n, k; cin >> n >> k;
   string s; cin >> s;
   vector<ll> a(n);


    for (ll i = 0; i < n; i++) {
        cin >> a[i];
    }
    s.push_back('R');

    // cout << a << endl;
    // cout << s << endl;
    auto check = [&] (ll mid) {
        
        ll mx = 0;
        ll tot = 0;
        vector<int> temp;
        for (int i = 0; i <= n; i++) {
            if (s[i] == 'B') {
                mx = max(mx, a[i]);
            } else {
                if (i > 0 && s[i - 1] == 'B') {
                    if (mx > mid) {
                        tot++;
                        temp.push_back(i - 1);
                    }
                }
                mx = 0; 
            }
        }
        
        if (tot <= k) {
            return true;
        }

        vector<ll> tt;
        for (int i = 0; i < temp.size() - 1; i++) {
            ll mx = 0; 
            for (int j = temp[i] + 1; j < temp[i + 1]; j++) {
                if (s[j] == 'R') {
                    mx = max(mx, a[j]);
                }
            }
            tt.push_back(mx);
        }
        sort(tt.begin(), tt.end());
        for (int i = 0; i < tt.size(); i++) {
            if (tt[i] <= mid) {
                tot--;
            }
        }
        return tot <= k;

    };

    // check(4);
   ll l = -1, r = 1e18;
   while (l + 1 < r) {
        ll mid = l + ((r - l) / 2);
        if (check(mid)) {
            r = mid;
        } else {
            l = mid;
        }
   }

    cout << r << endl;
   
 

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