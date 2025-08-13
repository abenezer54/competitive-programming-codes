#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> a(n - 2);
    for (int i = 0; i < n - 2; i++){
        cin >> a[i];
    }
    for (int i = 0; i < n - 4; i++){
        if (a[i] + a[i + 2] == 2 && a[i + 1] == 0){
            cout << "NO\n";
            return; 
        }
    }
    cout << "YES\n";

   
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