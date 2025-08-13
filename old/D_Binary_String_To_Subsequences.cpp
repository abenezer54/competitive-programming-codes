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
    string s; cin >> s;

    vector<int> ones, zeros;
    int cur = 1;
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') {
            if (zeros.empty()) {
                ones.push_back(cur);
                ans.push_back(cur);
                cur++;
            } else {
                int last = zeros.back(); zeros.pop_back();
                ans.push_back(last);
                ones.push_back(last);
            }
        } else {
            if (ones.empty()) {
                zeros.push_back(cur);
                ans.push_back(cur);
                cur++;
            } else {
                int last = ones.back(); ones.pop_back();
                ans.push_back(last);
                zeros.push_back(last);
            }

        }
    }
    cout << cur - 1 << endl;

    for (int val: ans) {
        cout << val << ' ';
    }
    cout << endl;
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