#ifndef _TAULAMC_HPP_
#include <vector>

class MCcases {
  std::vector<std::vector<std::vector<int> > > casos = {
    {},
    {{3, 10, 0 }},
    {{11, 3, 2 }},
    {{11, 0, 2 }, {11, 10, 0 }},
    {{10, 7, 4 }},
    {{3, 4, 0 }, {3, 7, 4 }},
    {{10, 2, 4 }, {2, 7, 4 }, {2, 11, 7 }, {10, 3, 2 }},
    {{11, 0, 2 }, {11, 4, 0 }, {11, 7, 4 }},
    {{7, 11, 6 }},
    {{7, 0, 6 }, {0, 11, 6 }, {0, 3, 11 }, {7, 10, 0 }},
    {{7, 2, 6 }, {7, 3, 2 }},
    {{7, 2, 6 }, {7, 0, 2 }, {7, 10, 0 }},
    {{10, 6, 4 }, {10, 11, 6 }},
    {{3, 4, 0 }, {3, 6, 4 }, {3, 11, 6 }},
    {{10, 6, 4 }, {10, 2, 6 }, {10, 3, 2 }},
    {{4, 2, 6 }, {4, 0, 2 }},
    {{8, 1, 0 }},
    {{8, 3, 10 }, {8, 1, 3 }},
    {{8, 3, 0 }, {8, 11, 3 }, {8, 2, 11 }, {8, 1, 2 }},
    {{8, 11, 10 }, {8, 2, 11 }, {8, 1, 2 }},
    {{8, 7, 4 }, {8, 1, 7 }, {1, 10, 7 }, {1, 0, 10 }},
    {{8, 7, 4 }, {8, 3, 7 }, {8, 1, 3 }},
    {{8, 7, 4 }, {8, 11, 7 }, {8, 2, 11 }, {8, 1, 2 }, {3, 0, 10 }},
    {{8, 7, 4 }, {8, 11, 7 }, {8, 2, 11 }, {8, 1, 2 }},
    {{8, 6, 7 }, {11, 6, 1 }, {0, 7, 11 }, {6, 8, 1 }, {0, 8, 7 }, {11, 1, 0 }},
    {{8, 7, 10 }, {8, 6, 7 }, {8, 11, 6 }, {8, 3, 11 }, {8, 1, 3 }},
    {{8, 3, 0 }, {8, 7, 3 }, {8, 6, 7 }, {8, 2, 6 }, {8, 1, 2 }},
    {{8, 7, 10 }, {8, 6, 7 }, {8, 2, 6 }, {8, 1, 2 }},
    {{8, 6, 4 }, {8, 11, 6 }, {8, 1, 11 }, {1, 10, 11 }, {1, 0, 10 }},
    {{8, 6, 4 }, {8, 11, 6 }, {8, 3, 11 }, {8, 1, 3 }},
    {{8, 6, 4 }, {8, 2, 6 }, {8, 1, 2 }, {3, 0, 10 }},
    {{8, 6, 4 }, {8, 2, 6 }, {8, 1, 2 }},
    {{1, 9, 2 }},
    {{1, 10, 0 }, {1, 9, 10 }, {9, 3, 10 }, {9, 2, 3 }},
    {{1, 11, 3 }, {1, 9, 11 }},
    {{1, 10, 0 }, {1, 11, 10 }, {1, 9, 11 }},
    {{1, 4, 10 }, {9, 7, 4 }, {10, 7, 2 }, {7, 9, 2 }, {4, 1, 9 }, {2, 1, 10 }},
    {{1, 4, 0 }, {1, 7, 4 }, {1, 9, 7 }, {9, 3, 7 }, {9, 2, 3 }},
    {{1, 10, 3 }, {1, 4, 10 }, {1, 7, 4 }, {1, 11, 7 }, {1, 9, 11 }},
    {{1, 4, 0 }, {1, 7, 4 }, {1, 11, 7 }, {1, 9, 11 }},
    {{1, 11, 2 }, {1, 7, 11 }, {1, 6, 7 }, {1, 9, 6 }},
    {{1, 10, 0 }, {1, 7, 10 }, {1, 6, 7 }, {1, 9, 6 }, {2, 3, 11 }},
    {{1, 7, 3 }, {1, 6, 7 }, {1, 9, 6 }},
    {{1, 10, 0 }, {1, 7, 10 }, {1, 6, 7 }, {1, 9, 6 }},
    {{1, 11, 2 }, {1, 10, 11 }, {1, 4, 10 }, {1, 6, 4 }, {1, 9, 6 }},
    {{1, 4, 0 }, {1, 6, 4 }, {1, 9, 6 }, {2, 3, 11 }},
    {{1, 10, 3 }, {1, 4, 10 }, {1, 6, 4 }, {1, 9, 6 }},
    {{1, 4, 0 }, {1, 6, 4 }, {1, 9, 6 }},
    {{8, 2, 0 }, {8, 9, 2 }},
    {{8, 3, 10 }, {8, 2, 3 }, {8, 9, 2 }},
    {{8, 3, 0 }, {8, 11, 3 }, {8, 9, 11 }},
    {{8, 11, 10 }, {8, 9, 11 }},
    {{8, 7, 4 }, {8, 2, 7 }, {2, 10, 7 }, {2, 0, 10 }, {8, 9, 2 }},
    {{8, 7, 4 }, {8, 3, 7 }, {8, 2, 3 }, {8, 9, 2 }},
    {{8, 7, 4 }, {8, 11, 7 }, {8, 9, 11 }, {3, 0, 10 }},
    {{8, 7, 4 }, {8, 11, 7 }, {8, 9, 11 }},
    {{8, 2, 0 }, {8, 11, 2 }, {8, 7, 11 }, {8, 6, 7 }, {8, 9, 6 }},
    {{8, 7, 10 }, {8, 6, 7 }, {8, 9, 6 }, {2, 3, 11 }},
    {{8, 3, 0 }, {8, 7, 3 }, {8, 6, 7 }, {8, 9, 6 }},
    {{8, 7, 10 }, {8, 6, 7 }, {8, 9, 6 }},
    {{8, 6, 4 }, {8, 9, 6 }, {2, 10, 11 }, {2, 0, 10 }},
    {{8, 6, 4 }, {8, 9, 6 }, {2, 3, 11 }},
    {{8, 6, 4 }, {8, 9, 6 }, {3, 0, 10 }},
    {{8, 6, 4 }, {8, 9, 6 }},
    {{5, 8, 4 }},
    {{5, 10, 4 }, {5, 3, 10 }, {5, 0, 3 }, {5, 8, 0 }},
    {{5, 2, 11 }, {8, 3, 2 }, {11, 3, 4 }, {3, 8, 4 }, {2, 5, 8 }, {4, 5, 11 }},
    {{5, 10, 4 }, {5, 11, 10 }, {5, 2, 11 }, {5, 0, 2 }, {5, 8, 0 }},
    {{5, 10, 7 }, {5, 8, 10 }},
    {{5, 3, 7 }, {5, 0, 3 }, {5, 8, 0 }},
    {{5, 11, 7 }, {5, 2, 11 }, {5, 3, 2 }, {5, 10, 3 }, {5, 8, 10 }},
    {{5, 11, 7 }, {5, 2, 11 }, {5, 0, 2 }, {5, 8, 0 }},
    {{5, 11, 6 }, {5, 8, 11 }, {8, 7, 11 }, {8, 4, 7 }},
    {{5, 11, 6 }, {5, 3, 11 }, {5, 0, 3 }, {5, 8, 0 }, {4, 7, 10 }},
    {{5, 2, 6 }, {5, 3, 2 }, {5, 8, 3 }, {8, 7, 3 }, {8, 4, 7 }},
    {{5, 2, 6 }, {5, 0, 2 }, {5, 8, 0 }, {4, 7, 10 }},
    {{5, 11, 6 }, {5, 10, 11 }, {5, 8, 10 }},
    {{5, 11, 6 }, {5, 3, 11 }, {5, 0, 3 }, {5, 8, 0 }},
    {{5, 2, 6 }, {5, 3, 2 }, {5, 10, 3 }, {5, 8, 10 }},
    {{5, 2, 6 }, {5, 0, 2 }, {5, 8, 0 }},
    {{5, 0, 4 }, {5, 1, 0 }},
    {{5, 10, 4 }, {5, 3, 10 }, {5, 1, 3 }},
    {{5, 0, 4 }, {5, 3, 0 }, {5, 11, 3 }, {5, 2, 11 }, {5, 1, 2 }},
    {{5, 10, 4 }, {5, 11, 10 }, {5, 2, 11 }, {5, 1, 2 }},
    {{5, 10, 7 }, {5, 0, 10 }, {5, 1, 0 }},
    {{5, 3, 7 }, {5, 1, 3 }},
    {{5, 11, 7 }, {5, 2, 11 }, {5, 1, 2 }, {3, 0, 10 }},
    {{5, 11, 7 }, {5, 2, 11 }, {5, 1, 2 }},
    {{5, 11, 6 }, {5, 0, 11 }, {0, 7, 11 }, {0, 4, 7 }, {5, 1, 0 }},
    {{5, 11, 6 }, {5, 3, 11 }, {5, 1, 3 }, {10, 4, 7 }},
    {{5, 2, 6 }, {5, 1, 2 }, {3, 4, 7 }, {3, 0, 4 }},
    {{5, 2, 6 }, {5, 1, 2 }, {4, 7, 10 }},
    {{5, 11, 6 }, {5, 10, 11 }, {5, 0, 10 }, {5, 1, 0 }},
    {{5, 11, 6 }, {5, 3, 11 }, {5, 1, 3 }},
    {{5, 2, 6 }, {5, 1, 2 }, {3, 0, 10 }},
    {{5, 2, 6 }, {5, 1, 2 }},
    {{1, 4, 2 }, {4, 9, 2 }, {4, 5, 9 }, {1, 8, 4 }},
    {{1, 8, 0 }, {2, 5, 9 }, {2, 4, 5 }, {2, 10, 4 }, {2, 3, 10 }},
    {{1, 11, 3 }, {1, 4, 11 }, {4, 9, 11 }, {4, 5, 9 }, {1, 8, 4 }},
    {{1, 8, 0 }, {9, 4, 5 }, {9, 10, 4 }, {9, 11, 10 }},
    {{1, 7, 2 }, {1, 10, 7 }, {7, 9, 2 }, {7, 5, 9 }, {1, 8, 10 }},
    {{1, 8, 0 }, {2, 5, 9 }, {2, 7, 5 }, {2, 3, 7 }},
    {{1, 10, 3 }, {1, 8, 10 }, {7, 9, 11 }, {7, 5, 9 }},
    {{1, 8, 0 }, {9, 7, 5 }, {9, 11, 7 }},
    {{1, 11, 2 }, {1, 7, 11 }, {1, 4, 7 }, {1, 8, 4 }, {6, 5, 9 }},
    {{1, 8, 0 }, {2, 3, 11 }, {4, 7, 10 }, {9, 6, 5 }},
    {{1, 7, 3 }, {1, 4, 7 }, {1, 8, 4 }, {6, 5, 9 }},
    {{1, 8, 0 }, {4, 7, 10 }, {9, 6, 5 }},
    {{1, 11, 2 }, {1, 10, 11 }, {1, 8, 10 }, {6, 5, 9 }},
    {{1, 8, 0 }, {2, 3, 11 }, {9, 6, 5 }},
    {{1, 10, 3 }, {1, 8, 10 }, {6, 5, 9 }},
    {{1, 8, 0 }, {9, 6, 5 }},
    {{5, 0, 4 }, {5, 2, 0 }, {5, 9, 2 }},
    {{5, 10, 4 }, {5, 3, 10 }, {5, 2, 3 }, {5, 9, 2 }},
    {{5, 0, 4 }, {5, 3, 0 }, {5, 11, 3 }, {5, 9, 11 }},
    {{5, 10, 4 }, {5, 11, 10 }, {5, 9, 11 }},
    {{5, 10, 7 }, {5, 0, 10 }, {5, 2, 0 }, {5, 9, 2 }},
    {{5, 3, 7 }, {5, 2, 3 }, {5, 9, 2 }},
    {{5, 11, 7 }, {5, 9, 11 }, {3, 0, 10 }},
    {{5, 11, 7 }, {5, 9, 11 }},
    {{5, 9, 6 }, {2, 7, 11 }, {2, 4, 7 }, {2, 0, 4 }},
    {{5, 9, 6 }, {2, 3, 11 }, {4, 7, 10 }},
    {{5, 9, 6 }, {3, 4, 7 }, {3, 0, 4 }},
    {{5, 9, 6 }, {4, 7, 10 }},
    {{5, 9, 6 }, {2, 10, 11 }, {2, 0, 10 }},
    {{5, 9, 6 }, {2, 3, 11 }},
    {{5, 0, 10 }, {9, 3, 0 }, {10, 3, 6 }, {3, 9, 6 }, {0, 5, 9 }, {6, 5, 10 }},
    {{5, 9, 6 }},
    {{9, 5, 6 }},
    {{9, 0, 3 }, {10, 0, 5 }, {6, 3, 10 }, {0, 9, 5 }, {6, 9, 3 }, {10, 5, 6 }},
    {{9, 3, 2 }, {9, 5, 3 }, {5, 11, 3 }, {5, 6, 11 }},
    {{9, 0, 2 }, {9, 10, 0 }, {9, 5, 10 }, {5, 11, 10 }, {5, 6, 11 }},
    {{9, 7, 6 }, {9, 10, 7 }, {9, 4, 10 }, {9, 5, 4 }},
    {{9, 7, 6 }, {9, 3, 7 }, {9, 0, 3 }, {9, 4, 0 }, {9, 5, 4 }},
    {{9, 3, 2 }, {9, 10, 3 }, {9, 4, 10 }, {9, 5, 4 }, {7, 6, 11 }},
    {{9, 0, 2 }, {9, 4, 0 }, {9, 5, 4 }, {6, 11, 7 }},
    {{9, 7, 11 }, {9, 5, 7 }},
    {{9, 3, 11 }, {9, 0, 3 }, {9, 10, 0 }, {9, 7, 10 }, {9, 5, 7 }},
    {{9, 3, 2 }, {9, 7, 3 }, {9, 5, 7 }},
    {{9, 0, 2 }, {9, 10, 0 }, {9, 7, 10 }, {9, 5, 7 }},
    {{9, 10, 11 }, {9, 4, 10 }, {9, 5, 4 }},
    {{9, 3, 11 }, {9, 0, 3 }, {9, 4, 0 }, {9, 5, 4 }},
    {{9, 3, 2 }, {9, 10, 3 }, {9, 4, 10 }, {9, 5, 4 }},
    {{9, 0, 2 }, {9, 4, 0 }, {9, 5, 4 }},
    {{9, 0, 6 }, {0, 5, 6 }, {0, 8, 5 }, {9, 1, 0 }},
    {{9, 10, 6 }, {9, 3, 10 }, {10, 5, 6 }, {10, 8, 5 }, {9, 1, 3 }},
    {{9, 1, 2 }, {3, 6, 11 }, {3, 5, 6 }, {3, 8, 5 }, {3, 0, 8 }},
    {{9, 1, 2 }, {5, 10, 8 }, {5, 11, 10 }, {5, 6, 11 }},
    {{9, 7, 6 }, {9, 10, 7 }, {9, 0, 10 }, {9, 1, 0 }, {4, 8, 5 }},
    {{9, 7, 6 }, {9, 3, 7 }, {9, 1, 3 }, {4, 8, 5 }},
    {{9, 1, 2 }, {3, 0, 10 }, {5, 4, 8 }, {6, 11, 7 }},
    {{9, 1, 2 }, {7, 6, 11 }, {5, 4, 8 }},
    {{9, 7, 11 }, {9, 0, 7 }, {0, 5, 7 }, {0, 8, 5 }, {9, 1, 0 }},
    {{9, 3, 11 }, {9, 1, 3 }, {5, 10, 8 }, {5, 7, 10 }},
    {{9, 1, 2 }, {3, 5, 7 }, {3, 8, 5 }, {3, 0, 8 }},
    {{9, 1, 2 }, {5, 10, 8 }, {5, 7, 10 }},
    {{9, 10, 11 }, {9, 0, 10 }, {9, 1, 0 }, {5, 4, 8 }},
    {{9, 3, 11 }, {9, 1, 3 }, {5, 4, 8 }},
    {{9, 1, 2 }, {3, 0, 10 }, {5, 4, 8 }},
    {{9, 1, 2 }, {5, 4, 8 }},
    {{1, 6, 2 }, {1, 5, 6 }},
    {{1, 10, 0 }, {1, 6, 10 }, {6, 3, 10 }, {6, 2, 3 }, {1, 5, 6 }},
    {{1, 11, 3 }, {1, 6, 11 }, {1, 5, 6 }},
    {{1, 10, 0 }, {1, 11, 10 }, {1, 6, 11 }, {1, 5, 6 }},
    {{1, 6, 2 }, {1, 7, 6 }, {1, 10, 7 }, {1, 4, 10 }, {1, 5, 4 }},
    {{1, 4, 0 }, {1, 5, 4 }, {2, 7, 6 }, {2, 3, 7 }},
    {{1, 10, 3 }, {1, 4, 10 }, {1, 5, 4 }, {7, 6, 11 }},
    {{1, 4, 0 }, {1, 5, 4 }, {6, 11, 7 }},
    {{1, 11, 2 }, {1, 7, 11 }, {1, 5, 7 }},
    {{1, 10, 0 }, {1, 7, 10 }, {1, 5, 7 }, {2, 3, 11 }},
    {{1, 7, 3 }, {1, 5, 7 }},
    {{1, 10, 0 }, {1, 7, 10 }, {1, 5, 7 }},
    {{1, 11, 2 }, {1, 10, 11 }, {1, 4, 10 }, {1, 5, 4 }},
    {{1, 4, 0 }, {1, 5, 4 }, {2, 3, 11 }},
    {{1, 10, 3 }, {1, 4, 10 }, {1, 5, 4 }},
    {{1, 4, 0 }, {1, 5, 4 }},
    {{8, 2, 0 }, {8, 6, 2 }, {8, 5, 6 }},
    {{8, 3, 10 }, {8, 2, 3 }, {8, 6, 2 }, {8, 5, 6 }},
    {{8, 3, 0 }, {8, 11, 3 }, {8, 6, 11 }, {8, 5, 6 }},
    {{8, 11, 10 }, {8, 6, 11 }, {8, 5, 6 }},
    {{8, 5, 4 }, {2, 7, 6 }, {2, 10, 7 }, {2, 0, 10 }},
    {{8, 5, 4 }, {2, 7, 6 }, {2, 3, 7 }},
    {{8, 5, 4 }, {3, 0, 10 }, {6, 11, 7 }},
    {{8, 5, 4 }, {7, 6, 11 }},
    {{8, 2, 0 }, {8, 11, 2 }, {8, 7, 11 }, {8, 5, 7 }},
    {{8, 7, 10 }, {8, 5, 7 }, {2, 3, 11 }},
    {{8, 3, 0 }, {8, 7, 3 }, {8, 5, 7 }},
    {{8, 7, 10 }, {8, 5, 7 }},
    {{8, 5, 4 }, {2, 10, 11 }, {2, 0, 10 }},
    {{8, 2, 3 }, {11, 2, 5 }, {4, 3, 11 }, {2, 8, 5 }, {4, 8, 3 }, {11, 5, 4 }},
    {{8, 5, 4 }, {3, 0, 10 }},
    {{8, 5, 4 }},
    {{9, 4, 6 }, {9, 8, 4 }},
    {{9, 4, 6 }, {9, 10, 4 }, {9, 3, 10 }, {9, 0, 3 }, {9, 8, 0 }},
    {{9, 3, 2 }, {9, 4, 3 }, {4, 11, 3 }, {4, 6, 11 }, {9, 8, 4 }},
    {{9, 0, 2 }, {9, 8, 0 }, {6, 10, 4 }, {6, 11, 10 }},
    {{9, 7, 6 }, {9, 10, 7 }, {9, 8, 10 }},
    {{9, 7, 6 }, {9, 3, 7 }, {9, 0, 3 }, {9, 8, 0 }},
    {{9, 3, 2 }, {9, 10, 3 }, {9, 8, 10 }, {7, 6, 11 }},
    {{9, 0, 2 }, {9, 8, 0 }, {6, 11, 7 }},
    {{9, 7, 11 }, {9, 4, 7 }, {9, 8, 4 }},
    {{9, 3, 11 }, {9, 0, 3 }, {9, 8, 0 }, {4, 7, 10 }},
    {{9, 3, 2 }, {9, 7, 3 }, {9, 4, 7 }, {9, 8, 4 }},
    {{9, 0, 2 }, {9, 8, 0 }, {10, 4, 7 }},
    {{9, 10, 11 }, {9, 8, 10 }},
    {{9, 3, 11 }, {9, 0, 3 }, {9, 8, 0 }},
    {{9, 3, 2 }, {9, 10, 3 }, {9, 8, 10 }},
    {{9, 0, 2 }, {9, 8, 0 }},
    {{9, 4, 6 }, {9, 0, 4 }, {9, 1, 0 }},
    {{9, 4, 6 }, {9, 10, 4 }, {9, 3, 10 }, {9, 1, 3 }},
    {{9, 1, 2 }, {3, 6, 11 }, {3, 4, 6 }, {3, 0, 4 }},
    {{9, 1, 2 }, {4, 11, 10 }, {4, 6, 11 }},
    {{9, 7, 6 }, {9, 10, 7 }, {9, 0, 10 }, {9, 1, 0 }},
    {{9, 7, 6 }, {9, 3, 7 }, {9, 1, 3 }},
    {{9, 1, 2 }, {3, 0, 10 }, {6, 11, 7 }},
    {{9, 1, 2 }, {7, 6, 11 }},
    {{9, 7, 11 }, {9, 4, 7 }, {9, 0, 4 }, {9, 1, 0 }},
    {{9, 3, 11 }, {9, 1, 3 }, {4, 7, 10 }},
    {{9, 1, 2 }, {3, 4, 7 }, {3, 0, 4 }},
    {{9, 4, 7 }, {10, 4, 1 }, {2, 7, 10 }, {4, 9, 1 }, {2, 9, 7 }, {10, 1, 2 }},
    {{9, 10, 11 }, {9, 0, 10 }, {9, 1, 0 }},
    {{9, 3, 11 }, {9, 1, 3 }},
    {{9, 1, 2 }, {3, 0, 10 }},
    {{9, 1, 2 }},
    {{1, 6, 2 }, {1, 4, 6 }, {1, 8, 4 }},
    {{1, 8, 0 }, {2, 4, 6 }, {2, 10, 4 }, {2, 3, 10 }},
    {{1, 11, 3 }, {1, 6, 11 }, {1, 4, 6 }, {1, 8, 4 }},
    {{1, 8, 0 }, {6, 10, 4 }, {6, 11, 10 }},
    {{1, 6, 2 }, {1, 7, 6 }, {1, 10, 7 }, {1, 8, 10 }},
    {{1, 8, 0 }, {2, 7, 6 }, {2, 3, 7 }},
    {{1, 10, 3 }, {1, 8, 10 }, {7, 6, 11 }},
    {{1, 6, 11 }, {7, 6, 8 }, {0, 11, 7 }, {6, 1, 8 }, {0, 1, 11 }, {7, 8, 0 }},
    {{1, 11, 2 }, {1, 7, 11 }, {1, 4, 7 }, {1, 8, 4 }},
    {{1, 8, 0 }, {2, 3, 11 }, {4, 7, 10 }},
    {{1, 7, 3 }, {1, 4, 7 }, {1, 8, 4 }},
    {{1, 8, 0 }, {10, 4, 7 }},
    {{1, 11, 2 }, {1, 10, 11 }, {1, 8, 10 }},
    {{1, 8, 0 }, {2, 3, 11 }},
    {{1, 10, 3 }, {1, 8, 10 }},
    {{1, 8, 0 }},
    {{0, 6, 2 }, {0, 4, 6 }},
    {{3, 6, 2 }, {3, 4, 6 }, {3, 10, 4 }},
    {{11, 4, 6 }, {11, 0, 4 }, {11, 3, 0 }},
    {{11, 4, 6 }, {11, 10, 4 }},
    {{10, 2, 0 }, {10, 6, 2 }, {10, 7, 6 }},
    {{3, 6, 2 }, {3, 7, 6 }},
    {{10, 3, 0 }, {7, 6, 11 }},
    {{11, 7, 6 }},
    {{7, 0, 4 }, {7, 2, 0 }, {7, 11, 2 }},
    {{7, 10, 4 }, {2, 3, 11 }},
    {{7, 0, 4 }, {7, 3, 0 }},
    {{7, 10, 4 }},
    {{10, 2, 0 }, {10, 11, 2 }},
    {{3, 11, 2 }},
    {{10, 3, 0 }},
{},
};

public:
  const std::vector<std::vector<int> >& operator()(int n) const {
    return casos.at(n);
  }
};
#define _TAULAMC_HPP_
#endif
