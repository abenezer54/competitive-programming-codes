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
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int first = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            first = i;
            break;
        }
    }
    int last = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            last = i;
        }
    }

    if (first == -1) {
        cout << 1 << endl;
        cout << 1 << ' ' << n << endl;
        return;
    }
    if (last - first + 1 == n) {
        cout << 3 << endl;
        cout << "1 2" << endl;
        cout << 2 << ' ' << n - 1 << endl;
        cout << "1 2" << endl;
        return;
    }

    if (first != last) {
        cout << 2 << endl;
        cout << first + 1 << ' ' << last + 1 << endl;
        n -= last - first;
        cout << 1 << ' ' << n << endl;
    
    } else {
        if (first + 1 < n) {
            cout << 2 << endl;
            cout << first + 1 << " " << first + 2 << endl;
            cout << 1 << ' ' << n - 1 << endl;
        } else {
            cout << 2 << endl;
            cout << first << ' ' << first + 1 << endl;
            cout << 1 << ' ' << n - 1 << endl;
        }
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