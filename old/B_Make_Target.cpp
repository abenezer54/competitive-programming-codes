#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<vector<char>> a(n, vector<char>(n, '.'));


    int left = 0; 
    int right = n;
    int top = 0;
    int bottom = n;
    while (true)
    {   
        bool found = false;
        int i = top, j = left;
        while (i < bottom && j < right) {
            a[i][j] = '#';
            found = true;
            j++; 
        }
        j--;
        i++;
        while (i < bottom && j < right) {
            a[i][j] = '#';
            found = true;
            i++;
        }
        i--;
        j--;

        while (j >= left) {
            a[i][j] = '#';
            found = true;
            j--;
        }
        j++;
        i--;

        while (i > top) {
            a[i][j] = '#';
            found = true;
            i--;
        }

        top += 2;
        left += 2;
        bottom -= 2;
        right -= 2;
        if (!found) {
            break;
        }
    }
    
    for (auto row: a) {
        for (auto val: row) {
            cout << val;
        }
        cout << endl;
    }
    
   
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