#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    string s; cin >> s;
    int n = s.size();
    int q; cin >> q;
    // cout << n << endl;
    if (n < 4){
        for (int i = 0; i < q; i++){
            int x, y;
            cin >> x>> y;
            cout << "NO" << '\n';
        }
        return;
    }
    int cnt = 0;
    vector<int> a(n);
    for (int i = 0; i < n - 3; i++){
        if(s[i] == '1' && s[i + 1] == '1' && s[i + 2] == '0' && s[i + 3] == '0'){
            a[i] = 1;
            cnt++;
        }
    }
    // cout << s << ' ' << cnt << endl;
    
    for (int i = 0; i < q; i++){
        // cout << "before " << s << endl;
        int idx;
        char val;
        cin >> idx >> val;
        idx--;
        if (s[idx] == val) {
            if(cnt){
                cout << "YES" << '\n';
            } else {
                cout << "NO" << '\n';
            } 
            continue;
        }
        for (int j = max(0, idx - 3); j < min(idx + 1, n - 3); j ++){
            if(s[j] == '1' && s[j + 1] == '1' && s[j + 2] == '0' && s[j + 3] == '0'){
                a[j] = 0;
                cnt--;
            }
        }
        s[idx] = val;
        for (int j = max(0, idx - 3); j < min(idx + 1, n - 3); j ++){
            if(s[j] == '1' && s[j + 1] == '1' && s[j + 2] == '0' && s[j + 3] == '0'){
                a[j] = 1;
                cnt++;
            }
        }
        // cout << "after " << s << endl; 
        if(cnt){
                cout << "YES" << '\n';
            } else {
                cout << "NO" << '\n';
            } 


    }

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