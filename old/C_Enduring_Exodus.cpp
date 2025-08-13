    #include "bits/stdc++.h"
    #ifndef ONLINE_JUDGE
    #include "debug/debug.h"
    #endif
    using namespace std;
    #define endl '\n'
    typedef long long ll;
    const int MOD = 1e9 + 7;

    void solve() {
        int n, k; cin >> n >> k;
        string s; cin >> s;
        vector<int> p(n + 1);
        for (int i = 0; i < n; i++) {
            p[i + 1] = p[i] + (s[i] == '0');
        }
        // cout << p << endl;

        auto check = [&] (int mid) {
            for (int i = 0; i < n; i++) {
                if (s[i] == '1') continue;

                int left = p[i] - p[max(i - mid, 0)];
                int right = p[min(i + mid + 1, n)] - p[i + 1];
                if (left + right >= k) return true;
            }
            return false;
        };

        int low = 0;
        int high = 1e9;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            // cout << low << ' ' << high << endl;
            if (check(mid)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        // cout << check(1) << endl;
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