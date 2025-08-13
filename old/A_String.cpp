#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    string s; cin >> s;
    int cnt = 0;
    for (auto x: s){
        if (x == '1'){
            cnt += 1;
        }
    }
    cout << cnt << '\n';
   
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
