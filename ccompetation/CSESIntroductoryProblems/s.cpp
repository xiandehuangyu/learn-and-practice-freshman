#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  int n, a, b;
  std::cin >> n >> a >> b;
  if (a * b == 0 && a + b != 0)
    std::cout << "NO" << std::endl;
  else if (a + b <= n && a + b != 1) {
    std::cout << "YES" << std::endl;
    for (int i = 1; i <= n; i++) {
      std::cout << i;
      if (i - n) std::cout << " ";
    }
    std::cout << std::endl;
    for (int i = 1; i <= a + b; i++) {
      int k = (i + a) % (a + b);
      if (k == 0) k = a + b;
      std::cout << k;
      if (i - n) std::cout << " ";
    }
    for (int i = a + b + 1; i <= n; i++) {
      std::cout << i;
      if (i - n) std::cout << " ";
    }
    std::cout << std::endl;
  } else
    std::cout << "NO" << std::endl;
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