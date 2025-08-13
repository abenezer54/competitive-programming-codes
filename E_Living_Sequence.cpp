#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll k; cin >> k;
    vector<int> ans;
    while (k) {
        ans.push_back(k % 9);
        k /= 9;
    }
    
    string res = "";
    for (int i = ans.size() - 1; i >= 0; i--) {
        if (ans[i] > 3) 
            ans[i]++;
        res += to_string(ans[i]);
    }

    cout << res << endl;
   
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