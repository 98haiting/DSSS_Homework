import unittest
from math_quiz import get_integer, get_operation, calculation


class TestMathGame(unittest.TestCase):

    def test_get_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_operation(self):
        # TODO
        # Test if the generated operation is within the specified range
        operators = ["+", "-", "*"]
        rand_operator = get_operation()
        self.assertTrue(rand_operator == operator for operator in operators)

    def test_calculation(self):
        # test if the equation is correctly calculated, and
        # if the user is assigned the correct score
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 7, '*', '4 * 7', 28),
                (6, 3, '-', '6 - 3', 3),
                (3, 7, '*', '3 * 7', 21),
                (4, 2, '+', '4 + 2', 6),
                (9, 6, '-', '9 - 6', 3),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, output = calculation(num1, num2, operator)
                self.assertTrue(output == expected_answer and problem == expected_problem)


if __name__ == "__main__":
    unittest.main()
