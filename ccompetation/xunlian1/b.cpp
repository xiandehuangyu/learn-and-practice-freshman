#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;

void solve() {
  int n, count = 0;
  std::cin >> n;
  std::string s1, s2, s3 = "";
  std::map<std::string, int> mp;
  for (int i = 0; i < n; i++) {
    std::cin >> s1 >> s2;
    for (int j = 0; j < 2; j++) {
      s3 += s1[j];
    }
    if (s2 != s3) {
      count += mp[s2 + s3];
      mp[s3 + s2]++;
    }
    s3.clear();
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