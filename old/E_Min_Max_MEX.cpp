#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k; cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    auto check = [&] (int mid) {
        int cnt = 0;
        vector<bool> seen(mid, false);
        int remaining = mid;
    
        for (int i = 0; i < n; i++) {
            if (a[i] < mid && !seen[a[i]]) {
                seen[a[i]] = true;
                remaining--;
            }
            if (remaining == 0) {
                cnt++;
                fill(seen.begin(), seen.end(), false);
                remaining = mid;
            }
        }
    
        return cnt >= k;
    };
    

    int low = 0, high = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (check(mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << high << endl;



   
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