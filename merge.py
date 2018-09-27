
def merge_sort(a):

    try:
        if len(a) < 2:
            return a

    except:
        print("Merge sort Exception caught")
        return


    mid = int(len(a)/2)

    left = merge_sort(a[mid:])
    right = merge_sort(a[:mid])

    to_return = []
    l_index = 0
    r_index = 0

    while(l_index < len(left) and r_index < len(right)):

        if left[l_index] < right[r_index]:
            to_return.append(left[l_index])
            l_index += 1
        else:
            to_return.append(right[r_index])
            r_index += 1

    for i in range(len(left) - l_index):
        to_return.append(left[l_index])
        l_index += 1

    for i in range(len(right) - r_index):
        to_return.append(right[r_index])
        r_index += 1

    return to_return

