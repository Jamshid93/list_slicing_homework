def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    reverse=list1[n::]
    return reverse[::-1]
print(main(['a', 'b', 'c', 'd', 'e', 'f'],3))