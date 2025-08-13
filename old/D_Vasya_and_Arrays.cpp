#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
   
    int m; cin >> m;
    vector<int> b(m);

    for (int j = 0; j < m; j++){
        cin >> b[j];
    }

    int i = 0, j = 0;
    ll a_sum = 0, b_sum = 0;
    int ans = 0;
    while (i < n && j < m){
        if (a_sum == b_sum){
            ++ans;
            a_sum = 0; b_sum = 0;
            a_sum += a[i]; b_sum += b[j];
            i++; j++; 

        } else if (a_sum < b_sum){
            a_sum += a[i];
            i++;
        } else {
            b_sum += b[j];
            j++;
        }   
    }

    
    while (i < n){
        a_sum += a[i];
        i++;
    }
    while (j < m){
        b_sum += b[j];
        j++;
    }
    
    if (a_sum != b_sum){
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }

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