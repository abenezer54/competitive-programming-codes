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

    vector<int> cnt(n + 1);
    for (auto x: a){
        cnt[x]++;
    }
    for (int i = 0; i < n; i++){
        cnt[i + 1] += max(0, cnt[i] - 2);
        if (cnt[i] == 1){
            cout << "No" << endl;
            return;
        }
    } 
    if (cnt[n] & 1){
        cout << "No" << endl;
    } else {
        cout << "Yes" << endl;
    }
   
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