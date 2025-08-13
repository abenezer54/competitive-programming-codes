#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n = 8;
    vector<string> grid(8);
    for (int i = 0; i < n; i++){
        cin >> grid[i];
    }
    vector<vector<set<int>>> times(8, vector<set<int>>(8));

    for (int j = 0; j < n; j++){
        set<int> cur;
        for (int i = 0; i < n; i++){
            if (grid[i][j] == 'S'){
                cur.insert(i);
            }
            times[i][j] = cur;
        }
    }
    vector<vector<bool>> vis(8, vector<bool>(8, false));
    vector<int> dx = {-1, 1, 0, 0, -1, -1, 1, 1}; 
    vector<int> dy = {0, 0, -1, 1, -1, 1, -1, 1}; 

    auto valid = [&](int i, int j, int t){
        if (i < 0 or i > 7 or j < 0 or j > 7)
            return false;

        for (auto val: times[i][j]){
            int diff = i - val;
            if (diff  == t - 1 or diff == t){
                return false;
            }
        }
        return true;
    };


    function<bool(int, int, int)> dfs = [&](int i, int j, int cur) {
        // vis[i][j] = true;
        if (grid[i][j] == 'A'){
            return true;
        }
        if (cur == 20){
            return false;
        }
        // cout << i << ' ' << j << endl;
        for (int k = 0; k < n; k++){
            int ni = i + dx[k];
            int nj = j + dy[k];
            if (valid(ni, nj, cur)){
                if (dfs(ni, nj, cur + 1)) return true;  
            } 
        }
        if (valid(i, j, cur) && dfs(i, j, cur + 1)) {
            return true;
        }
    
        return false;
    };
    // cout << "here" << endl;

    if (dfs(7, 0, 1)) {
        cout << "WIN" << '\n';
    } else {
        cout << "LOSE" <<'\n';
    }

   
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
