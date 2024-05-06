import palindrome
import test_list

from common.test.test_class import TestClass

test = TestClass(palindrome.palindrome, test_list.test)
test.assert_test()