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
    vector<int> a(n); 
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    auto temp = a;
    sort(temp.rbegin(), temp.rend());
    map<int, int> cnt;
    for (auto val: temp) {
        cnt[val]++;
    }
    
    map<int, int> ans;
    int r = 1;
    for (auto val: temp) {
        if (ans.count(val) == 0) {
            ans[val] = r;
            r+= cnt[val];
        }
    }
    for (auto val: a) {
        cout << ans[val] << endl;
    }

   
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