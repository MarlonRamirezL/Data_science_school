import unittest


def addition(num_1,num_2):
    return num_1 + num_2


class BlackBoxTest(unittest.TestCase):

    def test_addition_two_positivies_numbers(self):
        num_1= 10
        num_2= 5

        answer= addition(num_1,num_2)

        self.assertEqual(answer,15)
    
    def test_addition_two_negativies_numbers(self):
        num_1= -10
        num_2= -7

        answer= addition(num_1,num_2)

        self.assertEqual(answer, -17)



if __name__ == "__main__":
    unittest.main()