"""
Katherine Tran

"""

def get_file_contents(filename):
    """
    The function returns the contents of the file with the given filename.
    Arguments:
        Filename (str): The name of the file to be read.
    Return Value:
        str: The contents of the file if it exists and can be read, otherwise None.
    """
    try:
        f = open(filename, "r")
        s = f.read()
        f.close()
        return s
    except:
        return None

def get_votes(string):
    """
    The function takes a string of comma-separated rankings of candidates by voters and returns a list of lists
    representing the rankings.
    Arguments:
        String (str): A string of comma-separated rankings of candidates by voters.
    Return Value:
        list of lists: The list of lists represents the rankings of candidates by the voters. The inner list represents
        the ranking of the candidates by one voter.
    """
    result = []
    lines = string.split("\n")
    for line in lines:
        if len(line) != 0:
            element = line.split(",")
            result.append(element)
    return result

def borda_scores(votes):
    """
    The function calculates the Borda scores of each candidate based on a list of preference votes.
    Arguments:
        Votes (list): A list of preference votes, where each vote is a list of candidate names ordered by the voter's
        preference.
    Return Value:
        dict: A dictionary containing the Borda scores of each candidate. The keys are the names of the candidates and
        the values are their corresponding Borda scores.
    """
    result = {}
    for vote in votes:
        index = 0
        while index < len(vote):
            if vote[index] not in result:
                result[vote[index]] = len(vote) - index
            else:
                result[vote[index]] = result[vote[index]] + len(vote) - index
            index = index + 1
    return result

def plurality(votes):
    """
    The function calculates the plurality vote for each candidate based on a list of preference votes.
    Arguments:
        Votes (list): A list of preference votes, where each vote is a list of candidate names ordered by the voter's
        preference.
    Return Value:
        dict: A dictionary containing the number of first-choice votes for each candidate. The keys are the names of
        the candidates and the values are the corresponding number of votes.
    """
    result = {}
    for vote in votes:
        for index in range(len(vote)):
            letter = vote[index]
            if index == 0:
                if letter not in result:
                    result[letter] = 1
                else:
                    result[letter] = result[letter] + 1
    return result

def pairwise(votes):
    """
    The function calculates the pairwise vote for each pair of candidates based on a list of preference votes.
    Arguments:
        votes (list of list): A list of lists, where each inner list represents a vote or ranking. The elements in each
        inner list are assumed to be hashable.
    Return Value:
        dict: A dictionary where the keys are 2-tuples representing pairs of distinct elements that appear together in
        at least one vote, and the values are the number of votes in which the pair appears.
    """
    result = {}
    for vote in votes:
        for i in range(len(vote)):
            for j in range(i + 1, len(vote)):
                tuple1 = (vote[i], vote[j])
                if tuple1 not in result:
                    result[tuple1] = 0
                result[tuple1] = result[tuple1] + 1
    return result


def condorcet_winner(votes):
    """
    The function determines the Condorcet winner based on a list of preference votes.
    Arguments:
        Votes (list): A list of preference votes, where each vote is a list of candidate names ordered by the voter's
        preference.
    Return Value:
        str: The name of the Condorcet winner, if there is one. If there is no Condorcet winner, returns None.
    """
    result = votes[0]  # [a, b, c]
    winner = pairwise(votes)  # dictionary made from pairwise
    for candidate in result:  # iterating through result
        win = True  # boolean to check in the end
        for opponent in result:  # other elements in the last other than candidate
            if opponent != candidate:  # make sure its not checking the same candidate
                # tuple1 = (candidate, opponent)
                # tuple2 = (opponent, candidate)
                # votesfor = winner[tuple1]
                # votesagainst = winner[tuple2]
                votes_for = winner.get((candidate, opponent), 0)
                votes_against = winner.get((opponent, candidate), 0)
                if votes_for <= votes_against:
                    win = False
        if win == True:
            return candidate
    return None


def winners(scores):
    """
    The function determines the winner based on a dictionary of scores.
    Arguments:
        Scores (dict): A dictionary of scores, where the keys are the names of candidates and the values are their scores.
    Return Value:
        list: A list of the names of the winners, if there is more than one winner. If there is only one winner, returns
        a list with a single element. If the input dictionary is empty, returns an empty list.
    """
    result = []
    largest = 0
    for score in scores:
        if scores[score] > largest:
            result = []
            result.append(score)
            largest = scores[score]
        elif scores[score] == largest:
            result.append(score)
    return result


def main():

    print(get_votes("a,b,c\nc,b,a\na,c,b"))
    votes1 = [["a", "b", "c"], ["c", "b", "a"], ["a", "c", "b"]]
    votes2 = [["a", "b"], ["b", "a"], ["a", "b"]]
    votes3 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]
    print(borda_scores(votes1))
    print(borda_scores(votes2))
    print(borda_scores(votes3))
    print(plurality(votes1))
    print(winners({"a": 1, "b": 2, "c": 3}))
    print(winners({"a": 1, "b": 1, "c": 1}))
    print(pairwise(votes2))
    print(condorcet_winner(votes1))

main()
