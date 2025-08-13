#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
int n, x;

// vector<vector<int>> memo(n + 10, vector<int>(x + 10, -1));
void solve() {
    cin >> n >> x;
    vector<int> price(n);
    vector<int> pages(n);
    
    for(auto &x: price) cin >> x;
    for(auto &x: pages) cin >> x;
   for(int i = 0; i < n; i++){
        cin >> price[i] >> pages[i];
    }

    vector<ll> dp(x + 1);
    for (int i = 0; i < n; i ++){
        for(int j = x; j >= 0; j--){
            if(j - price[i] >= 0){
                dp[j] = max(dp[j], dp[j - price[i]] + pages[i]);
            }
        }
    }
    cout << dp[x] << '\n';
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