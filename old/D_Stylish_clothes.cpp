#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    vector<vector<int>> arr;
    vector<int> length(4, 0);
    for (int i = 0; i < 4; i++){
        int n; cin >> n;
        length[i] = n;
        vector<int> cur(n);
        for (int j = 0; j < n; j++){
            cin >> cur[j];
        }
        sort(cur.begin(), cur.end());
        arr.push_back(cur);
    }
    vector<int> idx = {0, 0, 0, 0};
    auto valid = [&]() {
        for (int i = 0; i < 4; i++){
            if (idx[i] < length[i]) return true;
        }
        return false;
    };
    int ans = 1e9;
    vector<int> res = {0, 0, 0, 0};
    
    while (valid()){
        vector<vector<int>> temp;
        vector<int> min_max;
        for (int i = 0; i < 4; i++){
            temp.push_back(vector<int>{arr[i][idx[i]], idx[i], i}); // value, inside index, array type (from the 4)
            min_max.push_back(arr[i][idx[i]]);
        }
        sort(temp.begin(), temp.end());
  
        int mx = *max_element(min_max.begin(), min_max.end());
        int mn = *min_element(min_max.begin(), min_max.end());
        if (mx - mn < ans){
            ans = mx - mn;
            for (int i = 0; i < 4; i++){
                res[temp[i][2]] = temp[i][0];
            }
        }


        bool found = false;
        for (int i = 0; i < 4; i++){
            if (temp[i][1] + 1 < length[temp[i][2]]){
                idx[temp[i][2]]++;
                found = true;
                break;
            }
        }
        if (!found){
            break;
        }
        
    }
   
    for (auto val: res){
        cout << val << ' ';
    }
    cout << endl;

   
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