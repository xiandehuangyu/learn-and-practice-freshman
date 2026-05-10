#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll n, temp;
  cin >> n;
  ll sum = n * (n + 1) / 2;
  while (--n) {
    cin >> temp;
    sum -= temp;
  }
  cout << sum << endl;
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