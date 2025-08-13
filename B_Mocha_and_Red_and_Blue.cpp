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
    string s; cin >> s; 

    for (int i = 0; i < n; i++) {
        if (s[i] == '?') {
            int start = 0;
            if (i > 0 && s[i - 1] == 'B') {
               start = 1;
            }
            if (i == 0) {
                for (int j = 1; j < n; j++) {
                    if (s[j] != '?') {
                        int dis = j;
                        if (dis & 1) {
                            if (s[j] == 'B') {
                                start = 1;
                            }
                        } else {
                            if (s[j] == 'R') {
                                start = 1;
                            }
                        }
                        break;
                    }
                }
            }

            int x = i; 
            while (s[x] == '?') {
                char c;
                if (start & 1) {
                    c = 'R';
                } else {
                    c = 'B';
                }
                s[x] = c;
                start++;
            }
            i = x;

        }
    }
    cout << s << endl;
   
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