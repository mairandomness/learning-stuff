def  main():
    f = open("IntegerArray.txt", "r")
    array = f.read()[:-1].split("\n")
    array = [int(numb) for numb in array]
    print(array[:10])
    print(array[len(array) -10:len(array)])
    print("This should be 1 ", count_inversions([2,1], 0)[1])
    print("This should be 2 ", count_inversions([2,3,1], 0)[1])
    print("This should be 2 ", count_inversions([2,1,4,3], 0)[1])
    print("This should be 6 ", count_inversions([2,3,5,6,1,4], 0)[1])

    print(count_inversions(array,0)[1])

def count_inversions(array, count):
    #There are inversions only if the array is longer than one element
    if len(array) > 1:
        #divide the array into two parts
        half_way = len(array)//2
        right_array = array[:half_way]
        left_array = array[half_way:]
        #send the parts away in the recursion
        right_array, count_r = count_inversions(right_array, 0)
        left_array, count_l = count_inversions(left_array, 0)

        #when they return, they'll be ordered, so we need to count the split inversions
        r = 0
        l = 0

        while r < len(right_array) and l < len(left_array):
            if right_array[r] > left_array[l]:
                count += len(right_array)-r
                l += 1
            else:
                r += 1

        count += count_r + count_l
        return (sorted(array), count)

    return(array, 0)







if __name__ == "__main__":
    main()
