import anagrams
import test_list

def assert_test(tuple, expected:bool = True):
    for n, v in tuple:
        try:
            assert anagrams.anagrams(n.replace(" ", ""), v.replace(" ", "")) == expected
        except AssertionError:
            print("Assertion Error: Anagrams test check failed for words: {} and {}".format(n, v))

# TRUE ASSERTS
assert_test(test_list.anagrams, True)
# FALSE ASSERTS
assert_test(test_list.not_anagrams, False)