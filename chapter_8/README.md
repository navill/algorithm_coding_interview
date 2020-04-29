# Chapter.8 재귀와 동적 프로그래밍


### 접근법
- 상향식: 이전에 풀었던 사례를 확장하며 문제를 해결
- 하향식: 전체 사례에서 일부를 해결하며 문제를 해결
- 반반 접근법: 이진탐색, 병합정렬 처럼 전체 데이터를 절반씩 나누고 각각 나뉜 문제를 해결

### 재귀적 해법 vs 순환적 해법
- 재귀 호출 = 메로리 스택에 새로운 층이 추가됨
- 재귀의 깊이가 n일 경우 공간 복잡도는 O(n)
    - 재귀적 해법과 순환적 해법 중 어떤것이 타당한지 고민하고 코드 작성
    
### 동적 계획법 & 메모이제이션
- 재귀 알고리즘에서 반복적으로 호출되는 부분을 찾는 것이 관건
  
    - 현재 결과를 캐시에 저장
- 하향식 동적 프로그래밍(메모이제이션)
    ```python
    # normal recur - O(2^N)
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        return fibonacci2(n - 1) + fibonacci2(n - 2)    
    
    # memoization - O(N)
    me = [None] * (n+1)
    def fibonacci(n, me):
        if n == 0 or n == 1:
            return n
        if me[n] is None:
            me[n] = fibonacci(n - 1, me) + fibonacci(n - 2, me)
        return me[n]
    ```

- 상향식 동적 프로그래밍: fibo(0), fibo(1),... 순서로 연산을 진행한다.

  ```python
  def fibonacci(n):
      if n == 0 or n == 1:
          return n
      memo = [None] * n
      memo[0] = 0
      memo[1] = 1
      for i in range(2, n):
          # memo[i]는 값을 담고 있을 뿐 이후 연산에 사용되지 않음
          memo[i] = memo[i - 1] + memo[i - 2]
      return memo[n - 1] + memo[n - 2]
  
  def fibonacci(n):
      if n == 0 or n == 1:
  	      return n
      a, b = 0, 1
      for i in range(2, n):
    	    a, b = b, a + b
      return a + b
  ```

  
- count_ways: 아이가 n개의 계단을 오를 때, 아이는 1개, 2개, 3개의 계단을 오를 수 있다. 계단에 오르는 방법이 몇 가지가 있는가?
