#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    string s; cin >> s;
    int ans = s.size();
    for (int i = 0; i < s.size() - 1; i++){
        if (s[i] == s[i + 1]){
            ans = 1;
        }
    }
    cout << ans << '\n';
   
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