#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll n;
  cin >> n;
  while (n - 1) {
    cout << n << " ";
    if (n % 2)
      n = n * 3 + 1;
    else {
      n = n >> 1;
    }
  }
  cout << 1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t = 1;
  // cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}