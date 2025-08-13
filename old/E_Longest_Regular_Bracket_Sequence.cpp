#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string s; cin >> s;
    int n = s.size();
    
    int ans = 0;
    int cnt = 1;
    vector<int> stk;
    vector<int> prev(n + 1, 0);
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            stk.push_back(i);
        } else {
            if (stk.empty()) {
                prev[i + 1] = 0;
            } else {
                int top = stk.back();
                int cur = i - top + 1;
                stk.pop_back();
                if (cur + prev[top] > ans) {
                    ans = cur + prev[top];
                    cnt = 1;
                } else if (cur + prev[top]  == ans) {
                    cnt += 1;
                }
                prev[i + 1] = cur + prev[top];
            }
        }
    }

    cout << ans << ' ' << cnt << endl;
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