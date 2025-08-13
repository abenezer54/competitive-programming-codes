#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
vector<int> prime_factors(int n) {
    vector<int> f;
    int sq = (int) sqrt(n);
    for (int i = 2; i <= sq; i++) {
        while (n % i == 0) {
            f.push_back(i);
            if (f.size() > 2) {
                return f;
            }
            n /= i;
        }
    }
    if (n > 1) {
        f.push_back(n);
    }
    return f;
}
void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector<int> one_factors(n + 1);
    vector<int> two_factors(n + 1);
    map<pair<int,int>, int> only_same;
    for (auto val: a) {
        auto f = prime_factors(val);
        if (f.size() > 2) continue;
        if (f.size() == 1) {
            one_factors[f[0]]++;
        } else if (f.size() == 2) {
            two_factors[f[0]]++;
            two_factors[f[1]] += f[0] != f[1];
            only_same[{f[0], f[1]}]++;
        }
    }
    ll ans = 0;
    ll d = 0;
    ll tot = accumulate(one_factors.begin(), one_factors.end(), 0LL);
    for (int i = 2; i <= n; i++) {
        d += (ll) one_factors[i] * (tot - one_factors[i]);
        ans += (ll) one_factors[i] * two_factors[i];
    }
    ans += d / 2;

    for (auto&[_, val]: only_same) {
        ans += ((ll)val * (val + 1)) / 2;
    }
    cout << ans << endl;
    

   
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