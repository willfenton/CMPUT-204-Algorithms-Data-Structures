# Insertion Sort algorithm implemented in Python 3
# January 9 2019

# The idea of insertion sort is to do one pass through the list, inserting each element encountered
# into it's proper position in the sorted sub-list to the left of the pointer j.
# This is done by swapping positions with the element to the left of it until
# it's larger than the element to the left and smaller than the element to the right.

# Worst case runtime: O(n^2)
# Average case runtime: O(n^2)
# Best case runtime: O(n)

# Space complexity: Sorts in-place, so constant O(1) additional memory usage

from random import randint

def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and key < array[i]:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array

# Ensures that the algorithm sorts correctly
def testCorrectness():
    tests = 10
    input_size = 10000

    bound = 1000000000

    for i in range(tests):

        unsorted_list = [randint(-bound, bound) for i in range(input_size)]
        sorted_list = list(unsorted_list)

        insertionSort(sorted_list)

        assert(sorted_list == sorted(unsorted_list))

    print("\nPassed all tests!\n")


if __name__ == "__main__":
    testCorrectness()