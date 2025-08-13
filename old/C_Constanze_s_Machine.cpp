#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

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
    string s; cin >> s;
    s.push_back('a');
    int n = s.size();
    vector<MI>dp(n, 0);
    
    MI ans = 1;

    for (int i = 0; i < n; i++){
        if (s[i] == 'm' || s[i] == 'w') {
            cout << "0" << endl;
            return;
        }
        if (s[i] == 'n' || s[i] == 'u') {
            if (i == 0 || s[i - 1] != s[i]) {
                dp[i] = 1;
            } else if (i > 1 && s[i - 2] == s[i]) {
                dp[i] += dp[i - 2];
                dp[i] += dp[i - 1]; 
            } else {
                dp[i] += 2;
            }
        } 
        if (i > 0 && (s[i - 1] == 'n' || s[i - 1] == 'u') && s[i] != s[i - 1]) {
            ans *= dp[i - 1];
        } 
    }

    cout << ans << endl;
   
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