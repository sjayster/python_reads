import unittest


class Solution:
    # @param num, a list of integers
    # @return an integer

    def majorityElement(self, num):
        if num:
            return sorted(num)[len(num) / 2]
        # This program uses the logic that , if a number appears more than n/2 times in the array - then the n/2-nd element
        # should be what we are looking for
        # 1. Sort the Array
        # 2. Return n/2th element


class TestMajorityElement(unittest.TestCase):
    my_solution = Solution()

    # looks like this test is missing in l33tcode
    def test_empty_array(self):
        self.assertEqual(self.my_solution.majorityElement([]), None)

    def test_default_pass(self):
        self.assertEqual(self.my_solution.majorityElement([1, 1, 1, 1, 1]), 1)
        print "Pass"

    def test_default_fail(self):
        self.assertEqual(self.my_solution.majorityElement(
            [1, 1, 1, 1, 1]), 2, "Incorrect")

if __name__ == "__main__":
    unittest.main()
