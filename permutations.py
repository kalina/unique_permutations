import sys

""" Intially I looked at the built in intertools  but it returned all permutations.
  So I decided to implement a solution using lexographic ordering.
"""

def get_permutations(string):
    """returns a list of unique permutations from the passed in string
        :param str string: String to find permutations
        :rtype list
    """
    # convert to list and sort it
    arr = list(string)
    arr.sort()
    process = True
    out = []

    while process:
        out.append(''.join(arr))
        process = get_next_permutation(arr)
    return out

def get_next_permutation(arr):
    """Modifies the passed in list to be the next permutation.
       Returns true until at the last permutation
        :param list arr array of sorted characters
        :rtype boolean
    """
    # Find largest index i where arr[i-1] < arr[i]
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0: # Already at last permutation
        return False

    # Find the largest j where j >= i and arr[j] > arr[i-1]
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    # swap arr[j] and arr[i-1]
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix beginning at arr[i]
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

def main():
    """Main entry point
    """
    print get_permutations(sys.argv[1])

if __name__ == "__main__":
    main()
