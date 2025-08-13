    #include "bits/stdc++.h"
    #ifndef ONLINE_JUDGE
    #include "debug/debug.h"
    #endif
    using namespace std;
    #define endl '\n'
    typedef long long ll;
    const int MOD = 1e9 + 7;

    void solve() {
        string s; cin >> s;
        ll twos = 0, threes = 0;
        ll tot = 0;
        for (auto c: s){
            if (c - '0' == 2) twos++;
            else if (c - '0' == 3) threes++;
            tot += c - '0';
        }

        for (int i = 0; i <= threes; i++) {
            for (int j = 0; j <= min(10LL, twos); j++){
                ll temp = tot + (6 * i) + (2 * j);
                if (temp % 9 == 0) {
                    cout << "YES" << endl;
                    return;
                }
            }
        }

        cout << "NO" << endl;
    
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