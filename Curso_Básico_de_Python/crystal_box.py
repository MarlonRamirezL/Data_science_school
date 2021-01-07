import unittest


def is_an_adult(age):
    if age >= 18:
        return True

    else:
        return False
class CrystalBoxTest (unittest.TestCase):
    
    def test_is_an_adult(self):
        age=20

        answer= is_an_adult(age)

        self.assertEqual(answer,True)

    def test_is_not_an_adult(self):
        age=15

        answer= is_an_adult(age)

        self.assertEqual(answer, False)


if __name__ == "__main__":
    unittest.main()