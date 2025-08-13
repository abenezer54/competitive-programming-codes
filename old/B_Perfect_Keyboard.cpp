#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    string s; cin>> s;
    int n = s.size();
    map<char, set<char>> adj;

    for (int i = 0; i < n; i++){
        if (i - 1 >= 0){
            adj[s[i]].insert(s[i - 1]);
            adj[s[i - 1]].insert(s[i]);
        }
        if (i + 1 < n){
            adj[s[i]].insert(s[i + 1]);
            adj[s[i + 1]].insert(s[i]);  
        }
    }

    for (auto &[node, nei]: adj){
        if (nei.size() > 2) {
            cout << "NO\n";
            return;
        }
    }
    
    vector<int> col(26, 0);
    function<vector<char>(char, char)> dfs = [&](char node, char parent) {
        col[node - 'a'] = 1;
        vector<char> path;
        for (auto nei: adj[node]){
            if (nei == parent) continue;
            
            if (col[nei - 'a'] == 1){
                return vector<char>{};
            }

            if (col[nei - 'a'] == 0){
                auto val  = dfs(nei, node);
                if (val.empty()) return vector<char>{};
                path.insert(path.begin(), val.begin(), val.end());
            }
        }
        path.push_back(node);
        col[node - 'a'] = 2;
        return path;
    };
    
    vector<char> ans;
    for (auto &[node, nei]: adj){
        if (col[node - 'a'] == 0 && nei.size() == 1) {
            auto val = dfs(node, '*');
            if (val.size() == 0){
                cout << "NO\n";
                return;
            }
            ans.insert(ans.end(), val.begin(), val.end());
        }
    }

    for (auto &[node, nei]: adj){
        if (col[node - 'a'] == 0) {
            cout << "NO\n";
            return;
        }
    }

    cout << "YES\n";
    
    for (int i = 0; i < 26; i++){
        char c = char(i + 97);
        if (col[i] == 0){
            ans.push_back(c);
        } 
    }
    for (auto val: ans){
        cout << val;
    }
    cout << '\n';
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