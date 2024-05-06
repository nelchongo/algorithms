import duplicates
import test_list

def assert_test(list):
    for key, n in list.items():
        try:
            assert duplicates.duplicates(n['input']) == n['expected']
        except AssertionError:
            print("Assertion Error: Anagrams test check failed for words: {}".format(n))

# TRUE ASSERTS
assert_test(test_list.test)