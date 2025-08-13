#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, m; cin >> n >> m;
    vector<string> grid(n);
    for(auto &x:grid) cin >> x;
    
    int layer = min(n, m) / 2;
    ll ans = 0;
    for (int l = 1; l <= layer; l++){
        string s;
        int i = l - 1;
        int j = l - 1;
        s += grid[i][j];

        int hdist = m - (2 * (l - 1)) - 1;
        int vdist = n - (2 *(l - 1)) - 1;
        for (int temp = 0; temp < hdist; temp++){
            // cout << i << ' ' << j << '\n';
            s += grid[i][j + 1];
            j++;
        }
        for (int temp = 0; temp < vdist; temp++){
            s += grid[i + 1][j];
            i++;
        }
        for (int temp = 0; temp < hdist; temp++){
            s += grid[i][j- 1];
            j--;
        }
        for (int temp = 0; temp < vdist - 1; temp++){
            s += grid[i - 1][j];
            i--;
        }
        s = s + s;
        for (int j = 0; j < s.size()/2; j++){
            if (s[j] == '1' && s[j + 1] == '5' && s[j + 2] == '4' && s[j + 3] == '3'){
                ans++;
            }
        }
    }
    // cout << s << endl;
    cout << ans << '\n';
    
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