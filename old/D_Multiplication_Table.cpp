    #include "bits/stdc++.h"
    #ifndef ONLINE_JUDGE
    #include "debug/debug.h"
    #endif
    using namespace std;
    #define endl '\n'
    typedef long long ll;
    const int MOD = 1e9 + 7;

    void solve() {
        ll n, m, k; cin >> n >> m >> k;
        
        auto check = [&] (ll mid) {
            ll cnt = 0;
            for (int row = 1; row <= n; row++) {
                cnt += min(m, mid / row);
            }
            return cnt >= k;
        };

        ll low = 1;
        ll high = n * m;
        while (low <= high) {
            ll mid = low + (high - low) / 2;
            if (check(mid)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        cout << low << endl;
    
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