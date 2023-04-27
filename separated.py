"""
Katherine Tran

The project consists of different function each related to separated elements with commas.
"""

def separate_by_commas(string):
    """
    The function splits a string by commas, ignoring commas within double quotes.
    Arguments:
        String (str): The string to be split.
    Return Value:
        list: A list of substrings obtained by splitting the input string at commas.
    """
    result = []
    new = ""
    i = 0

    if len(string) == 0:
        result.append(new)

    while i < len(string):
        if string[i] == '"':
            i += 1
            while i < len(string) and string[i] != '"':
                new += string[i]
                i += 1
        elif string[i] == ",":
            result.append(new)
            new = ""
        else:
            new += string[i]

        if i == len(string) - 1:
            result.append(new)
        i += 1
    return result

def create_comma_separated_string(list_of_strings):
    """
    The function concatenates a list of strings into a comma-separated string.
    Arguments:
        list_of_strings (list): A list of strings.
    Return Value:
        str: A string obtained by concatenating the input list of strings with commas.
    """
    result = ""
    for index in range(len(list_of_strings) - 1):
        string = list_of_strings[index]
        if "," in string:
            string = '"' + string + '"'
        result = result + string + ","
    return result + list_of_strings[len(list_of_strings) - 1]

def csv_file_to_list_of_lists(filename):
    """
    The function reads a CSV file and returns its contents as a list of lists.
    Arguments:
        filename (str): The name of the CSV file to read.
    Return Value:
        list: A list of lists representing the contents of the CSV file.
        If the file is empty or cannot be read, it returns None.
    """
    try:
        f = open(filename, "r")
        result = []
        s = f.read()
        f.close
        lines = s.split("\n")  # ["a,b", "x"]
        for line in lines:
            string = separate_by_commas
            if string == []:
                result.append([""])
            else:
                result.append(string(line))
        return result
    except:
        return None


def list_of_lists_to_csv_file(filename, list_of_lists):
    """
    The function writes a CSV file from a list of lists.
    Arguments:
        filename (str): the name of the file to create or overwrite.
        list_of_lists (list of lists): a list of lists where each inner list represents a row in the CSV file.
    Return Value:
        The function returns the number of rows written to the file.
    """
    result = []
    for lists in list_of_lists:
        result.append(create_comma_separated_string(lists))
    f = open(filename, "w")
    for index in range(len(result)):
        if index == 0:
            f.write(result[index])
        else:
            f.write("\n" + result[index])
    f.close
    return len(result)

def csv_file_to_list_of_dictionaries(filename):
    """
    The function converts a CSV file to a list of dictionaries where each row is represented as a dictionary.
    Arguments:
        filename (str): The name of the CSV file to be converted.
    Return Value:
        list of dict: A list of dictionaries, where each dictionary represents a row in the CSV file. The keys of the
        dictionaries are the headers of the CSV file, and the values are the corresponding values in each row.

        Returns None if the file cannot be read or if it has fewer than two rows.
        Returns None if the headers and rows have different number of columns.

        FileNotFoundError: If the file does not exist or cannot be found.
    """
    result = []
    element = csv_file_to_list_of_lists(filename)
    if element == None:
        return None
    if len(element) < 2:
        return []
    header = element[0]
    for index in range(1, len(element)):
        name_number = {}
        row = element[index]
        if len(header) != len(row):
            return None
        for i in range(len(header)):
            name_number[header[i]] = row[i]
        result.append(name_number)
    return result

def list_of_dictionaries_to_csv_file(filename, list_of_dictionaries):
    """
    The function writes a list of dictionaries to a CSV file.
    Arguments:
        filename (str): The name of the CSV file to be created or overwritten.
        list_of_dictionaries (list of dict): A list of dictionaries, where each dictionary represents a row in the CSV
        file. The keys of the dictionaries are the headers of the CSV file, and the values are the corresponding values
        in each row.
    Return Value:
        int: The number of rows written to the CSV file (including the header row).
        Returns None if the input list is empty, or if the file cannot be created or written to.
    """
    if len(list_of_dictionaries) == 0:
        return None
    try:
        f = open(filename, "w")
        keys = []
        for key in list_of_dictionaries[0]:
            keys.append(key)
        f.write(create_comma_separated_string(keys) + "\n")

        for index in range(len(list_of_dictionaries)):
            dictionaries = list_of_dictionaries[index]
            values = []
            for key in keys:
                values.append(dictionaries[key])
            csv_string = create_comma_separated_string(values)

            if index == 0:
                f.write(csv_string)
            else:
                f.write("\n" + csv_string)

        f.close()
        return len(list_of_dictionaries) + 1

    except:
        return None

def main():

    print(separate_by_commas(',"b,c"'))
    print(create_comma_separated_string(["a", "b,c", ""]))
    print(list_of_lists_to_csv_file("lol.csv", [["a", "b"], ["x"]]))

main()
