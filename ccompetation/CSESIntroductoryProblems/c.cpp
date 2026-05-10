#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  std::string s;
  std::cin >> s;
  char a = s[0];
  ll max = 1;
  ll now = 0;
  for (auto i : s) {
    if (i == a)
      now++;
    else {
      max = std::max(max, now);
      now = 1;
      a = i;
    }
  }
  max = std::max(max, now);
  std::cout << max;
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