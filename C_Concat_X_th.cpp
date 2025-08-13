#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k, x; cin >> n >> k >> x;
    vector<string> a;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        a.push_back(s);
    }
    vector<string> total; 
    vector<string> cur;
    function<void(int)> dfs = [&] (int idx) {
        if (cur.size() == k) {
            string temp = "";
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < cur[i].size(); j++) {
                    temp.push_back(cur[i][j]);
                }
            }
            total.push_back(temp);
            return;
        }
        for (int i = 0; i < n; i++) {
            // if (vis.count(i) == 0) {
                // vis.insert(i);
                cur.push_back(a[i]);
                dfs(i + 1);
                cur.pop_back();
            //     vis.erase(i);
            // }
        }
    };
    dfs(0);
    sort(total.begin(), total.end());
    cout << total[x - 1] << endl;
   
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