from enum import Enum
import random
import string
import unittest

from word_chain import word_chain


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)

    def test_word_chain(self):
        result = word_chain(InputFactory.factory(InputFactory.InputType.fixed))
        print(result)

    def test_word_chain_by_random(self):
        words = InputFactory.factory(InputFactory.InputType.random, 100)
        print(words)
        result = word_chain(words)
        print(result)


class InputFactory:
    class InputType(Enum):
        fixed = "fixed",
        random = "random"

    @staticmethod
    def factory(input_type, cnt=5):
        if input_type is InputFactory.InputType.fixed:
            # return ['dog', 'god', 'dragon', 'need']
            return ['ab', 'ba', 'bab', 'bsb', 'aca', 'aba', 'bc']
        elif input_type is InputFactory.InputType.random:
            input_words = []
            for i in range(cnt):
                word = ''
                while True:
                    word = ''.join([random.choice(string.ascii_lowercase) for j in range(4)])
                    if word not in input_words:
                        break
                input_words.append(word)
            return input_words


if __name__ == '__main__':
    unittest.main()
