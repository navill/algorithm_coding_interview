"""
M x N 행렬에서 한 요소가 0일 때 해당 행과 열의 모든 값을 0으로 변경
time complexity: O(MN)
"""


# 1
def first_zero_matrix(m):
    # 몇 번째 행이 0인지, 몇 번째 열이 0인지 확인하면 됨
    row = [False for _ in range(len(m[0]))]  # 공간 복잡도는 O(N)?? O(M+N)??
    col = [False for _ in range(len(m))]

    for i in range(len(m)):  # col
        for j in range(len(m[0])):  # row
            if m[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(len(col)):
        if col[i]:
            nullify_col(m, i)
    for i in range(len(row)):
        if row[i]:
            nullify_row(m, i)


# 2
def second_zero_matrix(m):
    # check_row = False  # 공간 복잡도 O(1)
    # check_col = False
    # # row에 0위치 확인
    # for i in range(len(m[0])):
    #     if m[0][i] == 0:
    #         check_row = True
    #
    # # col에 0위치 확인
    # for i in range(len(m)):
    #     if m[i][0] == 0:
    #         check_col = True
    #
    # # 첫 번째 행과 열에 0이 있을 경우
    # if check_col and check_row:
    #     nullify_col(m, 0)
    #     nullify_row(m, 0)
    #     return

    # 나머지 배열에 0이 있는지 확인
    for i in range(len(m)):  # col
        for j in range(len(m[0])):  # row
            if m[i][j] == 0:
                m[0][j] = 0  # row
                m[i][0] = 0  # col
    """
    m[i][j]에 0이 있을 경우 m[i][0], m[0][j]를 0으로 만들고 연산
    n n n n  ->  n n 0 n => m[3][0]:0, m[0][2]:0 => nullify_row(m, i), nullify_col(m, j)
    n n n n      n n n n
    n n n n      n n n n
    n n 0 n      0 n 0 n  
    """
    # 해당 row을 0으로
    for i in range(len(m)):
        if m[i][0] == 0:
            nullify_row(m, i)

    # 해당 col을 0으로
    for i in range(len(m[0])):
        if m[0][i] == 0:
            nullify_col(m, i)




def nullify_row(arg_m, r):
    for i in range(len(arg_m[0])):
        arg_m[r][i] = 0


def nullify_col(arg_m, c):
    for i in range(len(arg_m)):
        arg_m[i][c] = 0


m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11]]
# first_zero_matrix(m)
second_zero_matrix(m)
print(m)
