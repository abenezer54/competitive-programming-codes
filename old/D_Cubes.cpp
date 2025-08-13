#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
typedef __int128 int128;

const int128 MOD = (int128)1e9 + 7;

int128 readInt128() {
    string s;
    cin >> s;
    int128 num = 0;
    bool neg = false;
    std::size_t i = 0;

    if (s[0] == '-') {
        neg = true;
        i = 1;
    }

    for (; i < s.size(); i++)
        num = num * 10 + (s[i] - '0');

    return neg ? -num : num;
}

void printInt128(int128 num) {
    if (num == 0) {
        cout << "0";
        return;
    }

    if (num < 0) {
        cout << "-";
        num = -num;
    }

    string s = "";
    while (num) {
        s += '0' + (num % 10);
        num /= 10;
    }

    reverse(s.begin(), s.end());
    cout << s;
}

bool valid(int128 n) {
    int128 root = round(cbrt((double)n));
    return root * root * root == n;
}

void solve() {
    int128 n = readInt128();

    for (int128 y = 1; y <= (int128)1e6; y++) {
        int128 xcube = y * y * y + n;

        int128 x = round(cbrt((double)xcube));
        if (x > 0 && valid(xcube)) {  
            printInt128(x);
            cout << ' ';
            printInt128(y);
            cout << endl;
            return;
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
