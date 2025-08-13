#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
   string s; cin >> s;
//    cout << s << endl;
   reverse(s.begin(), s.end());
   bool first = false;
   bool second = false;
   int ans = 0;
   for(int i = 0; i < s.size(); i ++){
        if (!first){
            if(s[i] == '0'){
                first = true;
            } else {
                ans++;
            }
        } else {
            if(!second){
                if (s[i] == '0' || s[i] == '5'){
                    second = true;}
                else {
                    ans++;
                }
                
            } 
        }
   }

    first = false;
    second = false;
   int ans2 = 0;
   for(int i = 0; i < s.size(); i ++){
        if (!first){
            if(s[i] == '5'){
                first = true;
            } else {
                ans2++;
            }
        } else {
            if(!second){
                if (s[i] == '2' ||  s[i] == '7'){
                    second = true;}
                else {
                    ans2++;
                }
                
            } 
        }
   }


   cout << min(ans, ans2) << '\n';

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // cout << ll(1e18) << endl;
    // for(int i = 0; i <1000;i++){
    //     cout << i * 25<< endl;
    // }
    int t = 1;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}