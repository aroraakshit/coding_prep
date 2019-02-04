#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {

  // Dot product of two sparse vectors stored in hash tables
  unordered_map<int, double> asht({{0, 1.}, {7, 2.}, {8, 3.}});
  unordered_map<int, double> bsht({{7, 4.}, {8, 9.}});

  int idx_a;
  double val_a, val_b;
  double dot = 0;

  for (auto it : asht) {
    idx_a = it.first;
    val_a = it.second;
    auto itb = bsht.find(idx_a);
    if (itb != bsht.end()) {
      val_b = itb->second;
      dot += val_a * val_b;
    }
  }
  cout << dot; // 35

  return 0;
}