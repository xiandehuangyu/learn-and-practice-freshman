#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;
ll k[21] = {};
ll sum = 0, now = 0, ans = LL_INF;
void dfs(int i, int kk) {
  if (i >= kk) {
    ans = std::min(std::abs(sum - 2 * now), ans);
    return;
  } else if (now > sum / 2) {
    ans = std::min(std::abs(2 * now - sum), ans);
    return;
  } else {
    now += k[i];
    dfs(i + 1, kk);
    now -= k[i];
    dfs(i + 1, kk);
  }
}
void solve() {
  int n;
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    std::cin >> k[i];
    sum += k[i];
  }
  dfs(0, n);
  std::cout << ans;
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