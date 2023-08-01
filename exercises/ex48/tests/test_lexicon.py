import unittest

from ex48 import lexicon


class TestLexicon(unittest.TestCase):

    def test_directions(self):
        self.assertEqual(lexicon.scan("north"), [('direction', 'north')])
        result = lexicon.scan("north south east")
        self.assertEqual(result, [('direction', 'north'),
                                  ('direction', 'south'),
                                  ('direction', 'east')])

    def test_verbs(self):
        self.assertEqual(lexicon.scan("go"), [('verb', 'go')])
        result = lexicon.scan("go kill eat")
        self.assertEqual(result, [('verb', 'go'),
                                  ('verb', 'kill'),
                                  ('verb', 'eat')])

    def test_stops(self):
        self.assertEqual(lexicon.scan("the"), [('stop', 'the')])
        result = lexicon.scan("the in of")
        self.assertEqual(result, [('stop', 'the'),
                                  ('stop', 'in'),
                                  ('stop', 'of')])

    def test_nouns(self):
        self.assertEqual(lexicon.scan("bear"), [('noun', 'bear')])
        result = lexicon.scan("bear princess")
        self.assertEqual(result, [('noun', 'bear'),
                                  ('noun', 'princess')])

    def test_numbers(self):
        self.assertEqual(lexicon.scan("1234"), [('number', 1234)])
        result = lexicon.scan("3 91234")
        self.assertEqual(result, [('number', 3),
                                  ('number', 91234)])
    def test_errors(self):
        self.assertEqual(lexicon.scan("ASDFADFASDF"),
                         [('error', 'ASDFADFASDF')])
        result = lexicon.scan("bear IAS princess")
        self.assertEqual(result, [('noun', 'bear'),
                                  ('error', 'IAS'),
                                  ('noun', 'princess')])

    def test_capitals(self):
        # Study Drill 3: Handle capitalization.
        self.assertEqual(lexicon.scan("NORTH"), [('direction', 'NORTH')])
        result = lexicon.scan("go EaSt 3")
        self.assertEqual(result, [('verb', 'go'),
                                  ('direction', 'EaSt'),
                                  ('number', 3)])

    def test_int_conversion(self):
        # Study Drill 4: Find another to convert str to int.
        import math
        
        string_list = ['678', '-1', 'three']
        number_list = []

        for string in string_list:
            # Deal with negative numbers
            absolute_value = string.replace('-', '0')
            
            if absolute_value.isdigit():
                number_list.append(eval(string))
            else:
                number_list.append(math.nan)

        self.assertEqual(number_list, [678, -1, math.nan])
