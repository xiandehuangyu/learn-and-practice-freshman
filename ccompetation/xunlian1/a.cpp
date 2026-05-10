#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  int n, m, temp;
  std::cin >> n >> m;
  std::vector<int> k(n, -1);
  int now = 0, count = 0;
  for (int i = 0; i < m; i++) {
    std::cin >> temp;
    int have = 0;
    for (int j = 0; j < n; j++) {
      if (temp == k[j]) {
        have = 1;
        break;
      }
    }
    if (!have) {
      k[now] = temp;
      now++;
      now %= n;
      count++;
    }
  }
  std::cout << count;
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