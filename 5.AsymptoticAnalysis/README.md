# Q5. Asymptotic analysis

![amortized analysis](./src/amortized%20analysis.png)

$\Phi_{data\ structure}: Potential\ cost$

$Amortized\ cost_{function}(run\ time)\ =\ real\ cost_{function}+ \Delta \Phi$

##  1 단계
- 각 operation의 real cost를 구한다.
- 예1 2개의 stack을 이용한 queue 구현) isEmpty(): 2, Enqueue(): 1, Dequeue(): 2+3x
- 예2 사이즈가 변하는 hash table) insert() without reallocation: 1, insert() with reallocation: 1.5s, delete() without reallocation: 1, delete() with reallocation: s

## 2단계
- Potential cost 함수를 정의 한다.
- 예1) $\Phi_{queue} = 3\cdot N(elements\ in\ stack\ 1)$
- 얘2) $\Phi_{Hash\ table} = 5 \cdot N(elements\ from\ 60\% \ full)$

## 3단계
- 각 함수들의 amortized cost를 구한다.
- 각 amortized cost는 정수로 나와야 한다.
- 예) $amortized\ cost_{enqueue()} = 1 + (3k - 3(k-1)) = 4$
- 예) $amortized\ cost_{dequeue()} = (2+3x) +(0-3x) = 2$
- 만약에, amortized cost에 변수가 발생하면, potential cost 함수를 수정해야 한다.

## 4단계
- Worst case runtime을 구한다.
- Amortized cost로 나타내진 함수들의 cost 중에 가장 큰것을 고른 다음에, operation의 개수 만큼 곱한다.
- queue 구현의 예) $\sum_{i=1}^{n} real\ cost_{i} \leq \sum_{i=1}^{n} amortized\ cost_{i} \leq 4n = \Theta(n)$
- hash table 구현의 예) $\sum_{i=1}^{t} real\ cost_{i} \leq \sum_{i=1}^{t} amortized\ cost_{i} \leq 6t \leq O(t)$

# 참고 - Potential 함수의 예
|주제|$\Phi_{data\ structure}$|
|--|------|
|queue 구현|3*(stack1에 있는 element 개수)|
|hash table 구현|5*(60% full로 부터 element 개수)|
|largest prefix and suffix (Tuturial 8)|$\beta[i]의 값$