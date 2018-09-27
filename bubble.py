
def bubble_sort(a):

    try:
        length = len(a)

    except:
        print("Bubble sort Exception caught")
        return

    for i in range(length):

        for j in range(1, length-i):

            if a[j-1] > a[j]:

                temp = a[j]

                a[j] = a[j-1]

                a[j-1] = temp

    return a