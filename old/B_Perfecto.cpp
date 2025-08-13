#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
   ll n; cin >> n;
   auto f = [](ll n) {
        int s = sqrt(n);
        return 1LL * s * s == n;     
   };

   if (f((n * (n + 1)) / 2)) {
    cout << "-1\n";
    return;
   }


   vector<int> ans(n);
   iota(ans.begin(), ans.end(), 1);

   for (ll i = 0; i < n - 1; i++) {
        if (f(((i + 1) * (i + 2)) / 2)) {
            swap(ans[i], ans[i + 1]);
        }
   }

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