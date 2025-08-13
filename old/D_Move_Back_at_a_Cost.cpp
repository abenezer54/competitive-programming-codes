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
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }


    vector<int> stk;
    vector<int> temp;
    for (int i = 0; i < n; i++) {
        while (!stk.empty() && stk.back() > a[i]) {
            temp.push_back(stk.back() + 1);
            stk.pop_back();
        }
        stk.push_back(a[i]);
    }

    if (temp.empty()) {
        for (auto val: stk) {
            cout << val << ' ';
        }
        cout << endl;
        return;
    }

    int mn = *min_element(temp.begin(), temp.end());
    int idx = upper_bound(stk.begin(), stk.end(), mn) - stk.begin();
    
    int stp = idx;
    while (idx < stk.size()) {
        temp.push_back(stk[idx] + 1);
        idx++;
    }

    sort(temp.begin(), temp.end());

    for (int i = 0; i < stp; i++) {
        cout << stk[i] << ' ';
    }

    for (auto val: temp) {
        cout << val << ' ';
    }

    cout << endl; 
   
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
