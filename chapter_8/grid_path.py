"""
행의 개수는 r, 열의 개수는 c. 격자판의 왼쪽 상단에서 오른쪽 하단으로 로봇이 이동(오직 오른쪽과 아래로만 이동)할 때, 금지 구역(False)을 제외한 이동 경로를 찾는 알고리즘 설계

"""


# O(2^r+c), memoization을 사용할 경우 O(rc)
def get_path(maze):
    if maze is None or len(maze) == 0:
        return None
    p = list()  # result
    failed_point = list()  # memoization
    if is_path(maze, len(maze) - 1, len(maze[0]) - 1, p, failed_point):
        return p
    return None


def is_path(maze, row, col, path, failed_point):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    is_origin = (row == 0) and (col == 0)
    point = (row, col)
    if point in failed_point:  # cache
        return False

    # 도착점부터 역으로 진행한다. -> row-1, col-1
    if is_origin or is_path(maze, row, col - 1, path, failed_point) or is_path(maze, row - 1, col, path, failed_point):
        path.append(point)
        return True
    failed_point.append(point)
    return False


print(get_path([[True, True, True, True],
                [True, False, True, True]]))
