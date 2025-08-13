#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string s; cin >> s;
    int n = s.size();
    map<char, int> cnt;
    for (auto ch: s){
        cnt[ch]++;
    }


    int left = 0, right = n - 1;
    while (left < right) {
        if (s[left] != s[right]) break;
        cnt[s[left]]-= 2;
        left++; right--;
    }

    if (left > right){
        cout << "0\n";
        return;
    }

    vector<int> ok(n, 1);
    int p2 = n / 2;
    int p1 = p2 - 1;
    while (p1 >= 0 && p2 < n && s[p1] == s[p2]){
        cnt[s[p1]] -= 2;
        ok[p1] = 0;
        ok[p2] = 0;
        p1--; p2++;
    }
    
    map<char, int> cur;

    int i = left;
    auto valid = [&](){
        for (auto&[key, val]: cnt){
            if (cur[key] < val / 2) return false;
        }
        return true;
    };
    while(!valid()){
        if (ok[i]){
            cur[s[i]]++;
        } else {
            cur[s[i]]++;
            cnt[s[i]]++;
        }
        i++;
    }
    // map<char, int> cur2;
    // int j = right;
    // auto valid2 = [&](){
    //     for (auto&[key, val]: cnt){
    //         if (cur2[key] < val / 2) return false;
    //     }
    //     return true;
    // };
    // while(!valid2()){
    //     if (ok[j]){
    //         cur2[s[j]]++;
    //     } 
    //     j--;
    // }
    cout << min(i - left, MOD) << "\n";

   
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