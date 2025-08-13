#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (auto &x: a) cin >> x;
    unordered_map<int, int> last;
    vector<int> b(n, -1);


    for (int i = 0; i < n; i++){
        if(last.count(a[i])){
            b[i] = last[a[i]];
        }
        last[a[i]] = i + 1;
    }
     
    for (auto x: b) {
        cout << x << ' ';
    }
    cout << '\n';

    
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