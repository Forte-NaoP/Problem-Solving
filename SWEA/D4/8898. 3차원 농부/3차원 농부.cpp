#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <array>
#include <vector>
#include <cmath>

using namespace std;

pair<int, int> ans; 

int cow[500000];
int horse[500000];
int n, m;

void find(int x, int size) {
	int begin = 0;
	int end = size - 1;

	while (begin <= end) {
		int mid = begin + (end - begin) / 2;

		if(abs(x - horse[mid]) < ans.first) {
			ans.first = abs(x - horse[mid]);
			ans.second = 1;
		} else if (abs(x - horse[mid]) == ans.first) {
			ans.second += 1;
		}

		if (x < horse[mid]) end = mid - 1;
		else if (x > horse[mid]) begin = mid + 1;
		else break;
	}

}

int main() {
	int T;
    scanf("%d", &T);

	int c1, c2, x;
    for (int i=1; i<=T; ++i) {
		ans = make_pair(INT32_MAX, 0);

        scanf("%d%d", &n, &m);
		scanf("%d%d", &c1, &c2);
		int diff = abs(c1 - c2);

		for (int j=0; j<n; ++j) scanf("%d", &cow[j]);
		for (int j=0; j<m; ++j) scanf("%d", &horse[j]);
		sort(horse, horse+m);

		for (int j=0; j<n; ++j) find(cow[j], m);
		printf("#%d %d %d\n", i, ans.first+diff, ans.second);
    }
}