
def insertion_sort(a):

    try:
        length = len(a)

    except:
        print("Insertion sort Exception caught")
        return

    for i in range(1, length):

        current = a[i]

        j = i-1

        while(j >= 0 and current < a[j]):

            a[j+1] = a[j]

            j -= 1

        a[j+1] = current

    return a