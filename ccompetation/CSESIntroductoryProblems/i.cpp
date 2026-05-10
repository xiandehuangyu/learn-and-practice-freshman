#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll n;
  std::cin >> n;
  if (n == 1 || n == 2 || n * (n + 1) / 2 % 2)
    std::cout << "NO";
  else {
    std::cout << "YES" << std::endl;
    if (n % 2 == 0) {
      std::cout << n / 2 << std::endl;
      for (ll i = 1; i < n / 2 + 1; i++) {
        std::cout << i << " " << n + i - 1 << " ";
      }
      for (ll i = n / 2 + 1; i++) {
        std::cout << i << " " << n + i - 1 << " ";
      }
    }
  }
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int t = 1;
  // std::cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}