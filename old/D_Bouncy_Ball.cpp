#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

int n, m;
int dp[(int)1e5][10000];



int find_dir(string d){
    int cur_dir = 0;
    if (d == "DL"){
        cur_dir = 1;
    } else if (d == "UR"){
        cur_dir = 2;
    } else if (d == "UL"){
        cur_dir = 3;
    }
    return cur_dir;
}

void solve() {
    int i1, j1, i2, j2; 
    cin >> n >> m >> i1 >> j1 >> i2 >> j2;
    i1--; j1--; i2--; j2--;  
    string d; cin >> d;
    memset(dp, 1, sizeof(dp));
    auto change_dir = [&](int i, int j, int cur) {
        int new_dir = cur;
        if(cur == 0){
            if (i == n - 1 && j == m - 1){
                new_dir = 3;
            } else if (i == n - 1){
                new_dir = 2;
            } else if (j == m - 1){
                new_dir = 1;
            }
        } else if (cur == 1){
            if (i == n - 1 && j == 0){
                new_dir = 2;
            } else if (i == n - 1){
                new_dir = 3; 
            } else if (j == 0){
                new_dir = 0;
            }

        } else if (cur == 2){
            if (i == 0 && j == m - 1){
                new_dir = 1;
            } else if (i == 0){
                new_dir = 0;
            } else if (j = m - 1){
                new_dir = 3;
            }

        } else {
            if (i == 0 && j == 0){
                new_dir = 0;
            } else if (i == 0){
                new_dir = 1;
            } else if (j == 0){
                new_dir = 2;
            }

        }
        return new_dir;
    };


   
    
    
    vector<vector<int>> dd = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}; 

    int cur_dir = find_dir(d);
    vector<vector<vector<int>>> vis(n, vector<vector<int>>(m, vector<int>(4, 0)));

    
    int bounce = 0;
    function<bool(int, int, int)> dfs = [&](int i, int j, int dir) {
        if (i < 0 || i >= n || j < 0 || j >= m){
            int ni = i - dd[dir][0], nj = j - dd[dir][1];
            i = ni; j = nj;
            int new_dir = change_dir(i, j, dir);
            if (dir != new_dir) bounce++;
            dir = new_dir;

        } 
        if (vis[i][j][dir]) return false; 
        vis[i][j][dir] = 1;

        if (i == i2 && j == j2) return true;  
        int ni = i + dd[dir][0], nj = j + dd[dir][1];

        return dfs(ni, nj, dir);    
    };

    bool check = dfs(i1, j1, cur_dir);
    
    if (check) cout << bounce << endl;
    else cout << "-1\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}
