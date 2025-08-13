#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    vector<int> idx(n + 1);
    for (int i = 0; i < n; i++){
        cin >> a[i];
        idx[a[i]] = i;
    }

    string ans = "1";
    int mx = idx[1], mn = idx[1];
    int distance;
    for (int num = 2; num <= n; num++){
        if (mn < idx[num] && mx > idx[num]){
            distance = abs(idx[num] - mn) + abs(idx[num] - mx) + 1;
        } else if (mn > idx[num]){
            distance = abs(idx[num] - mx) + 1;
        } else {
            distance = abs(idx[num] - mn) + 1;
        }
        if (distance == num){   
            ans += '1';
        } else {
            ans += '0';
        }
        mx = max(mx, idx[num]);
        mn = min(mn, idx[num]);
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