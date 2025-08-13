#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

vector<int> primeFactors(int n) {
    vector<int> primfac;
    for (int i = 2; i * i <= n; ++i) {
        while (n % i == 0) {
            primfac.push_back(i);
            n /= i;
        }
    }
    if (n > 1) {
        primfac.push_back(n);
    }
    return primfac;
}

void solve() {
    int a, b, k;
    cin >> a >> b >> k;

    vector<int> x = primeFactors(a);
    vector<int> y = primeFactors(b);

    map<int, int> ca, cb;
    for (int val : x) {
        ca[val]++;
    }
    for (int val : y) {
        cb[val]++;
    }

    set<int> seen;
    int need = 0, aa = 0, bb = 0;

    for (auto& [key, val] : ca) {
        if (seen.find(key) == seen.end()) {
            seen.insert(key);
            int w = val;
            int z = cb[key];
            if (w != z) {
                need++;
                int diff = abs(w - z);
                if (w > z) {
                    aa += diff;
                } else {
                    bb += diff;
                }
            }
        }
    }

    for (auto& [key, val] : cb) {
        if (seen.find(key) == seen.end()) {
            seen.insert(key);
            int w = val;
            int z = ca[key];
            if (w != z) {
                need++;
                int diff = abs(w - z);
                if (w > z) {
                    bb += diff;
                } else {
                    aa += diff;
                }
            }
        }
    }

    int tot = 0;
    if (aa) tot++;
    if (bb) tot++;

    if (k < tot || k > (int)(x.size() + y.size())) {
        cout << "NO\n";
        return;
    }
    if (tot == 0 && k == 1) {
        cout << "NO\n";
        return;
    }

    cout << "YES\n";
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
