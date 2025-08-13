#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD =  998244353;
struct MI {
    ll v;
    explicit operator ll() const { return v; }
    MI() { v = 0; }
    MI(ll _v) {
        v = (-MOD < _v && _v < MOD) ? _v : _v % MOD;
        if (v < 0)
            v += MOD;
    }
    friend bool operator==(const MI& a, const MI& b) {
        return a.v == b.v;
    }
    friend bool operator!=(const MI& a, const MI& b) {
        return !(a == b);
    }
    friend bool operator<(const MI& a, const MI& b) {
        return a.v < b.v;
    }
 
    MI& operator+=(const MI& m) {
        if ((v += m.v) >= MOD)
            v -= MOD;
        return *this;
    }
    MI& operator-=(const MI& m) {
        if ((v -= m.v) < 0)
            v += MOD;
        return *this;
    }
    MI& operator*=(const MI& m) {
        v = v * m.v % MOD;
        return *this;
    }
    MI& operator/=(const MI& m) { return (*this) *= inv(m); }
    friend MI pow(MI a, ll p) {
        MI ans = 1;
        assert(p >= 0);
        for (; p; p /= 2, a *= a)
            if (p & 1)
                ans *= a;
        return ans;
    }
    friend MI inv(const MI& a) {
        assert(a.v != 0);
        return pow(a, MOD - 2);
    }
 
    MI operator-() const { return MI(-v); }
    MI& operator++() { return *this += 1; }
    MI& operator--() { return *this -= 1; }
    MI operator++(int) {
        v++;
        if (v == MOD)
            v = 0;
        return MI(v);
    }
    MI operator--(int) {
        v--;
        if (v < 0)
            v = MOD - 1;
        return MI(v);
    }
    friend MI operator+(MI a, const MI& b) { return a += b; }
    friend MI operator-(MI a, const MI& b) { return a -= b; }
    friend MI operator*(MI a, const MI& b) { return a *= b; }
    friend MI operator/(MI a, const MI& b) { return a /= b; }
    friend ostream& operator<<(ostream& os, const MI& m) {
        os << m.v;
        return os;
    }
    friend istream& operator>>(istream& is, MI& m) {
        ll x;
        is >> x;
        m.v = x;
        return is;
    }
};

void solve() {
    int n; cin >> n;
    vector<MI> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    if (n == 1) {
        if (a[0] == 0) {
            cout << 2 << endl;
            return;
        } else {
            cout << 1 << endl;
            return;
        }
    }

    vector<MI> dp(n);
    dp[0] = a[0] == 0; 
    
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i - 1]) dp[i] += dp[i - 1];

        if (i == 1 && a[i] == 1) dp[i]++;

        if (i > 1 && a[i] == a[i - 2] + 1) dp[i] += dp[i - 2];
    }

    MI ans = dp[n - 1];
    ans += (n > 1 ? dp[n - 2]: 0LL);
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