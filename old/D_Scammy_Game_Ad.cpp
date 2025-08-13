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
    vector<array<int, 4>> a;

    for (int i = 0; i < n; i++) {
        char op1, op2;
        int a1, a2;
        cin >> op1 >> a1 >> op2 >> a2;
        array<int, 4> temp;
        temp[0] = (op1 == 'x') ? 1 : 0;
        temp[2] = (op2 == 'x') ? 1 : 0;
        temp[1] = a1; temp[3] = a2;
        a.push_back(temp);
    }

    a.push_back({1, 2, 1, 1});
    ll left = 1, right = 1;
    for (int i = 0; i < n; i++) {
        ll cur = (a[i][0] ? left * (a[i][1] - 1) : a[i][1]);
        cur += (a[i][2] ? right * (a[i][3] - 1) : a[i][3]);

        for (int j = i + 1; j <= n; j++) {
            if (a[j][0] && a[j][2]) {
                if (a[j][1] > a[j][3]) {
                    left += cur;
                    break;
                } else if (a[j][3] > a[j][1]) {
                    right += cur;
                    break;
                }
            } else if (a[j][0]) {
                left += cur;
                break;
            } else if (a[j][2]) {
                right += cur;
                break;
            }
        }
    }

    cout << left + right << endl;
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
