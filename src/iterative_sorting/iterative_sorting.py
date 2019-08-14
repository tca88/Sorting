# TO-DO: Complete the selection_sort() function below
height = [65, 48, 60, 54, 32, 89, 72] 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for n in range(i+1, len(arr)):
        #     if arr[n] < arr[smallest_index]:
        #         smallest_index = n
        # arr[cur_index],arr[smallest_index]=arr[smallest_index],arr[cur_index]

        #alternative solution
            if arr[n] < arr[cur_index]:
                smallest_index = n
                temp = arr[cur_index]
                arr[cur_index]=arr[smallest_index]
                arr[smallest_index] = temp




        # TO-DO: swap




    return arr
selection_sort(height)
for h in height:
    print(h)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j -1]: # while we're not at the right spot (we're in the right place if the one below it is less)
            arr[j], arr[j - 1] = arr[j - 1], arr[j] #swap
            j -= 1
            #back up and look at the previous spot

    return arr
bubble_sort(height)
for x in height:
    print(x)

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr