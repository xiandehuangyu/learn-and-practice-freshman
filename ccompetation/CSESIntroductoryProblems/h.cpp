#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll n;
  std::cin >> n;
  std::vector<ll> k;
  ll now = 1, noww = 1;
  k.push_back(now);
  now *= 2;
  k.push_back(now);
  while (now < 1e6) {
    k.push_back((k[noww] * k[noww]) % MOD);
    now *= 2;
    noww++;
  }
  ll ans = 1;
  now = 1;
  while (n) {
    if (n % 2) {
      ans *= k[now];
      ans %= MOD;
    }
    n /= 2;
    now++;
  }
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