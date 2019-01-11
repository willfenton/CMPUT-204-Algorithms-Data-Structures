# Insertion Sort algorithm implemented in Python 3
# January 11 2019

# Selection sort works by scanning the array for the smallest element, then swapping it into the first position.
# Then repeat, finding second largest, swapping into second position. Repeat until array is sorted.
# Loop invariant: after n iterations of the outer for loop, the array[1..n] is sorted in non-decreasing order.

# Worst case runtime: O(n^2) (O(N) swaps)
# Average case runtime: O(n^2) (O(N) swaps)
# Best case runtime: O(n^2) (O(N) swaps)

# Space complexity: Sorts in-place, so constant O(1) additional memory usage

from random import randint

def selectionSort(array):
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

def selectionSortNonIncreasing(array):
    for i in range(0, len(array) - 1):
        max_index = i
        for j in range(i + 1, len(array)):
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]

    return array


# Ensures that the algorithm sorts correctly
def testCorrectness():
    tests = 10
    input_size = 10

    bound = 1000000000

    for i in range(tests):

        unsorted_list = [randint(-bound, bound) for i in range(input_size)]
        sorted_list = list(unsorted_list)

        selectionSort(sorted_list)

        print(unsorted_list)
        print(sorted_list)
        print(sorted(unsorted_list))
        print()

        assert(sorted_list == sorted(unsorted_list))

    print("\nPassed all tests!\n")


if __name__ == "__main__":
    testCorrectness()
