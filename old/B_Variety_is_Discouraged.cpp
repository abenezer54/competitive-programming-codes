#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector<int> cnt(n + 1);
    vector<int> idx(n + 1);

    for (int i = 0; i < n; i++) {
        cnt[a[i]]++;
        idx[a[i]] = i;
    }
    vector<int> arr;
    for (int i = 1; i <= n; i++) {
        if (cnt[i] == 1) {
            arr.push_back(idx[i]);
        }
    }
    if (arr.size() == 0) {
        cout << 0 << endl;
        return;
    }

    sort(arr.begin(), arr.end());
    int ln = 1;
    int left = arr[0] + 1, right = arr[0] + 1;
    int cur = 1;
    arr.push_back(n + 2);
    // cout << arr << endl;
    // cout << left << ' ' << right << endl;
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] - arr[i - 1] == 1) {
            cur++;
        } else {
            if (cur > ln) {
                right = arr[i - 1] + 1;
                left = arr[i - cur] + 1;
                ln = cur;
            }
            cur = 1;
        }
    }

    cout << left << ' ' << right << endl;
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