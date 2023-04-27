"""
Katherine Tran

This program has 11 independent functions that employ different dictionary operations.
"""

def letter_grade(score):
    """
    The function takes a numeric grade and returns a letter grade based on a predefined range of score to letter grade
    mapping.
    Arguments:
        Score (float): A numeric score.
    Return Value:
        str: A letter grade corresponding to the input score, based on a predefined range of score-to-letter-grade
        mappings.
    """
    if 100 >= score and score >= 90:
        return "A"
    elif 90 > score and score >= 80:
        return "B"
    elif 80 > score and score >= 70:
        return "C"
    elif 70 > score and score >= 60:
        return "D"
    else:
        return "E"

def count_vowels(strings):
    """
    The function takes a list of strings and returns a dictionary where each key represents a vowel ("aeiou") and its
    value represents the number of times that vowel appears in the list of strings.
    Arguments:
        Strings (list): A list of strings.
    Return Value:
        dict: A dictionary where each key represents a vowel ("aeiou") and its value represents the number of times that
        vowel appears in the input list of strings.
    """
    result = {"a":0, "e":0, "i":0, "o":0, "u":0}

    for string in strings:
        word = string.lower()
        for letter in word:
            if letter in result:
                result[letter] += 1
    return result

def count_words(strings):
    """
    The function takes a list of strings and returns a dictionary where each key is a unique word in the list and its
    value is the number of times that word appears in the list.
    Arguments:
        Strings (list): a list of strings.
    Return Value:
        dict: A dictionary where each key represents a unique word in the list and its value is the number of times that
        word appears in the list of strings
    """
    result = {}

    for string in strings:
        words = string.split()
        for word in words:
            if word not in result:
                result[word] = 0
            result[word] += 1
    return result

def words_by_first_letter(strings):
    """
    The function takes a list of strings and returns a dictionary where each key represents a unique first letter of a
    word in the list and its value is a list of words that start with that letter.
    Arguments:
        Strings (list): A list of strings.
    Return Value:
        dict: A dictionary where each key represents a unique first letter of a word in the input list, and its value is
        a list of all words in the input that start with that letter.
    """
    result = {}

    for string in strings:
        words = string.split()
        for word in words:
            letter = word[0]
            if letter not in result:
                result[letter] = [word]
            elif word not in result[letter]:
                result[letter].append(word)
    return result

def indices_of_words(strings):
    """
    The function takes a list of strings and returns a dictionary where each key is a unique word in the list, and the
    value associated with that key is a list of indices of strings where that word appears.
    Arguments:
        Strings (list): A list of strings.
    Return Value:
        dict: A dictionary where each key is a unique word in the input list of strings, and the corresponding value is
        a list of indices where that word appears in the list.
    """
    result = {}

    for index in range(len(strings)):
        words = strings[index].split()
        for word in words:
            if word not in result:
                result[word] = []
            if index not in result[word]:
                result[word].append(index)
    return result

def compute_letter_grades(grades):
    """
     The function returns a dictionary where the keys are students' names and the values are their letter grades
     determined by the average of their numeric grades. The function calls the letter_grade() function to assign a
     letter grade based on the numeric grade.
     Arguments:
        Grades (dict): A dictionary where the keys are student names and the values are another dictionary containing the
        students' grades in different categories.
    Return Value:
        dict: A dictionary where the keys are student names and the values are their corresponding letter grades, based
        on the average of their numeric grades.
    """
    result = {}

    for name in grades:
        scores = grades[name]
        total = 0
        for number in scores:
            total = total + number
        avg = total//len(scores)
        result[name] = letter_grade(avg)
    return result

def add_letter_grade(grades):
    """
    The function returns a dictionary where the keys are students' names and the values are a dictionary of their test,
    homework, and course grades. The function computes the overall course grade by adding the weighted grade of the test
    grade and the homework grade and dividing it by 3. The function calls letter_grade() to assign a letter grade based
    on the numeric grade.
     Arguments:
        Grades (dict): A dictionary where the keys are student names and the values are another dictionary containing the
        students' grades in different categories.
    Return Value:
        dict: A dictionary where the keys are student names and the values are another dictionary containing the students'
        grades in different categories, as well as their letter grades for each category.
    """
    for name in grades:
        scores = grades[name]
        if "hw" not in scores:
            scores["hw"] = 0
        if "test" not in scores:
            scores["test"] = 0
        grade = (2 * scores["test"] + scores["hw"]) // 3
        scores["course"] = letter_grade(grade)

def compute_all_letter_grades(grades):
    """
    The function returns a dictionary where the keys are students' names and the value is the letter grade of the
    student determined by a weighted test grade and homework grade. The function computes the student's grade for each
    category to compute the student's appropriately weighted average grade. The function calls letter_grade() to assign
    a letter grade based on the numeric grade.
    Arguments:
        Grades (dict): A dictionary where the keys represent different categories of grades and the values are another
        dictionary where the keys are student names and the values are their numeric grades in the given category.
    Return Value:
        dict: A dictionary where the keys represent student names and the values represent their letter grades, based on
        weighted test and homework grades.
    """
    result = {}
    for score in grades:
        names = grades[score]
        for name in names:
            if name not in result:
                result[name] = 0

    for name in result:
        test_score = 0
        hw_score = 0
        if name in grades["test"]:
            test_score = grades["test"][name] * 2
        if name in grades["hw"]:
            hw_score = grades["hw"][name]
        avg = (test_score + hw_score) // 3
        result[name] = letter_grade(avg)
    return result

def unflatten_grades(grades):
    """
    The function takes a list of strings and non-strings as an input and returns a dictionary where the keys are the
    strings in the input list and the values are all non-string elements that follow the respective string element.
    Arguments:
        Grades (dict): A list of dictionaries containing students' grades.
    Return Value:
         dict: A dictionary where the keys are students' names and the values are another dictionary containing the
         students' grades, categorized by type.
    """
    result = {}

    for dictionary in grades:
        name = dictionary["name"]
        category = dictionary["category"]
        score = dictionary["score"]

        if name not in result:
            result[name] = {}
            result[name][category] = [score]
        elif name in result:
            if category not in result[name]:
                result[name][category] = [score]
            else:
                result[name][category].append(score)
    return result

def gather(values):
    """
    The function takes in a list of values and returns a dictionary where the keys are strings and the values are all
    non-strings that follow the string.
    Arguments:
        Values (list): A list of values containing strings and non-strings.
    Return Value:
        dict: A dictionary containing key-value pairs, where the keys are strings found in the `values` list, and the
        values are a list of all non-string values that follow the corresponding string in the `values` list.
    """
    result = {}
    current_value = ""

    for value in values:
        if isinstance(value, str):
            current_value = value
            if current_value not in result:
                result[current_value] = []
        elif len(result) != 0:
            result[current_value].append(value)
    return result

def main():

    print(letter_grade(100))
    print(count_vowels(["Hello", "World"]))
    print(count_words(['Hello', 'World', 'Hello World'],))
    print(words_by_first_letter(["Hello", "World"]))
    print(indices_of_words(["Hello", "World", "Hello World"]))
    print(by_grade({"Alice": "A", "Bob": "B", "Charlie": "A"}))
    print(compute_letter_grades({"Alice": [100, 90, 100], "Bob": [100, 100, 100]}))
    print(add_letter_grade({'Alice': {'test': 92, 'hw': 90}},))
    print(compute_all_letter_grades({"test": {"Alice": 100, "Bob": 80, "Carol": 90},"hw": {"Alice": 100, "Bob": 70, "David": 90},}))
    print(unflatten_grades(
    [   {"name": "Alice", "category": "test", "score": 100},
        {"name": "Alice", "category": "test", "score": 99},
        {"name": "Alice", "category": "hw", "score": 100},
        {"name": "Bob", "category": "test", "score": 90},
        {"name": "Carol", "category": "hw", "score": 98},
        {"name": "David", "category": "test", "score": 100},
        {"name": "David", "category": "hw", "score": 100},
        {"name": "David", "category": "hw", "score": 98},   ]))
    print(gather([4, 5, "a", 1, 2, "b", "a", 5, "c"]))

main()

