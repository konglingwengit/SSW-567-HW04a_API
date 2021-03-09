import unittest
from GithubAPI import githubAPI


class TestGithubAPI567(unittest.TestCase):
    def testWorkingUserInput(self):
        self.assertEqual(githubAPI('konglingwengit'), True)

    def testNonWorkingUserInput1(self):
        self.assertEqual(githubAPI(44343), 'Github user not correct', 'only strings are allowed')

    def testNonWorkingUserInput2(self):
        self.assertEqual(githubAPI("HlooI"), False)

    def testNonWorkingUserInput3(self):
        self.assertEqual(githubAPI(11), 'Github user not correct', 'only strings are allowed')

    def testNonWorkingUserInput4(self):
        self.assertEqual(githubAPI(9999), 'Github user not correct', 'only strings are allowed')


if __name__ == "__main__":
    print('Testing...')
    unittest.main()
