#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
const int INF = 1e9;

void solve() {
    int n; cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int ans = 0;

    int half = n / 2;
    if (n % 2 == 0) {
        half--;
    }

    for (int i = 0; i < half; i++){
        // no change
        int val1 = (a[i] == a[i + 1]) + (a[n - 1 - i] == a[n - 2 - i]);
        // change
        int val2 = (a[i] == a[n - 2 - i]) + (a[n - 1 - i] == a[i + 1]);
        
        ans += min(val1, val2);
    }
    
    if (n % 2 == 0) {
        ans += a[n / 2] == a[n / 2 - 1];
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