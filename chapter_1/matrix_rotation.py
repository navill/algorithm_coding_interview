"""
이미지를 표현하는 N x N 행렬을 90도로 회전하는 문제 - time complexity: O(N^2)

for i range(n):
    temp = top[i]
    top[i] = left[i]
    left[i] = bottom[i]
    bottom[i] = right[i]
    right[i] = temp
"""


def rot_matrix(mat):
    if len(mat) == 0 or len(mat) != len(mat[0]):
        return False
    length = len(mat)
    """
        length: 3
        lenght//2: 1
        matrix = 
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
        for layer in range(lenght//2):
            first=layer:0일 때 -> 바깥쪽(1,2,3,6,9,7,8,4) 회전
            layer:1일 때 -> 안쪽(5) 회전 
            for i in range(first, last):
    """
    for layer in range(length // 2):
        first = layer  # first:0
        last = length - 1 - layer  # last:2
        for i in range(layer, last):
            offset = i - first  # i:0, offset:0 -> i:1, offset:1
            top = mat[first][i]
            # mat[0][0] == top
            # top=mat[0][0], left=mat[2][0], bottom=mat[2][2], right=mat[0][2]
            # top=mat[0][1], left=mat[1][0], bottom=mat[2][1], right=mat[1][2]
            mat[first][i], mat[last - offset][first], mat[last][last - offset], mat[i][last] = mat[last - offset][
                                                                                                   first], mat[last][
                                                                                                   last - offset], \
                                                                                               mat[i][last], top


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

rot_matrix(matrix)
print(matrix)

"""
top=mat[0][0], left=mat[2][0], bottom=mat[2][2], right=mat[0][2]
1[0][0]  2   3[0][2]
    4    5   6
7[2][0]  8   9[2][2]

7,4,1
8,5,2
9,6,3
"""
