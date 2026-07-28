print("chandu")


def is_palindrome(text: str) -> bool:
    """
    Check whether the given string is a palindrome.
    Ignores case, spaces, and non-alphanumeric characters.

    Examples:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_cases = ["madam", "racecar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw?", "chandu"]
    for word in test_cases:
        print(f"{word!r} -> {is_palindrome(word)}")
