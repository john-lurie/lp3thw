"""LP3THW Exercise 49: Sentence Parsing"""
import unittest

from ex48.lexicon import scan
from ex48.parser import ParserError, parse_sentence


class TestParser(unittest.TestCase):

    def test_implicit_subject(self):
        string = "go east"
        sentence = parse_sentence(scan(string))
        self.assertEqual(sentence.subject, "player")
        self.assertEqual(sentence.verb, "go")
        self.assertEqual(sentence.object, "east")

    def test_stop_words(self):
        string = "the princess eat the bear"
        sentence = parse_sentence(scan(string))
        self.assertEqual(sentence.subject, "princess")
        self.assertEqual(sentence.verb, "eat")
        self.assertEqual(sentence.object, "bear")

    def test_invalid_subject(self):
        string = "north go bear"
        message = "Expected a noun or verb first."
        with self.assertRaisesRegex(ParserError, message):
            sentence = parse_sentence(scan(string))

    def test_missing_verb(self):
        string = "princess south"
        message = "Expected a verb next."
        with self.assertRaisesRegex(ParserError, message):
            sentence = parse_sentence(scan(string))
    
    def test_missing_object(self):
        string = "bear eat"
        message = "Expected a noun or direction next."
        with self.assertRaisesRegex(ParserError, message):
            sentence = parse_sentence(scan(string))

    def test_unknown_word(self):
        string = "the bear kill the salmon"
        message = "Word not in lexicon: salmon"
        with self.assertRaisesRegex(ParserError, message):
            sentence = parse_sentence(scan(string))
