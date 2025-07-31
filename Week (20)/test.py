import random 
from typing import Optional, List

def generate_memorable_password(
    no_of_words: int = 4,
    separator: str = "-",
    capitalization: bool = False,
    vocabulary: Optional[List[str]] = None
) -> str:
    """
    Generate a memorable password from a list of vocabulary words.
    """
    if vocabulary is None:
        vocabulary = ['apple', 'banana', 'cherry', 'orange']  

    password_words = random.sample(vocabulary, no_of_words)


    if capitalization:
        password_words = [word.capitalize() for word in password_words]
    return separator.join(password_words)

print(generate_memorable_password(5, "-", True, ["Ad", "BD", "cd", "vd", 'xd']))

def test():
    try:
        x = generate_memorable_password(5, "-", True, ["Ad", "BD", "cd", "vd", 'xd'])
        assert len(x) == 14
    except:
        test()

test()