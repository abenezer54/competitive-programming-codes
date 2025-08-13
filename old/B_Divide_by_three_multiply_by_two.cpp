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
    vector<ll> a(n);
    map<ll, int> cnt;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        cnt[a[i]]++;
    }
    vector<array<ll, 3>> temp; 

    for (int i = 0; i < n; i++) {
        ll prev = a[i];
        int cnt = 0;
        while (a[i] % 3 == 0 && a[i] > 0) {
            cnt++;
            a[i] /= 3;
        }
        int two = 0;
        while (a[i] % 2 == 0 && a[i] > 0) {
            two++;
            a[i] /= 2;
        }
        temp.push_back({cnt, -two, prev});
    }
    
    sort(temp.begin(), temp.end());
    ll cur = temp.back()[2];
    vector<ll> ans = {};
    while (ans.size() < n) {
        ans.push_back(cur);
        if (cur % 3 == 0 && cnt[cur / 3] > 0) {
            cur = cur / 3;
            cnt[cur]--;
        } else {
            cur = cur * 2;
            cnt[cur]--;
        }
    }



    for (auto val: ans) {
        cout << val << ' ';
    }

    cout << endl;

    


   
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