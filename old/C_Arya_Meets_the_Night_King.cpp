#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<array<int, 2>> b(m);
    for (int i = 0; i < m; i++) {
        int d, g; cin >> d >> g;
        b[i][0] = d;
        b[i][1] = g;
    }
    vector<int> p(m + 1);
    sort(b.begin(), b.end());

    for (int i = 0; i < m; i++) {
        p[i + 1] = p[i] + b[i][1];
    }


    for (int val: a) {
        int low = 0;
        int high = m - 1;
        while (low <= high){
            int mid = low + (high - low) / 2;
            if (b[mid][0] <= val) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        int idx = upper_bound(b.begin(), b.end(), array<int, 2>{val, INT_MAX},
                      [](const array<int, 2>& x, const array<int, 2>& y) {
                          return x[0] < y[0]; 
                      }) - b.begin();
        cout << p[idx] << ' ';
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