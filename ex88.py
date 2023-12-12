def merge1(nums1, m, nums2):
    nums1[:] = nums2
    nums1 = nums2
    nums1.sort()


def merge2(nums1, m, nums2, n):
    helper = []
    p1, p2 = 0, 0
    while p1 < m or p2 < n:
        if p1 == m:
            helper.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            helper.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            helper.append(nums1[p1])
            p1 += 1
        else:
            helper.append(nums2[p2])
            p2 += 1
    nums1[:] = helper


def merge3(nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    tail = m + n - 1
    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1


if __name__ == '__main__':
    n1 = [1, 2, 5, 0, 0, 0]
    n2 = [2, 3, 4]
    len_m = 3
    len_n = 3

    # merge1(n1, len_m, n2)
    # print(n1)

    # merge2(n1, len_m, n2, len_n)
    # print(n1)

    merge3(n1, len_m, n2, len_n)
    print(n1)
