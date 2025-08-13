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

    vector<int> ans = {1};
    
    for (int i = 2; i <= n; i++) {
        ans.push_back(1);
        while (ans.size() >= 2 && ans[ans.size() - 2]  == ans.back()) {
            ans.pop_back();
            ans[ans.size() - 1]++;
        }
    }
    for (auto val: ans) {
        cout << val << ' ';
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