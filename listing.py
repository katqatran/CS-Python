"""
Katherine Tran

This program has 11 independent functions that employ lists.

"""

def second_largest(numbers):
    """
    The function returns the second-largest number in a list of numbers.
    Arguments:
        Numbers (list): A list of numbers.
    Return Value:
        int: The second-largest number in the list. If the list has less than two numbers, returns None.
    """

    max = numbers[0]
    second_max = numbers[1]
    if second_max > max:
        second_max = numbers[0]
        max = numbers[1]
    for number in numbers:
        if number > max:
            second_max = max
            max = number
        elif number > second_max and number < max:
            second_max = number

    return second_max

def between(numbers, lower, upper):
    """
    The function returns a list of numbers from the input list that are between the specified lower and upper bounds
    (inclusive).
    Arguments:
        Numbers (list): A list of numbers.
        Lower (int): A lower bound range.
        Upper (int): An upper bound range.
    Return Value:
        list: A list of numbers that fall within the specified range.
    """
    list = []
    for number in numbers:
        if number >= lower:
            if number <= upper:
                list.append(number)
    return list

def no_duplicates(numbers):
    """
    The function takes a list of numbers as input and returns a new list of unique elements from the input list, without
    any duplicates.
    Arguments:
        Numbers (list): A list of numbers.
    Return Value:
        list: A list of the unique elements from the input list, without any duplicates.
    """
    duplicate = []
    for number in numbers:
        if not(number in duplicate):
            duplicate.append(number)
    return duplicate

def del_duplicate_adjacents(numbers):
    """
    The function modifies the input list by removing adjacent duplicates of numbers.
    Arguments:
        Numbers (list): A list of numbers.
    Return Value:
        None.
    """
    index = 0
    while index <= len(numbers) - 2:
        if numbers[index] == numbers[index + 1]:
            del numbers[index + 1]
        else:
            index = index + 1

def sum_sublists(lists):
    """
    The function takes a list of lists and returns a new list with the sum of each sublist.
     Arguments:
        Lists (list of list): A list of sublists containing numbers.
    Return Value:
        list: A new list with the sum of each sublist in the input list.
    """
    sum_list = []
    for list in lists:
        sum = 0
        for number in list:
            sum = number + sum
        sum_list.append(sum)
    return sum_list

def flatten(lists):
    """
    The function takes in a list of lists and returns a single flattened list that contains all of the numbers from the
    sublists.
    Arguments:
        Lists (list): A list of lists containing numbers.
    Return Value:
        list: A flattened list containing all of the numbers from the sublists.
    """
    flat_list = []
    for list in lists:
        for number in list:
            flat_list.append(number)
    return flat_list

def is_median(number, target):
    """
    The functions takes a list of numbers and a target value as input, and returns True if the target value is the median
    of the input list, and False otherwise.
    False.
    Arguments:
        Number (list): List of numbers
        Target (int): A number
    Return Value:
        bool: A boolean value indicating whether the target value is the median of the input list.
    """
    lower = 0
    higher = 0

    for spot in number:
        if spot > target:
            higher = higher + 1
        if spot < target:
            lower = lower + 1
    if higher <= len(number)//2 and lower <= len(number)//2:
        return True
    return False

def differences(numbers):
    """
    The function takes a list of numbers as input and returns a new list of numbers where each element is the difference
    between adjacent elements in the input list.
    Arguments:
        Numbers (list): A list of numbers.
    Return Value:
        list: A new list of numbers where each element is the difference between two adjacent elements in the original
        list. If the input list contains only one number, an empty list is returned.
    """
    differences_list = []
    difference = 0

    for index in range(len(numbers) - 1):
        difference = numbers[index + 1] - numbers[index]
        differences_list.append(difference)

    return differences_list

def odds_or_evens(numbers):
    """
    The function takes a list of numbers and returns a new list containing only odd or even values, depending on which
    type of number occurs more frequently in the input list. The function determines the parity of each number using the
    modulus operator and adds it to a new list accordingly. The function compares the lengths of the two new lists and
    returns the list with more elements.
    Arguments:
        Numbers (list): A list of numbers.
    Return Value:
        list: A new list containing only odd or even values, depending on which type of number occurs more frequently in
        the input list.
    """
    odd_list = []
    even_list = []

    for number in numbers:
        if number % 2 == 1:
            odd_list.append(number)
        else:
            even_list.append(number)

    if len(odd_list) > len(even_list):
        return odd_list
    return even_list

def running_total(numbers):
    """
    The function takes a list of numbers and returns a new list where each element is the sum of all the preceding
    elements in the original list, including itself.
    Arguments:
        Numbers (list): A list of numbers to be converted to a comma-separated string.
    Return Value:
        str: A string with the numbers from the input list separated by a comma and a space.

    """
    total_list = []
    sum = 0

    for number in numbers:
        sum = number + sum
        total_list.append(sum)
    return total_list

def comma_separated(numbers) -> str:
    """
    The function takes a list of numbers and returns a new string where the numbers are separated by a comma and a space.
    Arguments:
        Numbers (list): A list of numbers to be converted to a comma-separated string.
    Return Value:
        str: A string with the numbers from the input list separated by a comma and a space. If the list contains less
        than 2 numbers, an empty string is returned.
    """
    comma = ""
    index = 0
    if len(numbers) == 0:
        return ""

    while index <= len(numbers) - 2:
        comma = comma + str(numbers[index]) + ", "
        index = index + 1
    return comma + str(numbers[len(numbers) - 1])

def main():

    print(second_largest([1, 2, 3, 4, 5]))
    print(between([1, 2, 3, 4, 5], 2, 4))
    print(no_duplicates([1, 2, 3, 4, 5, 1]))
    print(sum_sublists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(flatten([[1, 2], [4, 5], [7, 8]]))
    print(differences([1, 2, 3, 4, 5]))
    print(odds_or_evens([1, 2, 3, 4, 5]))
    print(running_total([1, 2, 3]))
    print(comma_separated([1, 2, 4, 3, 2, 6]))
    print(is_median([1,2,3,3,5], 3))

main()
