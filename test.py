from enum import Enum
import random
import string
import unittest

from allergy.allergy import allergy


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

    def test_allergy(self):
        pass
        # result = allergy(["cl", "bom", "dara", "minzy"], [["dara", "minzy"], ["cl", "minzy"], ["cl", "dara"], ["cl"], ["bom", "dara"], ["bom", "minzy"]])
        # result = allergy("a b c d e f g h i j".split(" "), ["a c d h i j".split(" "), "a d i".split(" "), "a c f g h i j".split(" "), "b d g".split(" "), "b c f h i".split(" "), "b e g j".split(" "), "b c g h i".split(" ")])

    def test_allergy_by_random(self):
        names = InputFactory.factory(InputFactory.InputType.random, 5)
        friends_for_dishes = []
        all = False
        while not all:
            all = True
            for name in names:
                isin = False
                for frs in friends_for_dishes:
                    if name in frs:
                        isin = True
                if not isin:
                    all = False
                    break
            friends_for_dish = []
            remain_names = names.copy()
            for i in range(random.randrange(1, 4)):
                if len(remain_names) == 0:
                    break
                name = random.choice(remain_names)
                friends_for_dish.append(name)
                remain_names.remove(name)
            friends_for_dishes.append(friends_for_dish)
        result = allergy(names, friends_for_dishes)
        print(friends_for_dishes, result)


"""
    def test_word_chain(self):
        result = word_chain(InputFactory.factory(InputFactory.InputType.fixed))
        print(result)

    def test_word_chain_by_random(self):
        words = InputFactory.factory(InputFactory.InputType.random, 100)
        print(words)
        result = word_chain(words)
        print(result)
"""


class InputFactory:
    class InputType(Enum):
        fixed = "fixed",
        random = "random"

    @staticmethod
    def factory(input_type, cnt=5):
        if input_type is InputFactory.InputType.fixed:
            # return ['dog', 'god', 'dragon', 'need']
            return ['ab', 'ba', 'cc']
        elif input_type is InputFactory.InputType.random:
            input_words = []
            for i in range(cnt):
                word = ''
                while True:
                    word = ''.join([random.choice(string.ascii_lowercase) for j in range(2)])
                    if word not in input_words:
                        break
                input_words.append(word)
            return input_words


if __name__ == '__main__':
    unittest.main()
