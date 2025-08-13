#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n;
    cin >> n;
    string s; 
    cin >> s;
    string r; 
    cin >> r;
    // cout << s <<  ' ' << r << endl;
    

    int cnt = 0;
    int zero = 0;
    for (auto ch: s){
        if (ch == '1')
            cnt++;
        else
            zero++;
    }


    for (int i = 0; i < n - 1; i++){
        if (cnt == 0 || zero == 0){
            cout << "NO" << endl;
            return;
        }
        if (r[i] == '1')
            {
            zero--;}
        else 
            {cnt--;
            }

    }

    cout << "YES" << endl;
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