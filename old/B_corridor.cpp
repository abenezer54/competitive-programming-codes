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
   vector<array<int, 2>> a(n);
   for (int i = 0; i < n; i++) {
    cin >> a[i][0] >> a[i][1];
   }
   sort(a.begin(), a.end());
   int k = INT_MAX;
   vector<int> vis(205);

   for (int i = 0; i < n; i++) {
    if (vis[i]) continue;
    vis[i] = 1;

    if (k < a[i][0]) break;
    k = min(k, a[i][0] + ((a[i][1] - 1) / 2));
   }
   cout << k << endl;
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