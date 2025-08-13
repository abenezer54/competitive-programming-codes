#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

int ask(int i, int j){
    cout << "? " << i << ' ' << j << endl;
    int val; cin >> val;
    return val;
}

void response(int type){
    if (type == 1){
        cout << "! A" << endl;
    } else { 
        cout << "! B" << endl;
    }
}

void solve() {
    int n; cin >> n;
    vector<int> x(n);
    vector<int> cnt(n + 1);
    int idx1 = 0,  idx2 = 0;
    for (int i = 0; i < n; i++){
        cin >> x[i];
        cnt[x[i]]++;
        if (x[i] == n ){
            idx1 = i + 1;
        } else if (x[i] == 1){
            idx2 = i + 1;
        }
    }


    for (int i = 1; i <= n; i++){
        if (cnt[i] == 0){
            int j = i + 1;
            if (i == n){
                j = 1;
            }
            int res = ask(i, j);
            if (res == 0){
                response(1);
            } else {
                response(2);
            }
            return;
        }
    }
    int res1 = ask(idx1, idx2);
    int res2 = ask(idx2, idx1);
    if (res1 != res2){
        response(1);
    } else {
        if (res1 < n - 1){
            response(1);
        } else {
            response(2);
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