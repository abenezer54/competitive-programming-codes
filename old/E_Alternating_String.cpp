#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    string s; cin >> s;
    if (n % 2 == 0){
        int ans = 0;
        vector<int> even_cnt(26, 0);
        vector<int> odd_cnt(26, 0);
        for (int i = 0; i < n; i++){
            if (i & 1){
                odd_cnt[s[i] - 'a']++;
            } else {
                even_cnt[s[i] - 'a']++;
            }
        }
        int tot = accumulate(even_cnt.begin(), even_cnt.end(), 0);
        int mx = *max_element(even_cnt.begin(), even_cnt.end());
        ans += tot - mx;
        tot = accumulate(odd_cnt.begin(), odd_cnt.end(), 0);
        mx = *max_element(odd_cnt.begin(), odd_cnt.end());
        ans += tot - mx;
        cout << ans << "\n";
        return;
    }

    vector<vector<int>> even_suffix(n + 1, vector<int>(26));
    vector<vector<int>> odd_suffix(n + 1, vector<int>(26));

    for (int i = n - 1; i >= 0; i--){
        for (int j = 0; j < 26; j++){
            even_suffix[i][j] += even_suffix[i + 1][j];
            odd_suffix[i][j] += odd_suffix[i + 1][j];
        }
        if (i & 1){
            odd_suffix[i][s[i] - 'a']++;
        } else {
            even_suffix[i][s[i] - 'a']++;
        }
    }
    // cout << even_suffix << endl;
    vector<int> even_cnt(26, 0);
    vector<int> odd_cnt(26, 0);
    int ans = 1e9;
    for (int i = 0; i < n; i++){
        vector<int> even_tot(26);
        vector<int> odd_tot(26);
        for (int j = 0; j < 26; j++){
            if (i % 2 == 0){
                even_tot[j] += odd_suffix[i + 1][j] + even_cnt[j];
                odd_tot[j] += even_suffix[i + 1][j] + odd_cnt[j];
            } else {
                even_tot[j] += odd_suffix[i + 1][j] + even_cnt[j];
                odd_tot[j] += even_suffix[i + 1][j] + odd_cnt[j];
            }
        }
        if (i & 1){
            odd_cnt[s[i] - 'a']++;
        } else {
            even_cnt[s[i] - 'a']++;
        }
        int cur = 1;
        int tot = accumulate(even_tot.begin(), even_tot.end(), 0);
        int mx = *max_element(even_tot.begin(), even_tot.end());
        cur += tot - mx;
        tot = accumulate(odd_tot.begin(), odd_tot.end(), 0);
        mx = *max_element(odd_tot.begin(), odd_tot.end());
        cur += tot - mx;
        ans = min(ans, cur);

    }

    cout << ans << "\n";


   
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