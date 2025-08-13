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
    int n = s.size();

    for (int i = 0; i < n; i++) {
        vector<pair<int, int>> temp;
        auto idx = i;
        auto val = s[i];
        for (int j = i; j < min(n, i + 9); j++){
            auto cur_val = (s[j] - '0') - (j - i);
            if (cur_val + '0' > val) {
                val = cur_val + '0';
                idx = j;
            }
        }
        
        while (idx > i){
            s[idx] = s[idx - 1];
            s[idx - 1] = val;
            idx--;
        }
    }
    
    cout << s << endl;
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