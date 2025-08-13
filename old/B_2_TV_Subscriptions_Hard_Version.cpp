#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k, d; cin >> n >> k >> d;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    map<int, int> cnt;
    int l = 0;
    int ans = n;
    for (int r = 0; r < n; r++){
        ++cnt[a[r]];
        if (r >= d - 1){
            ans = min(ans, (int)cnt.size());
            if (--cnt[a[l]] == 0){
                cnt.erase(a[l]);
            }
            l++;
        }
    }

    cout << ans << endl;
   
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
