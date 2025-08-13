#include <bits/stdc++.h>

using namespace std;
int n, m;

// vector<vector<int>> a(n);
vector<vector<int>> a;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    // cout << "here" << '\n';

    cin >> n >> m;
    for (int i = 0; i < m; i++){
        int type; cin >> type;
        int leng; cin >> leng;
        for (int j = 0; j < leng; j++){
            int x; cin >> x;
            if (type == 1){
                a[i].push_back(x);
            }
            else{
                a[i].push_back(double(x)/ 2);
            }
            
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < a[i].size(); j++){
            cout << a[i][j] << " ";
        }
        cout << '\n';
    }
    return 0;
}