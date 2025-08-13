#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<array<int, 2>> seg(n);

    for (int i = 0; i < n; i++) {
        int l, r; cin >> l >> r;
        seg[i][0] = l;
        seg[i][1] = r;
    }


    auto check = [&] (int k) {
        int prevl = 0;
        int prevr = 0;
        for (auto[l, r]: seg) {
            prevl -= k;
            prevr += k;
            if (prevl > r || prevr < l) return false;
            prevl = max(prevl, l);
            prevr = min(prevr, r);
        }
        return true;
    };


    int low = 0;
    int high = 1e9;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) high = mid - 1;
        else low = mid + 1;
    }
    cout << low << endl;

   
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