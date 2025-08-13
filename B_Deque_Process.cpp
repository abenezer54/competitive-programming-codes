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
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    string ans = "";

    int left = 0, right = n - 1;
    int step = 0;
    vector<int> check;
    while (left < right) {
        
        step++;
        vector<array<int, 2>> temp;
        temp.push_back({a[left], 0});

        left++;
        // if (left <= right) {
        //     temp.push_back({a[left], 0});
        //     left++;
        // }
        
        // if (right > left) {
        //     temp.push_back({a[right], 1});
        //     right--;
        // }
        temp.push_back({a[right], 1});
        right--;

        sort(temp.begin(), temp.end());

        if (step & 1) {
            if (temp[0][1] == 1) {
                ans.push_back('R');
                ans.push_back('L');
            } else {
                ans.push_back('L');
                ans.push_back('R');
            }
        } else {
            if (temp[0][1] == 0) {
                ans.push_back('R');
                ans.push_back('L');
            } else {
                ans.push_back('L');
                ans.push_back('R');
            }

        }

    }
    if (left == right) {
        ans.push_back('L'); 
    }
    cout << ans << endl;
   
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