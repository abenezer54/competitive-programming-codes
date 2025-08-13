    #include "bits/stdc++.h"
    #ifndef ONLINE_JUDGE
    #include "debug/debug.h"
    #endif
    using namespace std;
    #define endl '\n'
    typedef long long ll;
    const int MOD = 1e9 + 7;

    void solve() {
        ll n, w; cin >> n >> w;
        vector<vector<array<ll, 2>>> a(w);
        for (ll i = 0; i < n; i++) {
            ll x, y ; cin >> x >> y;
            --x; --y;
            a[x].push_back({y, i + 1});
        }

        for (ll i = 0; i < w; i++) {
            sort(a[i].rbegin(), a[i].rend());
        }

        map<ll, ll> mp;
        ll time = 0;
        while (true) {
            bool valid = true;
            ll mx = 0;
            vector<ll> temp;
            for (ll i = 0; i < w; i++) {
                if (a[i].empty()) {
                    valid = false;
                    break;
                }
                auto last = a[i].back();
                temp.push_back(last[1]);
                a[i].pop_back();
                mx = max(mx, last[0]);
            }
            if (!valid) {
                break;
            }
            time = mx;
            for (int i = 0; i < w; i++) {
                mp[temp[i]] = time;
            }
        }


        ll q; cin >> q;
        for (ll i = 0; i < q; i++) {
            ll T, A; cin >> T >> A;
            if (!mp.count(A)) {
                cout << "Yes" << endl;
            } else {
                if (mp[A] < T) {
                    cout << "No" << endl;
                } else {
                    cout << "Yes" << endl;
                }
            }
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