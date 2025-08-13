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
    for (int i = 0; i < n; i++) cin >> a[i];

    map<int, int> cnt;
    for (auto val: a) cnt[val]++;

    vector<array<int, 2>> temp;
    for (int i = 0; i < n; i++) {
        if (cnt[a[i]] == 1) {
            temp.push_back({a[i], i + 1});
        }
    }
    
    sort(temp.rbegin(), temp.rend());
    if (temp.size() == 0) cout << -1 << endl;
    else cout << temp[0][1] << endl;
   
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