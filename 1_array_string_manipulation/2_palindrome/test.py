import palindrome
import test_list

def assert_test(list, expected: bool = True):
    for n in list:
        try:
            assert palindrome.palindrom(n) == expected
        except AssertionError:
            print("Assertion Error: Anagrams test check failed for words: {}".format(n))

# TRUE ASSERTS
assert_test(test_list.palindrome, True)
# FALSE ASSERTS
assert_test(test_list.not_palindrome, False)