#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int N, R, C; cin >> N >> R >> C;
    string s; cin >> s;

    set<array<int, 2>> prev;
    prev.insert({0, 0});
    vector<int> ans(N, 0);
    
    int r = 0, c = 0;
    for (int i = 0; i < N; i++) {
        if (s[i] == 'N') r--;
        if (s[i] == 'S') r++;
        if (s[i] == 'E') c++;
        if (s[i] == 'W') c--;
        int tr = r - R, tc =  c - C;

        if (prev.count({tr, tc})) ans[i] = 1;
        prev.insert({r, c});
    }

    for (auto val: ans) {
        cout << val;
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