#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;


void solve() {
    int n; cin >> n;
    string s; cin >> s;
    int sz = s.size();
    vector<int> p(15);
    for (int i = 0; i <= 13; i++) {
        p[i] = pow(3, i);
    }

    function<array<int, 2>(int, int)> f = [&] (int cur, int idx) {
        if (cur == 0) {
            return array<int, 2>{s[idx] - '0', 1};
        }

        int second = idx + p[cur - 1];
        int third = idx + 2 * p[cur - 1];

        auto val1 = f(cur - 1, idx);
        auto val2 = f(cur - 1, second);
        auto val3 = f(cur - 1, third);

        vector<int> ones, zeros;
        (val1[0] == 1 ? ones.push_back(val1[1]) : zeros.push_back(val1[1]));
        (val2[0] == 1 ? ones.push_back(val2[1]) : zeros.push_back(val2[1]));
        (val3[0] == 1 ? ones.push_back(val3[1]) : zeros.push_back(val3[1]));
        
        sort(ones.begin(), ones.end());
        sort(zeros.begin(), zeros.end());

        if (ones.size() == 3) {
            return array<int, 2> {1, ones[0] + ones[1]};
        } else if (ones.size() == 2) {
            return array<int, 2> {1, ones[0]};
        } else if (ones.size() == 1) {
            return array<int, 2> {0, zeros[0]};
        } else {
            return array<int, 2> {0, zeros[0] + zeros[1]};
        }
   
    };

    cout << f(n, 0)[1] << endl;
    
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