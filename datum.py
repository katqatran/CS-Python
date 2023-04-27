"""
Katherine Tran

This program has 7 independent functions.
"""

def sum_two(D1, D2):
    """
    The functions returns a new dictionary that combines the key-value pairs from two input dictionaries.
    Arguments:
        D1 (dict): The first dictionary.
        D2 (dict): The second dictionary.
    Return Value:
        dict: A new dictionary that contains the key-value pairs from both D1 and D2. If a key is present in both
        dictionaries, the corresponding values are added together in the new dictionary.
    """
    result = {}
    for letter in D1:
        result[letter] = D1[letter]

    for value in D2:
        if value in result:
            result[value] = result[value] + D2[value]
        elif value not in result:
            result[value] = D2[value]
    return result

def sum_all(list_dictionaries):
    """
    The function takes a list of dictionaries, and returns a new dictionary that contains the sum of all the dictionaries.
    Arguments:
        list_dictionaries (list): A list of dictionaries.
    Return Value:
        dict: A new dictionary that contains the sum of all the dictionaries in the input list. If a key is present in
        multiple dictionaries, the corresponding values are added together in the new dictionary.
    """
    result = {}
    for lists in list_dictionaries:
        result = sum_two(result, lists)
    return result

def two_grams(words):
    """
    The function takes a list of words as input, and returns a dictionary that contains all the two-grams in the list,
    along with the number of times each two-gram appears. A two-gram is defined as a pair of consecutive words in the
    list.
    Arguments:
        Words (list): A list of words.
    Return Value:
        dict: A dictionary of all two-grams in the input list of words. Each key in the dictionary is a tuple containing
        two words, and the corresponding value is the number of times that two-gram appears in the input list of  words.
    """
    result = {}
    for i in range(len(words)-1):
        current_tuple = (words[i].lower(), words[i+1].lower())
        if current_tuple not in result:
            result[current_tuple] = 0
        result[current_tuple] = result[current_tuple] + 1
    return result

def keep_first(dictionaries):
    """
    The function takes a list of dictionaries, and returns a new dictionary that contains only the first occurrence of
    each unique name, along with the corresponding GPA.
    Arguments:
        Dictionaries (list): A list of dictionaries. Each dictionary represents a student, and contains at least the
        keys "First Name" and "Last Name". It may also contain a key "GPA", representing the student's grade point average
    Return Value:
        dict: A new dictionary that contains only the first occurrence of each unique name in the input list of
        dictionaries, along with the corresponding GPA, if present. The keys in the new dictionary are tuples containing
        the first and last name of each student, and the values are their corresponding GPAs, if present.
    """
    result = {}
    for dictionary in dictionaries:
        current_tuple = (dictionary["First Name"], dictionary["Last Name"])
        if "GPA" in dictionary and current_tuple not in result:
            result[current_tuple] = dictionary["GPA"]
    return result

def merge_ascending(L1, L2):
    """************
    The function merges two sorted lists in ascending order and returns the result.
    Arguments:
        L1 (list): A sorted list of elements
        L2 (list): Another sorted list of elements
    Return Value:
        list: A new list containing all the elements of L1 and L2, sorted in ascending order.
    """
    result = []
    i = 0
    index = 0
    while i < len(L1) and index < len(L2):
        if L1[i]< L2[index]:
            result.append(L1[i])
            i = i + 1
        else:
            result.append(L2[index])
            index = index + 1
    for element in range(i, len(L1)):
        result.append(L1[element])
    for element in range(index, len(L2)):
        result.append(L2[element])
    return result

def start_longest_run(numbers):
    """
    The function finds the starting index of the longest run of consecutive equal numbers in a list of integers.
    Arguments:
        Numbers (list): A list of integers.
    Return Value:
        int: The starting index of the longest run of consecutive equal numbers. If the input list is empty, returns -1.
    """
    if len(numbers) == 0:
        return -1

    longest_index = 0
    longest_run = 1
    current_index = 0
    current_run = 1
    for index in range(1, len(numbers)):
        if numbers[index] == numbers[index - 1]:
            current_run = current_run + 1
            if current_run > longest_run:
                longest_run = current_run
                longest_index = current_index
        elif numbers[index]!= numbers[index - 1]:
            current_run = 1
            current_index = index
    return longest_index

def mode(numbers):
    """
    The function finds the mode (most frequently occurring value) in a list of integers.
    Arguments:
        Numbers (list): a list of numbers.
    Return Value:
        int: The mode of the input list. If there is more than one mode, returns the smallest one. If the input list is
         empty, returns None.
    """
    if len(numbers) == 0:
        return None
    result = {}
    for number in numbers:
        if number not in result:
            result[number] = 1
        else:
            result[number] = result[number] + 1

    amount = result[numbers[0]]
    mode = numbers[0]

    for key in result:
        if result[key] > amount:
            mode = key
            amount = result[key]
        elif result[key] == amount and key < mode:
            mode = key
            amount = result[key]
    return mode

def main():

    print(sum_two({"a": 1}, {"a": 2, "b": 3}))
    print(sum_all([{}, {"a": 1}, {"a": 2}, {"b": 3}]))
    print(two_grams(["Hello", "hello", "hello", "world"]))
    print(keep_first(
    [{"First Name": "Alice", "Last Name": "Smith", "GPA": 4.0},
    {"First Name": "Bob", "Last Name": "Jones"},
    {"First Name": "Alice", "Last Name": "Smith", "GPA": 2.0},]))
    print(merge_ascending([1, 3, 5], [2, 4, 6, 7]))
    print(start_longest_run([1]))
    print(mode([3, 2, 3, 4]))
    print(mode([3, 1, 1, 3]))

main()
