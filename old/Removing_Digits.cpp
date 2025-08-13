#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

const int INF = 1e9;


void solve() {
    int n; cin >> n;
    vector<int> dp(n + 1, INF);
   
    dp[0] = 0;
    for (int i = 1; i <= n; i++){
        string s = to_string(i);
        for(char c: s){
            dp[i] = min(dp[i], dp[i - (c - '0')] + 1);
        }
    }
    
    cout << dp[n] << '\n';

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