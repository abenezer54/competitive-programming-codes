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
    string s; cin >> s;
    set<char> cnt = {s.begin(), s.end()};
    if (cnt.size() == 1) {
        cout << "NO" << endl;
        return;
    }
    
    int need = 1;
    for (int i = 0; i < n / 2; i++) {
        if (s[i] > s[n - i - 1]) {
            need = 1;
            break;
        }
        if (s[i] < s[n - i - 1]) {
            need = 0;
            break;
        }
    }

    if (need <= k) cout <<"YES" << endl;
    else cout << "NO" << endl;

   
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