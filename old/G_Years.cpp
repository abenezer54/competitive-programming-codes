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
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int a, b; cin >> a >> b;
        mp[a]++;
        mp[b]--;
    }
    vector<array<int,2>> p;
    
    for (auto [a, b]: mp) {
        p.push_back({a, b});
    }
    sort(p.begin(), p.end());

    
    for (int i = 1; i < p.size(); i++) {
        p[i][1] += p[i - 1][1];
    }
    int y = -1;
    int k = 0;
    for (int i = 0; i < p.size(); i++) {
        if (p[i][1] > k) {
            y = p[i][0];
            k = p[i][1];
        }
    }

    cout << y << " " << k << endl;
   
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