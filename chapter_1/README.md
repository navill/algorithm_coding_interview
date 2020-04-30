# chapter.1 배열과 문자열

- is_unique: 중복되는 문자가 없는지 확인

    - hash(set())를 이용해 문자를 저장하고, hash에 해당 문자가 있는지 확인

    - 각 문자의 이진값과 checkbit를 이용해 중복되는 bit를 판별

        ```python
        s = 'abcba'
        for i in s:
          	# i = 'a'일 때
            val = ord(i) - ord('a')
            # val = 0(a에 대한 값)
                if ((1 << val) & checker) > 0:
                # 1 & 0 == 0
                    print('False')
                checker = (1 << val) | checker
                # checker = 1 | 0 
                # checker는 1이 된다. 만일 이 후 a(0)이 한 번 더 올 경우
                # 1 & 1 > 0이 되면서 False를 반환한다.
                # a -> checker = 1
                # b -> checker = 11
                # c -> checker = 111
                # a -> checker = 111
                # 1 << 0 & checker == 1
        ```

        

- palindrome: 회문 알고리즘
    - 각 문자의 개수를 확인하고 홀수개의 문자가 두 개 이상일 경우 False 반환

    - 해당 문자에 대한 bit mask를 생성하고 이를 bitvector와 비교하면서 같은 문자열이 있는지 확인

      ```python
      bitvector = 0
      # s = 'abcba'
      for i in s:
          # i = 'a'
          mask = 1 << (ord(i) - ord('a'))
          # mask = 0b1
          if bitvector & mask == 0:  # True
              bitvector |= mask  # bit on
              # bitvector = 0b1
              # a, bitvector = 0b1
              # b, bitvector = 0b11
              # c, bitvector = 0b111
          else:
              bitvector &= ~mask  # bit off
              # b, bitvector = 0b101
              # a, bitvector = 0b100
          return True if bitvector & (bitvector - 1) == 0 or bitvector == 0 else False
        	# bitvector = 0b100
          # bitvector - 1 = 0b011
          # 0b100 & 0b011 == 0 
      ```

      ```python
      <1로 셋팅된 비트 확인>
      
      00010000 - 1 = 00001111
      00010000 & 00001111 = 0
      => 전체 비트 중 한 개의 비트만 1로 셋팅됨을 의미
      
      00010001 - 1 = 00010000
      00010001 & 00010000 = 00010000
      00010000 
      => 전체 비트 중 한 개 이상의 비트가 1로 셋팅됨을 의미 
      ```



- replace_spaces: 공백을 특정 문자로 변환하는 알고리즘
  - python의 replace()를 사용하지 않고 구현
    1. 전체 문자(원본)를 순환하며 공백 확인
    2. 공백 + 전체 문자 길이 만큼 배열 생성
    3. 원본의 뒤에서부터 문자를 확인해가며 공백이 있을 경우 '02%' 삽입

- string_compression: 문자열 압축(abbcaaaccc -> a1b2c1a3c3)

- string_permutation: 순열 문자 확인
- string_rotation: 두 개의 문자열 중 한 개의 문자열을 회전시켰을 때, 나머지 한 문자열과 동일한 문자열인지 판별하는 알고리즘
- subtract: 두 개의 문자열에서 문자열을 같게 만들기 위한 편집횟수가 1회 이내인지 확인하는 함수
- zero_matrix: 한 원소가 0일 때, 해당 원소가 속한 행과 열을 모두 0으로 변환하는 함수