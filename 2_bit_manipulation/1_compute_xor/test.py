import xor
import test_list
from common.test.test_class import TestClass

test = TestClass(xor.xor, test_list.test)
test.assert_test()