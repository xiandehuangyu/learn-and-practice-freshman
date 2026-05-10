#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll x, y;
  std::cin >> x >> y;
  ll max = std::max(x, y);
  ll k;
  if (max % 2) {
    if (x == max)
      k = y;
    else
      k = y + y - x;
  } else {
    if (y == max)
      k = x;
    else
      k = x + x - y;
  }
  std::cout << (max - 1) * (max - 1) + k << std::endl;
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int t = 1;
  std::cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}