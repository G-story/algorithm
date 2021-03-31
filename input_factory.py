import random
import string

from sqlalchemy import Enum


class InputFactory:
    class ProductionMethod(Enum):
        fixed = "fixed",
        random = "random"

    @staticmethod
    def factory(production_method, input_type, cnt=5, min_val=0, max_val=10):
        if production_method is InputFactory.ProductionMethod.fixed:
            if input_type == int:
                return [i for i in range(1, cnt + 1)]
        elif production_method is InputFactory.ProductionMethod.random:
            inputs = []
            if input_type == int:
                inputs = [random.randint(min_val, max_val) for j in range(cnt)]
            elif input_type == str:
                inputs = [''.join([random.choice(string.ascii_lowercase) for j in range(2)]) for k in range(cnt)]
            return inputs
