#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {

    // int n; cin >> n;
    // vector<pair<int, string>> a(n);
    // for (int i = 0; i < n; i++) {
    //     int val; cin >> val;
    //     string s; cin >> s; sort(s.begin(), s.end());
    //     a[i].first = val;
    //     a[i].second = s;
    // }


    // vector<unordered_map<string, int>> dp(n + 5);

    // for (int i = 0; i < n; i++) {
    //     dp[i][""] = 0;
    // }
    // vector<string> vals = {"A", "B", "C", "AC", "AB", "ABC"};

    // for (int i = 0; i < n; i++) {
    //     for (auto val: vals) {
    //         if (dp[i].count(val)) {
    //             if (dp[i].count(val)) {
    //                 dp[i + 1][val] = min(dp[i + 1][val], dp[i][val]);
    //             } else {
    //                 dp[i + 1][val] = dp[i][val];
    //             }
    //         }
    //         for (int ln = 1; ln < 3; ln++) {
    //             for (int j = 0; j < a[i].second.size(); j++){
    //                 string cur = a[i].second.substr(j, j + ln);
    //                 if (val.find(cur) != string::npos) {
    //                     i
    //                 }
    //             }
    //         }
    //     }
    // }


   
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