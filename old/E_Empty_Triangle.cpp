#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
// #define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
int ask(int i, int j, int k) {
    cout << "? " << i << ' ' << j << ' ' << k << endl;
    int p; cin >> p;
    return p;
}

void answer(int i, int j, int k) {
    cout << "! " << i << ' ' << j << ' ' << k << endl;
}

void solve() {
    int n; cin >> n;
    int i = 1, j = 2, k = 3;
    for (int q = 0; q < 75; q++) {
        
        int r = rand() % 3; 
        int res = ask(i, j, k);
        if (res == 0) {
            answer(i, j, k);
            return;
        }
        
        if (r % 3 == 0) {
            i = res;
        } else if (r % 3 == 1) {
            j = res;       
        } else {
            k = res;
        }
    }

   
}

int main() {
    srand(time(0) + clock());
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}