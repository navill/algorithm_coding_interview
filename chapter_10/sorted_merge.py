def sorted_merge(a, b):
    index_merged = len(a) - 1
    index_b = len(b) - 1
    index_a = len(a) - len(b) - 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1


a = [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0]
b = [1, 2, 3, 4, 5, 6]
sorted_merge(a, b)
print(a)

#
# def SortedMerge(A, B):
#     index = len(A) - 1
#     indexB = len(B) - 1
#     indexA = len(A) - len(B) - 1
#
#     while indexB >= 0:
#         if indexA > 0 and A[indexA] > B[indexB]:
#             A[index] = A[indexA]
#             indexA -= 1
#         else:
#             A[index] = B[indexB]
#             indexB -= 1
#         index -= 1
#     return A
#
#
# def FillArrayUpTo(maxnum):
#     nums = [0] * maxnum
#     for i in range(len(nums)):
#         nums[i] = 2 * i + 4
#     return nums
#
#
# def FillArrayWithBuffer(length, buffer):
#     nums = [0] * (length + buffer)
#     for i in range(length):
#         nums[i] = 3 * i + 1
#     return nums
#
# A = FillArrayWithBuffer(5, 10)
# B = FillArrayUpTo(10)
# print(A, B)
# print(SortedMerge(A, B))