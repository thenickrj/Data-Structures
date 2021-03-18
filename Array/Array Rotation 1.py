# def rotate2(arr, d, l):
#     temp = []
#     for i in range(0, d):
#         temp.append(arr[i])
#     for i in range(d, l):
#         arr[i - d] = arr[i]
#     for i in range(l - d, l):
#         arr[i] = temp.pop()
#     print(arr)


def rotate(arr, d, l):
    for i in range(d):
        arr.append(arr.pop(0))
    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 35, 53, 35]
rotate(arr, 2, 7)
#rotate2(arr, 2, 7)
