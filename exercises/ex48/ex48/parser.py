"""LP3THW Exercise 49: Sentence Parsing"""
from ex48.lexicon import scan


class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember, we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        # Study Drill 2: Handle words not in lexicon.
        if word[0] == 'error':
            raise ParserError(f"Word not in lexicon: {word[1]}")
        else:
            return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        # Modified Shaw's error message to differentiate from parse_verb(). 
        raise ParserError("Expected a noun or verb first.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
