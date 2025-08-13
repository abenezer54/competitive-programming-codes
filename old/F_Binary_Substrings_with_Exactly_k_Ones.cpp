#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;
ll atMostK(vector<int> nums, int k){
    if (k == -1)
        return 0LL;
    ll ans = 0;
    int l = 0;
    int cur_sum = 0;
    for (int r = 0; r < nums.size(); r++) {
        cur_sum += nums[r];
        while (cur_sum > k){
            cur_sum -= nums[l];
            l += 1;
        }
        ans += r - l + 1;
    }
    return ans;
}

void solve() {
    int k; cin >> k;
    string s; cin >> s;
    vector<int> a;
    for (auto ch: s){
        a.push_back(ch - '0');
    }

    cout << atMostK(a, k) - atMostK(a, k - 1) << endl;
   
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