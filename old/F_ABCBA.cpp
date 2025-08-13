#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

vector<int> manacher_odd(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    int l = 1, r = 1;
    for(int i = 1; i <= n; i++) {
        p[i] = max(0, min(r - i, p[l + (r - i)]));
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
        if(i + p[i] > r) {
            l = i - p[i], r = i + p[i];
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}

vector<int> manacher(string s) {
    string t;
    for(auto c: s) {
        t += string("#") + c;
    }
    auto res = manacher_odd(t + "#");
    return vector<int>(begin(res) + 1, end(res) - 1);
}

void solve() {
    string s; cin >> s;
    

    auto a = manacher(s);
    // cout << a << endl;
    int mx = 1;
    for (int i = 0; i < a.size(); i++) {
        a[i]--;
        int rb = min((int) a.size() - 1, i + a[i]);
        int lb = max(0, i - a[i]);
        int mn = min(rb, lb);
        int d1 = rb - i, d2 = i - lb;   
        int d = min(d1, d2);
        int cur;
        // character at i
        if (i % 2 == 0){
            cur = (d / 2) * 2 + 1;
            if (i + d>= a.size() - 1) {
                mx = max(mx, cur);
            }
        } else {
            cur = ((d + 1) / 2 )* 2;
            if (i + d >= a.size() - 1) {
                mx = max(mx, cur);
            }
        }
        
    }
    

    string need = s.substr(0, (s.size() - mx));
    reverse(need.begin(), need.end());
    cout << s + need << endl; 


   
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