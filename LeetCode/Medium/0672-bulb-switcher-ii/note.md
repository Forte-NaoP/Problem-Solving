# [Medium] 672. Bulb Switcher II

[문제 링크](https://leetcode.com/problems/bulb-switcher-ii/) 

## 풀이

1 ~ 4번 버튼에 의해 영향을 받는 전구를 나타내보자.

|전구|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|  | |2| |2| |2| |2| |2| |2| |2| |
|  |3| |3| |3| |3| |3| |3| |3| |3|
|  |4| | |4| | |4| | |4| | |4| | |

위의 표를 보면 전구 6개마다 패턴이 반복된다. 

그리고
```
전구 2 = 전구 6
전구 3 = 전구 5
전구 4 = 전구 1 ⊕ 전구 2 ⊕ 전구 3
```
임을 알 수 있다.

따라서 전구는 세개만 고려하면 되며, 버튼을 누르는 횟수에 따라 생기는 조합의 갯수를 세면 된다.

또한 버튼을 누르는 횟수가 3회 이상이면 전구 3개에 대해 모든 경우의 수를 만들 수 있으므로 3회 이상은 3회로 고려하면 된다.

경우의 수를 미리 계산해서 $O(1)$ 시간에 답을 구할 수도 있고
전구 3개에 대해 모든 경우의 수를 만들어서 답을 구할 수도 있다.
