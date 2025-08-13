#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string s; cin >> s;
    int n = s.size();
    if (count(s.begin(), s.end(), '1') != n){
        for (int i = 0; i < n; i++){
            s.push_back(s[i]);
        }
    } else {
        cout << (ll) n * n << endl;
        return;
    }
    int mx = 0;
    int cur = 0;
    for (int i = 0; i < n * 2; i++){
        if (s[i] == '1'){
            cur += 1;
        } else {
            cur = 0;
        }
        mx = max(mx, cur);
    }
    if (mx & 1){
        int val = mx / 2 + 1;
        cout << (ll) val * val << endl;
    } else {
        int val = mx / 2;
        cout << (ll) val * (val + 1) << endl;
    }
   
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