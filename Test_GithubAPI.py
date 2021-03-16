import unittest
from GithubAPI import githubAPI
from unittest.mock import MagicMock as Mock, patch


class TestGithubAPI567(unittest.TestCase):
    @patch('GithubAPI.githubAPI')
    def testWorkingUserInputMock(self, mockrequirements):
        mockrequirements.return_value.json.return_value = ('konglingwengit')
        res = githubAPI("konglingwengit")
        self.assertEqual(res, True)

    def TestWithErrorUserInputMock1(self):
        self.assertEqual(githubAPI(000), 'Github user not correct',
                         'only strings are allowed')

    def TestWithErrorUserInputMock2(self):
        self.assertEqual(githubAPI(9999), 'Github user not correct',
                         'only strings are allowed')


if __name__ == "__main__":
    print('Testing all the cases')
    unittest.main()
