#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;
int a[9][9] = {}, lie[9] = {}, zuoxie[16] = {}, youxie[16] = {};
int count = 0;
void dfs(int i) {
  if (i > 8) {
    count++;
    return;
  } else
    for (int j = 1; j < 9; j++) {
      if ((!a[i][j]) && (!lie[j]) && (!zuoxie[i + j - 1]) &&
          (!youxie[i - j + 8])) {
        a[i][j] = 1;
        lie[j] = 1;
        zuoxie[i + j - 1] = 1;
        youxie[i - j + 8] = 1;
        dfs(i + 1);
        a[i][j] = 0;
        lie[j] = 0;
        zuoxie[i + j - 1] = 0;
        youxie[i - j + 8] = 0;
      }
    }
}
void solve() {
  for (int i = 1; i < 9; i++) {
    for (int j = 1; j < 9; j++) {
      char k;
      std::cin >> k;
      if (k == '*') a[i][j] = 1;
    }
  }
  dfs(1);
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