#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

string my_adder(string a, string b) {
    string res = "";
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int carry = 0;
    int len = max(a.size(), b.size());

    for (int i = 0; i < len; i++) {
        int num1 = (i < a.size()) ? (a[i] - '0') : 0;
        int num2 = (i < b.size()) ? (b[i] - '0') : 0;
        int cur = carry + num1 + num2;
        
        res += (cur % 10) + '0'; 
        carry = cur / 10; 
    }
    
    if (carry > 0) {
        res += (carry + '0');
    }

    reverse(res.begin(), res.end());
    return res;
}

bool check(string val) {
    return val.find('7') != string::npos;
}

void solve() {
    ll n;
    cin >> n;

    queue<string> que;
    unordered_set<string> visited;  
    que.push(to_string(n));
    visited.insert(to_string(n));

    int lvl = 0;
    
    while (!que.empty()) {
        int sz = que.size();

        for (int j = 0; j < sz; j++) {
            auto node = que.front(); 
            que.pop();
            
            if (check(node)) {
                cout << lvl << endl;
                return;
            }

            for (int i = 1; i <= 9; i++) {
                string val = string(i, '9');  
                string next = my_adder(val, node);
                
                if (!visited.count(next) && next.size() < 11) { 
                    que.push(next);
                    visited.insert(next);
                }
            }
        }
        lvl++;
    }
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
