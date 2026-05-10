#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;
#define endl '\n'

void solve() {
  std::string s;
  std::cin >> s;
  if (s.size() % 2)
    std::cout << -1;
  else {
    int count1 = 0, count0 = 0;
    for (auto i : s) {
      if (i == '0') {
        count0++;
      } else
        count1++;
    }
    if (count0 != count1) {
      std::cout << -1;
      return;
    } else {
      int ci = 0, now = 0, nows = 1;
      std::cout << s.size() / 2 << endl;
      std::queue<char> q;
      while (ci < s.size() / 2) {
        if (s[now] == '0') {
          std::cout << nows << " " << 1 << endl;
          q.push('1');
        } else {
          std::cout << nows << " " << 2 << endl;
          q.push('0');
        }
        now++;
        while (!q.empty() && q.front() == s[now]) {
          nows++;
          now++;
          q.pop();
        }
        ci++;
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