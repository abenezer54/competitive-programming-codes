#include <iostream>
using namespace std;

int main() {
    int n = 2000;
    cout << n << endl;

    int val = (1 << 29) + (1 << 28);
    for (int i = 0; i < n; ++i)
        cout << val << endl;

    return 0;
}
