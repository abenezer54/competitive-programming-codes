#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
   int n, k; cin >> n >>  k;
   vector<int> a(k);
   for(int i = 0; i < k; i++){
        cin >> a[i];
   }
   sort(a.rbegin(), a.rend());
   ll cat = 0;
   int ans = 0;
   for (int i = 0; i < k; i++){
        if (cat >= a[i]){
            break;
        }
        int need = n - a[i];

        ans++;
        cat += need;        
        
   }
   cout << ans << endl;
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