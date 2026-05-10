#include <bits/stdc++.h>

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-8;
using ll = long long;
#define endl '\n'

void solve() {
  int n, m;
  std::cin >> n >> m;
  std::list<std::pair<int, int>> player;
  std::vector<int> win(n + 1, 1);
  for (int i = 1; i < n + 1; i++) {
    std::pair<int, int> temp;
    temp.first = i;
    std::cin >> temp.second;
    player.push_back(temp);
  }
  std::string s;
  std::cin >> s;
  int go = 1;
  auto now = player.begin();
  for (auto i : s) {
    if (i == 'S') {
      (*now).second--;
      auto next = now;
      if (go > 0) {
        next++;
        if (next == player.end()) {
          next = player.begin();
        }
      } else {
        if (next == player.begin()) {
          next = player.end();
        }
        next--;
      }
      if (go > 0) {
        next++;
        if (next == player.end()) {
          next = player.begin();
        }
      } else {
        if (next == player.begin()) {
          next = player.end();
        }
        next--;
      }
      if ((*now).second == 0) {
        win[(*now).first] = 0;
        player.erase(now);
      }
      now = next;
    } else if (i == 'C') {
      (*now).second--;
      auto next = now;
      if (go > 0) {
        next++;
        if (next == player.end()) {
          next = player.begin();
        }
      } else {
        if (next == player.begin()) {
          next = player.end();
        }
        next--;
      }
      if ((*now).second == 0) {
        win[(*now).first] = 0;
        player.erase(now);
      }
      now = next;
    } else if (i == 'D') {
      (*now).second--;
      auto next = now;
      if (go > 0) {
        next++;
        if (next == player.end()) {
          next = player.begin();
        }
      } else {
        if (next == player.begin()) {
          next = player.end();
        }
        next--;
      }
      (*next).second += 2;
      if (go > 0) {
        next++;
        if (next == player.end()) {
          next = player.begin();
        }
      } else {
        if (next == player.begin()) {
          next = player.end();
        }
        next--;
      }
      if ((*now).second == 0) {
        win[(*now).first] = 0;
        player.erase(now);
      }
      now = next;
    } else {
      (*now).second--;
      auto next = now;
      go *= -1;
      if (go > 0) {
        next++;
        if (next == player.end()) {
          next = player.begin();
        }
      } else {
        if (next == player.begin()) {
          next = player.end();
        }
        next--;
      }
      if ((*now).second == 0) {
        win[(*now).first] = 0;
        player.erase(now);
      }
      now = next;
    }
  }
  for (auto i = player.begin(); i != player.end(); i++) {
    win[(*i).first] = (*i).second;
  }
  for (int i = 1; i < n + 1; i++) {
    std::cout << win[i] << endl;
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