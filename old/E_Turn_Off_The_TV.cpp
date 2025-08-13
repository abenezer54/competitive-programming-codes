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
    vector<array<int, 2>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i][0] >> a[i][1];
    }

    map<int, int> mp;
    for (auto&[l, r]: a) {
        mp[l]++;
        mp[r + 1]--;
    }

    vector<array<int, 2>> prefix;
    for (auto&[k, v]: mp) {
        prefix.push_back({k, v});
    }

    sort(prefix.begin(), prefix.end());
    
    for (int i = 1; i < prefix.size(); i++) {
        prefix[i][1] += prefix[i - 1][1];
    }


    vector<array<int, 2>> arr;
    for (int i = 0; i < prefix.size() - 1; i++) {
        if (prefix[i][1] > 1) {
            if (i > 0 && prefix[i - 1][1] > 1) {
                arr[arr.size() - 1][1] = prefix[i + 1][0] - 1;
            } else {
                arr.push_back({prefix[i][0], prefix[i + 1][0] - 1});
            }
        } 
    }


    if (arr.empty()) {
        cout << -1 << endl;
        return;
    }


    vector<array<int, 3>> temp; 
    for (int i = 0; i < n; i++) {
        temp.push_back({a[i][0], a[i][1], i + 1});
    }


    sort(temp.begin(), temp.end());
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j < arr.size() && arr[j][1] < temp[i][0]) {
            j++;
        }
        if (temp[i][0] >= arr[j][0]) {
            if (j < arr.size() && arr[j][1] >= temp[i][1]) {
                cout << temp[i][2] << endl;
                return;
            } 
        }
    }
   
    cout << -1 << endl;

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