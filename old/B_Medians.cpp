#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, k;
    cin >> n >> k;
    int left = k - 1;
    int right = n - k;

    int p1 = left & 1, p2 = right & 1;
    // cout << "here " << p1 << p2 << endl; 
    if (n == 1) {
        cout << 1 << endl;
        cout << 1 << endl;
        return;
    }
    if (p1 != p2 || right == 0 || left == 0){
        cout << -1 << endl;
        return;
    }

    if (p1 & 1) {
        cout << 3 << endl;
        cout << 1 << ' ' << k << ' '<< k + 1 << endl;
    
    } else {
        cout << 5 << endl;
        cout << 1 << ' ' << 2 << ' ' << k << ' '<< k + 1 << ' '<< k + 2 << endl;
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