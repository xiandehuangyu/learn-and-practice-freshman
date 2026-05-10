#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  int n;
  std::cin >> n;
  if (n == 1)
    std::cout << 1;
  else if (n == 2 || n == 3)
    std::cout << "NO SOLUTION";
  else {
    for (int i = n - 1; i > 0; i -= 2) {
      std::cout << i << " ";
    }
    for (int i = n; i > 0; i -= 2) {
      std::cout << i;
      if (i > 2) std::cout << " ";
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