#include <bits/stdc++.h>
using namespace std;
int n, k;

vector<int> a(n);
vector<int> b(n); 

int dp(int idx, int cy,  int cb) {
    if (idx == n){
        if (cy >= k){
            return cb;
        }
        return -1;
    }
    int v1 = dp(idx + 1, cy + a[idx], cb);
    int v2 = dp(idx + 1, cy, cb + b[idx]);
    return max({v1, v2});
    }

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> k;
    
    for(int i = 0; i < n; i++){
        cin >> a[i];
        cin >> b[i];
    }
    cout << "here" << '\n';
    cout << dp(0, 0, 0) << '\n';
    
    

    return 0;
}