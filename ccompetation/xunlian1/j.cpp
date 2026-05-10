#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  ll n, temp;
  std::cin >> n;
  std::stack<ll> k;
  ll count = 0;
  std::cin >> temp;
  k.push(temp);
  for (ll i = 1; i < n; i++) {
    std::cin >> temp;
    while (!k.empty() && (temp >= k.top())) {
      k.pop();
    }
    if (!k.empty()) {
      count += k.size();
    }
    k.push(temp);
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