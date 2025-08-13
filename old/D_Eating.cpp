#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

vector<int> convert(int val) {
    vector<int> res;
    for (int bit = 30; bit >= 0; bit--) {
        if (1 << bit <= val) {
            res.push_back(1);
            val -= (1 << bit);
        } else {
            res.push_back(0);
        }
    }
    reverse(res.begin(), res.end());
    return res;
}

void solve() {
    int n, q;
    cin >> n >> q;
    vector<ll> w(n);
    for (int i = 0; i < n; i++) {
        cin >> w[i];
    }

    vector<vector<int>> prefix;
    prefix.push_back(convert(0));
    for (int i = n - 1; i >= 0; i--) {
        prefix.push_back(convert(w[i]));
    }
    prefix.push_back(convert((1 << 30) - 1));
    prefix.push_back(convert((1 << 30) - 1));

    for (int i = 1; i < prefix.size(); i++) {
        for (int bit = 0; bit <= 30; bit++) {
            prefix[i][bit] += prefix[i - 1][bit];
        }
    }

    auto win_search = [&](int w, int bit, int pro) {
        int l = w, r = pro;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (prefix[mid][bit] - prefix[w][bit] == 0) {
                l = mid;
            } else {
                r = mid;
            }
        }
        return l;
    };

    auto end_search = [&](int w, int bit, int pro) {
        int l = w, r = pro;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (prefix[mid][bit] - prefix[w][bit] >= 2) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return r;
    };

    auto end_search2 = [&](int w, int bit, int pro) {
        int l = w, r = pro;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (prefix[mid][bit] - prefix[w][bit] >= 1) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return r;
    };

    vector<int> ans;
    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;
        auto cur = convert(x);

        int win = 0;
        int end = n + 1;
        for (int bit = 30; bit >= 0; bit--) {
            if (cur[bit] == 1) {
                if (prefix[win][bit] & 1) {
                    auto new_end = end_search2(win, bit, end);
                    end = min(end, new_end);
                } else {
                    auto w = win_search(win, bit, end);
                    win = max(win, w);
                    auto new_end = end_search(win, bit, end);
                    end = min(end, new_end);
                }
            } else {
                if (prefix[win][bit] & 1) {
                    auto w = win_search(win, bit, end);
                    win = max(win, w);
                    auto new_end = end_search(win, bit, end);
                    end = min(end, new_end);
                } else {
                    auto new_end = end_search2(win, bit, end);
                    end = min(end, new_end);
                }
            }
        }
        ans.push_back(end - 1);
        }

    for (auto val : ans) {
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