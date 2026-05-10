#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll x, y;
  std::cin >> x >> y;
  if ((x + y) % 3 != 0)
    std::cout << "NO" << std::endl;
  else {
    ll max = std::max(x, y);
    ll min = std::min(x, y);
    x = max - min;
    max -= 2 * x;
    min -= x;
    if (max == min && max >= 0)
      std::cout << "YES" << std::endl;
    else
      std::cout << "NO" << std::endl;
  }
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