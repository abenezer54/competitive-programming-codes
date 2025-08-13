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
    vector<int> a;
    for (int i = 0; i < n; i++) {
        int c; cin >> c;
        if (!a.size() || a.back() != c) a.push_back(c);
    }
    n = a.size();

    function<int(int, int)> dp = [&] (int l, int r) {

        for (int i = l)

    };
   
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