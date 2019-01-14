# Merge Sort algorithm implemented in Python 3
# January 14 2019

# Merge Sort works by recursively splitting the array into equal segments,
# then merging the segments once they can no longer be divided.

# Worst case runtime: O(n*log(n))
# Average case runtime: O(n*log(n))
# Best case runtime: O(n*log(n))

# Space complexity: O(n) additional memory usage, because of storing left and right subarrays during the merge step

from random import randint

def merge(array, leftBound, midPoint, rightBound):
    n1 = midPoint - leftBound + 1
    n2 =  rightBound - midPoint

    left = array[leftBound : midPoint + 1]
    right = array[midPoint + 1 : rightBound + 1]

    leftIndex = rightIndex = 0
    arrayIndex = leftBound

    while leftIndex < n1 and rightIndex < n2:
        if left[leftIndex] <= right[rightIndex]:
            array[arrayIndex] = left[leftIndex]
            arrayIndex += 1
            leftIndex += 1
        else:
            array[arrayIndex] = right[rightIndex]
            arrayIndex += 1
            rightIndex += 1

    while leftIndex < n1:
        array[arrayIndex] = left[leftIndex]
        arrayIndex += 1
        leftIndex += 1

    while rightIndex < n2:
        array[arrayIndex] = right[rightIndex]
        arrayIndex += 1
        rightIndex += 1


def mergeSort(array, leftBound, rightBound):
    if leftBound < rightBound:
        midPoint = (leftBound + rightBound) // 2
        mergeSort(array, leftBound, midPoint)
        mergeSort(array, midPoint + 1, rightBound)
        merge(array, leftBound, midPoint, rightBound)


# Ensures that the algorithm sorts correctly
def testCorrectness():
    tests = 100
    input_size = 10000

    bound = 1000000000

    for i in range(tests):

        unsorted_list = [randint(-bound, bound) for i in range(input_size)]
        sorted_list = list(unsorted_list)

        mergeSort(sorted_list, 0, len(sorted_list) - 1)

        assert(sorted_list == sorted(unsorted_list))

    print("\nPassed all tests!\n")


if __name__ == "__main__":
    testCorrectness()
