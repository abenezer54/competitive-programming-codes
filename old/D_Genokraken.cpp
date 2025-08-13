#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

int query(int a, int b) {
    cout << "? " << a << " " << b << endl;
    int res;
    cin >> res;
    
    if (res == -1) { 
        exit(1);
    }
    return res;
}

void solve() {
    int n;
    cin >> n;
    
    vector<int> p(n); 
    int node = 2;
    while (node < n) {
        int r = query(1, node);
        if (r == 0) break; 
        node++;
    }

    int i = 2;

    p[node] = 1;
    node++;

    
    while (node < n) {
        

        int r = query(i , node);
        if (r == 0) {
            p[node] = i;
            node++;
        } 
        i++;
    }

    cout << "!";
    for (int j = 1; j < n; j++) {
        cout << " " << p[j];
    }
    cout << endl;
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
