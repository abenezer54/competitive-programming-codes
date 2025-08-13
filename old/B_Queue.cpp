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

    vector<int> ans(n, -1);
    vector<array<int, 2>> stk = {{a[n - 1] ,n - 1}};

    for (int i = n - 2; i >= 0; i--) {
        auto top = stk.back();
        if (top[0] < a[i]) {
            int l = -1, r = stk.size() - 1;
            while (l + 1 < r) {
                int mid = l + (r - l) / 2;
                if (stk[mid][0] < a[i]) r = mid;
                else l = mid; 
            }
            ans[i] = stk[r][1] - i - 1;
        }
        
        if (stk.empty() || a[i] < stk.back()[0]) {
            stk.push_back({a[i], i});
        }
    }

    for (auto val: ans) {
        cout << val << ' ';
    }
    cout << endl;
   
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