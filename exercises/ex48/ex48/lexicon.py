"""Advanced user input handling"""

def scan(user_input):
    """Parse a string and classify its words.
    
    Parameters
    ----------
    user_input : str
        Words separated by spaces

    Returns
    -------
    words_and_tokens : list
        A tuple for each word containing (token, word).
        token is the "type" of a word, such as a verb or noun.
    """
    tokens_dict = {"north": "direction",
                   "south": "direction",
                   "east": "direction",
                   "go": "verb",
                   "kill": "verb",
                   "eat": "verb",
                   "the": "stop",
                   "in": "stop",
                   "of": "stop",
                   "bear": "noun",
                   "princess": "noun"}

    word_list = user_input.split()
    words_and_tokens = []

    for word in word_list:
        # Study Drill 3: Handle capitalization
        token = tokens_dict.get(word.lower())
        
        if token is not None:
            # word is in tokens_dict
            words_and_tokens.append((token, word))
        else:
            # word is not in tokens_dict
            try:
                word_int = int(word)
                # word is an int
                words_and_tokens.append(("number", word_int))
            except:
                # word is unknown
                words_and_tokens.append(("error", word))

    return words_and_tokens
